import json
from .api_instance import get_api_instance

from openapi_evm_api.paths.wallets_balances.get import RequestQueryParams

def get_native_balances_for_addresses(api_key: str, params: RequestQueryParams):
    api_instance = get_api_instance(api_key)
    query_params = {k: v for k, v in params.items() if k in RequestQueryParams.__annotations__.keys()}
    api_response = api_instance.get_native_balances_for_addresses(
        query_params=query_params,
        accept_content_types='application/json; charset=utf-8',
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)
