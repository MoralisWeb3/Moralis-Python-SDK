# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_evm_api.paths.block_block_number_or_hash import Api

from openapi_evm_api.paths import PathValues

path = PathValues.BLOCK_BLOCK_NUMBER_OR_HASH