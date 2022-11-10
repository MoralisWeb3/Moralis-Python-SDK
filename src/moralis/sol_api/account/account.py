
import openapi_sol_api
from openapi_sol_api.apis.tags import account_api
import json
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_sol_api.Configuration()
    configuration.api_key['ApiKeyAuth'] = api_key
    api_client = openapi_sol_api.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = account_api.AccountApi(api_client)
    api_client.close()

    return api_instance


def balance(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.balance(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_nfts(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_nfts(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_portfolio(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_portfolio(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_spl(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_spl(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)

