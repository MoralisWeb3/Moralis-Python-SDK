import json
import typing
import typing_extensions
from .api_instance import get_api_instance
from openapi_evm_api.paths.nft_address_traits.get import RequestQueryParams, RequestPathParams



class QueryParams(RequestQueryParams):
    pass

class Params(QueryParams,RequestPathParams,):
    pass

def get_nft_traits_by_collection(api_key: str, params: Params):
    api_instance = get_api_instance(api_key, params)
    query_params: typing.Any = {k: v for k, v in params.items() if k in RequestQueryParams.__annotations__.keys()}
    path_params: typing.Any = {k: v for k, v in params.items() if k in RequestPathParams.__annotations__.keys()}
    api_response = api_instance.get_nft_traits_by_collection(
        query_params=query_params,
        path_params=path_params,
        accept_content_types=(
            'application/json; charset=utf-8',
        ),
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)
