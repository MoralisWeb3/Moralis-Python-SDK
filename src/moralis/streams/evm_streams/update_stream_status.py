import json
from .api_instance import get_api_instance
import typing
from openapi_streams.paths.streams_evm_id_status.post import RequestPathParams, SchemaForRequestBodyApplicationJson


def update_stream_status(api_key: str, params: RequestPathParams, body: SchemaForRequestBodyApplicationJson):
    api_instance = get_api_instance(api_key)
    path_params = {k: v for k, v in params.items() if k in RequestPathParams.__annotations__.keys()}

    api_response = api_instance.update_stream_status(
        body=body,
        path_params=path_params,
        accept_content_types='application/json; charset=utf-8',
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)

