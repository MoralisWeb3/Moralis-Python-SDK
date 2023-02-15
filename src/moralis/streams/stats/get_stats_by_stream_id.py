import json
import typing
import typing_extensions
from .api_instance import get_api_instance
from openapi_streams.paths.stats_stream_id.get import RequestPathParams





class Params(RequestPathParams,):
    pass

def get_stats_by_stream_id(api_key: str, params: Params):
    api_instance = get_api_instance(api_key, params)
    path_params: typing.Any = {k: v for k, v in params.items() if k in RequestPathParams.__annotations__.keys()}
    api_response = api_instance.get_stats_by_stream_id(
        path_params=path_params,
        accept_content_types=(
            'application/json; charset=utf-8',
        ),
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)
