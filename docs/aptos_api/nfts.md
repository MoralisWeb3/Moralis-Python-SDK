# nfts API:

> `aptos_api.nfts`

- [get_nft_owners_by_collection](#get_nft_owners_by_collection)
- [get_nft_owners_by_tokens](#get_nft_owners_by_tokens)
- [get_nft_owners_of_collection](#get_nft_owners_of_collection)
- [get_nft_transfers_by_collection](#get_nft_transfers_by_collection)
- [get_nft_transfers_by_creators](#get_nft_transfers_by_creators)
- [get_nft_transfers_by_ids](#get_nft_transfers_by_ids)
- [get_nft_transfers_by_wallets](#get_nft_transfers_by_wallets)
- [get_nfts_by_collection](#get_nfts_by_collection)
- [get_nfts_by_creators](#get_nfts_by_creators)
- [get_nfts_by_ids](#get_nfts_by_ids)


---
## get_nft_owners_by_collection

> `aptos_api.nfts.get_nft_owners_by_collection()`

Get NFT Owners by Collection

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "collection_data_id_hash": "", 
    "limit": 1.2, 
    "offset": 1.2, 
    "cursor": "", 
    "wallet_blacklist": [], 
    "wallet_whitelist": [], 
}

result = aptos_api.nfts.get_nft_owners_by_collection(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| collection_data_id_hash | str | The id of the token | Yes |  | "" |
| limit | float | The number of results to return | Yes | 10 | 1.2 |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |
| wallet_blacklist | List of str | The addresses of the wallets to blacklist |  |  | [] |
| wallet_whitelist | List of str | The addresses of the wallets to whitelist |  |  | [] |



---
## get_nft_owners_by_tokens

> `aptos_api.nfts.get_nft_owners_by_tokens()`

Get NFT Owners by tokens

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "token_ids": [], 
    "offset": 1.2, 
    "cursor": "", 
}

result = aptos_api.nfts.get_nft_owners_by_tokens(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| limit | float | The number of results to return | Yes | 10 | 1.2 |
| token_ids | List of str | The identifiers of the tokens to get owners for | Yes |  | [] |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |



---
## get_nft_owners_of_collection

> `aptos_api.nfts.get_nft_owners_of_collection()`

Get NFT Owners of Collection

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "collection_data_id_hash": "", 
    "limit": 1.2, 
    "offset": 1.2, 
    "cursor": "", 
}

result = aptos_api.nfts.get_nft_owners_of_collection(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| collection_data_id_hash | str | The id of the token | Yes |  | "" |
| limit | float | The number of results to return | Yes | 10 | 1.2 |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |



---
## get_nft_transfers_by_collection

> `aptos_api.nfts.get_nft_transfers_by_collection()`

Get NFT Transfers by Collection

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "collection_data_id_hash": "", 
    "limit": 1.2, 
    "offset": 1.2, 
    "cursor": "", 
    "wallet_whitelist": [], 
    "wallet_blacklist": [], 
}

result = aptos_api.nfts.get_nft_transfers_by_collection(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| collection_data_id_hash | str | The collection data id hash of the token | Yes |  | "" |
| limit | float | The number of results to return | Yes | 10 | 1.2 |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |
| wallet_whitelist | List of str | The addresses of the wallets to whitelist |  |  | [] |
| wallet_blacklist | List of str | The addresses of the wallets to blacklist |  |  | [] |



---
## get_nft_transfers_by_creators

> `aptos_api.nfts.get_nft_transfers_by_creators()`

Get NFT Transfers by creators

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "creator_addresses": [], 
    "offset": 1.2, 
    "cursor": "", 
    "collection_blacklist": [], 
    "collection_whitelist": [], 
}

result = aptos_api.nfts.get_nft_transfers_by_creators(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| limit | float | The number of results to return | Yes | 10 | 1.2 |
| creator_addresses | List of str | The addresses of the creators | Yes |  | [] |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |
| collection_blacklist | List of str | The ids of the collections to whitelist |  |  | [] |
| collection_whitelist | List of str | The ids of the collections to whitelist |  |  | [] |



---
## get_nft_transfers_by_ids

> `aptos_api.nfts.get_nft_transfers_by_ids()`

Get NFT Transfers by Token ids

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "token_ids": [], 
    "offset": 1.2, 
    "cursor": "", 
    "wallet_blacklist": [], 
    "wallet_whitelist": [], 
}

result = aptos_api.nfts.get_nft_transfers_by_ids(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| limit | float | The number of tokens to return | Yes | 10 | 1.2 |
| token_ids | List of str | The identifiers of the tokens to get | Yes |  | [] |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |
| wallet_blacklist | List of str | The addresses of the wallets to blacklist |  |  | [] |
| wallet_whitelist | List of str | The addresses of the wallets to whitelist |  |  | [] |



---
## get_nft_transfers_by_wallets

> `aptos_api.nfts.get_nft_transfers_by_wallets()`

Get NFT Transfers by wallets

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "wallet_addresses": [], 
    "offset": 1.2, 
    "cursor": "", 
    "collection_blacklist": [], 
    "collection_whitelist": [], 
}

result = aptos_api.nfts.get_nft_transfers_by_wallets(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| limit | float | The number of tokens to return | Yes | 10 | 1.2 |
| wallet_addresses | List of str | The addresses of the wallets to get transfers for | Yes |  | [] |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |
| collection_blacklist | List of str | The ids of the collections to whitelist |  |  | [] |
| collection_whitelist | List of str | The ids of the collections to whitelist |  |  | [] |



---
## get_nfts_by_collection

> `aptos_api.nfts.get_nfts_by_collection()`

Get NFTs by Collection

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "collection_data_id_hash": "", 
    "limit": 1.2, 
    "offset": 1.2, 
    "cursor": "", 
}

result = aptos_api.nfts.get_nfts_by_collection(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| collection_data_id_hash | str | The collection data id hash of the collection | Yes |  | "" |
| limit | float | The number of results to return | Yes | 10 | 1.2 |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |



---
## get_nfts_by_creators

> `aptos_api.nfts.get_nfts_by_creators()`

Get NFTs by creators

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "creator_addresses": [], 
    "offset": 1.2, 
    "cursor": "", 
}

result = aptos_api.nfts.get_nfts_by_creators(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| limit | float | The number of tokens to return | Yes | 10 | 1.2 |
| creator_addresses | List of str | The addresses of the creators | Yes |  | [] |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |



---
## get_nfts_by_ids

> `aptos_api.nfts.get_nfts_by_ids()`

Get NFTs by ids

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "token_ids": [], 
}

result = aptos_api.nfts.get_nfts_by_ids(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| token_ids | List of str | The identifiers of the tokens to get | Yes |  | [] |





