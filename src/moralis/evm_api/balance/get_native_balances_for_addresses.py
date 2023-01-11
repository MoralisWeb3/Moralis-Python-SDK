import json
from .api_instance import get_api_instance

from openapi_evm_api.paths.native_balances.post import RequestQueryParams, SchemaForRequestBodyApplicationJson

def get_native_balances_for_addresses(api_key: str, params: RequestQueryParams, body: SchemaForRequestBodyApplicationJson):
    api_instance = get_api_instance(api_key)
    query_params = {k: v for k, v in params.items() if k in RequestQueryParams.__annotations__.keys()}
    api_response = api_instance.get_native_balances_for_addresses(
        body=body,
        query_params=query_params,
        accept_content_types='application/json; charset=utf-8',
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)
