import typing_extensions

from openapi_auth.apis.tags import TagValues
from openapi_auth.apis.tags.bind_api import BindApi
from openapi_auth.apis.tags.challenge_api import ChallengeApi
from openapi_auth.apis.tags.profile_api import ProfileApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BIND: BindApi,
        TagValues.CHALLENGE: ChallengeApi,
        TagValues.PROFILE: ProfileApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BIND: BindApi,
        TagValues.CHALLENGE: ChallengeApi,
        TagValues.PROFILE: ProfileApi,
    }
)
