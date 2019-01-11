from sacademy import factory
import sacademy.utils as utils


class Academy:
    """
        Main Soccer Academy orchestrator.
    """

    """ receive dict but without verify params"""
    def __init__(self, options: dict) -> None:
        self.options = options

    def exit(self) -> None:
        """
            Handles interruption and exits safely
        :return:
        """
        raise NotImplementedError

    def run(self) -> None:
        """
            Main call
        :return:
        """
        module_options = load_json("conf/modules/example.json")
        self.module = new_module("example", module_options)

        self.module.start_module()
