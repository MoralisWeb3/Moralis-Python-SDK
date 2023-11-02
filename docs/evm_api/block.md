# block API:

> `evm_api.block`

- [get_block](#get_block)
- [get_block_stats](#get_block_stats)
- [get_date_to_block](#get_date_to_block)


---
## get_block

> `evm_api.block.get_block()`

Get the contents of a block given the block hash.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "block_number_or_hash": "15863321", 
    "chain": "eth", 
    "include": "", 
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
| block_number_or_hash | str | The block number or block hash | Yes |  | "15863321" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8" | The chain to query |  | "eth" | "eth" |
| include | enum[str]: <br/>- "internal_transactions" | If the result should contain the internal transactions. |  | "" | "" |



---
## get_block_stats

> `evm_api.block.get_block_stats()`

Get the stats for a block


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "block_number_or_hash": "", 
    "chain": "eth", 
}

result = evm_api.block.get_block_stats(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| block_number_or_hash | str | The block number or hash | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8" | The chain to query |  | "eth" | "eth" |



---
## get_date_to_block

> `evm_api.block.get_date_to_block()`

Get the closest block given the date.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "date": "", 
    "chain": "eth", 
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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8" | The chain to query |  | "eth" | "eth" |





