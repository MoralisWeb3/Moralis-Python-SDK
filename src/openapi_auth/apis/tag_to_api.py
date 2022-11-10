import typing_extensions

from openapi_auth.apis.tags import TagValues
from openapi_auth.apis.tags.challenge_api import ChallengeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CHALLENGE: ChallengeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CHALLENGE: ChallengeApi,
    }
)
