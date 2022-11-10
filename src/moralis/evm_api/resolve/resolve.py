
import openapi_evm_api
from openapi_evm_api.apis.tags import resolve_api
import json
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_evm_api.Configuration()
    configuration.api_key['ApiKeyAuth'] = api_key
    api_client = openapi_evm_api.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = resolve_api.ResolveApi(api_client)
    api_client.close()

    return api_instance


def resolve_address(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.resolve_address(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def resolve_domain(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.resolve_domain(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)

