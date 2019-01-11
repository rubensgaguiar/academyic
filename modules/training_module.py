from abc import ABC, abstractmethod
from os.path import join, dirname, abspath
import sacademy.utils as utils

class TrainingModule(ABC):

    """ receive dict but without verify params"""
    def __init__(self, module_map: dict) -> None:
        self.module_map = module_map
        self.session_conf = SessionConf(self.module_map['session'])
        __create_session()

    def __create_session(self) -> None:
        _modify_session_conf()
        self.session = Session(self.session_conf)

    def start_module(self) -> None:
        self.session.launch_all()

    def _modify_session_conf(self) -> None:
        """ modify SessionConf"""
        self.module_map['session']['players']['left'] = [] #
        
        """ update SessionConf"""
        self.session_conf = SessionConf(self.module_map['session'])

    def _update_session(self) -> None:
        _modify_session_conf()
        self.session.set_conf(self.session_conf)
