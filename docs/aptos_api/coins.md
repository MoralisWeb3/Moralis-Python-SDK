# coins API:

> `aptos_api.coins`

- [get_coin_info_by_coin_type_hashes](#get_coin_info_by_coin_type_hashes)
- [get_coin_transfers_by_block_heights](#get_coin_transfers_by_block_heights)
- [get_coin_transfers_by_coin_type](#get_coin_transfers_by_coin_type)
- [get_coin_transfers_by_owner_addresses](#get_coin_transfers_by_owner_addresses)
- [get_coins_by_creators](#get_coins_by_creators)
- [get_coins_by_name_range](#get_coins_by_name_range)
- [get_coins_by_symbol_range](#get_coins_by_symbol_range)
- [get_latest_coins](#get_latest_coins)
- [get_top_holders_by_coin](#get_top_holders_by_coin)


---
## get_coin_info_by_coin_type_hashes

> `aptos_api.coins.get_coin_info_by_coin_type_hashes()`

Get Coin Metadata by Coin Type Hashes

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "coin_type_hashes": [], 
}

result = aptos_api.coins.get_coin_info_by_coin_type_hashes(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| coin_type_hashes | List of str | The coin type hashes to fetch info about | Yes |  | [] |



---
## get_coin_transfers_by_block_heights

> `aptos_api.coins.get_coin_transfers_by_block_heights()`

Get Coin Transfers by block heights

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "block_heights": [], 
    "offset": 1.2, 
    "cursor": "", 
}

result = aptos_api.coins.get_coin_transfers_by_block_heights(
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
| block_heights | List of str | The coin types to fetch info about | Yes | [] | [] |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  | "" | "" |



---
## get_coin_transfers_by_coin_type

> `aptos_api.coins.get_coin_transfers_by_coin_type()`

Get Coin Transfers by Coin Type

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "coin_type": "", 
    "limit": 1.2, 
    "offset": 1.2, 
    "cursor": "", 
    "from_date": "", 
    "to_date": "", 
}

result = aptos_api.coins.get_coin_transfers_by_coin_type(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| coin_type | str | The coin type to fetch info about | Yes | "" | "" |
| limit | float | The number of results to return | Yes | 10 | 1.2 |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  | "" | "" |
| from_date | str | The date from which to fetch coin transfers |  | "" | "" |
| to_date | str | The date to which to fetch coin transfers |  | "" | "" |



---
## get_coin_transfers_by_owner_addresses

> `aptos_api.coins.get_coin_transfers_by_owner_addresses()`

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

result = aptos_api.coins.get_coin_transfers_by_owner_addresses(
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
## get_coins_by_creators

> `aptos_api.coins.get_coins_by_creators()`

Get Coin Metadata by creator addresses

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

result = aptos_api.coins.get_coins_by_creators(
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
| creator_addresses | List of str | The addresses of the creators | Yes | [] | [] |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  | "" | "" |



---
## get_coins_by_name_range

> `aptos_api.coins.get_coins_by_name_range()`

Get Coin Metadata by name range

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "offset": 1.2, 
    "cursor": "", 
    "from_name": "", 
    "to_name": "", 
}

result = aptos_api.coins.get_coins_by_name_range(
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
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |
| from_name | str | The name of the coin to start from (inclusive and case sensitive) |  |  | "" |
| to_name | str | The name of the coin to end at (inclusive and case sensitive) |  |  | "" |



---
## get_coins_by_symbol_range

> `aptos_api.coins.get_coins_by_symbol_range()`

Get Coin Metadata by symbol range

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "offset": 1.2, 
    "cursor": "", 
    "from_symbol": "", 
    "to_symbol": "", 
}

result = aptos_api.coins.get_coins_by_symbol_range(
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
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |
| from_symbol | str | The name of the coin to start from (inclusive and case sensitive) |  |  | "" |
| to_symbol | str | The name of the coin to end at (inclusive and case sensitive) |  |  | "" |



---
## get_latest_coins

> `aptos_api.coins.get_latest_coins()`

Get latest deployed coins

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "offset": 1.2, 
    "cursor": "", 
}

result = aptos_api.coins.get_latest_coins(
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
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  |  | "" |



---
## get_top_holders_by_coin

> `aptos_api.coins.get_top_holders_by_coin()`

Get top Holders of Coin

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "coin_type_hash": "", 
    "limit": 1.2, 
    "offset": 1.2, 
    "cursor": "", 
    "min_amount": 1.2, 
    "min_version": 1.2, 
    "wallet_blacklist": [], 
    "wallet_whitelist": [], 
}

result = aptos_api.coins.get_top_holders_by_coin(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| coin_type_hash | str | The coin type hash to fetch info about | Yes | "" | "" |
| limit | float | The number of results to return | Yes | 10 | 1.2 |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  | "" | "" |
| min_amount | float | The minimum amount of coins required for a wallet to be included in the results |  |  | 1.2 |
| min_version | float | The minimum version on when the balance was last updated |  |  | 1.2 |
| wallet_blacklist | List of str | The addresses of the wallets to blacklist |  |  | [] |
| wallet_whitelist | List of str | The addresses of the wallets to whitelist |  |  | [] |





