import json

from sacademy.options import SimulatorOptions, WindowOptions


class TestSimulatorOptions:

    @staticmethod
    def __from_json() -> SimulatorOptions:
        with open("tests/conf/simulator.json", "r") as file_obj:
            app = json.load(file_obj)
            options = SimulatorOptions(app['options'])
            file_obj.close()
        return options

    def test_from_json(self):
        options = self.__from_json()
        assert options is not None

    def test_serialized(self):
        options = self.__from_json()
        cmd_line = options.serialize()
        print(cmd_line)
        assert cmd_line is not None

    def test_synch_mode(self):
        options = self.__from_json()
        options.set_synch_mode(False)
        cmd_line = options.serialize()
        print(cmd_line)
        assert cmd_line is not None


class TestWindowOptions:

    @staticmethod
    def __from_json() -> WindowOptions:
        with open("tests/conf/window.json", "r") as file_obj:
            app = json.load(file_obj)
            options = WindowOptions(app['options'])
            file_obj.close()
        return options

    def test_from_json(self) -> None:
        options = self.__from_json()
        assert options is not None

    def test_serialized(self) -> None:
        options = self.__from_json()
        cmd_line = options.serialize()
        print(cmd_line)
        assert cmd_line is not None

    def test_port(self):
        options = self.__from_json()
        options.set_port(6000)
        cmd_line = options.serialize()
        print(cmd_line)
        assert cmd_line is not None
