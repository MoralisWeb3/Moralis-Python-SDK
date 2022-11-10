# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_sol_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACCOUNT_NETWORK_ADDRESS_BALANCE = "/account/{network}/{address}/balance"
    ACCOUNT_NETWORK_ADDRESS_TOKENS = "/account/{network}/{address}/tokens"
    ACCOUNT_NETWORK_ADDRESS_NFT = "/account/{network}/{address}/nft"
    ACCOUNT_NETWORK_ADDRESS_PORTFOLIO = "/account/{network}/{address}/portfolio"
    NFT_NETWORK_ADDRESS_METADATA = "/nft/{network}/{address}/metadata"
    TOKEN_NETWORK_ADDRESS_PRICE = "/token/{network}/{address}/price"
