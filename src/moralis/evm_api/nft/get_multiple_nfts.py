import json
import typing
import typing_extensions
from .api_instance import get_api_instance
from openapi_evm_api.paths.nft_get_multiple_nfts.post import RequestQueryParams, SchemaForRequestBodyApplicationJson



class QueryParams(RequestQueryParams):
    pass

class Params(QueryParams,):
    pass

def get_multiple_nfts(api_key: str, params: Params, body: SchemaForRequestBodyApplicationJson):
    api_instance = get_api_instance(api_key, params)
    query_params: typing.Any = {k: v for k, v in params.items() if k in RequestQueryParams.__annotations__.keys()}
    api_response = api_instance.get_multiple_nfts(
        body=body,
        query_params=query_params,
        accept_content_types=(
            'application/json; charset=utf-8',
        ),
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)
