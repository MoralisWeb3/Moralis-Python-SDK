import json
import typing
import typing_extensions
from .api_instance import get_api_instance
from openapi_aptos_api.paths.transactions_encode_submission.post import SchemaForRequestBodyApplicationJson

RequestNetworkQueryParams = typing_extensions.TypedDict("RequestNetworkQueryParams", {
    "network": typing.Literal["mainnet","testnet",]}, total=False)





def encode_submission(api_key: str, body: SchemaForRequestBodyApplicationJson):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.encode_submission(
        body=body,
        accept_content_types=(
            'application/json; charset=utf-8',
        ),
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)
