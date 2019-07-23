from modules.training_module import TrainingModule
from modules.learner import Learner
from sacademy.factory.app_factory import AppFactory
from sacademy.factory.builder_factory import FactoryBuilder

class ExampleModule(TrainingModule):

    """ call Training_Module inicializator"""
    def __init__(self, module_options: dict, builder: FactoryBuilder) -> None:
        app_factory = AppFactory(builder)
        super().__init__(module_options, app_factory)
        self.learner = Learner()
