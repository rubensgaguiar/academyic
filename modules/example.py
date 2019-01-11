from os.path import join, dirname, abspath
from modules.training_module import TrainingModule


class ExampleModule(TrainingModule):

    """ call Training_Module inicializator"""
    def __init__(self, module_options: dict) -> None:
        super().__init__(module_options)
