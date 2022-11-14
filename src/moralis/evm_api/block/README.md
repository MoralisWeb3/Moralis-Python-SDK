# evm_api: block

- [get_block](#get_block)
- [get_date_to_block](#get_date_to_block)


---
## `get_block()`
Get the contents of a block given the block hash.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "block_number_or_hash": "", 
    "chain": "eth", 
    "subdomain": "", 
}

result = evm_api.block.get_block(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| block_number_or_hash | str | The block number or block hash | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| subdomain | str | The subdomain of the Moralis server to use (only use when selecting local devchain as chain) |  |  | "" |



---
## `get_date_to_block()`
Get the closest block given the date.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "date": "", 
    "chain": "eth", 
    "providerUrl": "", 
}

result = evm_api.block.get_date_to_block(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| date | str | Unix date in milliseconds or a datestring (any format that is accepted by momentjs) | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| providerUrl | str | The web3 provider URL to use when using local dev chain |  |  | "" |





