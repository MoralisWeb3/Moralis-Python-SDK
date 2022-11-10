from openapi_streams.paths.streams_evm_id.get import ApiForget
from openapi_streams.paths.streams_evm_id.post import ApiForpost
from openapi_streams.paths.streams_evm_id.delete import ApiFordelete


class StreamsEvmId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
