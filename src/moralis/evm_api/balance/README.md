# evm_api: balance

- [get_native_balance](#get_native_balance)


---
## `get_native_balance()`
Get the native balance for a specific wallet address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x057Ec652A4F150f7FF94f089A38008f49a0DF88e", 
    "chain": "eth", 
    "providerUrl": "", 
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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| providerUrl | str | The web3 provider URL to use when using local dev chain |  |  | "" |
| to_block | float | The block number from which the balances should be checked |  |  | 1.2 |





