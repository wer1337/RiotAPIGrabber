import json


def get_champ_name():
    # Loads the json file
    with open("tools/champion.json") as f:
        loaded_json = json.load(f)

    return loaded_json
