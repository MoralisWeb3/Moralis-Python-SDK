# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_evm_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ADDRESS_NFT = "/{address}/nft"
    NFT_GET_MULTIPLE_NFTS = "/nft/getMultipleNFTs"
    ADDRESS_NFT_TRANSFERS = "/{address}/nft/transfers"
    ADDRESS_NFT_COLLECTIONS = "/{address}/nft/collections"
    NFT_ADDRESS = "/nft/{address}"
    NFT_ADDRESS_OWNERS = "/nft/{address}/owners"
    NFT_ADDRESS_TRANSFERS = "/nft/{address}/transfers"
    NFT_TRANSFERS = "/nft/transfers"
    BLOCK_BLOCK_NUMBER_OR_HASH_NFT_TRANSFERS = "/block/{block_number_or_hash}/nft/transfers"
    NFT_ADDRESS_TRAITS = "/nft/{address}/traits"
    NFT_ADDRESS_TRAITS_PAGINATE = "/nft/{address}/traits/paginate"
    NFT_ADDRESS_TRAITS_RESYNC = "/nft/{address}/traits/resync"
    NFT_ADDRESS_TRADES = "/nft/{address}/trades"
    NFT_ADDRESS_TOKEN_ID_TRADES = "/nft/{address}/{token_id}/trades"
    WALLETS_ADDRESS_NFTS_TRADES = "/wallets/{address}/nfts/trades"
    NFT_ADDRESS_METADATA = "/nft/{address}/metadata"
    NFT_METADATA = "/nft/metadata"
    NFT_ADDRESS_TOKEN_ID = "/nft/{address}/{token_id}"
    NFT_ADDRESS_TOKEN_ID_TRANSFERS = "/nft/{address}/{token_id}/transfers"
    NFT_ADDRESS_TOKEN_ID_OWNERS = "/nft/{address}/{token_id}/owners"
    NFT_ADDRESS_SYNC = "/nft/{address}/sync"
    NFT_ADDRESS_TOKEN_ID_METADATA_RESYNC = "/nft/{address}/{token_id}/metadata/resync"
    NFT_ADDRESS_LOWESTPRICE = "/nft/{address}/lowestprice"
    NFT_ADDRESS_PRICE = "/nft/{address}/price"
    NFT_ADDRESS_TOKEN_ID_PRICE = "/nft/{address}/{token_id}/price"
    ERC20_ADDRESS_PRICE = "/erc20/{address}/price"
    ERC20_PRICES = "/erc20/prices"
    ERC20_TOKEN_ADDRESS_OWNERS = "/erc20/{token_address}/owners"
    ADDRESS_ERC20 = "/{address}/erc20"
    ADDRESS_ERC20_TRANSFERS = "/{address}/erc20/transfers"
    ERC20_METADATA = "/erc20/metadata"
    ERC20_METADATA_SYMBOLS = "/erc20/metadata/symbols"
    ERC20_ADDRESS_ALLOWANCE = "/erc20/{address}/allowance"
    ERC20_ADDRESS_TRANSFERS = "/erc20/{address}/transfers"
    ADDRESS_BALANCE = "/{address}/balance"
    WALLETS_BALANCES = "/wallets/balances"
    WALLETS_ADDRESS_HISTORY = "/wallets/{address}/history"
    WALLETS_ADDRESS_TOKENS = "/wallets/{address}/tokens"
    WALLETS_ADDRESS_NETWORTH = "/wallets/{address}/net-worth"
    ADDRESS = "/{address}"
    ADDRESS_VERBOSE = "/{address}/verbose"
    TRANSACTION_TRANSACTION_HASH_INTERNALTRANSACTIONS = "/transaction/{transaction_hash}/internal-transactions"
    TRANSACTION_TRANSACTION_HASH = "/transaction/{transaction_hash}"
    TRANSACTION_TRANSACTION_HASH_VERBOSE = "/transaction/{transaction_hash}/verbose"
    BLOCK_BLOCK_NUMBER_OR_HASH = "/block/{block_number_or_hash}"
    LATEST_BLOCK_NUMBER_CHAIN = "/latestBlockNumber/{chain}"
    DATE_TO_BLOCK = "/dateToBlock"
    ADDRESS_LOGS = "/{address}/logs"
    ADDRESS_EVENTS = "/{address}/events"
    ADDRESS_FUNCTION = "/{address}/function"
    WEB3_VERSION = "/web3/version"
    INFO_ENDPOINT_WEIGHTS = "/info/endpointWeights"
    RESOLVE_ADDRESS_REVERSE = "/resolve/{address}/reverse"
    RESOLVE_DOMAIN = "/resolve/{domain}"
    RESOLVE_ADDRESS_DOMAIN = "/resolve/{address}/domain"
    RESOLVE_ENS_DOMAIN = "/resolve/ens/{domain}"
    TOKEN0_ADDRESS_TOKEN1_ADDRESS_PRICE = "/{token0_address}/{token1_address}/price"
    PAIR_ADDRESS_RESERVES = "/{pair_address}/reserves"
    TOKEN0_ADDRESS_TOKEN1_ADDRESS_PAIR_ADDRESS = "/{token0_address}/{token1_address}/pairAddress"
    IPFS_UPLOAD_FOLDER = "/ipfs/uploadFolder"
    MARKETDATA_ERC20S_TOPTOKENS = "/market-data/erc20s/top-tokens"
    MARKETDATA_ERC20S_TOPMOVERS = "/market-data/erc20s/top-movers"
    MARKETDATA_NFTS_TOPCOLLECTIONS = "/market-data/nfts/top-collections"
    MARKETDATA_NFTS_HOTTESTCOLLECTIONS = "/market-data/nfts/hottest-collections"
    MARKETDATA_GLOBAL_MARKETCAP = "/market-data/global/market-cap"
    MARKETDATA_GLOBAL_VOLUME = "/market-data/global/volume"
    CONTRACTSREVIEW = "/contracts-review"
    WALLETS_ADDRESS_DEFI_SUMMARY = "/wallets/{address}/defi/summary"
    WALLETS_ADDRESS_DEFI_PROTOCOL_POSITIONS = "/wallets/{address}/defi/{protocol}/positions"
    WALLETS_ADDRESS_DEFI_POSITIONS = "/wallets/{address}/defi/positions"
    WALLETS_ADDRESS_CHAINS = "/wallets/{address}/chains"
    WALLETS_ADDRESS_STATS = "/wallets/{address}/stats"
    NFT_ADDRESS_STATS = "/nft/{address}/stats"
    NFT_ADDRESS_TOKEN_ID_STATS = "/nft/{address}/{token_id}/stats"
    ERC20_ADDRESS_STATS = "/erc20/{address}/stats"
    BLOCK_BLOCK_NUMBER_OR_HASH_STATS = "/block/{block_number_or_hash}/stats"
    DISCOVERY_TOKENS_RISINGLIQUIDITY = "/discovery/tokens/rising-liquidity"
    DISCOVERY_TOKENS_BUYINGPRESSURE = "/discovery/tokens/buying-pressure"
    DISCOVERY_TOKENS_SOLIDPERFORMERS = "/discovery/tokens/solid-performers"
    DISCOVERY_TOKENS_EXPERIENCEDBUYERS = "/discovery/tokens/experienced-buyers"
    DISCOVERY_TOKENS_RISKYBETS = "/discovery/tokens/risky-bets"
    DISCOVERY_TOKENS_BLUECHIP = "/discovery/tokens/blue-chip"
    DISCOVERY_TOKENS_TOPGAINERS = "/discovery/tokens/top-gainers"
    DISCOVERY_TOKENS_TOPLOSERS = "/discovery/tokens/top-losers"
    DISCOVERY_TOKENS_TRENDING = "/discovery/tokens/trending"
    DISCOVERY_TOKEN = "/discovery/token"
    WALLETS_ADDRESS_PROFITABILITY_SUMMARY = "/wallets/{address}/profitability/summary"
    WALLETS_ADDRESS_PROFITABILITY = "/wallets/{address}/profitability"
    ERC20_ADDRESS_TOPGAINERS = "/erc20/{address}/top-gainers"
