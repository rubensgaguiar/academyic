from sacademy.factory.builder_factory import FactoryBuilder
from sacademy.factory.module_factory import ModuleFactory


class Academy:
    """
        Main Soccer Academy orchestrator.
    """

    def __init__(self, options: dict) -> None:
        self.options = options
        self.factory = FactoryBuilder(options)
        self.module_factory = ModuleFactory(self.factory)
        self.module = self.module_factory.new_module()
        self.module.init()

    def exit(self) -> None:
        """
            Handles interruption and exits safely
        :return:
        """
        self.module.stop()

    def run(self) -> None:
        """
            Main call
        :return:
        """
        self.module.start()
