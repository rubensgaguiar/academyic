from typing import Union, Set, List, Optional

from sacademy.options import CoachOptions, PlayerOptions
from sacademy.applications import Player, Coach
from sacademy.factory.app_factory import AppFactory
from sacademy.launcher import Launcher


class SessionDeclarationException(Exception):
    """ Exception raised in the event of invalid session configuration. """
    def __init__(self, msg: str):
        super(Exception, self).__init__(msg)


class Team:
    """ Collection of client applications presented in the same team side"""

    def __init__(self) -> None:
        self.players: List[Player] = []
        self.coach: Optional[Coach] = None


class AppHub:
    """ Collection of applications presented in a Session. """

    DECLARATION_FORMAT = {
        'left': {
            'players': list,
            'coach': str
        },
        'right': {
            'players': list,
            'coach': str
        },
    }

    def __init__(self, app_factory: AppFactory, session_declaration: dict, extra_options: dict) -> None:
        try:
            self.__verify_syntax(AppHub.DECLARATION_FORMAT, session_declaration)
        except SessionDeclarationException as e:
            raised_msg = str(e)
            raise ValueError(f"Invalid session declaration syntax.\n{raised_msg}")

        self.__conf = session_declaration
        self.__conf_extra = extra_options

        self.simulator = app_factory.new_simulator()
        self.window = app_factory.new_window()
        self.__create_teams(app_factory, session_declaration)
        try:
            self.__check_validity()
        except SessionDeclarationException as e:
            raised_msg = str(e)
            raise ValueError(f"Invalid session declaration.\n{raised_msg}")

    def __verify_syntax(self, expected: Union[dict, Set], declaration: Union[dict, Set]) -> None:
        """ Verifies session declaration syntax. """
        def verify_dict(expected_dict: dict, declaration_dict: dict) -> None:
            for key, value in expected_dict.items():
                if key not in declaration_dict:
                    raise SessionDeclarationException(f"Missing expected field {key}.")
                elif type(value) in [dict, Set]:
                    try:
                        self.__verify_syntax(value, declaration_dict[key])
                    except SessionDeclarationException as e:
                        raised_msg = str(e)
                        raise SessionDeclarationException(f"At field {key}:\n{raised_msg}")
                elif not isinstance(declaration_dict[key], value):
                    raise ValueError(f"Expected value of type {value} in field {key}.")

        def verify_set(expected_set: Set, declaration_set: Set) -> None:
            for key in expected_set:
                if key not in declaration_set:
                    raise SessionDeclarationException(f"Missing expected field {key}.")

        if type(expected) != type(declaration):
            raise SessionDeclarationException(f"Expected declaration of type {type(expected)} and got \
            {type(declaration)}.")
        elif isinstance(expected, dict):
            return verify_dict(expected, declaration)
        elif isinstance(expected, Set):
            return verify_set(expected, declaration)

    def __create_teams(self, app_factory: AppFactory, declaration: dict) -> None:
        self.left_team = self.__create_team(app_factory, declaration['left'], self.__conf_extra)
        self.right_team = self.__create_team(app_factory, declaration['right'], self.__conf_extra)

    @staticmethod
    def __create_team(app_factory: AppFactory, team_declaration: dict, extra_options) -> Team:
        team = Team()
        for player in team_declaration['players']:
            team.players.append(app_factory.new_player(player))
        team.coach = app_factory.new_coach(team_declaration['coach'], extra_options)
        return team

    def __check_validity(self) -> None:
        """ Verifies session declaration semantics. """
        if self.left_coach is None:
            raise SessionDeclarationException("Left team has no declared coach.")
        if len(self.left_players) == 0 and len(self.right_players) == 0:
            raise SessionDeclarationException("Training session has no declared players.")

    @property
    def left_players(self) -> List[Player]:
        return self.left_team.players

    def left_player(self, unum: int) -> Player:
        if unum <= 0 or unum > len(self.left_players):
            raise IndexError(f"No left player with uniform number {unum}")
        return self.left_players[unum-1]

    @property
    def left_coach(self) -> Optional[Coach]:
        return self.left_team.coach

    @property
    def right_players(self) -> List[Player]:
        return self.right_team.players

    def right_player(self, unum: int) -> Player:
        if unum <= 0 or unum > len(self.right_players):
            raise IndexError(f"No right player with uniform number {unum}")
        return self.left_players[unum-1]

    @property
    def right_coach(self) -> Optional[Coach]:
        return self.right_team.coach

    @property
    def all_players(self) -> List[Player]:
        return self.left_players + self.right_players

    @property
    def all_coaches(self) -> Optional[List[Coach]]:
        coaches = []
        if self.left_coach is not None:
            coaches.append(self.left_coach)
        if self.right_coach is not None:
            coaches.append(self.right_coach)
        if len(coaches) == 0:
            return None
        return coaches


class SessionException(Exception):
    """ Exception raised by Session faced with runtime issues. """
    def __init__(self, msg: str) -> None:
        super(Exception, self).__init__(msg)


