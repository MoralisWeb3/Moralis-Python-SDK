import json
from .api_instance import get_api_instance
from openapi_sol_api.paths.account_network_address_portfolio.get import RequestPathParams


def get_portfolio(api_key: str, params: RequestPathParams):
    api_instance = get_api_instance(api_key)
    path_params = {k: v for k, v in params.items() if k in RequestPathParams.__annotations__.keys()}

    api_response = api_instance.get_portfolio(
        path_params=path_params,
        accept_content_types='application/json; charset=utf-8',
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)

