# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_aptos_api.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCOUNTS = "accounts"
    BLOCKS = "blocks"
    COINS = "coins"
    COLLECTIONS = "collections"
    NFTS = "nfts"
    TRANSACTIONS = "transactions"
    WALLETS = "wallets"
