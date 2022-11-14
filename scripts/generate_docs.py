# Generate all docs based on the generated moralis modules
from pathlib import Path
import os
import json
import re
from operation_params import get_required_for_param, get_param_details, get_type_for_body, resolve_ref_to_type, get_description_for_param
from operations_generation_utils import generate_operation_example

root_path = Path(__file__).parent.parent
moralis_module_path = Path(__file__).parent.parent / 'src/moralis'
docs_path = root_path / 'docs'
snippet_path = docs_path / 'code_snippets.json'

nl = '\n'
quote = '"'

code_snippets = {}


def camel_to_snake(string):
    string = re.sub(r'NFT', 'Nft', string)
    string = re.sub(r'SPL', 'Spl', string)

    string = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    return ''.join(string.lower())


def register_snippet(module_name, group_name, operation, snippet):
    if not module_name in code_snippets:
        code_snippets[module_name] = {}
    if not group_name in code_snippets[module_name]:
        code_snippets[module_name][group_name] = {}

    code_snippets[module_name][group_name][operation] = snippet

    print("Registered snippet for", module_name, group_name, operation)


def save_snippets():
    with open(snippet_path, 'w') as outfile:
        json.dump(code_snippets, outfile, indent=4)


def generate_operation_params_row(param, swagger):
    type, example, default = get_param_details(
        param["schema"], swagger)
    name = param["name"]
    required = get_required_for_param(param)
    description = get_description_for_param(param)

    return f'| {name} | {type} | {description} | {required} | {default} | {example} |{nl}'


def generate_operation_body_params_row(data, swagger):
    name, schema = data
    type, example, default = get_param_details(
        schema, swagger)
    required = '' if 'nullable' in data and data['nullable'] == True else 'Yes'
    description = get_description_for_param(schema)

    return f'| {name} | {type} | {description} | {required} | {default} | {example} |{nl}'


def generate_operation_params(swagger_data, swagger):
    if not "parameters" in swagger_data or len(swagger_data["parameters"]) == 0:
        return ""

    params = sorted(
        list(swagger_data["parameters"]), key=lambda h: get_required_for_param(h), reverse=True)

    return f'''\
### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
{''.join(
    (map(lambda param: generate_operation_params_row(param, swagger), params)))}

'''


def generate_operation_body(swagger_data, swagger):
    if not "requestBody" in swagger_data:
        return ""

    schema = swagger_data["requestBody"]["content"]["application/json"]["schema"]

    # Body is Array of objects
    if 'type' in schema and schema['type'] == 'array' and '$ref' in schema['items']:
        resolved_ref_type = resolve_ref_to_type(
            schema['items'], swagger)

        # TODO: add check if it has properties
        params = dict.items(resolved_ref_type["properties"])
        return f'''\
### Body
Array of objects, with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
{''.join(
    (map(lambda param: generate_operation_body_params_row(param, swagger), params)))}
'''

    # Body is object
    if '$ref' in schema:
        resolved_ref_type = resolve_ref_to_type(
            schema, swagger)
        params = dict.items(resolved_ref_type["properties"])

        return f'''\
### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
{''.join(
    (map(lambda param: generate_operation_body_params_row(param, swagger), params)))}
'''

    # Or just show the type of the body
    body_type, example, default = get_type_for_body(schema, swagger)
    required = "Yes" if "required" in swagger_data[
        "requestBody"] and swagger_data["requestBody"]["required"] else "No"
    description = swagger_data["requestBody"]["description"] if "description" in swagger_data[
        "requestBody"] else "-"

    return f'''\
### Body

| Type | Description | Required |
|------|-------------|----------|
| {body_type} | {description} | {required} |

'''


def generate_operation_snippet(module_name, group_name, operation, swagger_path_by_operation, swagger):
    swagger_data = swagger_path_by_operation[operation]["data"]

    snippet = generate_operation_example(
        module_name, group_name, operation, swagger, swagger_data)
    register_snippet(module_name, group_name, operation, snippet)

    return f'''\
---
## `{operation}()`
{f'{swagger_data["description"]}{nl}' if 'description' in swagger_data else swagger_data["summary"]}

### Example
```python
{snippet}
```

{generate_operation_params(swagger_data, swagger)}\
{generate_operation_body(swagger_data, swagger)}\

'''


