import shutil
import importlib
import inspect
import re
from pathlib import Path
from typing import Type, TypedDict, List
from inspect import signature
from enum import Enum
from .paths import moralis_modules_root_path
from .files import ensure_empty_folder, save_py
from .Template import useTemplate, Template


class NetworkConfig(TypedDict):
    parameter_value: str
    base_url: str


class SubNetworkConfig(TypedDict):
    parameter_name: str
    default_network: str
    networks: List[NetworkConfig]


def generate_modules(api_name: str, security_key: str, subnetworks: SubNetworkConfig | None = None):
    print(f"⏳ Generating modules for {api_name}...")
    module = MoralisModule(api_name, security_key, subnetworks)
    module.clear()
    module.generate_modules()
    print(f"✅ Generated modules for {api_name}")


class MoralisModule:
    def __init__(self, api_name: str, security_key: str, subnetworksConfig: SubNetworkConfig | None):
        self.api_name: str = api_name
        self.security_key: str = security_key
        self.subnetworksConfig = subnetworksConfig
        self.version = self.get_version()
        Tags: Type[Enum] = getattr(importlib.import_module(
            f'openapi_{api_name}.apis.tags'), "TagValues")
        self.tags = [tag.value for tag in Tags if tag.value is not 'default']

        self.tag_to_api = getattr(importlib.import_module(
            f'openapi_{api_name}.apis.tag_to_api'), "tag_to_api")
        pass

    def clear(self):
        print(f"⏳ Removing modules for {self.api_name}...")
        if (self.modules_path.exists()):
            shutil.rmtree(self.modules_path)
        print(f"✅ Removed modules for {self.api_name} done")

    def generate_modules(self):
        print(f"⏳ Generating modules for {self.api_name}...")
        ensure_empty_folder(self.modules_path)

        generateAndSave(
            path=self.modules_path / '__init__.py',
            template=Template.API_INIT,
            values={
                "api_name": self.api_name
            },
        )

        generateAndSave(
            path=self.modules_path / f'{self.api_name}.py',
            template=Template.API_TAGS,
            values={
                "tags": self.tags
            },
        )

        generateAndSave(
            path=self.modules_path / f'version.py',
            template=Template.API_VERSION,
            values={
                "version": self.version
            },
        )

        generateAndSave(
            path=self.modules_path / f'utilities.py',
            template=Template.API_UTILS,
        )

        # Generate all files for all modules
        for tag in self.tags:
            self.generate_module(tag)

        print(f"✅ Generating modules for {self.api_name} done")

    def generate_module(self, tag: str):
        print(f"⏳ Generating module {tag} for {self.api_name}...")
        module_path = self.modules_path / tag
        ensure_empty_folder(module_path)

        operations = self.get_tag_operations(tag)

        generateAndSave(
            path=module_path / f'{tag}.py',
            template=Template.MODULE_TAG,
            values={
                "operations": map(lambda operation: operation[0], operations)
            },
        )

        generateAndSave(
            path=module_path / '__init__.py',
            template=Template.MODULE_INIT,
            values={
                "tag": tag
            },
        )

        generateAndSave(
            path=module_path / 'api_instance.py',
            template=Template.MODULE_API_INSTANCE,
            values={
                "api_name": self.api_name,
                "tag": tag,
                "api_client_name": self.get_api_client_name(tag),
                "security_key": self.security_key,
                "subnetworksConfig": {
                    "host_parameter": self.subnetworksConfig["parameter_name"],
                    "default_host_name": self.subnetworksConfig["default_network"],
                    "networks": self.subnetworksConfig["networks"]
                } if self.subnetworksConfig is not None else None

            },
        )

        # Generate files for all opertions
        for operation in operations:
            generateAndSave(
                path=module_path / f'{operation[0]}.py',
                template=Template.OPERATION,
                values={
                    **get_operation_data(operation),
                    "operation_name": operation[0],
                    "subnetworksConfig": {
                        "host_parameter": self.subnetworksConfig["parameter_name"],
                        "default_host_name": self.subnetworksConfig["default_network"],
                        "networks": self.subnetworksConfig["networks"]
                    } if self.subnetworksConfig is not None else None
                }
            )

        print(f"✅ Generating module {tag} for {self.api_name} done")

    @property
    def modules_path(self):
        return moralis_modules_root_path / self.api_name

    def get_version(self):
        version = '0.0.0'
        if self.modules_path.exists() and self.modules_path.is_dir():
            version_file_path = self.modules_path / 'version.py'
            if version_file_path.exists() and version_file_path.is_file():
                version_file = open(version_file_path, 'r')
                version_file_content = version_file.read()
                version_match = re.search(
                    r'__version__ = "(.*)"', version_file_content)
                if version_match:
                    version = version_match.group(1)
                version_file.close()

        return version

    def get_api_client_name(self, tag: str):
        return self.tag_to_api[tag].__name__

    def get_tag_operations(self, tag: str):
        api_client_name = self.get_api_client_name(tag)
        api = getattr(importlib.import_module(
            f'openapi_{self.api_name}.apis.tags'), f'{tag}_api')
        api_instance = dict(inspect.getmembers(api))[api_client_name]
        operations = inspect.getmembers(
            api_instance, predicate=api_operation_predicate)

        return operations


def get_operation_data(operation):
    function_reference = operation[1]
    fn_params = signature(function_reference).parameters
    fn_module = function_reference.__module__
    imports = []

    has_body = 'body' in fn_params.keys()
    # Note we assume this on the accept_content_types param, not the response type
    # This is currently true for all endpoints, except where we return no data
    is_json_response = 'accept_content_types' in fn_params.keys()
    has_query_params = 'query_params' in fn_params.keys()
    has_path_params = 'path_params' in fn_params.keys()
    has_any_params = has_query_params or has_path_params

    if has_query_params:
        query_params_sig = fn_params["query_params"].annotation
        imports.append(query_params_sig.__name__)
    if has_path_params:
        path_params_sig = fn_params["path_params"].annotation
        imports.append(path_params_sig.__name__)

    imports = []
    if (has_query_params):
        imports.append("RequestQueryParams")
    if (has_path_params):
        imports.append("RequestPathParams")
    if (has_body):
        imports.append("SchemaForRequestBodyApplicationJson")

    import_statement = f'from {fn_module} import {", ".join(imports)}' if len(
        imports) > 0 else None

    return {
        "has_any_params": has_any_params,
        "has_query_params": has_query_params,
        "has_path_params": has_path_params,
        "has_body": has_body,
        "is_json_response": is_json_response,
        "import_statement": import_statement,
        # "imports": imports,
    }


def api_operation_predicate(o):
    if inspect.isfunction(o) and not o.__name__.startswith("_"):
        return True
    else:
        return False


def generateAndSave(template: Template, path: Path, values: dict = {}):
    content = useTemplate(template, values)
    save_py(content, path)
