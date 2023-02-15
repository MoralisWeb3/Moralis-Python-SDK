from .MoralisModule import generate_modules
from .api_config import get_api_config


def generate_lib():
    '''
    Generate the Moralis Lib based on the generated openapi clients
    Note make sure that openapi clients are generated beforehand via `python scripts/generate/generate_openapi.py`
    Note make sure that the generated openapi clients are installed locally beforehand via `pip install -e .` in the root folder
    '''
    print(f"⏳ start generating lib...")

    for api in get_api_config():
        print(f'⏳ start generating lib for {api["name"]}')
        generate_modules(api["name"], api["security_key"], api["sub_networks"] if "sub_networks" in api else None)
        print(f'⏳ start generating lib for {api["name"]}')

    print(f"🏁 done generating lib\n")
