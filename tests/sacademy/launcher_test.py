import json
import time
from sacademy.launcher import Launcher
from sacademy.applications import Window, Simulator, Player, Coach


class TestLauncher:

    @staticmethod
    def __app_from_json(app_conf: str) -> dict:
        with open('tests/conf/' + app_conf + '.json', "r") as file_obj:
            app = json.load(file_obj)
            # app['options']['game_log_dir'] = path.join(path.dirname(path.abspath(__file__)), '../logs')
            # app['options']['text_log_dir'] = path.join(path.dirname(path.abspath(__file__)), '../logs')
            file_obj.close()
        return app

    def __launcher_from_options(self, app_conf: str) -> Launcher:
        if app_conf == "window":
            app = self.__app_from_json("sacademy/window")
            launcher = Launcher(Window(app['bin'], app['options']))
        if app_conf == "simulator":
            app = self.__app_from_json("sacademy/simulator")
            launcher = Launcher(Simulator(app['bin'], app['options']))
        if app_conf == "player":
            app = (self.__app_from_json("sacademy"))['factory']['applications']['players']['itandroids_actor']
            options = self.__app_from_json("applications/itandroids2d_player")
            launcher = Launcher(Player(app['bin'], options, app['goalie'], app['mode'], "example"))
        if app_conf == "coach":
            app = (self.__app_from_json("sacademy"))['factory']['applications']['coaches']['itandroids_trainer']
            options = self.__app_from_json("applications/itandroids2d_trainer")
            launcher = Launcher(Coach(app['bin'], options, app['mode'], "example"))
        return launcher

    def test_launch_window(self):
        launcher = self.__launcher_from_options("window")
        launcher.launch()
        time.sleep(2)
        launcher.kill()
        time.sleep(1)
        assert launcher.process.poll() is not None

    def test_launch_simulator(self):
        launcher = self.__launcher_from_options("simulator")
        launcher.launch()
        time.sleep(2)
        launcher.kill()
        time.sleep(1)
        assert launcher.process.poll() is not None

    def test_launch_player(self):
        launcher = self.__launcher_from_options("player")
        launcher.launch()
        time.sleep(2)
        launcher.kill()
        time.sleep(1)
        assert launcher.process.poll() is not None

    def test_launch_coach(self):
        launcher = self.__launcher_from_options("coach")
        launcher.launch()
        time.sleep(2)
        launcher.kill()
        time.sleep(1)
        assert launcher.process.poll() is not None
