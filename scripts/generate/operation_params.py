quote = '"'


def walk_ref_schema(obj, path):
    node = path.pop(0)
    if (len(path) > 0):
        return walk_ref_schema(obj[node], path)
    else:
        return obj[node]


def resolve_string_param(schema):
    type = 'str'
    example = '""'
    default = ''

    if 'enum' in schema:
        type = f'enum[{type}]: <br/>{"<br/>".join(map(lambda x: f"- {quote}{x}{quote}",schema["enum"]))}'
    if 'default' in schema:
        default = f'{quote}{schema["default"]}{quote}'
    if 'example' in schema:
        example = f'{quote}{schema["example"]}{quote}'

    return type, example, default


def resolve_integer_param(schema):
    type = 'int'
    example = '0'
    default = ''

    if 'default' in schema:
        default = schema["default"]
    if 'example' in schema:
        example = schema["example"]

    return type, example, default


def resolve_number_param(schema):
    type = 'float'
    example = '1.2'
    default = ''

    if 'default' in schema:
        default = schema["default"]
    if 'example' in schema:
        example = schema["example"]

    return type, example, default


def resolve_boolean_param(schema):
    type = 'bool'
    example = 'True'
    default = ''

    if 'default' in schema:
        default = schema["default"]
    if 'example' in schema:
        example = schema["example"]

    return type, example, default


def resolve_array_param(schema, swagger):
    # Edge case when swagger has not specified list items
    if not 'items' in schema:
        return 'List', '[]', ''

    list_item_type, item_example, item_default = get_type_for_param(
        schema['items'], swagger)
    type = f'List of {list_item_type}'
    example = '[]'
    default = ''

    if 'default' in schema:
        default = schema["default"]
    if 'example' in schema:
        example = schema["example"]

    return type, example, default


def resolve_object_param(schema, swagger):
    type = f'object'
    example = '{}'
    default = ''

    if 'properties' in schema:
        type = f'{type}: <br/>{"<br/>".join(map(lambda property_name: resolve_properties_for_object(property_name, schema,swagger),schema["properties"]))}'
    if 'default' in schema:
        default = schema["default"]
    if 'example' in schema:
        example = schema["example"]

    return type, example, default


def resolve_properties_for_object(property_name, parent_schema, swagger):
    property = parent_schema["properties"][property_name]
    type, example, default = get_type_for_param(property, swagger)
    out = f' - {property_name}: {type}'
    return out


def resolve_properties_param(schema, swagger):
    return resolve_object_param(schema, swagger)


def resolve_ref_param(schema, swagger):
    value = resolve_ref_to_type(schema, swagger)
    path = schema["$ref"][2:].split("/")
    # Prevent recursion as docs are defined as a recursive type
    if 'AbiInput' in path:
        return 'AbiInput', '[]', ''
    if 'AbiOutput' in path:
        return 'AbiOutput', '[]', ''

    return get_type_for_param(value, swagger)


def resolve_ref_to_type(schema, swagger):
    path = schema["$ref"][2:].split("/")

    value = walk_ref_schema(swagger, path)
    return value


def resolve_anyof_param(schema, swagger):
    # TODO: add other members of array to type def as well
    return get_type_for_param(schema["anyOf"][0], swagger)


def get_type_for_param(schema, swagger):
    if ('type' in schema and schema['type'] == 'string'):
        return resolve_string_param(schema)
    if ('type' in schema and schema['type'] == 'integer'):
        return resolve_integer_param(schema)
    if ('type' in schema and schema['type'] == 'number'):
        return resolve_number_param(schema)
    if ('type' in schema and schema['type'] == 'boolean'):
        return resolve_boolean_param(schema)
    if ('type' in schema and schema['type'] == 'array'):
        return resolve_array_param(schema, swagger)
    if ('type' in schema and schema['type'] == 'object'):
        return resolve_object_param(schema, swagger)
    if ('properties' in schema):
        return resolve_properties_param(schema, swagger)
    if ('anyOf' in schema):
        return resolve_anyof_param(schema, swagger)

    elif ('$ref' in schema):
        return resolve_ref_param(schema, swagger)

    raise Exception(f"⛔️ Missing param check for {schema}")


def get_type_for_body(schema, swagger):
    type = get_type_for_param(schema, swagger)

    return type


def sanitize_example(example):
    if type(example) is str:
        return f'{example}'.replace("\n", "<br/>") if example else ''
    return example


def get_description_for_param(param):
    return param["description"].replace("\n", "<br/>") if "description" in param else ""


def get_required_for_param(param):
    return 'Yes' if "required" in param and param["required"] else ""


def get_param_details(param, swagger):
    type, example, default = get_type_for_param(param, swagger)

    return type, sanitize_example(example), default
