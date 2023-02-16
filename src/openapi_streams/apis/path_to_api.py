import typing_extensions

from openapi_streams.paths import PathValues
from openapi_streams.apis.paths.history import History
from openapi_streams.apis.paths.history_replay_stream_id_id import HistoryReplayStreamIdId
from openapi_streams.apis.paths.history_logs import HistoryLogs
from openapi_streams.apis.paths.settings import Settings
from openapi_streams.apis.paths.stats import Stats
from openapi_streams.apis.paths.stats_stream_id import StatsStreamId
from openapi_streams.apis.paths.streams_evm import StreamsEvm
from openapi_streams.apis.paths.streams_evm_id import StreamsEvmId
from openapi_streams.apis.paths.streams_evm_id_status import StreamsEvmIdStatus
from openapi_streams.apis.paths.streams_evm_id_address import StreamsEvmIdAddress
from openapi_streams.apis.paths.streams_aptos import StreamsAptos
from openapi_streams.apis.paths.streams_aptos_id import StreamsAptosId
from openapi_streams.apis.paths.streams_aptos_id_address import StreamsAptosIdAddress
from openapi_streams.apis.paths.streams_aptos_id_status import StreamsAptosIdStatus

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.HISTORY: History,
        PathValues.HISTORY_REPLAY_STREAM_ID_ID: HistoryReplayStreamIdId,
        PathValues.HISTORY_LOGS: HistoryLogs,
        PathValues.SETTINGS: Settings,
        PathValues.STATS: Stats,
        PathValues.STATS_STREAM_ID: StatsStreamId,
        PathValues.STREAMS_EVM: StreamsEvm,
        PathValues.STREAMS_EVM_ID: StreamsEvmId,
        PathValues.STREAMS_EVM_ID_STATUS: StreamsEvmIdStatus,
        PathValues.STREAMS_EVM_ID_ADDRESS: StreamsEvmIdAddress,
        PathValues.STREAMS_APTOS: StreamsAptos,
        PathValues.STREAMS_APTOS_ID: StreamsAptosId,
        PathValues.STREAMS_APTOS_ID_ADDRESS: StreamsAptosIdAddress,
        PathValues.STREAMS_APTOS_ID_STATUS: StreamsAptosIdStatus,
    }
)

path_to_api = PathToApi(
    {
        PathValues.HISTORY: History,
        PathValues.HISTORY_REPLAY_STREAM_ID_ID: HistoryReplayStreamIdId,
        PathValues.HISTORY_LOGS: HistoryLogs,
        PathValues.SETTINGS: Settings,
        PathValues.STATS: Stats,
        PathValues.STATS_STREAM_ID: StatsStreamId,
        PathValues.STREAMS_EVM: StreamsEvm,
        PathValues.STREAMS_EVM_ID: StreamsEvmId,
        PathValues.STREAMS_EVM_ID_STATUS: StreamsEvmIdStatus,
        PathValues.STREAMS_EVM_ID_ADDRESS: StreamsEvmIdAddress,
        PathValues.STREAMS_APTOS: StreamsAptos,
        PathValues.STREAMS_APTOS_ID: StreamsAptosId,
        PathValues.STREAMS_APTOS_ID_ADDRESS: StreamsAptosIdAddress,
        PathValues.STREAMS_APTOS_ID_STATUS: StreamsAptosIdStatus,
    }
)
