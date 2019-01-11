from abc import ABC, abstractmethod
from functools import reduce
from sacademy import utils
import subprocess


class LauncherOptions(ABC):

    def __init__(self, param_map: dict) -> None:
        self.params = param_map
        self.diff_params = None
        self._verify_params()

    @abstractmethod
    def _verify_params(self) -> None:
        """ Verify if object params are structured as expected by the program to be launched."""
        raise NotImplementedError

    @abstractmethod
    def _load_default_values(self) -> str:
        """ Load json defaul."""
        raise NotImplementedError
        
    @abstractmethod
    def serialize(self) -> str:
        """ Translate object params to the program command line options string format."""
        raise NotImplementedError


class SimulatorOptions(LauncherOptions):
    """ Class that wraps launching options to the rcssserver simulator."""

    OPTIONS = {
        'include'
    }
    SERVER_OPTIONS = {
        'version',
        'catch_ban_cycle',
        'clang_advice_win',
        'clang_define_win',
        'clang_del_win',
        'clang_info_win',
        'clang_mess_delay',
        'clang_mess_per_cycle',
        'clang_meta_win',
        'clang_rule_win',
        'clang_win_size',
        'coach_port',
        'connect_wait',
        'drop_ball_time',
        'extra_half_time',
        'foul_cycles',
        'freeform_send_period',
        'freeform_wait_period',
        'game_log_compression',
        'game_log_version',
        'game_over_wait',
        'goalie_max_moves',
        'half_time',
        'hear_decay',
        'hear_inc',
        'hear_max',
        'keepaway_start',
        'kick_off_wait',
        'max_goal_kicks',
        'max_monitors',
        'nr_extra_halfs',
        'nr_normal_halfs',
        'olcoach_port',
        'pen_before_setup_wait',
        'pen_max_extra_kicks',
        'pen_nr_kicks',
        'pen_ready_wait',
        'pen_setup_wait',
        'pen_taken_wait',
        'point_to_ban',
        'point_to_duration',
        'port',
        'recv_step',
        'say_coach_cnt_max',
        'say_coach_msg_size',
        'say_msg_size',
        'send_step',
        'send_vi_step',
        'sense_body_step',
        'simulator_step',
        'slow_down_factor',
        'start_goal_l',
        'start_goal_r',
        'synch_micro_sleep',
        'synch_offset',
        'synch_see_offset',
        'tackle_cycles',
        'text_log_compression',
        'auto_mode',
        'back_passes',
        'coach',
        'coach_w_referee',
        'forbid_kick_off_offside',
        'free_kick_faults',
        'fullstate_l',
        'fullstate_r',
        'game_log_dated',
        'game_log_fixed',
        'game_logging',
        'golden_goal',
        'keepaway',
        'keepaway_log_dated',
        'keepaway_log_fixed',
        'keepaway_logging',
        'log_times',
        'old_coach_hear',
        'pen_allow_mult_kicks',
        'pen_coach_moves_players',
        'pen_random_winner',
        'penalty_shoot_outs',
        'profile',
        'proper_goal_kicks',
        'record_messages',
        'send_comms',
        'synch_mode',
        'team_actuator_noise',
        'text_log_dated',
        'text_log_fixed',
        'text_logging',
        'use_offside',
        'verbose',
        'wind_none',
        'wind_random',
        'audio_cut_dist',
        'back_dash_rate',
        'ball_accel_max',
        'ball_decay',
        'ball_rand',
        'ball_size',
        'ball_speed_max',
        'ball_stuck_area',
        'ball_weight',
        'catch_probability',
        'catchable_area_l',
        'catchable_area_w',
        'ckick_margin',
        'control_radius',
        'dash_angle_step',
        'dash_power_rate',
        'effort_dec',
        'effort_dec_thr',
        'effort_inc',
        'effort_inc_thr',
        'effort_init',
        'effort_min',
        'extra_stamina',
        'foul_detect_probability',
        'foul_exponent',
        'goal_width',
        'inertia_moment',
        'keepaway_length',
        'keepaway_width',
        'kick_power_rate',
        'kick_rand',
        'kick_rand_factor_l',
        'kick_rand_factor_r',
        'kickable_margin',
        'max_back_tackle_power',
        'max_dash_angle',
        'max_dash_power',
        'max_tackle_power',
        'maxmoment',
        'maxneckang',
        'maxneckmoment',
        'maxpower',
        'min_dash_angle',
        'min_dash_power',
        'minmoment',
        'minneckang',
        'minneckmoment',
        'minpower',
        'offside_active_area_size',
        'offside_kick_margin',
        'pen_dist_x',
        'pen_max_goalie_dist_x',
        'player_accel_max',
        'player_decay',
        'player_rand',
        'player_size',
        'player_speed_max',
        'player_speed_max_min',
        'player_weight',
        'prand_factor_l',
        'prand_factor_r',
        'quantize_step',
        'quantize_step_l',
        'recover_dec',
        'recover_dec_thr',
        'recover_init',
        'recover_min',
        'red_card_probability',
        'side_dash_rate',
        'slowness_on_top_for_left_team',
        'slowness_on_top_for_right_team',
        'stamina_capacity',
        'stamina_inc_max',
        'stamina_max',
        'stopped_ball_vel',
        'tackle_back_dist',
        'tackle_dist',
        'tackle_exponent',
        'tackle_power_rate',
        'tackle_rand_factor',
        'tackle_width',
        'visible_angle',
        'visible_distance',
        'wind_ang',
        'wind_dir',
        'wind_force',
        'wind_rand',
        'coach_msg_file',
        'game_log_dir',
        'game_log_fixed_name',
        'keepaway_log_dir',
        'keepaway_log_fixed_name',
        'landmark_file',
        'log_date_format',
        'team_l_start',
        'team_r_start',
        'text_log_dir',
        'text_log_fixed_name'
    }
    PLAYER_OPTIONS = {
        'version',
        'player_types',
        'pt_max',
        'random_seed',
        'subs_max',
        'allow_mult_default_type',
        'catchable_area_l_stretch_max',
        'catchable_area_l_stretch_min',
        'dash_power_rate_delta_max',
        'dash_power_rate_delta_min',
        'effort_max_delta_factor',
        'effort_min_delta_factor',
        'extra_stamina_delta_max',
        'extra_stamina_delta_min',
        'foul_detect_probability_delta_factor',
        'inertia_moment_delta_factor',
        'kick_power_rate_delta_max',
        'kick_power_rate_delta_min',
        'kick_rand_delta_factor',
        'kickable_margin_delta_max',
        'kickable_margin_delta_min',
        'new_dash_power_rate_delta_max',
        'new_dash_power_rate_delta_min',
        'new_stamina_inc_max_delta_factor',
        'player_decay_delta_max',
        'player_decay_delta_min',
        'player_size_delta_factor',
        'player_speed_max_delta_max',
        'player_speed_max_delta_min',
        'stamina_inc_max_delta_factor'
    }
    CSVSAVER_OPTIONS = {
        'version',
        'save',
        'filename'
    }
    NAMESPACES = {
        'server': SERVER_OPTIONS,
        'player': PLAYER_OPTIONS,
        'csvsaver': CSVSAVER_OPTIONS
    }

    def __init__(self, options: dict) -> None:
        super().__init__(options)
        self.__verify_namespaces_params()
        self._load_default_values()

    def _verify_params(self) -> None:
        expected_params = SimulatorOptions.OPTIONS | SimulatorOptions.NAMESPACES.keys()

        for param in self.params['options']:
            if param not in expected_params:
                print(f"Parameter {param} received not in expected param list")

        for param in expected_params:
            if param not in self.params['options']:
                print(f"Expected parameter {param} not in received param map")

    def __verify_namespaces_params(self) -> None:
        """ Verify if simulator's namespaces options are structured as expected by the simulator."""

        for namespace in SimulatorOptions.NAMESPACES:
            namespace_params = SimulatorOptions.NAMESPACES[namespace]
            serialized_params = self.params['options'][namespace]

            for param in serialized_params:
                if param not in namespace_params:
                    print(f"Parameter {param} in serialized params not in namespace params")

            for param in namespace_params:
                if param not in serialized_params:
                    print(f"Parameter {param} in namespace params not in serialized params")

    def _load_default_values(self) -> None:
        """ Load json and create a default params objetc"""
        self.default_params = utils.load_json("conf/sacademy/default/simulator.json")

    def jsons_diff(self) -> None:
        """ json object was created by difference of default parameters and input parameters"""
        self.diff_params = utils.diff_json(self.default_params, self.params)

    def adapt_string(self, namespace: str, option: str) -> str:
        """ Adapt string to cmd line."""
        if type(self.diff_params['options'][namespace][option]) is str:
            return f" {namespace}::{option}='{self.diff_params['options'][namespace][option]}'"
        elif self.diff_params['options'][namespace][option] is True:
            return f" {namespace}::{option}=true"
        elif self.diff_params['options'][namespace][option] is False:
            return f" {namespace}::{option}=false"
        elif self.diff_params['options'][namespace][option] is int or float:
            return f" {namespace}::{option}={self.diff_params['options'][namespace][option]}"
        else:
            return ""

    def serialize(self) -> str:
        # Check desire to overwrite simulator settings with an include file
        self.jsons_diff()
        if self.params['options']['include'] != "":
            return reduce(lambda serialized, option: serialized + f" {option}={self.params['options'][option]}",
                          SimulatorOptions.OPTIONS,
                          "")

        return reduce(lambda serialized, namespace: serialized + self.__serialize_namespace(namespace),
                      SimulatorOptions.NAMESPACES,
                      "")

    def __serialize_namespace(self, namespace: str) -> str:
        """ Serialize specific namespace options into command line structure."""
        if 'options' in self.diff_params:
            if namespace in self.diff_params['options']:
                return reduce(lambda joined, option: joined + self.adapt_string(namespace, option),
                              self.diff_params['options'][namespace],
                              "")
            else:
                return ""
        else:
            return ""

    def set_synch_mode(self, synch_mode: bool) -> None:
        self.params['options']['server']['sync_mode'] = synch_mode

    # TODO: CORRIGIR A INDEXAÇÃO DO DICIONARIO
    def set_penalty_only(self, penalty_only: bool) -> None:
        """ Changes params to no penalty shootouts only penalty shootouts.

            Parameters
            ----------
            penalty_only : bool
                Penalty Only setting flag.
        """
        self.params["penalty_shoot_outs"] = penalty_only
        if penalty_only:
            self.params["nr_extra_halfs"] = 0
            self.params["nr_normal_halfs"] = 0
        else:
            self.params["nr_extra_halfs"] = 2
            self.params["nr_normal_halfs"] = 2


