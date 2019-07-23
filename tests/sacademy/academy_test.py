import json
import time

from sacademy.academy import Academy


class TestAcademy:

    @staticmethod
    def __options_from_json() -> dict:
        with open('tests/conf/sacademy.json', "r") as file_obj:
            options = json.load(file_obj)
            # app['options']['game_log_dir'] = path.join(path.dirname(path.abspath(__file__)), '../logs')
            # app['options']['text_log_dir'] = path.join(path.dirname(path.abspath(__file__)), '../logs')
            file_obj.close()
        return options

    def test_academy(self):
        options = self.__options_from_json()
        academy = Academy(options)
        assert academy.run() is None
        time.sleep(10)
        assert academy.exit() is None
        time.sleep(3)
