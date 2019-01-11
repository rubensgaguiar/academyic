""" this module contains utilitary operations """
import json
from jsondiff import diff


def load_json(path: str) -> dict:
    with open(path, "r") as json_opt:
        file_obj = json.load(json_opt)
        json_opt.close()
    return file_obj


def diff_json(json1: dict, json2: dict) -> dict:
    return diff(json1, json2)
