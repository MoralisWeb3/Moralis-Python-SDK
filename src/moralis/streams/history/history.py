
import openapi_streams
from openapi_streams.apis.tags import history_api
import json
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_streams.Configuration()
    configuration.api_key['x-api-key'] = api_key
    api_client = openapi_streams.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = history_api.HistoryApi(api_client)
    api_client.close()

    return api_instance


def get_history(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_history(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def replay_history(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.replay_history(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)

