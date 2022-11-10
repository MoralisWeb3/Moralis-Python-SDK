
import openapi_streams
from openapi_streams.apis.tags import evm_api
import json
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_streams.Configuration()
    configuration.api_key['x-api-key'] = api_key
    api_client = openapi_streams.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = evm_api.EvmApi(api_client)
    api_client.close()

    return api_instance


def add_address_to_stream(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.add_address_to_stream(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def create_stream(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.create_stream(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def delete_address_from_stream(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.delete_address_from_stream(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def delete_stream(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.delete_stream(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_addresses(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_addresses(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_stream(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_stream(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_streams(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_streams(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def update_stream(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.update_stream(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def update_stream_status(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.update_stream_status(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)

