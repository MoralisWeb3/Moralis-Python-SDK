from generate.generate_swaggers import generate_swaggers
from generate.generate_openapi_clients import generate_openapi_clients
from generate.generate_prepare import generate_prepare

def generate():
    '''
    Phase 1 on ci: Preparation + generate the openapi clients
    Note: after this phase the generated packages need to be installed locally via `pip install -e .`
    '''
    print("🚀 Generating Moralis Python SDK phase 1...")
    generate_prepare()
    generate_swaggers()
    generate_openapi_clients()
    print("🏁 Done Moralis Python SDK phase 1")

generate()