class WindowOptions(LauncherOptions):
    """ Class that wraps launching options to the window."""

    MONITOR_CLIENT_OPTIONS = {
        'connect',
        'host',
        'port',
        'client-version',
        'wait-seconds',
        'auto-quit-mode',
        'kill-server',
        'server-pid',
        'server-path',
        'time-shift-replay'
    }
    LOG_PLAYER_OPTIONS = {
        'game-log',
        'game-log-dir',
        'auto-loop-mode',
        'time-interval'
    }
    WINDOW_OPTIONS = {
        'geometry',
        'maximize',
        'full-screen',
        'canvas-size',
        'tool-bar-area',
        'hide-menu-bar',
        'hide-tool-bar',
        'hide-status-bar'
    }
    VIEW_OPTIONS = {
        'anonymous-mode',
        'paint-style',
        'field-grass-type',
        'keepaway-mode',
        'show-score-board',
        'hide-score-board',
        'show-team-graphic',
        'hide-team-grahip',
        'anti-aliasing',
        'gradient',
        'reverse-side',
        'player-reverse-draw',
        'show-player-number',
        'hide-player-number',
        'show-player-type',
        'hide-player-type',
        'show-view-area',
        'hide-view-area',
        'show-pointto',
        'hide-pointto',
        'show-attentionto',
        'hide-attentionto',
        'show-stamina',
        'hide-stamina',
        'show-stamina-capacity',
        'hide-stamina-capacity',
        'show-card',
        'hide-card',
        'enlarge-mode',
        'ball-size',
        'player-size'
    }
    DEBUG_SERVER_OPTIONS = {
        'debug-server-mode',
        'debug-server-port',
        'debug-log-dir'
    }
    DEBUG_VIEW_OPTIONS = {
        'show-debug-view',
        'hide-debug-view',
        'show-debug-view-ball',
        'hide-debug-view-ball',
        'show-debug-view-self',
        'hide-debug-view-self',
        'show-debug-view-teammates',
        'hide-debug-view-teammates',
        'show-debug-view-opponents',
        'hide-debug-view-opponents',
        'show-debug-view-comment',
        'hide-debug-view-comment',
        'show-debug-view-shape',
        'hide-debug-view-shape',
        'show-debug-view-target',
        'hide-debug-view-target',
        'show-debug-view-message',
        'hide-debug-view-message',
        'show-debug-log-objects',
        'hide-debug-log-objects'
    }
    IMAGE_SAVE_OPTIONS = {
        'auto-image-save',
        'image-save-dir',
        'image-name-prefix',
        'image-save-format'
    }
    NAMESPACES = {
        'monitor_client': MONITOR_CLIENT_OPTIONS,
        'log_player': LOG_PLAYER_OPTIONS,
        'window': WINDOW_OPTIONS,
        'view': VIEW_OPTIONS,
        'debug_server': DEBUG_SERVER_OPTIONS,
        'debug_view': DEBUG_VIEW_OPTIONS,
        'image_save': IMAGE_SAVE_OPTIONS
    }

    def __init__(self, options: dict) -> None:
        super().__init__(options)
        self.__verify_namespaces_params()
        self._load_default_values()

    def _verify_params(self) -> None:
        expected_params = WindowOptions.NAMESPACES.keys()

        for param in self.params['options']:
            if param not in expected_params:
                print(f"Parameter {param} received is not in expected param list")

        for param in expected_params:
            if param not in self.params['options']:
                print(f"Expected parameter {param} in received param map")

    def __verify_namespaces_params(self) -> None:
        """ Verify if window's namespaces options are structured as expected by the window."""

        for namespace in WindowOptions.NAMESPACES:
            namespace_params = WindowOptions.NAMESPACES[namespace]
            serialized_params = self.params['options'][namespace]

            for param in serialized_params:
                if param not in namespace_params:
                    print(f"Parameter {param} in serialized params is not in namespace params")

            for param in namespace_params:
                if param not in serialized_params:
                    print(f"Parameter {param} in namespace params is not in serialized params")

    def _load_default_values(self) -> None:
        """ Load json and create a default params objetc"""
        self.default_params = utils.load_json("conf/sacademy/default/window.json")

    def jsons_diff(self) -> None:
        """ json object was created by difference of default parameters and input parameters"""
        self.diff_params = utils.diff_json(self.default_params,self.params)

    def adapt_string(self, namespace: str, option: str) -> str:
        """ Adapt string to cmd line."""
        if self.diff_params['options'][namespace][option] == "off":
            return f" --{option}=off"
        elif self.diff_params['options'][namespace][option] == "on":
            return f" --{option}=on"
        elif self.diff_params['options'][namespace][option] == True:
            return f" --{option}=true"
        elif self.diff_params['options'][namespace][option] == False:
            return f" --{option}=false"
        elif type(self.diff_params['options'][namespace][option]) is (int or float):
            return f" --{option}={self.diff_params['options'][namespace][option]}"
        elif type(self.diff_params['options'][namespace][option]) is str:
            return f" --{option}=\"{self.diff_params['options'][namespace][option]}\""
        else:
            return ""

    def serialize(self) -> str:
        # Check desire to overwrite window settings with an include file
        self.jsons_diff()
        return reduce(lambda serialized, namespace: serialized + self.__serialize_namespace(namespace),
                      WindowOptions.NAMESPACES,
                      "")

    def __serialize_namespace(self, namespace: str) -> str:
        """ Serialize specific namespace options into command line structure."""
        if 'options' in self.diff_params:
            if namespace in self.diff_params['options']:
                return reduce(lambda joined, option: joined + self.adapt_string(namespace,option),
                              self.diff_params['options'][namespace],
                              "")
            else:
                return ""
        else:
            return ""

    def set_port(self, port: int) -> None:
        self.params['options']['monitor_client']['port'] = port


