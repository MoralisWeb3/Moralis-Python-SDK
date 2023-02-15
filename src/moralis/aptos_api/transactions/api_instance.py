import openapi_aptos_api
from openapi_aptos_api.apis.tags import transactions_api
from ..utilities import get_common_headers

hosts = {
    "mainnet": "https://mainnet-aptos-api.moralis.io",
    "testnet": "https://testnet-aptos-api.moralis.io",
    }

def get_host_url(params = None):
    if params is not None and "network" in params:
        if params["network"] in hosts:
            return hosts[params["network"]]
        else:
            raise Exception('Unknown value provided for .')
    return hosts["mainnet"]


def get_api_instance(api_key, params = None):
    configuration = openapi_aptos_api.Configuration()
    configuration.host = get_host_url(params)
    configuration.access_token = api_key
    api_client = openapi_aptos_api.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = transactions_api.TransactionsApi(api_client)
    api_client.close()

    return api_instance
