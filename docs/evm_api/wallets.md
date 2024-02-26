# wallets API:

> `evm_api.wallets`

- [get_wallet_active_chains](#get_wallet_active_chains)
- [get_wallet_net_worth](#get_wallet_net_worth)
- [get_wallet_stats](#get_wallet_stats)
- [get_wallet_token_balances_price](#get_wallet_token_balances_price)


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
| chains | List of enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base testnet"<br/>- "0x14a33"<br/>- "optimism"<br/>- "0xa" | The chains to query |  |  | [] |



---
## get_wallet_net_worth

> `evm_api.wallets.get_wallet_net_worth()`

Get the net worth of a wallet in USD. We recommend to filter out spam tokens and unverified contracts to get a more accurate result.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xd8da6bf26964af9d7eed9e03e53415d37aa96045", 
    "chains": [], 
    "exclude_spam": True, 
    "exclude_unverified_contracts": True, 
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
| address | str | The wallet address | Yes |  | "0xd8da6bf26964af9d7eed9e03e53415d37aa96045" |
| chains | List of enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base testnet"<br/>- "0x14a33"<br/>- "optimism"<br/>- "0xa" | The chains to query |  |  | [] |
| exclude_spam | bool | Exclude spam tokens from the result |  | False | True |
| exclude_unverified_contracts | bool | Exclude unverified contracts from the result |  | False | True |



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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base testnet"<br/>- "0x14a33"<br/>- "optimism"<br/>- "0xa" | The chain to query |  | "eth" | "eth" |



---
## get_wallet_token_balances_price

> `evm_api.wallets.get_wallet_token_balances_price()`

Get token balances for a specific wallet address and their token prices in USD.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xd8da6bf26964af9d7eed9e03e53415d37aa96045", 
    "chain": "eth", 
    "to_block": 1.2, 
    "token_addresses": [], 
    "exclude_spam": True, 
    "exclude_unverified_contracts": True, 
    "cursor": "", 
    "limit": 0, 
    "exclude_native": True, 
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
| address | str | The address from which token balances will be checked | Yes |  | "0xd8da6bf26964af9d7eed9e03e53415d37aa96045" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base testnet"<br/>- "0x14a33"<br/>- "optimism"<br/>- "0xa" | The chain to query |  | "eth" | "eth" |
| to_block | float | The block number up to which the balances will be checked. |  |  | 1.2 |
| token_addresses | List of str | The addresses to get balances for (optional) |  |  | [] |
| exclude_spam | bool | Exclude spam tokens from the result |  | False | True |
| exclude_unverified_contracts | bool | Exclude unverified contracts from the result |  | False | True |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| exclude_native | bool | Exclude native balance from the result |  | False | True |





