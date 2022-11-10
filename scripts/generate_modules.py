# Generate all modules based on the generated open-api clients

import inspect
import os
from pathlib import Path
from distutils.dir_util import copy_tree
import json
import importlib
import shutil

root_path = Path(__file__).parent.parent
moralis_module_path = (root_path / 'src/moralis')


def make_module_base_code(api_name, tag, api_client_name, security_key):
    return f'''
import openapi_{api_name}
from openapi_{api_name}.apis.tags import {tag}_api
import json
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_{api_name}.Configuration()
    configuration.api_key['{security_key}'] = api_key
    api_client = openapi_{api_name}.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = {tag}_api.{api_client_name}(api_client)
    api_client.close()

    return api_instance

'''


def make_operation_snippet(function_name):
    return f'''
def {function_name}(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.{function_name}(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)

'''


def make_utililities():
    return '''
import pkg_resources


def get_common_headers():
    """Get the headers for the requests."""
    return {
        "x-moralis-platform": 'Python SDK',
        "x-moralis-build-target": 'python',
        "x-moralis-build-target": pkg_resources.get_distribution('moralis').version,
    }
 
'''


def api_operation_predicate(o):
    if inspect.isfunction(o) and not o.__name__.startswith("_"):
        return True
    else:
        return False


def get_function_names(api_name, tag, api_client_name):
    api = getattr(importlib.import_module(
        f'openapi_{api_name}.apis.tags'), f'{tag}_api')
    api_instance = dict(inspect.getmembers(api))[api_client_name]
    functions = inspect.getmembers(
        api_instance, predicate=api_operation_predicate)

    return functions


def make_module(api_name, tag, api_client_name, security_key):
    print(f"⏳ Generating modules for {api_name} [{tag}]...")
    module_path = moralis_module_path / api_name / tag.value

    if not os.path.exists(module_path):
        os.makedirs(module_path)

    functions = get_function_names(api_name, tag, api_client_name)

    with open(module_path / '__init__.py', 'w') as f:
        f.write(f'from .{tag} import *\n')

    with open(module_path / f'{tag}.py', 'w') as f:
        f.write(make_module_base_code(
            api_name, tag, api_client_name, security_key))
        for function_name in functions:
            f.write(make_operation_snippet(function_name[0]))

    print(f"✅ Generated modules for {api_name} [{tag}]")


def cleanup_modules(api_name, modules_path):
    print(f"⏳ Removing modules for {api_name}...")
    if modules_path.exists() and modules_path.is_dir():
        shutil.rmtree(modules_path)
    print(f"✅ Removed modules for {api_name}")


def make_modules(api_name, security_key):
    print(f"⏳ Generating modules for {api_name}...")
    TagValues = getattr(importlib.import_module(
        f'openapi_{api_name}.apis.tags'), "TagValues")
    tag_to_api = getattr(importlib.import_module(
        f'openapi_{api_name}.apis.tag_to_api'), "tag_to_api")

    modules_path = moralis_module_path / api_name

    cleanup_modules(api_name, modules_path)

    for tag in TagValues:
        make_module(api_name, tag, tag_to_api[tag].__name__, security_key)

    with open(modules_path / '__init__.py', 'w') as f:
        f.write(f'from .{api_name} import *\n')

    with open(modules_path / 'utilities.py', 'w') as f:
        f.write(make_utililities())

    with open(modules_path / f'{api_name}.py', 'w') as f:
        for tag in TagValues:
            f.write(f'from .{tag.value} import {tag.value}\n')
    print(f"✅ Finished generating modules for {api_name}")


def generate_modules():
    print("⏳ Generating all modules...")
    apis = json.load(open(root_path / 'api-config.json'))
    for api in apis:
        make_modules(api["name"], api["security_key"])
    print("🏁 Finished generation of all modules\n")
