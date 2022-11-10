# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_streams.paths.history import Api

from openapi_streams.paths import PathValues

path = PathValues.HISTORY