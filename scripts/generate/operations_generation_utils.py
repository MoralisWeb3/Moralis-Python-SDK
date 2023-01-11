from .operation_params import get_required_for_param, get_param_details, resolve_ref_to_type

nl = '\n'
quote = '"'


def generate_operation_params_example_item(param, swagger):
    type, example, default = get_param_details(param["schema"], swagger)
    name = param["name"]
    required = get_required_for_param(param)

    return f'    {quote}{name}{quote}: {example if example != "" else quote+quote}, {" # Required" if required == "Y" else ""}{nl}'


def generate_operation_body_example_item(data, swagger):
    name, schema = data
    type, example, default = get_param_details(schema, swagger)
    required = '' if 'nullable' in data and data['nullable'] == True else 'Yes'

    return f'    {quote}{name}{quote}: {example if example != "" else quote+quote}, {" # Required" if required == "Y" else ""}{nl}'


def generate_params_example(swagger_data, swagger):
    if not "parameters" in swagger_data:
        return ""

    params = sorted(
        list(swagger_data["parameters"]), key=lambda h: get_required_for_param(h), reverse=True)

    return f'''\
{{
{''.join(
    (map(lambda param: generate_operation_params_example_item(param, swagger), params)))}}}\
'''


def generate_body_example(swagger_data, swagger):
    # TODO: resolve examples of body params better
    if not "requestBody" in swagger_data:
        return ""


    # Body is Array of objects
    schema = swagger_data["requestBody"]["content"]["application/json"]["schema"]

    if 'type' in schema and schema['type'] == 'array' and "items" in schema and '$ref' in schema['items']:
        resolved_ref_type = resolve_ref_to_type(
            schema['items'], swagger)

        # TODO: add check if it has properties
        params = dict.items(resolved_ref_type["properties"])
        return f'''\
[{{
{''.join(
    (map(lambda param: generate_operation_body_example_item(param, swagger), params)))}}}]\
'''

    # Body is object
    if '$ref' in schema:
        resolved_ref_type = resolve_ref_to_type(
            schema, swagger)
        params = dict.items(resolved_ref_type["properties"])
        return f'''\
{{
{''.join(
    (map(lambda param: generate_operation_body_example_item(param, swagger), params)))}}}\
'''

    return '""'


def generate_operation_example(module_name, group_name, operation, swagger, swagger_data):
    hasParams = 'parameters' in swagger_data and len(
        swagger_data['parameters']) > 0
    hasBody = 'requestBody' in swagger_data

    return f'''\
from moralis import {module_name}

api_key = "YOUR_API_KEY"
{f'params = {generate_params_example(swagger_data, swagger)}{nl}' if hasParams else ''}\
{f'body = {generate_body_example(swagger_data, swagger)}{nl}' if hasBody else ''}\

result = {module_name}.{group_name}.{operation}(
    api_key=api_key,
{'    params=params,'+nl if hasParams else ''}\
{'    body=body,'+nl if hasBody else ''}\
)

print(result)
'''
