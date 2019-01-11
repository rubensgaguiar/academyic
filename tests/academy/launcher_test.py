import pytest
import json

from sacademy.launcher import SimulatorOptions, WindowOptions, Launcher


"""class TestSimulatorOptions:

    def __from_json(self):
        with open("tests/conf/sacademy/simulator.json", "r") as jsonOpt:
            fileObj = json.load(jsonOpt)
            options = SimulatorOptions(fileObj)
            jsonOpt.close()
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

	def __from_json(self):
		with open ("tests/conf/sacademy/window.json", "r") as jsonOpt:
			fileObj = json.load(jsonOpt)
			options = WindowOptions(fileObj)
			jsonOpt.close()
		return options

	def test_from_json(self):
		options = self.__from_json()
		assert options is not None

	def test_serialized(self):
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
"""
class TestLauncher:

	def __from_json(self):
		with open ("tests/conf/sacademy/simulator.json", "r") as jsonOpt:
			fileObj = json.load(jsonOpt)
			options = SimulatorOptions(fileObj)
			jsonOpt.close()
		return options

	def __from_options(self):
		options = self.__from_json()
		launch = Launcher("/usr/local/bin/rcssserver",options)
		return launch

	def test_launch(self):
		Launcher = self.__from_options()
		launch = Launcher.launch()
		assert Launcher is not None