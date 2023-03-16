# blocks API:

> `aptos_api.blocks`

- [get_block_by_height](#get_block_by_height)
- [get_block_by_version](#get_block_by_version)


---
## get_block_by_height

> `aptos_api.blocks.get_block_by_height()`

Get block by height

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "block_height": 1.2, 
    "with_transactions": True, 
}

result = aptos_api.blocks.get_block_by_height(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| block_height | float | Block height to lookup. Starts at 0 | Yes |  | 1.2 |
| with_transactions | bool | If set to true, include all transactions in the block |  |  | True |



---
## get_block_by_version

> `aptos_api.blocks.get_block_by_version()`

Get block by version

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "version": 1.2, 
    "with_transactions": True, 
}

result = aptos_api.blocks.get_block_by_version(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| version | float | Ledger version to lookup block information for. | Yes |  | 1.2 |
| with_transactions | bool | If set to true, include all transactions in the block |  |  | True |





