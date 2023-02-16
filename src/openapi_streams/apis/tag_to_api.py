import typing_extensions

from openapi_streams.apis.tags import TagValues
from openapi_streams.apis.tags.aptos_streams_api import AptosStreamsApi
from openapi_streams.apis.tags.evm_streams_api import EvmStreamsApi
from openapi_streams.apis.tags.history_api import HistoryApi
from openapi_streams.apis.tags.logs_api import LogsApi
from openapi_streams.apis.tags.project_api import ProjectApi
from openapi_streams.apis.tags.stats_api import StatsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.APTOS_STREAMS: AptosStreamsApi,
        TagValues.EVM_STREAMS: EvmStreamsApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.LOGS: LogsApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.STATS: StatsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.APTOS_STREAMS: AptosStreamsApi,
        TagValues.EVM_STREAMS: EvmStreamsApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.LOGS: LogsApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.STATS: StatsApi,
    }
)
