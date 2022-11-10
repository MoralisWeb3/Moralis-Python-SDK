# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_evm_api.paths.transaction_transaction_hash import Api

from openapi_evm_api.paths import PathValues

path = PathValues.TRANSACTION_TRANSACTION_HASH