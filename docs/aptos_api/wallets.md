# wallets API:

> `aptos_api.wallets`

- [get_coin_balances_by_wallets](#get_coin_balances_by_wallets)
- [get_coin_transfers_by_wallet_addresses](#get_coin_transfers_by_wallet_addresses)
- [get_historical_coin_balances_by_wallets](#get_historical_coin_balances_by_wallets)
- [get_nft_by_owners](#get_nft_by_owners)
- [get_wallets_nft_transfers](#get_wallets_nft_transfers)


---
## get_coin_balances_by_wallets

> `aptos_api.wallets.get_coin_balances_by_wallets()`

Get Coin Balances by wallet addresses

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "owner_addresses": [], 
    "offset": 1.2, 
    "cursor": "", 
    "coin_type_hash_blacklist": [], 
    "coin_type_hash_whitelist": [], 
}

result = aptos_api.wallets.get_coin_balances_by_wallets(
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
| owner_addresses | List of str | The addresses of the owners to get coin balances for | Yes |  | [] |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |
| coin_type_hash_blacklist | List of str | The coin type hashes of the coins to whitelist |  |  | [] |
| coin_type_hash_whitelist | List of str | The coin type hashes of the coins to whitelist |  |  | [] |



---
## get_coin_transfers_by_wallet_addresses

> `aptos_api.wallets.get_coin_transfers_by_wallet_addresses()`

Get Coin Transfers by wallet addresses

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "owner_addresses": [], 
    "offset": 1.2, 
    "cursor": "", 
    "from_date": "", 
    "to_date": "", 
    "coin_type_blacklist": [], 
    "coin_type_whitelist": [], 
}

result = aptos_api.wallets.get_coin_transfers_by_wallet_addresses(
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
| owner_addresses | List of str | The addresses of the owners to get tokens for | Yes | [] | [] |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |
| from_date | str | The date from which to fetch coin transfers |  |  | "" |
| to_date | str | The date to which to fetch coin transfers |  |  | "" |
| coin_type_blacklist | List of str | The coin types of the coins to whitelist |  | [] | [] |
| coin_type_whitelist | List of str | The coin types of the coins to whitelist |  |  | [] |



---
## get_historical_coin_balances_by_wallets

> `aptos_api.wallets.get_historical_coin_balances_by_wallets()`

Get Historical Coin Balances by wallet addresses

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "owner_addresses": [], 
    "offset": 1.2, 
    "cursor": "", 
    "coin_type_hash_blacklist": [], 
    "coin_type_hash_whitelist": [], 
}

result = aptos_api.wallets.get_historical_coin_balances_by_wallets(
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
| owner_addresses | List of str | The addresses of the owner addresses to get historical balances for | Yes |  | [] |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |
| coin_type_hash_blacklist | List of str | The coin type hash of the coins to whitelist |  |  | [] |
| coin_type_hash_whitelist | List of str | The coin type hash of the coins to whitelist |  |  | [] |



---
## get_nft_by_owners

> `aptos_api.wallets.get_nft_by_owners()`

Get NFTs by wallet addresses

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "owner_addresses": [], 
    "offset": 1.2, 
    "cursor": "", 
    "collection_blacklist": [], 
    "collection_whitelist": [], 
}

result = aptos_api.wallets.get_nft_by_owners(
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
| owner_addresses | List of str | The addresses of the owners to get tokens for | Yes |  | [] |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |
| collection_blacklist | List of str | The collection data id hashes of the collections to whitelist |  |  | [] |
| collection_whitelist | List of str | The collection data id hashes of the collections to whitelist |  |  | [] |



---
## get_wallets_nft_transfers

> `aptos_api.wallets.get_wallets_nft_transfers()`

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

result = aptos_api.wallets.get_wallets_nft_transfers(
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





