# nft API:

> `evm_api.nft`

- [get_contract_nfts](#get_contract_nfts)
- [get_multiple_nfts](#get_multiple_nfts)
- [get_nft_bulk_contract_metadata](#get_nft_bulk_contract_metadata)
- [get_nft_collection_stats](#get_nft_collection_stats)
- [get_nft_contract_metadata](#get_nft_contract_metadata)
- [get_nft_contract_sale_prices](#get_nft_contract_sale_prices)
- [get_nft_contract_transfers](#get_nft_contract_transfers)
- [get_nft_lowest_price](#get_nft_lowest_price)
- [get_nft_metadata](#get_nft_metadata)
- [get_nft_owners](#get_nft_owners)
- [get_nft_sale_prices](#get_nft_sale_prices)
- [get_nft_token_id_owners](#get_nft_token_id_owners)
- [get_nft_token_stats](#get_nft_token_stats)
- [get_nft_trades](#get_nft_trades)
- [get_nft_trades_by_token](#get_nft_trades_by_token)
- [get_nft_trades_by_wallet](#get_nft_trades_by_wallet)
- [get_nft_transfers](#get_nft_transfers)
- [get_nft_transfers_by_block](#get_nft_transfers_by_block)
- [get_nft_transfers_from_to_block](#get_nft_transfers_from_to_block)
- [get_wallet_nft_collections](#get_wallet_nft_collections)
- [get_wallet_nft_transfers](#get_wallet_nft_transfers)
- [get_wallet_nfts](#get_wallet_nfts)
- [re_sync_metadata](#re_sync_metadata)
- [sync_nft_contract](#sync_nft_contract)


---
## get_contract_nfts

> `evm_api.nft.get_contract_nfts()`

Get NFTs for a given contract address, including metadata for all NFTs (where available).
* Results are limited to 100 per page by default
* Requests for contract addresses not yet indexed will automatically start the indexing process for that NFT collection.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB", 
    "chain": "eth", 
    "format": "decimal", 
    "limit": 0, 
    "totalRanges": 0, 
    "range": 0, 
    "cursor": "", 
    "normalizeMetadata": True, 
    "media_items": True, 
}

result = evm_api.nft.get_contract_nfts(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| totalRanges | int | The number of subranges to split the results into |  |  | 0 |
| range | int | The desired subrange to query |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| normalizeMetadata | bool | Should normalized metadata be returned? |  | False | True |
| media_items | bool | Should preview media data be returned? |  | False | True |



---
## get_multiple_nfts

> `evm_api.nft.get_multiple_nfts()`

Returns an array of NFTs specified in the request.
* Note that results will include all indexed NFTs
* Any request that includes the token_address param will start the indexing process for that NFT collection the very first time it is requested.
* Only 25 NFTs can be fetched in one API call.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "chain": "eth", 
}
body = {
    "tokens": [{'token_address': '0xa4991609c508b6d4fb7156426db0bd49fe298bd8', 'token_id': '12'}, {'token_address': '0x3c64dc415ebb4690d1df2b6216148c8de6dd29f7', 'token_id': '1'}, {'token_address': '0x3c64dc415ebb4690d1df2b6216148c8de6dd29f7', 'token_id': '200'}], 
    "normalizeMetadata": False, 
    "media_items": False, 
}

result = evm_api.nft.get_multiple_nfts(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |


### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| tokens | List of object: <br/> - token_address: str<br/> - token_id: str | The tokens to be fetched (max 25 tokens) | Yes |  | [{'token_address': '0xa4991609c508b6d4fb7156426db0bd49fe298bd8', 'token_id': '12'}, {'token_address': '0x3c64dc415ebb4690d1df2b6216148c8de6dd29f7', 'token_id': '1'}, {'token_address': '0x3c64dc415ebb4690d1df2b6216148c8de6dd29f7', 'token_id': '200'}] |
| normalizeMetadata | bool | Should normalized metadata be returned? | Yes |  | False |
| media_items | bool | Should preview media data be returned? | Yes |  | False |


---
## get_nft_bulk_contract_metadata

> `evm_api.nft.get_nft_bulk_contract_metadata()`

Get the collection / contract level metadata for a given list of contract addresses (name, symbol). Supports batching up to 25 addresses.
* Requests for contract addresses not yet indexed will automatically start the indexing process for that NFT collection



### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "chain": "eth", 
}
body = ""

result = evm_api.nft.get_nft_bulk_contract_metadata(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |


### Body

| Type | Description | Required |
|------|-------------|----------|
| object: <br/> - addresses: List of str | Body | Yes |


---
## get_nft_collection_stats

> `evm_api.nft.get_nft_collection_stats()`

Get the stats for a nft collection address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
}

result = evm_api.nft.get_nft_collection_stats(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT collection | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |



---
## get_nft_contract_metadata

> `evm_api.nft.get_nft_contract_metadata()`

Get the collection / contract level metadata for a given contract (name, symbol, base token URI).
* Requests for contract addresses not yet indexed will automatically start the indexing process for that NFT collection



### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x524cab2ec69124574082676e6f654a18df49a048", 
    "chain": "eth", 
}

result = evm_api.nft.get_nft_contract_metadata(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0x524cab2ec69124574082676e6f654a18df49a048" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |



---
## get_nft_contract_sale_prices

> `evm_api.nft.get_nft_contract_sale_prices()`

Get the sold price for an NFT contract for the last x days (only trades paid in ETH).


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D", 
    "chain": "eth", 
    "days": 0, 
}

result = evm_api.nft.get_nft_contract_sale_prices(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT collection | Yes |  | "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "base"<br/>- "0x2105"<br/>- "optimism"<br/>- "0xa" | The chain to query |  | "eth" | "eth" |
| days | int | The number of days to look back to find the lowest price<br/>If not provided 7 days will be the default and 365 is the maximum<br/> |  |  | 0 |



---
## get_nft_contract_transfers

> `evm_api.nft.get_nft_contract_transfers()`

Get transfers of NFTs for a given contract and other parameters.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB", 
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "from_date": "", 
    "to_date": "", 
    "format": "decimal", 
    "limit": 0, 
    "order": "DESC", 
    "cursor": "", 
}

result = evm_api.nft.get_nft_contract_transfers(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from where to get the transfers<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from where to get the transfers.<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The date from where to get the transfers (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | Get transfers up until this date (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| order | enum[str]: <br/>- "ASC"<br/>- "DESC" | The order of the result, in ascending (ASC) or descending (DESC) |  | "DESC" | "DESC" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |



---
## get_nft_lowest_price

> `evm_api.nft.get_nft_lowest_price()`

Get the lowest executed price for an NFT contract for the last x days (only trades paid in ETH).


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D", 
    "chain": "eth", 
    "days": 0, 
    "marketplace": "opensea", 
    "nft_metadata": True, 
}

result = evm_api.nft.get_nft_lowest_price(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "base"<br/>- "0x2105"<br/>- "optimism"<br/>- "0xa" | The chain to query |  | "eth" | "eth" |
| days | int | The number of days to look back to find the lowest price<br/>If not provided 7 days will be the default and 365 is the maximum<br/> |  |  | 0 |
| marketplace | enum[str]: <br/>- "opensea"<br/>- "blur"<br/>- "looksrare"<br/>- "x2y2"<br/>- "0xprotocol" | Marketplace from which to get the trades. See [supported Marketplaces](https://docs.moralis.io/web3-data-api/evm/nft-marketplaces). |  | "opensea" | "opensea" |
| nft_metadata | bool | Include the NFT Metadata of the NFT Token |  | False | True |



---
## get_nft_metadata

> `evm_api.nft.get_nft_metadata()`

Get NFT data, including metadata (where available), for the given NFT token ID and contract address.
* Requests for contract addresses not yet indexed will automatically start the indexing process for that NFT collection



### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x524cab2ec69124574082676e6f654a18df49a048", 
    "token_id": "1", 
    "chain": "eth", 
    "format": "decimal", 
    "normalizeMetadata": True, 
    "media_items": True, 
}

result = evm_api.nft.get_nft_metadata(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0x524cab2ec69124574082676e6f654a18df49a048" |
| token_id | str | The ID of the token | Yes |  | "1" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| normalizeMetadata | bool | Should normalized metadata be returned? |  | False | True |
| media_items | bool | Should preview media data be returned? |  | False | True |



---
## get_nft_owners

> `evm_api.nft.get_nft_owners()`

Get owners of NFTs for a given contract.
* Requests for contract addresses not yet indexed will automatically start the indexing process for that NFT collection.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB", 
    "chain": "eth", 
    "format": "decimal", 
    "limit": 0, 
    "cursor": "", 
    "normalizeMetadata": True, 
    "media_items": True, 
}

result = evm_api.nft.get_nft_owners(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| normalizeMetadata | bool | Should normalized metadata be returned? |  | False | True |
| media_items | bool | Should preview media data be returned? |  | False | True |



---
## get_nft_sale_prices

> `evm_api.nft.get_nft_sale_prices()`

Get the sold price for an NFT token for the last x days (only trades paid in ETH).


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D", 
    "token_id": "", 
    "chain": "eth", 
    "days": 0, 
}

result = evm_api.nft.get_nft_sale_prices(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT collection | Yes |  | "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D" |
| token_id | str | The token id of the NFT collection | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "base"<br/>- "0x2105"<br/>- "optimism"<br/>- "0xa" | The chain to query |  | "eth" | "eth" |
| days | int | The number of days to look back to find the lowest price<br/>If not provided 7 days will be the default and 365 is the maximum<br/> |  |  | 0 |



---
## get_nft_token_id_owners

> `evm_api.nft.get_nft_token_id_owners()`

Get owners of a specific NFT given the contract address and token ID. 
* Requests for contract addresses not yet indexed will automatically start the indexing process for that NFT collection



### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x524cab2ec69124574082676e6f654a18df49a048", 
    "token_id": "1", 
    "chain": "eth", 
    "format": "decimal", 
    "limit": 0, 
    "cursor": "", 
    "normalizeMetadata": True, 
    "media_items": True, 
}

result = evm_api.nft.get_nft_token_id_owners(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0x524cab2ec69124574082676e6f654a18df49a048" |
| token_id | str | The ID of the token | Yes |  | "1" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| normalizeMetadata | bool | Should normalized metadata be returned? |  | False | True |
| media_items | bool | Should preview media data be returned? |  | False | True |



---
## get_nft_token_stats

> `evm_api.nft.get_nft_token_stats()`

Get the stats for a nft token


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "token_id": "", 
    "chain": "eth", 
}

result = evm_api.nft.get_nft_token_stats(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT collection | Yes |  | "" |
| token_id | str | The token id of the NFT collection | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |



---
## get_nft_trades

> `evm_api.nft.get_nft_trades()`

Get trades of NFTs for a given contract with the ability to filter by marketplace.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x524cab2ec69124574082676e6f654a18df49a048", 
    "chain": "eth", 
    "from_block": 0, 
    "to_block": "", 
    "from_date": "", 
    "to_date": "", 
    "marketplace": "opensea", 
    "cursor": "", 
    "limit": 0, 
    "nft_metadata": True, 
}

result = evm_api.nft.get_nft_trades(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0x524cab2ec69124574082676e6f654a18df49a048" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "base"<br/>- "0x2105"<br/>- "optimism"<br/>- "0xa" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the transfers<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | str | The block number to get the trades from |  |  | "" |
| from_date | str | The start date from which to get the transfers (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | The end date from which to get the transfers (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| marketplace | enum[str]: <br/>- "opensea"<br/>- "blur"<br/>- "looksrare"<br/>- "x2y2"<br/>- "0xprotocol" | Marketplace from which to get the trades. See [supported Marketplaces](https://docs.moralis.io/web3-data-api/evm/nft-marketplaces). |  | "opensea" | "opensea" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| nft_metadata | bool | Include the NFT Metadata of the NFT Token |  | False | True |



---
## get_nft_trades_by_token

> `evm_api.nft.get_nft_trades_by_token()`

Get trades of NFTs for a given contract and token ID.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x524cab2ec69124574082676e6f654a18df49a048", 
    "token_id": "123", 
    "chain": "eth", 
    "from_block": 0, 
    "to_block": "", 
    "from_date": "", 
    "to_date": "", 
    "cursor": "", 
    "limit": 0, 
    "nft_metadata": True, 
}

result = evm_api.nft.get_nft_trades_by_token(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0x524cab2ec69124574082676e6f654a18df49a048" |
| token_id | str | The token ID of the NFT contract | Yes |  | "123" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "base"<br/>- "0x2105"<br/>- "optimism"<br/>- "0xa" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the transfers<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | str | The block number to get the trades from |  |  | "" |
| from_date | str | The start date from which to get the transfers (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | The end date from which to get the transfers (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| nft_metadata | bool | Include the NFT Metadata of the NFT Token |  | False | True |



---
## get_nft_trades_by_wallet

> `evm_api.nft.get_nft_trades_by_wallet()`

Get trades of NFTs for a given wallet.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xcB1C1FdE09f811B294172696404e88E658659905", 
    "chain": "eth", 
    "from_block": 0, 
    "to_block": "", 
    "from_date": "", 
    "to_date": "", 
    "cursor": "", 
    "limit": 0, 
    "nft_metadata": True, 
}

result = evm_api.nft.get_nft_trades_by_wallet(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The owner wallet address | Yes |  | "0xcB1C1FdE09f811B294172696404e88E658659905" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "base"<br/>- "0x2105"<br/>- "optimism"<br/>- "0xa" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the transfers<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | str | The block number to get the trades from |  |  | "" |
| from_date | str | The start date from which to get the transfers (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | The end date from which to get the transfers (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| nft_metadata | bool | Include the NFT Metadata of the NFT Token |  | False | True |



---
## get_nft_transfers

> `evm_api.nft.get_nft_transfers()`

Get transfers of an NFT given a contract address and token ID.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x524cab2ec69124574082676e6f654a18df49a048", 
    "token_id": "1", 
    "chain": "eth", 
    "format": "decimal", 
    "limit": 0, 
    "order": "DESC", 
    "cursor": "", 
}

result = evm_api.nft.get_nft_transfers(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0x524cab2ec69124574082676e6f654a18df49a048" |
| token_id | str | The ID of the token | Yes |  | "1" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| order | enum[str]: <br/>- "ASC"<br/>- "DESC" | The order of the result, in ascending (ASC) or descending (DESC) |  | "DESC" | "DESC" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |



---
## get_nft_transfers_by_block

> `evm_api.nft.get_nft_transfers_by_block()`

Get transfers of NFTs given a block number or block hash.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "block_number_or_hash": "15846571", 
    "chain": "eth", 
    "limit": 0, 
    "order": "DESC", 
    "cursor": "", 
}

result = evm_api.nft.get_nft_transfers_by_block(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| block_number_or_hash | str | The block number or block hash | Yes |  | "15846571" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| limit | int | The desired page size of the result. |  | 100 | 0 |
| order | enum[str]: <br/>- "ASC"<br/>- "DESC" | The order of the result, in ascending (ASC) or descending (DESC) |  | "DESC" | "DESC" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |



---
## get_nft_transfers_from_to_block

> `evm_api.nft.get_nft_transfers_from_to_block()`

Get transfers of NFTs from a block number to a block number.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "from_date": "", 
    "to_date": "", 
    "format": "decimal", 
    "limit": 0, 
    "order": "DESC", 
    "cursor": "", 
}

result = evm_api.nft.get_nft_transfers_from_to_block(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the transfers<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from which to get the transfers.<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The start date from which to get the transfers (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | The end date from which to get the transfers (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| order | enum[str]: <br/>- "ASC"<br/>- "DESC" | The order of the result, in ascending (ASC) or descending (DESC) |  | "DESC" | "DESC" |
| cursor | str | The cursor returned in the previous response (for getting the next page)<br/> |  |  | "" |



---
## get_wallet_nft_collections

> `evm_api.nft.get_wallet_nft_collections()`

Get NFT collections owned by a given wallet address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xcB1C1FdE09f811B294172696404e88E658659905", 
    "chain": "eth", 
    "limit": 0, 
    "exclude_spam": True, 
    "cursor": "", 
    "token_counts": True, 
}

result = evm_api.nft.get_wallet_nft_collections(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The wallet address of the owner of NFTs in the collections | Yes |  | "0xcB1C1FdE09f811B294172696404e88E658659905" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| limit | int | The desired page size of the result. |  |  | 0 |
| exclude_spam | bool | Should spam NFTs be excluded from the result? |  | False | True |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| token_counts | bool | Should token counts per collection be included in the response? |  | False | True |



---
## get_wallet_nft_transfers

> `evm_api.nft.get_wallet_nft_transfers()`

Get transfers of NFTs given the wallet and other parameters.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xcB1C1FdE09f811B294172696404e88E658659905", 
    "chain": "eth", 
    "contract_addresses": [], 
    "format": "decimal", 
    "from_block": 0, 
    "to_block": "", 
    "from_date": "", 
    "to_date": "", 
    "limit": 0, 
    "order": "DESC", 
    "cursor": "", 
}

result = evm_api.nft.get_wallet_nft_transfers(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The wallet address of the sender or recipient of the transfers | Yes |  | "0xcB1C1FdE09f811B294172696404e88E658659905" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| contract_addresses | List of str | List of contract addresses of transfers |  |  | [] |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| from_block | int | The minimum block number from which to get the transfers<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | str | To get the reserves at this block number |  |  | "" |
| from_date | str | The date from where to get the transfers (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | Get transfers up until this date (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| order | enum[str]: <br/>- "ASC"<br/>- "DESC" | The order of the result, in ascending (ASC) or descending (DESC) |  | "DESC" | "DESC" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |



---
## get_wallet_nfts

> `evm_api.nft.get_wallet_nfts()`

Get NFTs owned by a given address.
* The response will include status [SYNCED/SYNCING] based on the contracts being indexed.
* Use the token_address param to get results for a specific contract only
* Note that results will include all indexed NFTs
* Any request that includes the token_address param will start the indexing process for that NFT collection the very first time it is requested.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xcB1C1FdE09f811B294172696404e88E658659905", 
    "chain": "eth", 
    "format": "decimal", 
    "limit": 0, 
    "exclude_spam": True, 
    "token_addresses": [], 
    "cursor": "", 
    "normalizeMetadata": True, 
    "media_items": True, 
}

result = evm_api.nft.get_wallet_nfts(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the wallet | Yes |  | "0xcB1C1FdE09f811B294172696404e88E658659905" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| format | enum[str]: <br/>- "decimal"<br/>- "hex" | The format of the token ID |  | "decimal" | "decimal" |
| limit | int | The desired page size of the result. |  |  | 0 |
| exclude_spam | bool | Should spam NFTs be excluded from the result? |  | False | True |
| token_addresses | List of str | The addresses to get balances for (optional) |  |  | [] |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| normalizeMetadata | bool | Should normalized metadata be returned? |  | False | True |
| media_items | bool | Should preview media data be returned? |  | False | True |



---
## re_sync_metadata

> `evm_api.nft.re_sync_metadata()`

Resync the metadata for an NFT
* The metadata flag will request the NFT's metadata from an already existing token_uri
* The uri (default) flag will fetch the latest token_uri from the given NFT contract address. In sync mode the metadata will also be fetched
* The sync mode will make the endpoint synchronous so it will wait for the task to be completed before responding
* The async mode (default) will make the endpoint asynchronous so we will wait for the task to be completed before responding



### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB", 
    "token_id": "1", 
    "chain": "eth", 
    "flag": "uri", 
    "mode": "sync", 
}

result = evm_api.nft.re_sync_metadata(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB" |
| token_id | str | The ID of the token | Yes |  | "1" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| flag | enum[str]: <br/>- "uri"<br/>- "metadata" | The type of resync to operate |  | "uri" | "uri" |
| mode | enum[str]: <br/>- "async"<br/>- "sync" | To define the behaviour of the endpoint |  | "async" | "sync" |



---
## sync_nft_contract

> `evm_api.nft.sync_nft_contract()`

Initiates a sync of a previously non synced contract.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB", 
    "chain": "eth", 
}

result = evm_api.nft.sync_nft_contract(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the NFT contract | Yes |  | "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |





