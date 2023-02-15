from .files import copy_and_replace_folder, remove_folder
from .paths import src_path, temp_generated_api_path
from .openapi import generate_openapi
from .apply_patches import apply_patches
from .api_config import get_api_config

def generate_openapi_clients():
    '''
    Generate the openapi clients, used as references in the moralis Lib with following the steps:
    - Generate open-api client based on the swagger
    - Apply patches for custom changes/fixes on the generated open-api clients
    Note: make sure to have have run generate_swagger beforehand
    Note: during this process temporary files are saved locally in a temp folder (/temp)
    '''

    print(f"⏳ start generating openapi client...")

    for api in get_api_config():
        package_name = generate_openapi(api["name"])
        generated_open_api_folder = temp_generated_api_path / package_name
        destination_openapi_folder = src_path / package_name
        copy_and_replace_folder(generated_open_api_folder,
                                destination_openapi_folder)
        remove_folder(destination_openapi_folder / 'docs')

        print(f'⏳ start generating openapi client for {api["name"]}')

    apply_patches()

    print(f"🏁 done generating openapi clients\n")
