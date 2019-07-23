from os.path import join, dirname, normpath

from sacademy import utils

from modules.training_module import TrainingModule
from modules.example import ExampleModule
from sacademy.factory.builder_factory import FactoryBuilder

PROJECT_PATH = dirname(normpath(__file__))
MODULE_PATH = normpath(join(PROJECT_PATH, "../../conf/modules"))


class ModuleFactory:
    TRAINING_MODULES_KEYMAP = {
        "example": ExampleModule
    }

    def __init__(self, builder: FactoryBuilder):
        self.builder = builder

    def new_module(self) -> TrainingModule:
        try:
            module_path_file = join(MODULE_PATH, self.builder.module + '.json')
        except KeyError:
            raise FileNotFoundError
        module_options = utils.load_json(module_path_file)
        try:
            return self.TRAINING_MODULES_KEYMAP[self.builder.module](module_options, self.builder)
        except KeyError:
            raise ValueError
