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
from openapi_evm_api.apis.paths.nft_search import NftSearch
from openapi_evm_api.apis.paths.erc20_address_price import Erc20AddressPrice
from openapi_evm_api.apis.paths.address_erc20 import AddressErc20
from openapi_evm_api.apis.paths.address_erc20_transfers import AddressErc20Transfers
from openapi_evm_api.apis.paths.erc20_metadata import Erc20Metadata
from openapi_evm_api.apis.paths.erc20_metadata_symbols import Erc20MetadataSymbols
from openapi_evm_api.apis.paths.erc20_address_allowance import Erc20AddressAllowance
from openapi_evm_api.apis.paths.erc20_address_transfers import Erc20AddressTransfers
from openapi_evm_api.apis.paths.address_balance import AddressBalance
from openapi_evm_api.apis.paths.address import Address
from openapi_evm_api.apis.paths.address_verbose import AddressVerbose
from openapi_evm_api.apis.paths.transaction_transaction_hash import TransactionTransactionHash
from openapi_evm_api.apis.paths.block_block_number_or_hash import BlockBlockNumberOrHash
from openapi_evm_api.apis.paths.date_to_block import DateToBlock
from openapi_evm_api.apis.paths.address_logs import AddressLogs
from openapi_evm_api.apis.paths.address_events import AddressEvents
from openapi_evm_api.apis.paths.address_function import AddressFunction
from openapi_evm_api.apis.paths.web3_version import Web3Version
from openapi_evm_api.apis.paths.info_endpoint_weights import InfoEndpointWeights
from openapi_evm_api.apis.paths.resolve_address_reverse import ResolveAddressReverse
from openapi_evm_api.apis.paths.resolve_domain import ResolveDomain
from openapi_evm_api.apis.paths.pair_address_reserves import PairAddressReserves
from openapi_evm_api.apis.paths.token0_address_token1_address_pair_address import Token0AddressToken1AddressPairAddress
from openapi_evm_api.apis.paths.ipfs_upload_folder import IpfsUploadFolder

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
        PathValues.NFT_SEARCH: NftSearch,
        PathValues.ERC20_ADDRESS_PRICE: Erc20AddressPrice,
        PathValues.ADDRESS_ERC20: AddressErc20,
        PathValues.ADDRESS_ERC20_TRANSFERS: AddressErc20Transfers,
        PathValues.ERC20_METADATA: Erc20Metadata,
        PathValues.ERC20_METADATA_SYMBOLS: Erc20MetadataSymbols,
        PathValues.ERC20_ADDRESS_ALLOWANCE: Erc20AddressAllowance,
        PathValues.ERC20_ADDRESS_TRANSFERS: Erc20AddressTransfers,
        PathValues.ADDRESS_BALANCE: AddressBalance,
        PathValues.ADDRESS: Address,
        PathValues.ADDRESS_VERBOSE: AddressVerbose,
        PathValues.TRANSACTION_TRANSACTION_HASH: TransactionTransactionHash,
        PathValues.BLOCK_BLOCK_NUMBER_OR_HASH: BlockBlockNumberOrHash,
        PathValues.DATE_TO_BLOCK: DateToBlock,
        PathValues.ADDRESS_LOGS: AddressLogs,
        PathValues.ADDRESS_EVENTS: AddressEvents,
        PathValues.ADDRESS_FUNCTION: AddressFunction,
        PathValues.WEB3_VERSION: Web3Version,
        PathValues.INFO_ENDPOINT_WEIGHTS: InfoEndpointWeights,
        PathValues.RESOLVE_ADDRESS_REVERSE: ResolveAddressReverse,
        PathValues.RESOLVE_DOMAIN: ResolveDomain,
        PathValues.PAIR_ADDRESS_RESERVES: PairAddressReserves,
        PathValues.TOKEN0_ADDRESS_TOKEN1_ADDRESS_PAIR_ADDRESS: Token0AddressToken1AddressPairAddress,
        PathValues.IPFS_UPLOAD_FOLDER: IpfsUploadFolder,
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
        PathValues.NFT_SEARCH: NftSearch,
        PathValues.ERC20_ADDRESS_PRICE: Erc20AddressPrice,
        PathValues.ADDRESS_ERC20: AddressErc20,
        PathValues.ADDRESS_ERC20_TRANSFERS: AddressErc20Transfers,
        PathValues.ERC20_METADATA: Erc20Metadata,
        PathValues.ERC20_METADATA_SYMBOLS: Erc20MetadataSymbols,
        PathValues.ERC20_ADDRESS_ALLOWANCE: Erc20AddressAllowance,
        PathValues.ERC20_ADDRESS_TRANSFERS: Erc20AddressTransfers,
        PathValues.ADDRESS_BALANCE: AddressBalance,
        PathValues.ADDRESS: Address,
        PathValues.ADDRESS_VERBOSE: AddressVerbose,
        PathValues.TRANSACTION_TRANSACTION_HASH: TransactionTransactionHash,
        PathValues.BLOCK_BLOCK_NUMBER_OR_HASH: BlockBlockNumberOrHash,
        PathValues.DATE_TO_BLOCK: DateToBlock,
        PathValues.ADDRESS_LOGS: AddressLogs,
        PathValues.ADDRESS_EVENTS: AddressEvents,
        PathValues.ADDRESS_FUNCTION: AddressFunction,
        PathValues.WEB3_VERSION: Web3Version,
        PathValues.INFO_ENDPOINT_WEIGHTS: InfoEndpointWeights,
        PathValues.RESOLVE_ADDRESS_REVERSE: ResolveAddressReverse,
        PathValues.RESOLVE_DOMAIN: ResolveDomain,
        PathValues.PAIR_ADDRESS_RESERVES: PairAddressReserves,
        PathValues.TOKEN0_ADDRESS_TOKEN1_ADDRESS_PAIR_ADDRESS: Token0AddressToken1AddressPairAddress,
        PathValues.IPFS_UPLOAD_FOLDER: IpfsUploadFolder,
    }
)
