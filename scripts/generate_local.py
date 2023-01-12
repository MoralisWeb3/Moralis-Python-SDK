from generate.generate_lib import generate_lib
from generate.generate_openapi_clients import generate_openapi_clients
from generate.generate_docs import generate_docs
from generate.generate_prepare import generate_prepare
from generate.generate_cleanup import generate_cleanup


def generate():
    '''
    Generate the lib and docs locally
    Note: on CI this is done in seperate steps to ensure that the generated openapi-clients are installed correctly
    '''
    print("🚀 Generating Moralis Python SDK...")
    generate_prepare()
    generate_openapi_clients()
    generate_lib()
    generate_docs()
    generate_cleanup()
    print("🎉 Done Generating Moralis Python SDK")


generate()
