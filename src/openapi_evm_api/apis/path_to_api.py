import typing_extensions

from openapi_evm_api.paths import PathValues
from openapi_evm_api.apis.paths.address_nft import AddressNft
from openapi_evm_api.apis.paths.nft_get_multiple_nfts import NftGetMultipleNFTs
from openapi_evm_api.apis.paths.address_nft_transfers import AddressNftTransfers
from openapi_evm_api.apis.paths.address_nft_collections import AddressNftCollections
from openapi_evm_api.apis.paths.nft_address import NftAddress
from openapi_evm_api.apis.paths.nft_address_owners import NftAddressOwners
from openapi_evm_api.apis.paths.nft_address_transfers import NftAddressTransfers
from openapi_evm_api.apis.paths.nft_transfers import NftTransfers
from openapi_evm_api.apis.paths.block_block_number_or_hash_nft_transfers import BlockBlockNumberOrHashNftTransfers
from openapi_evm_api.apis.paths.nft_address_trades import NftAddressTrades
from openapi_evm_api.apis.paths.nft_address_metadata import NftAddressMetadata
from openapi_evm_api.apis.paths.nft_address_token_id import NftAddressTokenId
from openapi_evm_api.apis.paths.nft_address_token_id_transfers import NftAddressTokenIdTransfers
from openapi_evm_api.apis.paths.nft_address_token_id_owners import NftAddressTokenIdOwners
from openapi_evm_api.apis.paths.nft_address_sync import NftAddressSync
from openapi_evm_api.apis.paths.nft_address_token_id_metadata_resync import NftAddressTokenIdMetadataResync
from openapi_evm_api.apis.paths.nft_address_lowestprice import NftAddressLowestprice
from openapi_evm_api.apis.paths.erc20_address_price import Erc20AddressPrice
from openapi_evm_api.apis.paths.erc20_prices import Erc20Prices
from openapi_evm_api.apis.paths.address_erc20 import AddressErc20
from openapi_evm_api.apis.paths.address_erc20_transfers import AddressErc20Transfers
from openapi_evm_api.apis.paths.erc20_metadata import Erc20Metadata
from openapi_evm_api.apis.paths.erc20_metadata_symbols import Erc20MetadataSymbols
from openapi_evm_api.apis.paths.erc20_address_allowance import Erc20AddressAllowance
from openapi_evm_api.apis.paths.erc20_address_transfers import Erc20AddressTransfers
from openapi_evm_api.apis.paths.address_balance import AddressBalance
from openapi_evm_api.apis.paths.wallets_balances import WalletsBalances
from openapi_evm_api.apis.paths.address import Address
from openapi_evm_api.apis.paths.address_verbose import AddressVerbose
from openapi_evm_api.apis.paths.transaction_transaction_hash_internal_transactions import TransactionTransactionHashInternalTransactions
from openapi_evm_api.apis.paths.transaction_transaction_hash import TransactionTransactionHash
from openapi_evm_api.apis.paths.transaction_transaction_hash_verbose import TransactionTransactionHashVerbose
from openapi_evm_api.apis.paths.block_block_number_or_hash import BlockBlockNumberOrHash
from openapi_evm_api.apis.paths.date_to_block import DateToBlock
from openapi_evm_api.apis.paths.address_logs import AddressLogs
from openapi_evm_api.apis.paths.address_events import AddressEvents
from openapi_evm_api.apis.paths.address_function import AddressFunction
from openapi_evm_api.apis.paths.web3_version import Web3Version
from openapi_evm_api.apis.paths.info_endpoint_weights import InfoEndpointWeights
from openapi_evm_api.apis.paths.resolve_address_reverse import ResolveAddressReverse
from openapi_evm_api.apis.paths.resolve_domain import ResolveDomain
from openapi_evm_api.apis.paths.resolve_address_domain import ResolveAddressDomain
from openapi_evm_api.apis.paths.resolve_ens_domain import ResolveEnsDomain
from openapi_evm_api.apis.paths.pair_address_reserves import PairAddressReserves
from openapi_evm_api.apis.paths.token0_address_token1_address_pair_address import Token0AddressToken1AddressPairAddress
from openapi_evm_api.apis.paths.ipfs_upload_folder import IpfsUploadFolder
from openapi_evm_api.apis.paths.market_data_erc20s_top_tokens import MarketDataErc20sTopTokens
from openapi_evm_api.apis.paths.market_data_erc20s_top_movers import MarketDataErc20sTopMovers
from openapi_evm_api.apis.paths.market_data_nfts_top_collections import MarketDataNftsTopCollections
from openapi_evm_api.apis.paths.market_data_nfts_hottest_collections import MarketDataNftsHottestCollections
from openapi_evm_api.apis.paths.contracts_review import ContractsReview
from openapi_evm_api.apis.paths.wallets_address_chains import WalletsAddressChains
from openapi_evm_api.apis.paths.wallets_address_stats import WalletsAddressStats
from openapi_evm_api.apis.paths.nft_address_stats import NftAddressStats
from openapi_evm_api.apis.paths.nft_address_token_id_stats import NftAddressTokenIdStats
from openapi_evm_api.apis.paths.erc20_address_stats import Erc20AddressStats
from openapi_evm_api.apis.paths.block_block_number_or_hash_stats import BlockBlockNumberOrHashStats
from openapi_evm_api.apis.paths.discovery_tokens_rising_liquidity import DiscoveryTokensRisingLiquidity
from openapi_evm_api.apis.paths.discovery_tokens_buying_pressure import DiscoveryTokensBuyingPressure
from openapi_evm_api.apis.paths.discovery_tokens_solid_performers import DiscoveryTokensSolidPerformers
from openapi_evm_api.apis.paths.discovery_tokens_experienced_buyers import DiscoveryTokensExperiencedBuyers
from openapi_evm_api.apis.paths.discovery_tokens_risky_bets import DiscoveryTokensRiskyBets
from openapi_evm_api.apis.paths.discovery_tokens_blue_chip import DiscoveryTokensBlueChip
from openapi_evm_api.apis.paths.discovery_token import DiscoveryToken

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ADDRESS_NFT: AddressNft,
        PathValues.NFT_GET_MULTIPLE_NFTS: NftGetMultipleNFTs,
        PathValues.ADDRESS_NFT_TRANSFERS: AddressNftTransfers,
        PathValues.ADDRESS_NFT_COLLECTIONS: AddressNftCollections,
        PathValues.NFT_ADDRESS: NftAddress,
        PathValues.NFT_ADDRESS_OWNERS: NftAddressOwners,
        PathValues.NFT_ADDRESS_TRANSFERS: NftAddressTransfers,
        PathValues.NFT_TRANSFERS: NftTransfers,
        PathValues.BLOCK_BLOCK_NUMBER_OR_HASH_NFT_TRANSFERS: BlockBlockNumberOrHashNftTransfers,
        PathValues.NFT_ADDRESS_TRADES: NftAddressTrades,
        PathValues.NFT_ADDRESS_METADATA: NftAddressMetadata,
        PathValues.NFT_ADDRESS_TOKEN_ID: NftAddressTokenId,
        PathValues.NFT_ADDRESS_TOKEN_ID_TRANSFERS: NftAddressTokenIdTransfers,
        PathValues.NFT_ADDRESS_TOKEN_ID_OWNERS: NftAddressTokenIdOwners,
        PathValues.NFT_ADDRESS_SYNC: NftAddressSync,
        PathValues.NFT_ADDRESS_TOKEN_ID_METADATA_RESYNC: NftAddressTokenIdMetadataResync,
        PathValues.NFT_ADDRESS_LOWESTPRICE: NftAddressLowestprice,
        PathValues.ERC20_ADDRESS_PRICE: Erc20AddressPrice,
        PathValues.ERC20_PRICES: Erc20Prices,
        PathValues.ADDRESS_ERC20: AddressErc20,
        PathValues.ADDRESS_ERC20_TRANSFERS: AddressErc20Transfers,
        PathValues.ERC20_METADATA: Erc20Metadata,
        PathValues.ERC20_METADATA_SYMBOLS: Erc20MetadataSymbols,
        PathValues.ERC20_ADDRESS_ALLOWANCE: Erc20AddressAllowance,
        PathValues.ERC20_ADDRESS_TRANSFERS: Erc20AddressTransfers,
        PathValues.ADDRESS_BALANCE: AddressBalance,
        PathValues.WALLETS_BALANCES: WalletsBalances,
        PathValues.ADDRESS: Address,
        PathValues.ADDRESS_VERBOSE: AddressVerbose,
        PathValues.TRANSACTION_TRANSACTION_HASH_INTERNALTRANSACTIONS: TransactionTransactionHashInternalTransactions,
        PathValues.TRANSACTION_TRANSACTION_HASH: TransactionTransactionHash,
        PathValues.TRANSACTION_TRANSACTION_HASH_VERBOSE: TransactionTransactionHashVerbose,
        PathValues.BLOCK_BLOCK_NUMBER_OR_HASH: BlockBlockNumberOrHash,
        PathValues.DATE_TO_BLOCK: DateToBlock,
        PathValues.ADDRESS_LOGS: AddressLogs,
        PathValues.ADDRESS_EVENTS: AddressEvents,
        PathValues.ADDRESS_FUNCTION: AddressFunction,
        PathValues.WEB3_VERSION: Web3Version,
        PathValues.INFO_ENDPOINT_WEIGHTS: InfoEndpointWeights,
        PathValues.RESOLVE_ADDRESS_REVERSE: ResolveAddressReverse,
        PathValues.RESOLVE_DOMAIN: ResolveDomain,
        PathValues.RESOLVE_ADDRESS_DOMAIN: ResolveAddressDomain,
        PathValues.RESOLVE_ENS_DOMAIN: ResolveEnsDomain,
        PathValues.PAIR_ADDRESS_RESERVES: PairAddressReserves,
        PathValues.TOKEN0_ADDRESS_TOKEN1_ADDRESS_PAIR_ADDRESS: Token0AddressToken1AddressPairAddress,
        PathValues.IPFS_UPLOAD_FOLDER: IpfsUploadFolder,
        PathValues.MARKETDATA_ERC20S_TOPTOKENS: MarketDataErc20sTopTokens,
        PathValues.MARKETDATA_ERC20S_TOPMOVERS: MarketDataErc20sTopMovers,
        PathValues.MARKETDATA_NFTS_TOPCOLLECTIONS: MarketDataNftsTopCollections,
        PathValues.MARKETDATA_NFTS_HOTTESTCOLLECTIONS: MarketDataNftsHottestCollections,
        PathValues.CONTRACTSREVIEW: ContractsReview,
        PathValues.WALLETS_ADDRESS_CHAINS: WalletsAddressChains,
        PathValues.WALLETS_ADDRESS_STATS: WalletsAddressStats,
        PathValues.NFT_ADDRESS_STATS: NftAddressStats,
        PathValues.NFT_ADDRESS_TOKEN_ID_STATS: NftAddressTokenIdStats,
        PathValues.ERC20_ADDRESS_STATS: Erc20AddressStats,
        PathValues.BLOCK_BLOCK_NUMBER_OR_HASH_STATS: BlockBlockNumberOrHashStats,
        PathValues.DISCOVERY_TOKENS_RISINGLIQUIDITY: DiscoveryTokensRisingLiquidity,
        PathValues.DISCOVERY_TOKENS_BUYINGPRESSURE: DiscoveryTokensBuyingPressure,
        PathValues.DISCOVERY_TOKENS_SOLIDPERFORMERS: DiscoveryTokensSolidPerformers,
        PathValues.DISCOVERY_TOKENS_EXPERIENCEDBUYERS: DiscoveryTokensExperiencedBuyers,
        PathValues.DISCOVERY_TOKENS_RISKYBETS: DiscoveryTokensRiskyBets,
        PathValues.DISCOVERY_TOKENS_BLUECHIP: DiscoveryTokensBlueChip,
        PathValues.DISCOVERY_TOKEN: DiscoveryToken,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ADDRESS_NFT: AddressNft,
        PathValues.NFT_GET_MULTIPLE_NFTS: NftGetMultipleNFTs,
        PathValues.ADDRESS_NFT_TRANSFERS: AddressNftTransfers,
        PathValues.ADDRESS_NFT_COLLECTIONS: AddressNftCollections,
        PathValues.NFT_ADDRESS: NftAddress,
        PathValues.NFT_ADDRESS_OWNERS: NftAddressOwners,
        PathValues.NFT_ADDRESS_TRANSFERS: NftAddressTransfers,
        PathValues.NFT_TRANSFERS: NftTransfers,
        PathValues.BLOCK_BLOCK_NUMBER_OR_HASH_NFT_TRANSFERS: BlockBlockNumberOrHashNftTransfers,
        PathValues.NFT_ADDRESS_TRADES: NftAddressTrades,
        PathValues.NFT_ADDRESS_METADATA: NftAddressMetadata,
        PathValues.NFT_ADDRESS_TOKEN_ID: NftAddressTokenId,
        PathValues.NFT_ADDRESS_TOKEN_ID_TRANSFERS: NftAddressTokenIdTransfers,
        PathValues.NFT_ADDRESS_TOKEN_ID_OWNERS: NftAddressTokenIdOwners,
        PathValues.NFT_ADDRESS_SYNC: NftAddressSync,
        PathValues.NFT_ADDRESS_TOKEN_ID_METADATA_RESYNC: NftAddressTokenIdMetadataResync,
        PathValues.NFT_ADDRESS_LOWESTPRICE: NftAddressLowestprice,
        PathValues.ERC20_ADDRESS_PRICE: Erc20AddressPrice,
        PathValues.ERC20_PRICES: Erc20Prices,
        PathValues.ADDRESS_ERC20: AddressErc20,
        PathValues.ADDRESS_ERC20_TRANSFERS: AddressErc20Transfers,
        PathValues.ERC20_METADATA: Erc20Metadata,
        PathValues.ERC20_METADATA_SYMBOLS: Erc20MetadataSymbols,
        PathValues.ERC20_ADDRESS_ALLOWANCE: Erc20AddressAllowance,
        PathValues.ERC20_ADDRESS_TRANSFERS: Erc20AddressTransfers,
        PathValues.ADDRESS_BALANCE: AddressBalance,
        PathValues.WALLETS_BALANCES: WalletsBalances,
        PathValues.ADDRESS: Address,
        PathValues.ADDRESS_VERBOSE: AddressVerbose,
        PathValues.TRANSACTION_TRANSACTION_HASH_INTERNALTRANSACTIONS: TransactionTransactionHashInternalTransactions,
        PathValues.TRANSACTION_TRANSACTION_HASH: TransactionTransactionHash,
        PathValues.TRANSACTION_TRANSACTION_HASH_VERBOSE: TransactionTransactionHashVerbose,
        PathValues.BLOCK_BLOCK_NUMBER_OR_HASH: BlockBlockNumberOrHash,
        PathValues.DATE_TO_BLOCK: DateToBlock,
        PathValues.ADDRESS_LOGS: AddressLogs,
        PathValues.ADDRESS_EVENTS: AddressEvents,
        PathValues.ADDRESS_FUNCTION: AddressFunction,
        PathValues.WEB3_VERSION: Web3Version,
        PathValues.INFO_ENDPOINT_WEIGHTS: InfoEndpointWeights,
        PathValues.RESOLVE_ADDRESS_REVERSE: ResolveAddressReverse,
        PathValues.RESOLVE_DOMAIN: ResolveDomain,
        PathValues.RESOLVE_ADDRESS_DOMAIN: ResolveAddressDomain,
        PathValues.RESOLVE_ENS_DOMAIN: ResolveEnsDomain,
        PathValues.PAIR_ADDRESS_RESERVES: PairAddressReserves,
        PathValues.TOKEN0_ADDRESS_TOKEN1_ADDRESS_PAIR_ADDRESS: Token0AddressToken1AddressPairAddress,
        PathValues.IPFS_UPLOAD_FOLDER: IpfsUploadFolder,
        PathValues.MARKETDATA_ERC20S_TOPTOKENS: MarketDataErc20sTopTokens,
        PathValues.MARKETDATA_ERC20S_TOPMOVERS: MarketDataErc20sTopMovers,
        PathValues.MARKETDATA_NFTS_TOPCOLLECTIONS: MarketDataNftsTopCollections,
        PathValues.MARKETDATA_NFTS_HOTTESTCOLLECTIONS: MarketDataNftsHottestCollections,
        PathValues.CONTRACTSREVIEW: ContractsReview,
        PathValues.WALLETS_ADDRESS_CHAINS: WalletsAddressChains,
        PathValues.WALLETS_ADDRESS_STATS: WalletsAddressStats,
        PathValues.NFT_ADDRESS_STATS: NftAddressStats,
        PathValues.NFT_ADDRESS_TOKEN_ID_STATS: NftAddressTokenIdStats,
        PathValues.ERC20_ADDRESS_STATS: Erc20AddressStats,
        PathValues.BLOCK_BLOCK_NUMBER_OR_HASH_STATS: BlockBlockNumberOrHashStats,
        PathValues.DISCOVERY_TOKENS_RISINGLIQUIDITY: DiscoveryTokensRisingLiquidity,
        PathValues.DISCOVERY_TOKENS_BUYINGPRESSURE: DiscoveryTokensBuyingPressure,
        PathValues.DISCOVERY_TOKENS_SOLIDPERFORMERS: DiscoveryTokensSolidPerformers,
        PathValues.DISCOVERY_TOKENS_EXPERIENCEDBUYERS: DiscoveryTokensExperiencedBuyers,
        PathValues.DISCOVERY_TOKENS_RISKYBETS: DiscoveryTokensRiskyBets,
        PathValues.DISCOVERY_TOKENS_BLUECHIP: DiscoveryTokensBlueChip,
        PathValues.DISCOVERY_TOKEN: DiscoveryToken,
    }
)
