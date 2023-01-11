import json
from .swagger import generate_swagger
from .files import ensure_temp_folder, save_json, copy_and_replace_folder, remove_folder
from .paths import root_path, src_path, temp_swaggers_path, temp_generated_api_path
from .openapi import generate_openapi
from .MoralisModule import generate_modules
from .apply_patches import apply_patches

def generate_lib():
    '''
    Part 2/3 of generation process
    Generate the Moralis Lib based on the generated openapi clients
    Note make sure that the generated openapi clients are installed locally beforehand via `pip install -e .` in the root folder
    '''
    api_definitions = json.load(open(root_path / 'api-config.json'))

    print(f"⏳ start generating lib...")


    for api in api_definitions:
        print(f'⏳ start generating lib for {api["name"]}')
        generate_modules(api["name"], api["security_key"])
        print(f'⏳ start generating lib for {api["name"]}')

    print(f"✅ done generating lib")
