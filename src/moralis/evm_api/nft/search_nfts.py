import json
from .api_instance import get_api_instance
from openapi_evm_api.paths.nft_search.get import RequestQueryParams


def search_nfts(api_key: str, params: RequestQueryParams):
    api_instance = get_api_instance(api_key)
    query_params = {k: v for k, v in params.items() if k in RequestQueryParams.__annotations__.keys()}

    api_response = api_instance.search_nfts(
        query_params=query_params,
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)

