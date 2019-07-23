import time
from os.path import join, dirname, normpath, abspath

from sacademy.academy import Academy
from sacademy.utils import load_json

PROJECT_PATH = dirname(abspath(__file__))
MODULE_PATH = normpath(join(PROJECT_PATH, "conf"))


def main():
    conf_file_path = join(MODULE_PATH, "sacademy.json")
    try:
        academy_options = load_json(conf_file_path)
    except FileNotFoundError:
        print(f"ERROR: Failed to load sacademy.json at {conf_file_path}")
        exit(1)

    academy = Academy(academy_options)

    try:
        academy.run()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        academy.exit()
        time.sleep(3)


if __name__ == '__main__':
    main()
