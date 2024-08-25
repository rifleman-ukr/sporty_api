import json
from os import path


def schema(template_name):
    with open(path.join(path.dirname(path.abspath(__file__)),
                        path.join('templates', f'{template_name}.json'))) as schema_json:
        return json.load(schema_json)
