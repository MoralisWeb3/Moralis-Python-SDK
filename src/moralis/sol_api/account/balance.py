import json
from .api_instance import get_api_instance
from openapi_sol_api.paths.account_network_address_balance.get import RequestPathParams


def balance(api_key: str, params: RequestPathParams):
    api_instance = get_api_instance(api_key)
    path_params = {k: v for k, v in params.items() if k in RequestPathParams.__annotations__.keys()}

    api_response = api_instance.balance(
        path_params=path_params,
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)

