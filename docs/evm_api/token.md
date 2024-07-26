# token API:

> `evm_api.token`

- [get_multiple_token_prices](#get_multiple_token_prices)
- [get_token_allowance](#get_token_allowance)
- [get_token_metadata](#get_token_metadata)
- [get_token_metadata_by_symbol](#get_token_metadata_by_symbol)
- [get_token_owners](#get_token_owners)
- [get_token_price](#get_token_price)
- [get_token_stats](#get_token_stats)
- [get_token_transfers](#get_token_transfers)
- [get_top_profitable_wallet_per_token](#get_top_profitable_wallet_per_token)
- [get_wallet_token_balances](#get_wallet_token_balances)
- [get_wallet_token_transfers](#get_wallet_token_transfers)


---
## get_multiple_token_prices

> `evm_api.token.get_multiple_token_prices()`

Returns an array of token prices denominated in the blockchain's native token and USD for a given token contract address


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "chain": "eth", 
    "include": "", 
    "max_token_inactivity": 1.2, 
}
body = {
    "tokens": [{'token_address': '0xdac17f958d2ee523a2206206994597c13d831ec7'}, {'token_address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'}, {'token_address': '0xae7ab96520de3a18e5e111b5eaab095312d7fe84', 'exchange': 'uniswapv2', 'to_block': '16314545'}, {'token_address': '0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0'}], 
}

result = evm_api.token.get_multiple_token_prices(
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
| include | enum[str]: <br/>- "percent_change" | If the result should contain the 24hr percent change |  | "" | "" |
| max_token_inactivity | float | Exclude tokens inactive for more than the given amount of days |  |  | 1.2 |


### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| tokens | List of object: <br/> - token_address: str<br/> - exchange: str<br/> - to_block: str | The tokens to be fetched | Yes |  | [{'token_address': '0xdac17f958d2ee523a2206206994597c13d831ec7'}, {'token_address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'}, {'token_address': '0xae7ab96520de3a18e5e111b5eaab095312d7fe84', 'exchange': 'uniswapv2', 'to_block': '16314545'}, {'token_address': '0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0'}] |


---
## get_token_allowance

> `evm_api.token.get_token_allowance()`

Get the amount which the spender is allowed to withdraw on behalf of the owner.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "owner_address": "", 
    "spender_address": "", 
    "chain": "eth", 
}

result = evm_api.token.get_token_allowance(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the token contract | Yes |  | "" |
| owner_address | str | The address of the token owner | Yes |  | "" |
| spender_address | str | The address of the token spender | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |



---
## get_token_metadata

> `evm_api.token.get_token_metadata()`

Get the metadata for a given token contract address (name, symbol, decimals, logo).


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "addresses": [], 
    "chain": "eth", 
}

result = evm_api.token.get_token_metadata(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| addresses | List of str | The addresses to get metadata for | Yes |  | [] |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |



---
## get_token_metadata_by_symbol

> `evm_api.token.get_token_metadata_by_symbol()`

Get the metadata for a list of token symbols (name, symbol, decimals, logo).


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "symbols": [], 
    "chain": "eth", 
}

result = evm_api.token.get_token_metadata_by_symbol(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| symbols | List of str | The symbols to get metadata for | Yes |  | [] |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |



---
## get_token_owners

> `evm_api.token.get_token_owners()`

Identify the major holders of an ERC20 token and understand their ownership percentages


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "token_address": "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0", 
    "chain": "eth", 
    "limit": 0, 
    "cursor": "", 
    "order": "DESC", 
}

result = evm_api.token.get_token_owners(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| token_address | str | The address of the token contract | Yes |  | "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| limit | int | The desired page size of the result. |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| order | enum[str]: <br/>- "ASC"<br/>- "DESC" | The order of the result, in ascending (ASC) or descending (DESC) |  | "DESC" | "DESC" |



---
## get_token_price

> `evm_api.token.get_token_price()`

Get the token price denominated in the blockchain's native token and USD.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0", 
    "chain": "eth", 
    "exchange": "", 
    "to_block": 0, 
    "include": "", 
    "max_token_inactivity": 1.2, 
}

result = evm_api.token.get_token_price(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the token contract | Yes |  | "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| exchange | str | The factory name or address of the token exchange |  |  | "" |
| to_block | int | The block number from which the token price should be checked |  |  | 0 |
| include | enum[str]: <br/>- "percent_change" | If the result should contain the 24hr percent change |  | "" | "" |
| max_token_inactivity | float | Exclude tokens inactive for more than the given amount of days |  |  | 1.2 |



---
## get_token_stats

> `evm_api.token.get_token_stats()`

Get the stats for a erc20 token


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
}

result = evm_api.token.get_token_stats(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the erc20 token | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |



---
## get_token_transfers

> `evm_api.token.get_token_transfers()`

Get ERC20 token transactions from a contract ordered by block number in descending order.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0", 
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "from_date": "", 
    "to_date": "", 
    "limit": 0, 
    "order": "DESC", 
    "cursor": "", 
}

result = evm_api.token.get_token_transfers(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the token contract | Yes |  | "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the transfers<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from which to get the transfers.<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The start date from which to get the transfers (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | Get transfers up until this date (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| order | enum[str]: <br/>- "ASC"<br/>- "DESC" | The order of the result, in ascending (ASC) or descending (DESC) |  | "DESC" | "DESC" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |



---
## get_top_profitable_wallet_per_token

> `evm_api.token.get_top_profitable_wallet_per_token()`

Retrieves a list of the top profitable wallets for a specific ERC20 token.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "days": "", 
    "chain": "eth", 
}

result = evm_api.token.get_top_profitable_wallet_per_token(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The ERC20 token address. | Yes |  | "" |
| days | str | Timeframe in days for which profitability is calculated, Options include 'all', '7', '30', '60', '90' default is 'all'. |  |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "mainnet"<br/>- "0x1"<br/>- "matic"<br/>- "0x89"<br/>- "polygon"<br/>- "bsc"<br/>- "binance"<br/>- "0x38"<br/>- "fantom"<br/>- "ftm"<br/>- "0xfa"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "optimism"<br/>- "0xa"<br/>- "pulsechain"<br/>- "0x171"<br/>- "base"<br/>- "0x2105"<br/>- "linea"<br/>- "0xe708" | The chain to query |  |  | "eth" |



---
## get_wallet_token_balances

> `evm_api.token.get_wallet_token_balances()`

Get token balances for a specific wallet address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xcB1C1FdE09f811B294172696404e88E658659905", 
    "chain": "eth", 
    "to_block": 1.2, 
    "token_addresses": [], 
    "exclude_spam": True, 
}

result = evm_api.token.get_wallet_token_balances(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address from which token balances will be checked | Yes |  | "0xcB1C1FdE09f811B294172696404e88E658659905" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| to_block | float | The block number up to which the balances will be checked. |  |  | 1.2 |
| token_addresses | List of str | The addresses to get balances for (optional) |  |  | [] |
| exclude_spam | bool | Exclude spam tokens from the result |  | True | True |



---
## get_wallet_token_transfers

> `evm_api.token.get_wallet_token_transfers()`

Get ERC20 token transactions ordered by block number in descending order.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xcB1C1FdE09f811B294172696404e88E658659905", 
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "from_date": "", 
    "to_date": "", 
    "contract_addresses": [], 
    "limit": 0, 
    "order": "DESC", 
    "cursor": "", 
}

result = evm_api.token.get_wallet_token_transfers(
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
| from_block | int | The minimum block number from which to get the transactions<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from which to get the transactions.<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The start date from which to get the transactions (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | Get the transactions up to this date (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| contract_addresses | List of str | List of contract addresses of transfers |  |  | [] |
| limit | int | The desired page size of the result. |  |  | 0 |
| order | enum[str]: <br/>- "ASC"<br/>- "DESC" | The order of the result, in ascending (ASC) or descending (DESC) |  | "DESC" | "DESC" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |





