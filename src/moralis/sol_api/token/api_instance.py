import openapi_sol_api
from openapi_sol_api.apis.tags import token_api
from ..utilities import get_common_headers


def get_api_instance(api_key, params = None):
    configuration = openapi_sol_api.Configuration()
    configuration.api_key['ApiKeyAuth'] = api_key
    api_client = openapi_sol_api.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = token_api.TokenApi(api_client)
    api_client.close()

    return api_instance
