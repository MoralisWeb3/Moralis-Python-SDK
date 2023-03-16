import json
from .swagger import generate_swagger
from .files import save_json
from .paths import temp_swaggers_path
from .api_config import get_api_config


def generate_swaggers():
    '''
    Generate and process the swagger, that is used for the open-api-generator with following the steps:
    - Fetching the swagger from remote url as defined in api-config.json
    - Processing the swagger to be used by the SDK
    Note: make sure to have have run generate_prepare beforehand
    Note: during this process temporary files are saved locally in a temp folder (/temp)
    '''
    print(f"⏳ start generating swaggers...")

    for api in get_api_config():
        print(f'⏳ start generating swagger  for {api["name"]}')
        swagger_content = generate_swagger(
            swagger_url=api["swagger"],
            api_name=api["name"],
            overwrite_host=api["overwrite_host"] if "overwrite_host" in api else None
        )
        save_json(swagger_content, temp_swaggers_path, api["name"])
        print(f'⏳ start generating swagger  for {api["name"]}')

    print(f"🏁 done generating swaggers\n")
