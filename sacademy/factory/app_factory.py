from sacademy import utils

from sacademy.applications import Application, Window, Simulator, Player, Coach
from sacademy.factory.builder_factory import FactoryBuilder


class AppFactory:

    def __init__(self, builder: FactoryBuilder):
        self.window = builder.window
        self.simulator = builder.simulator
        self.module = builder.module
        self.players = builder.players
        self.coach = builder.coach

    def new_simulator(self) -> Simulator:
        try:
            simulator_options = utils.load_json(self.simulator['options'])
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.simulator['options']} not found")
        try:
            return Simulator(self.simulator['bin'], simulator_options['options'])
        except KeyError as e:
            raise ValueError(str(e))

    def new_window(self) -> Window:
        try:
            window_options = utils.load_json(self.window['options'])
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.window['options']} not found")
        try:
            return Window(self.window['bin'], window_options['options'])
        except KeyError as e:
            raise ValueError(str(e))

    def new_player(self, player: str) -> Player:
        try:
            player_options = utils.load_json(self.players[player]['options'])
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.players[player]['options']} not found")
        try:
            return Player(self.players[player]['bin'], player_options, self.players[player]['goalie'],
                          self.players[player]['mode'], self.module)
        except KeyError:
            raise ValueError(f"Required field not present in {player}")

    def new_coach(self, coach: str, coach_extra_options: dict) -> Coach:
        coach_options = utils.load_json(self.coach[coach]['options'])
        try:
            return Coach(self.coach[coach]['bin'], coach_options, coach_extra_options, self.coach[coach]['mode'], self.module)
        except KeyError:
            raise ValueError(f"Required field not present in {coach}")
