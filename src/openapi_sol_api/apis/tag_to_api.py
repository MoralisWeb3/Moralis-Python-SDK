import typing_extensions

from openapi_sol_api.apis.tags import TagValues
from openapi_sol_api.apis.tags.account_api import AccountApi
from openapi_sol_api.apis.tags.nft_api import NftApi
from openapi_sol_api.apis.tags.token_api import TokenApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.NFT: NftApi,
        TagValues.TOKEN: TokenApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.NFT: NftApi,
        TagValues.TOKEN: TokenApi,
    }
)
