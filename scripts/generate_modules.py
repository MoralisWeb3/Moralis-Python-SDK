# Generate all modules based on the generated open-api clients

import inspect
import os
from pathlib import Path
from distutils.dir_util import copy_tree
import json
import importlib
import shutil
from inspect import signature, getmembers

nl = '\n'

root_path = Path(__file__).parent.parent
moralis_module_path = (root_path / 'src/moralis')


def make_module_api_instance(api_name, tag, api_client_name, security_key):
    return f'''\
import openapi_{api_name}
from openapi_{api_name}.apis.tags import {tag}_api
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


def make_operation_snippet(function_name, fn_data):
    has_query_params = fn_data["has_query_params"]
    has_path_params = fn_data["has_path_params"]
    has_body = fn_data["has_body"]
    fn_module = fn_data["fn_module"]
    has_any_params = has_query_params or has_path_params

    imports = []
    params = []
    if (has_query_params):
        imports.append("RequestQueryParams")
        params.append("RequestQueryParams")
    if (has_path_params):
        imports.append("RequestPathParams")
        params.append("RequestPathParams")
    if (has_body):
        imports.append("SchemaForRequestBodyApplicationJson")

    import_statement = f'from {fn_module} import {", ".join(imports)}' if len(
        imports) > 0 else None
    params_union = f'typing.Union[{", ".join(params)}]' if len(
        params) > 1 else ", ".join(params)

    return f'''\
import json
from .api_instance import get_api_instance
{f'import typing{nl}' if has_any_params and len(imports) > 1  else ''}\
{f'{import_statement}{nl}' if import_statement else ''}\


def {function_name}(api_key: str{f', params: {params_union}' if has_any_params else ''}{', body: SchemaForRequestBodyApplicationJson' if has_body else ''}):
    api_instance = get_api_instance(api_key)
{f'    query_params = {{k: v for k, v in params.items() if k in RequestQueryParams.__annotations__.keys()}}{nl}' if has_query_params else ''}\
{f'    path_params = {{k: v for k, v in params.items() if k in RequestPathParams.__annotations__.keys()}}{nl}' if has_path_params else ''}\

    api_response = api_instance.{function_name}(
{f'        body=body,{nl}' if has_body else ''}\
{f'        query_params=query_params,{nl}' if has_query_params else ''}\
{f'        path_params=path_params,{nl}' if has_path_params else ''}\
{f"        accept_content_types='application/json; charset=utf-8',{nl}" if has_body else ''}\
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)

'''


def make_utililities():
    return '''\
from .version import __version__


def get_common_headers():
    """Get the headers for the requests."""
    return {
        "x-moralis-platform": 'Python SDK',
        "x-moralis-platform-version": __version__,
        "x-moralis-build-target": 'python',
    }

'''


def api_operation_predicate(o):
    if inspect.isfunction(o) and not o.__name__.startswith("_"):
        return True
    else:
        return False


def get_function_data(fn):
    function_reference = fn[1]
    fn_params = signature(function_reference).parameters
    fn_module = function_reference.__module__
    imports = []
    required_query_params = None
    optional_query_params = None
    required_path_params = None
    optional_path_params = None

    has_body = 'body' in fn_params.keys()
    has_query_params = 'query_params' in fn_params.keys()
    has_path_params = 'path_params' in fn_params.keys()

    if has_query_params:
        query_params_sig = fn_params["query_params"].annotation
        required_query_params = query_params_sig.__required_keys__
        optional_query_params = query_params_sig.__optional_keys__
        imports.append(query_params_sig.__name__)
    if has_path_params:
        path_params_sig = fn_params["path_params"].annotation
        required_path_params = path_params_sig.__required_keys__
        optional_path_params = path_params_sig.__optional_keys__
        imports.append(path_params_sig.__name__)

    return {
        "imports": imports,
        "has_body": has_body,
        "has_query_params": has_query_params,
        "has_path_params": has_path_params,
        "required_query_params": required_query_params,
        "optional_query_params": optional_query_params,
        "required_path_params": required_path_params,
        "optional_path_params": optional_path_params,
        "fn_module": fn_module
    }


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

    with open(module_path / f'{tag}.py', 'w') as f:
        for fn in functions:
            f.write(f'from .{fn[0]} import {fn[0]}\n')

    with open(module_path / f'api_instance.py', 'w') as f:
        f.write(make_module_api_instance(
            api_name, tag, api_client_name, security_key))

    with open(module_path / f'__init__.py', 'w') as f:
        f.write(f'from .{tag} import *\n')

    for fn in functions:
        fn_data = get_function_data(fn)
        with open(module_path / f'{fn[0]}.py', 'w') as f:
            f.write(make_operation_snippet(fn[0], fn_data))

    print(f"✅ Generated modules for {api_name} [{tag}]")


def cleanup_modules(api_name, modules_path):
    print(f"⏳ Removing modules for {api_name}...")
    # Remove the modules folder, but keep the version file (note we only return the version of the last module, but they all should be the same)
    version_file_content = None

    if modules_path.exists() and modules_path.is_dir():
        version_file_path = modules_path / 'version.py'
        if version_file_path.exists() and version_file_path.is_file():
            version_file = open(version_file_path, 'r')
            version_file_content = version_file.read()
            version_file.close()
        shutil.rmtree(modules_path)
    print(f"✅ Removed modules for {api_name}")
    return version_file_content


def make_modules(api_name, security_key):
    print(f"⏳ Generating modules for {api_name}...")
    TagValues = getattr(importlib.import_module(
        f'openapi_{api_name}.apis.tags'), "TagValues")
    tag_to_api = getattr(importlib.import_module(
        f'openapi_{api_name}.apis.tag_to_api'), "tag_to_api")

    modules_path = moralis_module_path / api_name

    version_file_content = cleanup_modules(api_name, modules_path)

    for tag in TagValues:
        make_module(api_name, tag, tag_to_api[tag].__name__, security_key)

    with open(modules_path / '__init__.py', 'w') as f:
        f.write(f'from .{api_name} import *\n')

    with open(modules_path / 'utilities.py', 'w') as f:
        f.write(make_utililities())

    with open(modules_path / f'version.py', 'w') as f:
        # version will be updated once bumpver (according to bumpver.toml) is run before release
        f.write(version_file_content)

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
