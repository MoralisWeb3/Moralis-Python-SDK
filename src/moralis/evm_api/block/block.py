
import openapi_evm_api
from openapi_evm_api.apis.tags import block_api
import json
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_evm_api.Configuration()
    configuration.api_key['ApiKeyAuth'] = api_key
    api_client = openapi_evm_api.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = block_api.BlockApi(api_client)
    api_client.close()

    return api_instance


def get_block(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_block(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_date_to_block(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_date_to_block(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)

