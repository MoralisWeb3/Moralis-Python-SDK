import typing_extensions

from openapi_aptos_api.paths import PathValues
from openapi_aptos_api.apis.paths.nfts import Nfts
from openapi_aptos_api.apis.paths.nfts_collections_collection_data_id_hash_tokens import NftsCollectionsCollectionDataIdHashTokens
from openapi_aptos_api.apis.paths.nfts_creators import NftsCreators
from openapi_aptos_api.apis.paths.collections import Collections
from openapi_aptos_api.apis.paths.collections_ids import CollectionsIds
from openapi_aptos_api.apis.paths.collections_creators import CollectionsCreators
from openapi_aptos_api.apis.paths.nfts_owners import NftsOwners
from openapi_aptos_api.apis.paths.nfts_collections_collection_data_id_hash_owners import NftsCollectionsCollectionDataIdHashOwners
from openapi_aptos_api.apis.paths.nfts_collections_collection_data_id_hash_owners_list import NftsCollectionsCollectionDataIdHashOwnersList
from openapi_aptos_api.apis.paths.nfts_transfers import NftsTransfers
from openapi_aptos_api.apis.paths.nfts_transfers_collections_collection_data_id_hash import NftsTransfersCollectionsCollectionDataIdHash
from openapi_aptos_api.apis.paths.nfts_transfers_creators import NftsTransfersCreators
from openapi_aptos_api.apis.paths.nfts_transfers_wallets import NftsTransfersWallets
from openapi_aptos_api.apis.paths.coins import Coins
from openapi_aptos_api.apis.paths.coins_latest import CoinsLatest
from openapi_aptos_api.apis.paths.coins_names import CoinsNames
from openapi_aptos_api.apis.paths.coins_symbols import CoinsSymbols
from openapi_aptos_api.apis.paths.coins_creators import CoinsCreators
from openapi_aptos_api.apis.paths.coins_transfers_wallets import CoinsTransfersWallets
from openapi_aptos_api.apis.paths.coins_transfers_blocks import CoinsTransfersBlocks
from openapi_aptos_api.apis.paths.coins_transfers_coin_type import CoinsTransfersCoinType
from openapi_aptos_api.apis.paths.coins_owners_coin_type_hash_top_holders import CoinsOwnersCoinTypeHashTopHolders
from openapi_aptos_api.apis.paths.wallets_coins import WalletsCoins
from openapi_aptos_api.apis.paths.wallets_coins_history import WalletsCoinsHistory
from openapi_aptos_api.apis.paths.wallets_coins_transfers import WalletsCoinsTransfers
from openapi_aptos_api.apis.paths.wallets_nfts import WalletsNfts
from openapi_aptos_api.apis.paths.wallets_nfts_transfers import WalletsNftsTransfers
from openapi_aptos_api.apis.paths.accounts_address import AccountsAddress
from openapi_aptos_api.apis.paths.accounts_address_resources import AccountsAddressResources
from openapi_aptos_api.apis.paths.accounts_address_modules import AccountsAddressModules
from openapi_aptos_api.apis.paths.accounts_address_resource_resource_type import AccountsAddressResourceResourceType
from openapi_aptos_api.apis.paths.accounts_address_resource_module_name import AccountsAddressResourceModuleName
from openapi_aptos_api.apis.paths.accounts_address_events_creation_number import AccountsAddressEventsCreationNumber
from openapi_aptos_api.apis.paths.accounts_address_events_event_handle_field_name import AccountsAddressEventsEventHandleFieldName
from openapi_aptos_api.apis.paths.transactions import Transactions
from openapi_aptos_api.apis.paths.transactions_by_hash_txn_hash import TransactionsByHashTxnHash
from openapi_aptos_api.apis.paths.transactions_by_version_txn_version import TransactionsByVersionTxnVersion
from openapi_aptos_api.apis.paths.accounts_address_transactions import AccountsAddressTransactions
from openapi_aptos_api.apis.paths.transactions_batch import TransactionsBatch
from openapi_aptos_api.apis.paths.transactions_simulate import TransactionsSimulate
from openapi_aptos_api.apis.paths.transactions_encode_submission import TransactionsEncodeSubmission
from openapi_aptos_api.apis.paths.transactions_estimate_gas_price import TransactionsEstimateGasPrice
from openapi_aptos_api.apis.paths.blocks_block_height import BlocksBlockHeight
from openapi_aptos_api.apis.paths.blocks_by_version_version import BlocksByVersionVersion

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.NFTS: Nfts,
        PathValues.NFTS_COLLECTIONS_COLLECTION_DATA_ID_HASH_TOKENS: NftsCollectionsCollectionDataIdHashTokens,
        PathValues.NFTS_CREATORS: NftsCreators,
        PathValues.COLLECTIONS: Collections,
        PathValues.COLLECTIONS_IDS: CollectionsIds,
        PathValues.COLLECTIONS_CREATORS: CollectionsCreators,
        PathValues.NFTS_OWNERS: NftsOwners,
        PathValues.NFTS_COLLECTIONS_COLLECTION_DATA_ID_HASH_OWNERS: NftsCollectionsCollectionDataIdHashOwners,
        PathValues.NFTS_COLLECTIONS_COLLECTION_DATA_ID_HASH_OWNERS_LIST: NftsCollectionsCollectionDataIdHashOwnersList,
        PathValues.NFTS_TRANSFERS: NftsTransfers,
        PathValues.NFTS_TRANSFERS_COLLECTIONS_COLLECTION_DATA_ID_HASH: NftsTransfersCollectionsCollectionDataIdHash,
        PathValues.NFTS_TRANSFERS_CREATORS: NftsTransfersCreators,
        PathValues.NFTS_TRANSFERS_WALLETS: NftsTransfersWallets,
        PathValues.COINS: Coins,
        PathValues.COINS_LATEST: CoinsLatest,
        PathValues.COINS_NAMES: CoinsNames,
        PathValues.COINS_SYMBOLS: CoinsSymbols,
        PathValues.COINS_CREATORS: CoinsCreators,
        PathValues.COINS_TRANSFERS_WALLETS: CoinsTransfersWallets,
        PathValues.COINS_TRANSFERS_BLOCKS: CoinsTransfersBlocks,
        PathValues.COINS_TRANSFERS_COIN_TYPE: CoinsTransfersCoinType,
        PathValues.COINS_OWNERS_COIN_TYPE_HASH_TOPHOLDERS: CoinsOwnersCoinTypeHashTopHolders,
        PathValues.WALLETS_COINS: WalletsCoins,
        PathValues.WALLETS_COINS_HISTORY: WalletsCoinsHistory,
        PathValues.WALLETS_COINS_TRANSFERS: WalletsCoinsTransfers,
        PathValues.WALLETS_NFTS: WalletsNfts,
        PathValues.WALLETS_NFTS_TRANSFERS: WalletsNftsTransfers,
        PathValues.ACCOUNTS_ADDRESS: AccountsAddress,
        PathValues.ACCOUNTS_ADDRESS_RESOURCES: AccountsAddressResources,
        PathValues.ACCOUNTS_ADDRESS_MODULES: AccountsAddressModules,
        PathValues.ACCOUNTS_ADDRESS_RESOURCE_RESOURCE_TYPE: AccountsAddressResourceResourceType,
        PathValues.ACCOUNTS_ADDRESS_RESOURCE_MODULE_NAME: AccountsAddressResourceModuleName,
        PathValues.ACCOUNTS_ADDRESS_EVENTS_CREATION_NUMBER: AccountsAddressEventsCreationNumber,
        PathValues.ACCOUNTS_ADDRESS_EVENTS_EVENT_HANDLE_FIELD_NAME: AccountsAddressEventsEventHandleFieldName,
        PathValues.TRANSACTIONS: Transactions,
        PathValues.TRANSACTIONS_BY_HASH_TXN_HASH: TransactionsByHashTxnHash,
        PathValues.TRANSACTIONS_BY_VERSION_TXN_VERSION: TransactionsByVersionTxnVersion,
        PathValues.ACCOUNTS_ADDRESS_TRANSACTIONS: AccountsAddressTransactions,
        PathValues.TRANSACTIONS_BATCH: TransactionsBatch,
        PathValues.TRANSACTIONS_SIMULATE: TransactionsSimulate,
        PathValues.TRANSACTIONS_ENCODE_SUBMISSION: TransactionsEncodeSubmission,
        PathValues.TRANSACTIONS_ESTIMATE_GAS_PRICE: TransactionsEstimateGasPrice,
        PathValues.BLOCKS_BLOCK_HEIGHT: BlocksBlockHeight,
        PathValues.BLOCKS_BY_VERSION_VERSION: BlocksByVersionVersion,
    }
)

