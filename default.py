import json


def get(default):
    try:
        with open(default, "r") as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found.")
