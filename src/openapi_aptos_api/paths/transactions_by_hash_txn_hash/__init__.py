# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_aptos_api.paths.transactions_by_hash_txn_hash import Api

from openapi_aptos_api.paths import PathValues

path = PathValues.TRANSACTIONS_BY_HASH_TXN_HASH