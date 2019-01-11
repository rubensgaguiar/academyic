from os.path import join, dirname, abspath

from sacademy.academy import Academy
from sacademy.utils import load_json


PROJECT_PATH = dirname(abspath(__file__))
CONF_PATH = join(PROJECT_PATH, "conf/")


def main():
    conf_file_path = CONF_PATH.join("sacademy.json")
    try:
        academy_options = load_json(conf_file_path)
    finally:
        print(f"ERROR: Failed to load sacademy.json at {conf_file_path}")
        exit(1)

    academy = Academy(academy_options)

    try:
        academy.run()
    except KeyboardInterrupt:
        academy.exit()


if __name__ == '__main__':
    main()
