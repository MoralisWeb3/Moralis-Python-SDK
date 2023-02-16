# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_streams.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    APTOS_STREAMS = "aptos_streams"
    EVM_STREAMS = "evm_streams"
    HISTORY = "history"
    LOGS = "logs"
    PROJECT = "project"
    STATS = "stats"
