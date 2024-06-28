# events API:

> `evm_api.events`

- [get_contract_events](#get_contract_events)
- [get_contract_logs](#get_contract_logs)


---
## get_contract_events

> `evm_api.events.get_contract_events()`

Get events for a contract ordered by block number in descending order. [Try it with Swagger](https://deep-index.moralis.io/api-docs-2.1/#/Events/getContractEvents).


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "topic": "", 
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "from_date": "", 
    "to_date": "", 
    "offset": 0, 
    "limit": 0, 
    "order": "DESC", 
    "cursor": "", 
}
body = ""

result = evm_api.events.get_contract_events(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the contract | Yes |  | "" |
| topic | str | The topic of the event | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the logs<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from which to get the logs.<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The start date from which to get the logs (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | Get the logs up to this date (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| offset | int | offset |  |  | 0 |
| limit | int | The desired page size of the result. |  |  | 0 |
| order | enum[str]: <br/>- "ASC"<br/>- "DESC" | The order of the result, in ascending (ASC) or descending (DESC) |  | "DESC" | "DESC" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |


### Body

| Type | Description | Required |
|------|-------------|----------|
| object | ABI of the specific event | Yes |


---
## get_contract_logs

> `evm_api.events.get_contract_logs()`

Get the logs for a contract.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB", 
    "topic0": "", 
    "chain": "eth", 
    "block_number": "", 
    "from_block": "", 
    "to_block": "", 
    "from_date": "", 
    "to_date": "", 
    "limit": 0, 
    "order": "DESC", 
    "cursor": "", 
}

result = evm_api.events.get_contract_logs(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the contract | Yes |  | "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB" |
| topic0 | str | topic0 | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| block_number | str | The block number<br/>* Provide the param 'block_numer' or ('from_block' and / or 'to_block')<br/>* If 'block_numer' is provided in combination with 'from_block' and / or 'to_block', 'block_number' will will be used<br/> |  |  | "" |
| from_block | str | The minimum block number from which to get the logs<br/>* Provide the param 'block_numer' or ('from_block' and / or 'to_block')<br/>* If 'block_numer' is provided in combination with 'from_block' and / or 'to_block', 'block_number' will will be used<br/> |  |  | "" |
| to_block | str | The maximum block number from which to get the logs<br/>* Provide the param 'block_numer' or ('from_block' and / or 'to_block')<br/>* If 'block_numer' is provided in combination with 'from_block' and / or 'to_block', 'block_number' will will be used<br/> |  |  | "" |
| from_date | str | The start date from which to get the logs (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/>* If 'from_date' and the block params are provided, the block params will be used. Please refer to the blocks params sections (block_number,from_block and to_block) on how to use them<br/> |  |  | "" |
| to_date | str | Get the logs up to this date (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/>* If 'to_date' and the block params are provided, the block params will be used. Please refer to the blocks params sections (block_number,from_block and to_block) on how to use them<br/> |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| order | enum[str]: <br/>- "ASC"<br/>- "DESC" | The order of the result, in ascending (ASC) or descending (DESC) |  | "DESC" | "DESC" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |





