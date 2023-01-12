import json
from .swagger import generate_swagger
from .files import save_json, copy_and_replace_folder, remove_folder
from .paths import root_path, src_path, temp_swaggers_path, temp_generated_api_path
from .openapi import generate_openapi
from .apply_patches import apply_patches


def generate_openapi_clients():
    '''
    Generate the openapi clients, used as references in the moralis Lib with following the steps:
    - Fetching the swagger from remote url as defined in api-config.json
    - Processing the swagger to be used by the SDK
    - Generate open-api client based on the swagger
    - Apply patches for custom changes/fixes on the generated open-api clients
    Note: make sure to have have run generate_prepare beforehand
    Note: during this process temporary files (processed swaggers and openapi-clients) are saved locally in a temp folder (/temp)
    '''
    api_definitions = json.load(open(root_path / 'api-config.json'))

    print(f"⏳ start generating openapi client...")

    for api in api_definitions:
        # Generate the swagger
        print(f'⏳ start generating openapi client for {api["name"]}')
        swagger_content = generate_swagger(api["swagger"], api["name"])
        save_json(swagger_content, temp_swaggers_path, api["name"])

        # Generate and replace open-api client
        package_name = generate_openapi(api["name"])
        generated_open_api_folder = temp_generated_api_path / package_name
        destination_openapi_folder = src_path / package_name
        copy_and_replace_folder(generated_open_api_folder,
                                destination_openapi_folder)
        remove_folder(destination_openapi_folder / 'docs')

        print(f'⏳ start generating openapi client for {api["name"]}')

    apply_patches()

    print(f"🏁 done generating openapi clients\n")
