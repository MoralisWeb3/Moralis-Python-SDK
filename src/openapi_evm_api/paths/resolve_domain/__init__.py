# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_evm_api.paths.resolve_domain import Api

from openapi_evm_api.paths import PathValues

path = PathValues.RESOLVE_DOMAIN