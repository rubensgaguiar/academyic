import json
import time
from os.path import join, dirname, abspath

from sacademy import utils
from sacademy.factory.builder_factory import FactoryBuilder

from sacademy.factory.module_factory import ModuleFactory


class TestExampleModule:

    @staticmethod
    def __load_example():
        with open('tests/conf/sacademy.json', "r") as file_obj:
            academy_options = json.load(file_obj)
            file_obj.close()
        return academy_options

    def test_module(self):
        academy_options = self.__load_example()
        factory = FactoryBuilder(academy_options)
        module_factory = ModuleFactory(factory)
        module = module_factory.new_module()
        assert module.init() is None
        assert module.start() is None
        time.sleep(3)
        assert module.reset() is None
        time.sleep(3)
        module.init()
        time.sleep(3)
        module.start()
        time.sleep(3)
        assert module.stop() is None
        time.sleep(3)
