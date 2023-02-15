# default API:

> `evm_api.default`

- [get_internal_transactions](#get_internal_transactions)


---
## get_internal_transactions

> `evm_api.default.get_internal_transactions()`

Get the contents of a internal transaction by transaction hash.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "transaction_hash": "0xdc85cb1b75fd09c2f6d001fea4aba83764193cbd7881a1fa8ccde350a5681109", 
    "chain": "eth", 
}

result = evm_api.default.get_internal_transactions(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| transaction_hash | str | The transaction hash | Yes |  | "0xdc85cb1b75fd09c2f6d001fea4aba83764193cbd7881a1fa8ccde350a5681109" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |





