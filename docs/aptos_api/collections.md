# collections API:

> `aptos_api.collections`

- [get_nft_collections](#get_nft_collections)
- [get_nft_collections_by_creator](#get_nft_collections_by_creator)
- [get_nft_collections_by_ids](#get_nft_collections_by_ids)


---
## get_nft_collections

> `aptos_api.collections.get_nft_collections()`

Get NFT Collections

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "offset": 1.2, 
    "cursor": "", 
    "fromName": "", 
    "toName": "", 
}

result = aptos_api.collections.get_nft_collections(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| limit | float | The number of results to return | Yes | 10 | 1.2 |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  | "" | "" |
| fromName | str | The name of the collection to start from (inclusive and case sensitive) |  |  | "" |
| toName | str | The name of the collection to end at (inclusive and case sensitive) |  |  | "" |



---
## get_nft_collections_by_creator

> `aptos_api.collections.get_nft_collections_by_creator()`

Get NFT Collections by creator

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "creator_address": "", 
    "offset": 1.2, 
    "cursor": "", 
}

result = aptos_api.collections.get_nft_collections_by_creator(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| limit | float | The number of results to return | Yes | 10 | 1.2 |
| creator_address | str | The address of the creator | Yes | "" | "" |
| offset | float | The number of results to skip |  | 0 | 1.2 |
| cursor | str | The cursor to use for getting the next page |  | "" | "" |



---
## get_nft_collections_by_ids

> `aptos_api.collections.get_nft_collections_by_ids()`

Get NFT Collections by ids

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "ids": [], 
}

result = aptos_api.collections.get_nft_collections_by_ids(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| ids | List of str | The identifiers of the collections to get | Yes | [] | [] |





