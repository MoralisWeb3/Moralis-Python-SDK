import typing_extensions

from openapi_streams.paths import PathValues
from openapi_streams.apis.paths.history import History
from openapi_streams.apis.paths.history_replay_stream_id_id import HistoryReplayStreamIdId
from openapi_streams.apis.paths.settings import Settings
from openapi_streams.apis.paths.stats import Stats
from openapi_streams.apis.paths.stats_stream_id import StatsStreamId
from openapi_streams.apis.paths.streams_evm import StreamsEvm
from openapi_streams.apis.paths.streams_evm_id import StreamsEvmId
from openapi_streams.apis.paths.streams_evm_id_status import StreamsEvmIdStatus
from openapi_streams.apis.paths.streams_evm_id_address import StreamsEvmIdAddress

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.HISTORY: History,
        PathValues.HISTORY_REPLAY_STREAM_ID_ID: HistoryReplayStreamIdId,
        PathValues.SETTINGS: Settings,
        PathValues.STATS: Stats,
        PathValues.STATS_STREAM_ID: StatsStreamId,
        PathValues.STREAMS_EVM: StreamsEvm,
        PathValues.STREAMS_EVM_ID: StreamsEvmId,
        PathValues.STREAMS_EVM_ID_STATUS: StreamsEvmIdStatus,
        PathValues.STREAMS_EVM_ID_ADDRESS: StreamsEvmIdAddress,
    }
)

path_to_api = PathToApi(
    {
        PathValues.HISTORY: History,
        PathValues.HISTORY_REPLAY_STREAM_ID_ID: HistoryReplayStreamIdId,
        PathValues.SETTINGS: Settings,
        PathValues.STATS: Stats,
        PathValues.STATS_STREAM_ID: StatsStreamId,
        PathValues.STREAMS_EVM: StreamsEvm,
        PathValues.STREAMS_EVM_ID: StreamsEvmId,
        PathValues.STREAMS_EVM_ID_STATUS: StreamsEvmIdStatus,
        PathValues.STREAMS_EVM_ID_ADDRESS: StreamsEvmIdAddress,
    }
)
