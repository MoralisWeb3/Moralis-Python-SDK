import json
from .api_instance import get_api_instance


def endpoint_weights(api_key: str):
    api_instance = get_api_instance(api_key)

    api_response = api_instance.endpoint_weights(
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)

