import json
from .api_instance import get_api_instance
from openapi_streams.paths.streams_evm_id.get import RequestPathParams


def get_stream(api_key: str, params: RequestPathParams):
    api_instance = get_api_instance(api_key)
    path_params = {k: v for k, v in params.items() if k in RequestPathParams.__annotations__.keys()}

    api_response = api_instance.get_stream(
        path_params=path_params,
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)

