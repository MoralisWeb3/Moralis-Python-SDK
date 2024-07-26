# wallets API:

> `evm_api.wallets`

- [get_defi_positions_by_protocol](#get_defi_positions_by_protocol)
- [get_defi_positions_summary](#get_defi_positions_summary)
- [get_defi_summary](#get_defi_summary)
- [get_wallet_active_chains](#get_wallet_active_chains)
- [get_wallet_history](#get_wallet_history)
- [get_wallet_net_worth](#get_wallet_net_worth)
- [get_wallet_profitability](#get_wallet_profitability)
- [get_wallet_profitability_summary](#get_wallet_profitability_summary)
- [get_wallet_stats](#get_wallet_stats)
- [get_wallet_token_balances_price](#get_wallet_token_balances_price)


---
## get_defi_positions_by_protocol

> `evm_api.wallets.get_defi_positions_by_protocol()`

Get the detailed defi positions by protocol for a wallet address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "protocol": "uniswap-v3", 
    "chain": "eth", 
}

result = evm_api.wallets.get_defi_positions_by_protocol(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | Wallet address | Yes |  | "" |
| protocol | enum[str]: <br/>- "uniswap-v2"<br/>- "uniswap-v3"<br/>- "pancakeswap-v2"<br/>- "pancakeswap-v3"<br/>- "quickswap-v2"<br/>- "sushiswap-v2"<br/>- "aave-v2"<br/>- "aave-v3"<br/>- "fraxswap-v1"<br/>- "fraxswap-v2"<br/>- "lido"<br/>- "makerdao"<br/>- "eigenlayer"<br/>- "pendle"<br/>- "etherfi"<br/>- "rocketpool"<br/>- "sparkfi" | The protocol to query | Yes | "uniswap-v3" | "uniswap-v3" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |



---
## get_defi_positions_summary

> `evm_api.wallets.get_defi_positions_summary()`

Get the positions summary of a wallet address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
}

result = evm_api.wallets.get_defi_positions_summary(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | Wallet address | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |



---
## get_defi_summary

> `evm_api.wallets.get_defi_summary()`

Get the defi summary of a wallet address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
}

result = evm_api.wallets.get_defi_summary(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | Wallet address | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |



---
## get_wallet_active_chains

> `evm_api.wallets.get_wallet_active_chains()`

Get the active chains for a wallet address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chains": [], 
}

result = evm_api.wallets.get_wallet_active_chains(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | Wallet address | Yes |  | "" |
| chains | List of enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chains to query |  |  | [] |



---
## get_wallet_history

> `evm_api.wallets.get_wallet_history()`

Get the complete history of a wallet


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
    "include_internal_transactions": True, 
    "include_input_data": True, 
    "nft_metadata": True, 
    "cursor": "", 
    "order": "DESC", 
    "limit": 0, 
}

result = evm_api.wallets.get_wallet_history(
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
| include_internal_transactions | bool | If the result should contain the internal transactions. |  |  | True |
| include_input_data | bool | Set the input data from the result |  | False | True |
| nft_metadata | bool | If the result should contain the nft metadata. |  |  | True |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| order | enum[str]: <br/>- "ASC"<br/>- "DESC" | The order of the result, in ascending (ASC) or descending (DESC) |  | "DESC" | "DESC" |
| limit | int | The desired page size of the result. |  |  | 0 |



---
## get_wallet_net_worth

> `evm_api.wallets.get_wallet_net_worth()`

Get the net worth of a wallet in USD. We recommend to filter out spam tokens and unverified contracts to get a more accurate result.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xcB1C1FdE09f811B294172696404e88E658659905", 
    "chains": [], 
    "exclude_spam": True, 
    "exclude_unverified_contracts": True, 
    "max_token_inactivity": 1.2, 
}

result = evm_api.wallets.get_wallet_net_worth(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The wallet address | Yes |  | "0xcB1C1FdE09f811B294172696404e88E658659905" |
| chains | List of enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chains to query |  |  | [] |
| exclude_spam | bool | Exclude spam tokens from the result |  | False | True |
| exclude_unverified_contracts | bool | Exclude unverified contracts from the result |  | False | True |
| max_token_inactivity | float | Exclude tokens inactive for more than the given amount of days |  |  | 1.2 |



---
## get_wallet_profitability

> `evm_api.wallets.get_wallet_profitability()`

Retrieves profitability information for a specific wallet address. Can be filtered by one or more tokens.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "days": "", 
    "chain": "eth", 
    "token_addresses": [], 
}

result = evm_api.wallets.get_wallet_profitability(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The wallet address for which profitability is to be retrieved. | Yes |  | "" |
| days | str | Timeframe in days for which profitability is calculated, Options include 'all', '7', '30', '60', '90' default is 'all'. |  |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "mainnet"<br/>- "0x1"<br/>- "matic"<br/>- "0x89"<br/>- "polygon"<br/>- "bsc"<br/>- "binance"<br/>- "0x38"<br/>- "fantom"<br/>- "ftm"<br/>- "0xfa"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "optimism"<br/>- "0xa"<br/>- "pulsechain"<br/>- "0x171"<br/>- "base"<br/>- "0x2105"<br/>- "linea"<br/>- "0xe708" | The chain to query |  |  | "eth" |
| token_addresses | List of str | The token addresses list to filter the result with |  |  | [] |



---
## get_wallet_profitability_summary

> `evm_api.wallets.get_wallet_profitability_summary()`

Retrieves a summary of wallet profitability based on specified parameters including optional token addresses.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "days": "", 
    "chain": "eth", 
}

result = evm_api.wallets.get_wallet_profitability_summary(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The wallet address for which profitability summary is to be retrieved. | Yes |  | "" |
| days | str | Timeframe in days for the profitability summary. Options include 'all', '7', '30', '60', '90' default is 'all'. |  |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "mainnet"<br/>- "0x1"<br/>- "matic"<br/>- "0x89"<br/>- "polygon"<br/>- "bsc"<br/>- "binance"<br/>- "0x38"<br/>- "fantom"<br/>- "ftm"<br/>- "0xfa"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "optimism"<br/>- "0xa"<br/>- "pulsechain"<br/>- "0x171"<br/>- "base"<br/>- "0x2105"<br/>- "linea"<br/>- "0xe708" | The chain to query |  |  | "eth" |



---
## get_wallet_stats

> `evm_api.wallets.get_wallet_stats()`

Get the stats for a wallet address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
}

result = evm_api.wallets.get_wallet_stats(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | Wallet address | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |



---
## get_wallet_token_balances_price

> `evm_api.wallets.get_wallet_token_balances_price()`

Get token balances for a specific wallet address and their token prices in USD.


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
    "exclude_unverified_contracts": True, 
    "cursor": "", 
    "limit": 0, 
    "exclude_native": True, 
    "max_token_inactivity": 1.2, 
}

result = evm_api.wallets.get_wallet_token_balances_price(
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
| exclude_spam | bool | Exclude spam tokens from the result |  | False | True |
| exclude_unverified_contracts | bool | Exclude unverified contracts from the result |  | False | True |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| exclude_native | bool | Exclude native balance from the result |  | False | True |
| max_token_inactivity | float | Exclude tokens inactive for more than the given amount of days |  |  | 1.2 |





