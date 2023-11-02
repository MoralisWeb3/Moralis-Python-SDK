import typing_extensions

from openapi_evm_api.apis.tags import TagValues
from openapi_evm_api.apis.tags.balance_api import BalanceApi
from openapi_evm_api.apis.tags.block_api import BlockApi
from openapi_evm_api.apis.tags.default_api import DefaultApi
from openapi_evm_api.apis.tags.defi_api import DefiApi
from openapi_evm_api.apis.tags.events_api import EventsApi
from openapi_evm_api.apis.tags.ipfs_api import IpfsApi
from openapi_evm_api.apis.tags.market_data_api import MarketDataApi
from openapi_evm_api.apis.tags.nft_api import NftApi
from openapi_evm_api.apis.tags.resolve_api import ResolveApi
from openapi_evm_api.apis.tags.token_api import TokenApi
from openapi_evm_api.apis.tags.transaction_api import TransactionApi
from openapi_evm_api.apis.tags.utils_api import UtilsApi
from openapi_evm_api.apis.tags.wallets_api import WalletsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BALANCE: BalanceApi,
        TagValues.BLOCK: BlockApi,
        TagValues.DEFAULT: DefaultApi,
        TagValues.DEFI: DefiApi,
        TagValues.EVENTS: EventsApi,
        TagValues.IPFS: IpfsApi,
        TagValues.MARKET_DATA: MarketDataApi,
        TagValues.NFT: NftApi,
        TagValues.RESOLVE: ResolveApi,
        TagValues.TOKEN: TokenApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.UTILS: UtilsApi,
        TagValues.WALLETS: WalletsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BALANCE: BalanceApi,
        TagValues.BLOCK: BlockApi,
        TagValues.DEFAULT: DefaultApi,
        TagValues.DEFI: DefiApi,
        TagValues.EVENTS: EventsApi,
        TagValues.IPFS: IpfsApi,
        TagValues.MARKET_DATA: MarketDataApi,
        TagValues.NFT: NftApi,
        TagValues.RESOLVE: ResolveApi,
        TagValues.TOKEN: TokenApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.UTILS: UtilsApi,
        TagValues.WALLETS: WalletsApi,
    }
)
