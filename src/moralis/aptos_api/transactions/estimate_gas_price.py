import json
import typing
import typing_extensions
from .api_instance import get_api_instance


RequestNetworkQueryParams = typing_extensions.TypedDict("RequestNetworkQueryParams", {
    "network": typing.Literal["mainnet","testnet",]}, total=False)





def estimate_gas_price(api_key: str):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.estimate_gas_price(
        accept_content_types=(
            'application/json; charset=utf-8',
        ),
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)
