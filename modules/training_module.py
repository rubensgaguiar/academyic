from abc import ABC, abstractmethod
from sacademy.session import Session, AppHub
from sacademy.factory.app_factory import AppFactory


class TrainingException(Exception):
    """ Exception raised by TrainingModule faced with runtime issues. """

    def __init__(self, msg: str = '') -> None:
        super(Exception, self).__init__(msg)


class TrainingModule(ABC):
    """ Abstract class for creating Training descriptions. """
    SESSION_DECLARATION_FIELD = 'session'
    EXTRA_OPTIONS_DECLARATION_FIELD = 'extra-options'

    def __init__(self, module_options: dict, app_factory: AppFactory) -> None:
        self._options = module_options
        if TrainingModule.SESSION_DECLARATION_FIELD not in module_options:
            raise TrainingException(f"There's no field {TrainingModule.SESSION_DECLARATION_FIELD} \
            in the training options.")

        apps_dict = module_options[TrainingModule.SESSION_DECLARATION_FIELD]
        extra_options_dict = module_options[TrainingModule.EXTRA_OPTIONS_DECLARATION_FIELD]
        self._apps = AppHub(app_factory, apps_dict, extra_options_dict)
        self._session = Session()

    def init(self) -> None:
        self._session.create_launchers(self._apps)

    def start(self) -> None:
        self._session.launch_all()

    def reset(self) -> None:
        self._session.reset()

    def stop(self) -> None:
        self._session.stop()
