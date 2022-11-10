import typing_extensions

from openapi_streams.apis.tags import TagValues
from openapi_streams.apis.tags.evm_api import EvmApi
from openapi_streams.apis.tags.history_api import HistoryApi
from openapi_streams.apis.tags.project_api import ProjectApi
from openapi_streams.apis.tags.stats_api import StatsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EVM: EvmApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.STATS: StatsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EVM: EvmApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.STATS: StatsApi,
    }
)
