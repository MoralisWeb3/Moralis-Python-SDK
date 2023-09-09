import openapi_evm_api
from openapi_evm_api.apis.tags import wallets_api
from ..utilities import get_common_headers


def get_api_instance(api_key, params = None):
    configuration = openapi_evm_api.Configuration()
    configuration.api_key['ApiKeyAuth'] = api_key
    api_client = openapi_evm_api.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = wallets_api.WalletsApi(api_client)
    api_client.close()

    return api_instance
