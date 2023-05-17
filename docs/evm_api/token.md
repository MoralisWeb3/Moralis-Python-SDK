# token API:

> `evm_api.token`

- [get_erc20_approvals](#get_erc20_approvals)
- [get_erc20_burns](#get_erc20_burns)
- [get_erc20_mints](#get_erc20_mints)
- [get_erc20_transfers](#get_erc20_transfers)
- [get_token_allowance](#get_token_allowance)
- [get_token_metadata](#get_token_metadata)
- [get_token_metadata_by_symbol](#get_token_metadata_by_symbol)
- [get_token_price](#get_token_price)
- [get_token_transfers](#get_token_transfers)
- [get_wallet_token_balances](#get_wallet_token_balances)
- [get_wallet_token_transfers](#get_wallet_token_transfers)


---
## get_erc20_approvals

> `evm_api.token.get_erc20_approvals()`




### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "limit": 0, 
    "contract_addresses": [], 
    "exclude_contracts": [], 
    "wallet_addresses": [], 
    "exclude_wallets": [], 
    "cursor": "", 
}

result = evm_api.token.get_erc20_approvals(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| from_block | int | The block number from which the approvals will be returned |  |  | 0 |
| to_block | int | The block number to which the approvals will be returned |  |  | 0 |
| limit | int | The desired page size of the result. |  |  | 0 |
| contract_addresses | List of str | Contract addresses to only include |  |  | [] |
| exclude_contracts | List of str | Contract addresses to ignore |  |  | [] |
| wallet_addresses | List of str | Wallet addresses to only include |  |  | [] |
| exclude_wallets | List of str | Wallet addresses to ignore |  |  | [] |
| cursor | str | The cursor returned in the previous response (used to getting the next page). |  |  | "" |



---
## get_erc20_burns

> `evm_api.token.get_erc20_burns()`




### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "limit": 0, 
    "contract_addresses": [], 
    "exclude_contracts": [], 
    "wallet_addresses": [], 
    "exclude_wallets": [], 
    "cursor": "", 
}

result = evm_api.token.get_erc20_burns(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| from_block | int | The block number from which the burns will be returned |  |  | 0 |
| to_block | int | The block number to which the burns will be returned |  |  | 0 |
| limit | int | The desired page size of the result. |  |  | 0 |
| contract_addresses | List of str | Contract addresses to only include |  |  | [] |
| exclude_contracts | List of str | Contract addresses to ignore |  |  | [] |
| wallet_addresses | List of str | Wallet addresses to only include |  |  | [] |
| exclude_wallets | List of str | Wallet addresses to ignore |  |  | [] |
| cursor | str | The cursor returned in the previous response (used to getting the next page). |  |  | "" |



---
## get_erc20_mints

> `evm_api.token.get_erc20_mints()`




### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "limit": 0, 
    "contract_addresses": [], 
    "exclude_contracts": [], 
    "wallet_addresses": [], 
    "exclude_wallets": [], 
    "cursor": "", 
}

result = evm_api.token.get_erc20_mints(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| from_block | int | The block number from which the mints will be returned |  |  | 0 |
| to_block | int | The block number to which the mints will be returned |  |  | 0 |
| limit | int | The desired page size of the result. |  |  | 0 |
| contract_addresses | List of str | Contract addresses to only include |  |  | [] |
| exclude_contracts | List of str | Contract addresses to ignore |  |  | [] |
| wallet_addresses | List of str | Wallet addresses to only include |  |  | [] |
| exclude_wallets | List of str | Wallet addresses to ignore |  |  | [] |
| cursor | str | The cursor returned in the previous response (used to getting the next page). |  |  | "" |



---
## get_erc20_transfers

> `evm_api.token.get_erc20_transfers()`




### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "limit": 0, 
    "contract_addresses": [], 
    "exclude_contracts": [], 
    "wallet_addresses": [], 
    "exclude_wallets": [], 
    "cursor": "", 
}

result = evm_api.token.get_erc20_transfers(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| from_block | int | The block number from which the transfers will be returned |  |  | 0 |
| to_block | int | The block number to which the transfers will be returned |  |  | 0 |
| limit | int | The desired page size of the result. |  |  | 0 |
| contract_addresses | List of str | Contract addresses to only include |  |  | [] |
| exclude_contracts | List of str | Contract addresses to ignore |  |  | [] |
| wallet_addresses | List of str | Wallet addresses to only include |  |  | [] |
| exclude_wallets | List of str | Wallet addresses to ignore |  |  | [] |
| cursor | str | The cursor returned in the previous response (used to getting the next page). |  |  | "" |



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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |



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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |



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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |



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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| exchange | str | The factory name or address of the token exchange |  |  | "" |
| to_block | int | The block number from which the token price should be checked |  |  | 0 |



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
    "disable_total": True, 
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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the transfers<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from which to get the transfers.<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The start date from which to get the transfers (any format that is accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | Get transfers up until this date (any format that is accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| disable_total | bool | If the result should skip returning the total count (Improves performance). |  | True | True |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |



---
## get_wallet_token_balances

> `evm_api.token.get_wallet_token_balances()`

Get token balances for a specific wallet address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xd8da6bf26964af9d7eed9e03e53415d37aa96045", 
    "chain": "eth", 
    "to_block": 1.2, 
    "token_addresses": [], 
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
| address | str | The address from which token balances will be checked | Yes |  | "0xd8da6bf26964af9d7eed9e03e53415d37aa96045" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| to_block | float | The block number from which the balances should be checked |  |  | 1.2 |
| token_addresses | List of str | The addresses to get balances for (optional) |  |  | [] |



---
## get_wallet_token_transfers

> `evm_api.token.get_wallet_token_transfers()`

Get ERC20 token transactions ordered by block number in descending order.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xd8da6bf26964af9d7eed9e03e53415d37aa96045", 
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "from_date": "", 
    "to_date": "", 
    "limit": 0, 
    "disable_total": True, 
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
| address | str | The address of the wallet | Yes |  | "0xd8da6bf26964af9d7eed9e03e53415d37aa96045" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the transactions<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from which to get the transactions.<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The start date from which to get the transactions (any format that is accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | Get the transactions up to this date (any format that is accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| disable_total | bool | If the result should skip returning the total count (Improves performance). |  | True | True |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |





