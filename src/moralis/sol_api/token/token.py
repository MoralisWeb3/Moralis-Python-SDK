
import openapi_sol_api
from openapi_sol_api.apis.tags import token_api
import json
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_sol_api.Configuration()
    configuration.api_key['ApiKeyAuth'] = api_key
    api_client = openapi_sol_api.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = token_api.TokenApi(api_client)
    api_client.close()

    return api_instance


def get_token_price(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_token_price(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)

