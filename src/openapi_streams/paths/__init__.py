# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_streams.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    HISTORY = "/history"
    HISTORY_REPLAY_STREAM_ID_ID = "/history/replay/{streamId}/{id}"
    HISTORY_LOGS = "/history/logs"
    SETTINGS = "/settings"
    STATS = "/stats"
    STATS_STREAM_ID = "/stats/{streamId}"
    STREAMS_EVM = "/streams/evm"
    STREAMS_EVM_ID = "/streams/evm/{id}"
    STREAMS_EVM_ID_STATUS = "/streams/evm/{id}/status"
    STREAMS_EVM_ID_ADDRESS = "/streams/evm/{id}/address"
    STREAMS_APTOS = "/streams/aptos"
    STREAMS_APTOS_ID = "/streams/aptos/{id}"
    STREAMS_APTOS_ID_ADDRESS = "/streams/aptos/{id}/address"
    STREAMS_APTOS_ID_STATUS = "/streams/aptos/{id}/status"
