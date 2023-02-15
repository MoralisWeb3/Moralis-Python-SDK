from openapi_streams.paths.streams_aptos_id_address.get import ApiForget
from openapi_streams.paths.streams_aptos_id_address.post import ApiForpost
from openapi_streams.paths.streams_aptos_id_address.delete import ApiFordelete


class StreamsAptosIdAddress(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