class PlayerOptions(LauncherOptions):

    REQUIRED_FIELDS = {
        "mode",
        "module-name",
        "options"
    }

    def __init__(self, params: dict) -> None:
        super().__init__(params)
        self.params = params


class LauncherException(Exception):
    """ Exception class to handle unsuccessfull launching."""

    def __init__(self, launchedcmd: str, return_code: int) -> None:
        super(Exception, self).__init__(f"Execution of {launchedcmd} failed. Exited with status code {return_code}.")
        self.launchedcmd = launchedcmd
        self.return_code = return_code


class Launcher:
    """ Class responsible for launching a given task in a separate process through the OS."""

    def __init__(self, binpath: str=None, options: LauncherOptions=None) -> None:
        self.binpath = binpath
        self.options = options

    def launch(self) -> None:
        """ Launches the binary path set with the option list set"""
        if self.binpath is None:
            raise RuntimeError("No launching path set.")
        
        cmdline_options = self.options.serialize() if self.options is not None else ""
        cmd = ""
        try:
            process = subprocess.run(f"{self.binpath} {cmdline_options}", check=True, shell=True)
            returncode = process.returncode
        except subprocess.CalledProcessError as error:
            cmd = error.cmd
            returncode = error.returncode

        if returncode != 0:
            raise LauncherException(cmd, returncode)
