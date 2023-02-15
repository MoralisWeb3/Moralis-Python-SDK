# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_auth.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CHALLENGE_REQUEST_EVM = "/challenge/request/evm"
    CHALLENGE_VERIFY_EVM = "/challenge/verify/evm"
    CHALLENGE_REQUEST_SOLANA = "/challenge/request/solana"
    CHALLENGE_VERIFY_SOLANA = "/challenge/verify/solana"
    CHALLENGE_REQUEST_APTOS = "/challenge/request/aptos"
    CHALLENGE_VERIFY_APTOS = "/challenge/verify/aptos"
    PROFILE_PROFILE_ID_ADDRESSES = "/profile/{profileId}/addresses"
    BIND_REQUEST = "/bind/request"
    BIND_REQUEST_VERIFY = "/bind/request/verify"
    BIND_REMOVE = "/bind/remove"
    BIND_REMOVE_VERIFY = "/bind/remove/verify"
