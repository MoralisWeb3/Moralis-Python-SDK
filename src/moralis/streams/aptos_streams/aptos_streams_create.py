import json
import typing
import typing_extensions
from .api_instance import get_api_instance
from openapi_streams.paths.streams_aptos.put import SchemaForRequestBodyApplicationJson







def aptos_streams_create(api_key: str, body: SchemaForRequestBodyApplicationJson):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.aptos_streams_create(
        body=body,
        accept_content_types=(
            'application/json; charset=utf-8',
        ),
        skip_deserialization=True
    )

    return json.loads(api_response.response.data)
