
import openapi_auth
from openapi_auth.apis.tags import challenge_api
import json
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_auth.Configuration()
    configuration.api_key['X-API-KEY'] = api_key
    api_client = openapi_auth.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = challenge_api.ChallengeApi(api_client)
    api_client.close()

    return api_instance


def request_challenge_evm(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.request_challenge_evm(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def request_challenge_solana(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.request_challenge_solana(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def verify_challenge_evm(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.verify_challenge_evm(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def verify_challenge_solana(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.verify_challenge_solana(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)

