import json
import time

from sacademy.session import SessionDeclarationException, Team, AppHub, Session
from sacademy.factory.builder_factory import FactoryBuilder
from sacademy.factory.app_factory import AppFactory


class TestSessionDeclarationException:

    def test_session_declaration_exception(self):
        raised_message = str(SessionDeclarationException("oi"))
        assert raised_message is "oi"


class TestTeam:

    def test_list_players(self):
        team = Team()
        assert team.players == []

    def test_optional_coach(self):
        team = Team()
        assert team.coach is None


class TestAppHub:

    @staticmethod
    def __options_from_json() -> dict:
        with open('tests/conf/sacademy.json', "r") as file_obj:
            options = json.load(file_obj)
            # app['options']['game_log_dir'] = path.join(path.dirname(path.abspath(__file__)), '../logs')
            # app['options']['text_log_dir'] = path.join(path.dirname(path.abspath(__file__)), '../logs')
            file_obj.close()
        return options

    def __app_factory_from_options(self) -> AppFactory:
        options = self.__options_from_json()
        factory = FactoryBuilder(options)
        return AppFactory(factory)

    def __session_declaration(self) -> dict:
        options = self.__options_from_json()
        with open('tests/conf/modules/' + options['training-module'] + '.json', "r") as file_obj:
            session_declaration = json.load(file_obj)
            file_obj.close()
        return session_declaration['session']

    def __app_hub(self):
        app_factory = self.__app_factory_from_options()
        session_declaration = self.__session_declaration()
        return AppHub(app_factory, session_declaration)

    def test_left_players(self):
        factory = self.__app_factory_from_options()
        app_hub = self.__app_hub()
        list_player = []
        player = factory.new_player('itandroids_npc')
        list_player.append(player)
        player = factory.new_player('itandroids_actor')
        list_player.append(player)
        player = factory.new_player('itandroids_support')
        list_player.append(player)
        i = 0
        bool = True
        for player in list_player:
            if bool is True:
                bool = player.options.params['mode'] == app_hub.left_team.players[i].options.params['mode']
                i += 1
        assert bool is True

    def test_left_coach(self):
        factory = self.__app_factory_from_options()
        app_hub = self.__app_hub()
        coach = factory.new_coach('itandroids_trainer')
        assert coach.options.params['mode'] == app_hub.left_coach.options.params['mode']

    def test_right_players(self):
        factory = self.__app_factory_from_options()
        app_hub = self.__app_hub()
        list_player = []
        player = factory.new_player('itandroids_npc')
        list_player.append(player)
        list_player.append(player)
        list_player.append(player)
        i = 0
        bool = True
        for player in list_player:
            if bool is True:
                bool = player.options.params['mode'] == app_hub.right_team.players[i].options.params['mode']
                i += 1
        assert bool is True

    def test_right_coach(self):
        factory = self.__app_factory_from_options()
        app_hub = self.__app_hub()
        coach = factory.new_coach('itandroids_trainer')
        assert coach.options.params['mode'] == app_hub.right_coach.options.params['mode']


class TestSession:

    @staticmethod
    def __options_from_json() -> dict:
        with open('tests/conf/sacademy.json', "r") as file_obj:
            options = json.load(file_obj)
            # app['options']['game_log_dir'] = path.join(path.dirname(path.abspath(__file__)), '../logs')
            # app['options']['text_log_dir'] = path.join(path.dirname(path.abspath(__file__)), '../logs')
            file_obj.close()
        return options

    def __app_factory_from_options(self) -> AppFactory:
        options = self.__options_from_json()
        factory = FactoryBuilder(options)
        return AppFactory(factory)

    def __session_declaration(self) -> dict:
        options = self.__options_from_json()
        with open('tests/conf/modules/' + options['training-module'] + '.json', "r") as file_obj:
            session_declaration = json.load(file_obj)
            file_obj.close()
        return session_declaration['session']

    def __app_hub(self):
        app_factory = self.__app_factory_from_options()
        session_declaration = self.__session_declaration()
        return AppHub(app_factory, session_declaration)

    def test_session(self):
        self._session = Session()
        self._apps = self.__app_hub()
        self._session.create_launchers(self._apps)
        assert self._session.status == 'READY'
        self._session.launch_all()
        assert self._session.status == 'LAUNCHING'
        time.sleep(5)
        self._session.stop()
        assert self._session.status == 'STOPPED'
        time.sleep(5)
