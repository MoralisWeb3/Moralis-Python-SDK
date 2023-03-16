import typing_extensions

from openapi_aptos_api.apis.tags import TagValues
from openapi_aptos_api.apis.tags.accounts_api import AccountsApi
from openapi_aptos_api.apis.tags.blocks_api import BlocksApi
from openapi_aptos_api.apis.tags.coins_api import CoinsApi
from openapi_aptos_api.apis.tags.collections_api import CollectionsApi
from openapi_aptos_api.apis.tags.nfts_api import NftsApi
from openapi_aptos_api.apis.tags.transactions_api import TransactionsApi
from openapi_aptos_api.apis.tags.wallets_api import WalletsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.BLOCKS: BlocksApi,
        TagValues.COINS: CoinsApi,
        TagValues.COLLECTIONS: CollectionsApi,
        TagValues.NFTS: NftsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.WALLETS: WalletsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.BLOCKS: BlocksApi,
        TagValues.COINS: CoinsApi,
        TagValues.COLLECTIONS: CollectionsApi,
        TagValues.NFTS: NftsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.WALLETS: WalletsApi,
    }
)