def generate_group_snippet(module_name, group_name, operations, swagger_path_by_operation, swagger):
    return f'''\
# {module_name}: {group_name}

{''.join(list(map(
    lambda operation: f"- [{Path(operation).stem}](#{Path(operation).stem}){nl}", operations)))}

{''.join(map(lambda operation: generate_operation_snippet(module_name,
         group_name, Path(operation).stem, swagger_path_by_operation, swagger), operations))}

'''


def generate_docs_for_group(module_name, group_name, swagger_path_by_operation, swagger):
    print(f"⏳ Generating docs for group {module_name}.{group_name}...")

    module_path = moralis_module_path / module_name
    group_path = module_path / group_name
    operations = [operation for operation in os.listdir(
        group_path) if os.path.isfile(group_path / operation) and operation.endswith('.py') and not operation.startswith('__') and not operation == 'api_instance.py' and not operation == f'{group_name}.py']

    content = generate_group_snippet(
        module_name, group_name, operations, swagger_path_by_operation, swagger)
    out_path = group_path / 'README.md'
    with open(out_path, "w") as f:
        f.write(content)
    print(f"✅ Generated docs for group {module_name}.{group_name}")


def generate_docs_for_module(module_name):
    print(f"⏳ Generating docs for module {module_name}...")
    swagger_path = root_path / f'temp/swagger/{module_name}.json'
    swagger_file = open(swagger_path, "r")
    swagger = json.loads(swagger_file.read())
    swagger_path_by_operation = {}
    for path in swagger['paths']:
        for method in swagger['paths'][path]:
            operation = swagger['paths'][path][method]
            operation_id = camel_to_snake(
                operation["operationId"])
            swagger_path_by_operation[operation_id] = {}
            swagger_path_by_operation[operation_id]["data"] = operation
            swagger_path_by_operation[operation_id]["path"] = path
            swagger_path_by_operation[operation_id]["method"] = method

    swagger_file.close()

    module_path = moralis_module_path / module_name
    groups = [directory for directory in os.listdir(
        module_path) if os.path.isdir(module_path / directory) and directory != 'moralis.egg-info' and not directory.startswith('__')]
    for group in groups:
        generate_docs_for_group(
            module_name, group, swagger_path_by_operation, swagger)

    with open(module_path / 'README.md', "w") as f:
        f.write(f"# {module_name}\n\n")
        f.write(
            f"{''.join(list(map(lambda group: f'- [{group}](./{group}/README.md){nl}', groups)))}")

    print(f"✅ Generated docs for module {module_name}")
    return groups, module_name


def generate_modules_list(modules, groups):
    out = ""
    for module in modules:
        out += f"## {module}{nl}{nl}"
        for group in groups[module]:
            out += f"- [{group}](./src/moralis/{module}/{group}/README.md){nl}"
        out += f"{nl}"

    return out


def generate_root_readme(modules, groups):
    readme_path = root_path / 'README.md'

    with open(readme_path, 'r+') as f:
        current_content = f.read()
        new_content = re.sub(
            pattern=r'<!-- Start: generated:references -->(.*)<!-- End: generated:references -->',
            repl=f'<!-- Start: generated:references -->{nl}{nl}{generate_modules_list(modules, groups)}{nl}{nl}<!-- End: generated:references -->',
            string=current_content,
            flags=re.DOTALL
        )
        with open(readme_path, 'w') as write_file:
            write_file.write(new_content)


def generate_docs():
    print(f"⏳ Generating docs...")
    apis = json.load(open(root_path / 'api-config.json'))
    modules = [api["name"] for api in apis]
    groups = {}
    for module in modules:
        module_groups, module_name = generate_docs_for_module(module)
        groups[module_name] = module_groups
    generate_root_readme(modules, groups)
    save_snippets()
    print(f"🏁 Generatied docs")
