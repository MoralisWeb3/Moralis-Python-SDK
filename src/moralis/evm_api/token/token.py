
import openapi_evm_api
from openapi_evm_api.apis.tags import token_api
import json
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_evm_api.Configuration()
    configuration.api_key['ApiKeyAuth'] = api_key
    api_client = openapi_evm_api.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = token_api.TokenApi(api_client)
    api_client.close()

    return api_instance


def get_token_allowance(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_token_allowance(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_token_metadata(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_token_metadata(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_token_metadata_by_symbol(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_token_metadata_by_symbol(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_token_price(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_token_price(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_token_transfers(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_token_transfers(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_wallet_token_balances(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_wallet_token_balances(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_wallet_token_transfers(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_wallet_token_transfers(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)

