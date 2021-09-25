import json


def read_from_json(json_path):
    with open(json_path) as json_file:
        json_data = json.load(json_file)
        json_file.close()
        return json_data


