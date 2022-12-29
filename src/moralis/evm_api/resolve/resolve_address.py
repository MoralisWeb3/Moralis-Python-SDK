import json
from .api_instance import get_api_instance
from openapi_evm_api.paths.resolve_address_reverse.get import RequestPathParams


def resolve_address(api_key: str, params: RequestPathParams):
    api_instance = get_api_instance(api_key)
    path_params = {k: v for k, v in params.items() if k in RequestPathParams.__annotations__.keys()}

    api_response = api_instance.resolve_address(
        path_params=path_params,
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)

