# balance API:

> `evm_api.balance`

- [get_native_balance](#get_native_balance)
- [get_native_balances_for_addresses](#get_native_balances_for_addresses)


---
## get_native_balance

> `evm_api.balance.get_native_balance()`

Get the native balance for a specific wallet address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x057Ec652A4F150f7FF94f089A38008f49a0DF88e", 
    "chain": "eth", 
    "to_block": 1.2, 
}

result = evm_api.balance.get_native_balance(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address from which the native balance will be checked | Yes |  | "0x057Ec652A4F150f7FF94f089A38008f49a0DF88e" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| to_block | float | The block number up to which the balances will be checked. |  |  | 1.2 |



---
## get_native_balances_for_addresses

> `evm_api.balance.get_native_balances_for_addresses()`

Get the native balances for a set of specific addresses


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "wallet_addresses": [], 
    "chain": "eth", 
    "to_block": 1.2, 
}

result = evm_api.balance.get_native_balances_for_addresses(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| wallet_addresses | List of str | The addresses to get metadata for | Yes |  | [] |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| to_block | float | The block number on which the balances should be checked |  |  | 1.2 |