class Session:
    """ Manager of Application Launching """

    # Session status
    IDLE = 'IDLE'  # Initial state, no launchers set
    READY = 'READY'  # Launcher creation completed, ready to start launching applications
    LAUNCHING = 'LAUNCHING'  # Applications are being launched, training session is starting
    RUNNING = 'RUNNING'  # All applications have been launched, training session is running
    STOPPED = 'STOPPED'  # All applications have been terminated, training session is over

    def __init__(self) -> None:
        self.__status = Session.IDLE
        self.simulator_launcher: Optional[Launcher] = None
        self.window_launcher: Optional[Launcher] = None
        self.left_team_launchers: List[Launcher] = []
        self.right_team_launchers: List[Launcher] = []

    def create_launchers(self, apps: AppHub) -> None:
        """ Creates Launchers for given applications in current session. """
        if self.__status != Session.IDLE:
            self.reset()
            self.__status = Session.IDLE
        self.simulator_launcher = Launcher(apps.simulator)
        if apps.window:
            self.window_launcher = Launcher(apps.window)
        self.left_team_launchers = self.__create_team_launchers(apps.left_team)
        self.right_team_launchers = self.__create_team_launchers(apps.right_team)
        self.__status = Session.READY

    @staticmethod
    def __create_team_launchers(team: Team) -> List[Launcher]:
        launcher_list = []
        for player in team.players:
            launcher_list.append(Launcher(player))
        if team.coach is not None:
            launcher_list.append(Launcher(team.coach))
        return launcher_list

    @property
    def status(self):
        """ The current status of the Session. """
        return self.__status

    def __update_status(self) -> None:
        """ Checks if all launchers have been launched to update status to RUNNING"""
        def team_launcher_status(team_launchers: List[Launcher]) -> List[bool]:
            return [launcher.launched for launcher in team_launchers]

        statuses = [self.simulator_launcher.launched]
        if self.window_launcher is not None:
            statuses.append(self.window_launcher.launched)
        statuses += team_launcher_status(self.left_team_launchers)
        statuses += team_launcher_status(self.right_team_launchers)

        self.__status = Session.RUNNING if all(statuses) else Session.LAUNCHING

    def __track_status(launch_fn):
        """ Decorator to execute launching safely while keeping status updated"""
        def safe_launch(*args):
            if args[0].status == Session.IDLE:
                raise SessionException('Session Launchers have not been created.')
            if args[0].status == Session.RUNNING:
                raise SessionException('Session is already completely launched.')
            launch_fn(args[0])
            args[0].__update_status()
        return safe_launch

    @__track_status
    def launch_simulator(self) -> None:
        """ Launches the Simulator application"""
        if self.simulator_launcher is not None:
            self.simulator_launcher.launch()

    @__track_status
    def launch_window(self) -> None:
        """ Launches the Window application if available. """
        if self.window_launcher is not None:
            self.window_launcher.launch()

    @staticmethod
    def __launch_players(team_launcher: List[Launcher]) -> None:
        for launcher in team_launcher:
            if isinstance(launcher.options, PlayerOptions):
                launcher.launch()

    @__track_status
    def launch_left_players(self) -> None:
        """ Launches all Player applications of the left team. """
        self.__launch_players(self.left_team_launchers)

    @__track_status
    def launch_right_players(self) -> None:
        """ Launches all Player applications of the right team. """
        self.__launch_players(self.right_team_launchers)

    @__track_status
    def launch_all_players(self) -> None:
        """ Launches all Player applications. """
        self.launch_left_players()
        self.launch_right_players()

    @__track_status
    def launch_left_coach(self) -> None:
        """ Launches the coach application of the left team. """
        if len(self.left_team_launchers) > 0 and isinstance(self.left_team_launchers[-1].options, CoachOptions):
            self.left_team_launchers[-1].launch()

    @__track_status
    def launch_right_coach(self) -> None:
        """ Launches the coach application of the right team. """
        if len(self.left_team_launchers) > 0 and isinstance(self.right_team_launchers[-1].options, CoachOptions):
            self.right_team_launchers[-1].launch()

    def __launch_left(self) -> None:
        self.launch_left_players()
        self.launch_left_coach()

    def __launch_right(self) -> None:
        self.launch_right_players()
        self.launch_right_coach()

    @__track_status
    def launch_all(self) -> None:
        """ Launches all available Launchers. """
        self.launch_simulator()
        self.launch_window()
        self.__launch_left()
        self.__launch_right()

    def stop(self) -> None:
        """ Stops session execution. """
        self.simulator_launcher.kill()
        if self.window_launcher is not None:
            self.window_launcher.kill()
        for launcher in self.left_team_launchers + self.right_team_launchers:
            launcher.kill()
        self.__status = Session.STOPPED

    def reset(self, apps: AppHub = None) -> None:
        """ Stops session execution and deletes all Launchers. """
        self.stop()
        del self.simulator_launcher
        self.simulator_launcher = None
        if self.window_launcher is not None:
            del self.window_launcher
            self.window_launcher = None
        self.left_team_launchers.clear()
        self.right_team_launchers.clear()
        self.__status = Session.IDLE
        if apps is not None:
            self.create_launchers(apps)
