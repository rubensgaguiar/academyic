from sacademy.options import *


def format_client_options(options: dict, mode: str, training: str) -> dict:
    """ Format an application options' dictionary to contain SoccerAcademy client metadata. """
    return {
        "mode": mode,
        "module-name": training,
        "options": options
    }


class Application(ABC):
    """ Launchable application class"""

    def __init__(self, binpath: str, options: LauncherOptions) -> None:
        self.bin = binpath
        self.options = options


class Simulator(Application):

    def __init__(self, binpath: str, options: dict) -> None:
        super().__init__(binpath, SimulatorOptions(options))


class Window(Application):

    def __init__(self, binpath: str, options: dict) -> None:
        super().__init__(binpath, WindowOptions(options))


class Player(Application):

    def __init__(self, binpath: str, options: dict, goalie: bool, mode: str, training: str) -> None:
        options = format_client_options(options, mode, training)
        options['goalie'] = goalie
        super().__init__(binpath, PlayerOptions(options))


class Coach(Application):

    def __init__(self, binpath: str, options: dict, extra_options: dict, mode: str, training: str) -> None:
        options = format_client_options(options, mode, training)
        super().__init__(binpath, CoachOptions(options, extra_options))
