from os import listdir, makedirs
from os.path import abspath, join, dirname, exists
from shutil import copyfile
from setuptools import setup, find_packages

PROJECT_PATH = dirname(abspath(__file__))
CONF_PATH = join(PROJECT_PATH, "conf/")
ACADEMY_CONF_PATH = join(CONF_PATH, "sacademy/")
ACADEMY_DEFAULT_CONF_PATH = join(ACADEMY_CONF_PATH, "default/")

# Create configuration files from default conf files
try:
    for file in listdir(ACADEMY_DEFAULT_CONF_PATH):
        if file.endswith(".json"):
            file_src = join(ACADEMY_DEFAULT_CONF_PATH, file)
            file_dest = join(ACADEMY_CONF_PATH, file)
            copyfile(file_src, file_dest)
except OSError:
    print("An error occured while setting up the configuration files. Please verify project structure integrity.")
    exit()

# Packaging setup

setup(
    name="sacademy",
    version="0.1",
    description="A general purpose reinforcement learning environment for the Soccer Simulation 2D League.",
#   license="",
    author="ITAndroids Soccer2D",
    author_email="itandroids-soccer2d@googlegroups.com",
#    url="",
    packages=find_packages(),
    tests_require=["pytest"],
    setup_requires=["pytest-runner"],
)