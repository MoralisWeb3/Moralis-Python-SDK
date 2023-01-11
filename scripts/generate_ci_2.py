from generate.generate_lib import generate_lib
from generate.generate_openapi_clients import generate_openapi_clients
from generate.generate_docs import generate_docs
from generate.generate_prepare import generate_prepare
from generate.generate_cleanup import generate_cleanup

def generate():
    '''
    Phase 2/2 on ci: Generate the moralis modules and docs + cleanup
    '''
    print("🚀 Generating Moralis Python SDK phase 2...")
    generate_lib()
    generate_docs()
    generate_cleanup()
    print("🏁 Done Moralis Python SDK phase 2...")

generate()