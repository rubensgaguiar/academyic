import sacademy.utils as utils
from sacademy.launcher import LauncherOptions, SimulatorOptions, WindowOptions, Launcher

class SessionConf:
	
    SESSION = {
        'players': {
            'left',
            'right'
        },
        'trainer': {
        
        }
    }

    def __init__(self, session_map: dict) -> None:
        self.session_params = session_map
        self._verify_params()

    def _verify_params(self) -> None:
        expected_params = SessionConf.SESSION

        for param in self.session_params:
            if param not in expected_params:
                print(f"Parameter {param} received not in expected param list")

        for param in expected_params:
            if param not in self.session_params:
                print(f"Expected parameter {param} not in received param map")


class Session:

    def __init__(self, conf: SessionConf = None) -> None:
        self.conf = conf

    """ methods to launcher"""
    def __create_launcher(self, options: LauncherOptions = None) -> None:
        raise NotImplementedError

    def launch_simulator(self) -> None:
        file_obj = utils.load_json("tests/conf/sacademy/simulator.json")
        options = SimulatorOptions(file_obj)
        launch_simulator = Launcher("/usr/local/bin/rcssserver",options)

    def launch_window(self) -> None:
        file_obj = utils.load_json("tests/conf/sacademy/window.json")
        options = WindowOptions(file_obj)
        launch_window = Launcher("/usr/local/bin/soccerwindow2",options)

    def launch_all(self) -> None:
        launch_window()
        launch_simulator()

    """ public methods to edit Session object """
    def set_conf(self, new_session: SessionConf) -> None:
            raise NotImplementedError
