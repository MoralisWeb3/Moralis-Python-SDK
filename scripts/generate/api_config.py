import json
from .paths import root_path


def get_api_config():
    config = json.load(open(root_path / 'api-config.json'))
    api_definitions = config["apis"]
    return [definition for definition in api_definitions if not ('skip' in definition and definition.get("skip") == True)]
