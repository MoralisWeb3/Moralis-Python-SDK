# wallets API:

> `evm_api.wallets`

- [get_wallet_active_chains](#get_wallet_active_chains)
- [get_wallet_net_worth](#get_wallet_net_worth)


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
| chains | List of enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chains to query |  |  | [] |



---
## get_wallet_net_worth

> `evm_api.wallets.get_wallet_net_worth()`

Get the net worth of a wallet



### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x21197e3ec0f53db9d1d570f39151c410deba957a", 
    "chains": [], 
    "include": "", 
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
| address | str | The address of the wallet | Yes |  | "0x21197e3ec0f53db9d1d570f39151c410deba957a" |
| chains | List of enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chains to query |  |  | [] |
| include | enum[str]: <br/>- "possible_spam" | If the result should contain possible spam tokens |  | "" | "" |





