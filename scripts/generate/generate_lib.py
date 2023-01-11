import json
from .swagger import generate_swagger
from .files import ensure_temp_folder, save_json, copy_and_replace_folder, remove_folder
from .paths import root_path, src_path, temp_swaggers_path, temp_generated_api_path
from .openapi import generate_openapi
from .MoralisModule import generate_modules
from .apply_patches import apply_patches

def generate_lib():
    '''
    Generate the Moralis Lib following the steps:
    - Fetching the swagger from remote url as defined in api-config.json
    - Processing the swagger to be used by the SDK
    - Generate open-api client based on the swagger
    - Generate the SDK modules based on the open-api client (to make the experience more uniform with other SDKs and user friendly)
    Note: during this process temporary files (processed swaggers and openapi-clients) are saved locally in a temp folder (/temp), and cleaned up at the end
    '''
    api_definitions = json.load(open(root_path / 'api-config.json'))

    print(f"⏳ start generating lib...")

    ensure_temp_folder()

    for api in api_definitions:
        # Prepare 
        print(f'⏳ start generating lib for {api["name"]}')
        swagger_content = generate_swagger(api["swagger"], api["name"])
        save_json(swagger_content, temp_swaggers_path, api["name"])
        
        # TODO: this is using an older version of the generator??
        # Generate and replace open-api client
        package_name = generate_openapi(api["name"])
        generated_open_api_folder = temp_generated_api_path / package_name
        destination_openapi_folder = src_path / package_name
        copy_and_replace_folder(generated_open_api_folder, destination_openapi_folder)
        remove_folder(destination_openapi_folder / 'docs')
        
        # Regenerate and replace SDK modules
        generate_modules(api["name"], api["security_key"])



        print(f'⏳ start generating lib for {api["name"]}')


    apply_patches()

    print(f"✅ done generating lib")