path_to_api = PathToApi(
    {
        PathValues.NFTS: Nfts,
        PathValues.NFTS_COLLECTIONS_COLLECTION_DATA_ID_HASH_TOKENS: NftsCollectionsCollectionDataIdHashTokens,
        PathValues.NFTS_CREATORS: NftsCreators,
        PathValues.COLLECTIONS: Collections,
        PathValues.COLLECTIONS_IDS: CollectionsIds,
        PathValues.COLLECTIONS_CREATORS: CollectionsCreators,
        PathValues.NFTS_OWNERS: NftsOwners,
        PathValues.NFTS_COLLECTIONS_COLLECTION_DATA_ID_HASH_OWNERS: NftsCollectionsCollectionDataIdHashOwners,
        PathValues.NFTS_COLLECTIONS_COLLECTION_DATA_ID_HASH_OWNERS_LIST: NftsCollectionsCollectionDataIdHashOwnersList,
        PathValues.NFTS_TRANSFERS: NftsTransfers,
        PathValues.NFTS_TRANSFERS_COLLECTIONS_COLLECTION_DATA_ID_HASH: NftsTransfersCollectionsCollectionDataIdHash,
        PathValues.NFTS_TRANSFERS_CREATORS: NftsTransfersCreators,
        PathValues.NFTS_TRANSFERS_WALLETS: NftsTransfersWallets,
        PathValues.COINS: Coins,
        PathValues.COINS_LATEST: CoinsLatest,
        PathValues.COINS_NAMES: CoinsNames,
        PathValues.COINS_SYMBOLS: CoinsSymbols,
        PathValues.COINS_CREATORS: CoinsCreators,
        PathValues.COINS_TRANSFERS_WALLETS: CoinsTransfersWallets,
        PathValues.COINS_TRANSFERS_BLOCKS: CoinsTransfersBlocks,
        PathValues.COINS_TRANSFERS_COIN_TYPE: CoinsTransfersCoinType,
        PathValues.COINS_OWNERS_COIN_TYPE_HASH_TOPHOLDERS: CoinsOwnersCoinTypeHashTopHolders,
        PathValues.WALLETS_COINS: WalletsCoins,
        PathValues.WALLETS_COINS_HISTORY: WalletsCoinsHistory,
        PathValues.WALLETS_COINS_TRANSFERS: WalletsCoinsTransfers,
        PathValues.WALLETS_NFTS: WalletsNfts,
        PathValues.WALLETS_NFTS_TRANSFERS: WalletsNftsTransfers,
        PathValues.ACCOUNTS_ADDRESS: AccountsAddress,
        PathValues.ACCOUNTS_ADDRESS_RESOURCES: AccountsAddressResources,
        PathValues.ACCOUNTS_ADDRESS_MODULES: AccountsAddressModules,
        PathValues.ACCOUNTS_ADDRESS_RESOURCE_RESOURCE_TYPE: AccountsAddressResourceResourceType,
        PathValues.ACCOUNTS_ADDRESS_RESOURCE_MODULE_NAME: AccountsAddressResourceModuleName,
        PathValues.ACCOUNTS_ADDRESS_EVENTS_CREATION_NUMBER: AccountsAddressEventsCreationNumber,
        PathValues.ACCOUNTS_ADDRESS_EVENTS_EVENT_HANDLE_FIELD_NAME: AccountsAddressEventsEventHandleFieldName,
        PathValues.TRANSACTIONS: Transactions,
        PathValues.TRANSACTIONS_BY_HASH_TXN_HASH: TransactionsByHashTxnHash,
        PathValues.TRANSACTIONS_BY_VERSION_TXN_VERSION: TransactionsByVersionTxnVersion,
        PathValues.ACCOUNTS_ADDRESS_TRANSACTIONS: AccountsAddressTransactions,
        PathValues.TRANSACTIONS_BATCH: TransactionsBatch,
        PathValues.TRANSACTIONS_SIMULATE: TransactionsSimulate,
        PathValues.TRANSACTIONS_ENCODE_SUBMISSION: TransactionsEncodeSubmission,
        PathValues.TRANSACTIONS_ESTIMATE_GAS_PRICE: TransactionsEstimateGasPrice,
        PathValues.BLOCKS_BLOCK_HEIGHT: BlocksBlockHeight,
        PathValues.BLOCKS_BY_VERSION_VERSION: BlocksByVersionVersion,
    }
)
