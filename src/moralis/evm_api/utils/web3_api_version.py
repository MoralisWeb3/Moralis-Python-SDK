import json
import typing
import typing_extensions
from .api_instance import get_api_instance








def web3_api_version(api_key: str):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.web3_api_version(
        accept_content_types=(
            'application/json; charset=utf-8',
        ),
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)
