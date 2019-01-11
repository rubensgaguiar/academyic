from typing import Type

from sacademy.launcher import LauncherOptions, SimulatorOptions, WindowOptions

from modules.training_module import TrainingModule
from modules.example import ExampleModule

TRAINING_MODULES_KEYMAP = {
    "example": ExampleModule
}

OPTIONS_KEYMAP = {
    "simulator": SimulatorOptions,
    "window": WindowOptions
}


def new_option(option: str, *args) -> LauncherOptions:
    try:
        return OPTIONS_KEYMAP[option](args)
    except KeyError:
        raise ValueError


def new_module(module: str, *args) -> TrainingModule:
    try:
        return TRAINING_MODULES_KEYMAP[module](args)
    except KeyError:
        raise ValueError
