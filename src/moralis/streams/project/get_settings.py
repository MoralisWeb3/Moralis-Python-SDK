import json
from .api_instance import get_api_instance


def get_settings(api_key: str):
    api_instance = get_api_instance(api_key)

    api_response = api_instance.get_settings(
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)

