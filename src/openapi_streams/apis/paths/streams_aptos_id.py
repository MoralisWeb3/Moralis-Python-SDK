from openapi_streams.paths.streams_aptos_id.get import ApiForget
from openapi_streams.paths.streams_aptos_id.post import ApiForpost
from openapi_streams.paths.streams_aptos_id.delete import ApiFordelete


class StreamsAptosId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
