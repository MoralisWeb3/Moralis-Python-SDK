# events API: 

> `Moralis.evm_api.events`

- [get_contract_events](#get_contract_events)
- [get_contract_logs](#get_contract_logs)


---
## `get_contract_events()`
Get events for a contract ordered by block number in descending order.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "topic": "", 
    "chain": "eth", 
    "subdomain": "", 
    "providerUrl": "", 
    "from_block": 0, 
    "to_block": 0, 
    "from_date": "", 
    "to_date": "", 
    "offset": 0, 
    "limit": 0, 
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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| subdomain | str | The subdomain of the Moralis server to use (only use when selecting local devchain as chain) |  |  | "" |
| providerUrl | str | The web3 provider URL to use when using local dev chain |  |  | "" |
| from_block | int | The minimum block number from which to get the logs<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from which to get the logs.<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The start date from which to get the logs (any format that is accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | Get the logs up to this date (any format that is accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| offset | int | offset |  |  | 0 |
| limit | int | The desired page size of the result. |  |  | 0 |


### Body

| Type | Description | Required |
|------|-------------|----------|
| object | ABI of the specific event | No |


---
## `get_contract_logs()`
Get the logs for a contract.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "chain": "eth", 
    "subdomain": "", 
    "block_number": "", 
    "from_block": "", 
    "to_block": "", 
    "from_date": "", 
    "to_date": "", 
    "topic0": "", 
    "topic1": "", 
    "topic2": "", 
    "topic3": "", 
    "limit": 0, 
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
| address | str | The address of the contract | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| subdomain | str | The subdomain of the Moralis server to use (only use when selecting local devchain as chain) |  |  | "" |
| block_number | str | The block number<br/>* Provide the param 'block_numer' or ('from_block' and / or 'to_block')<br/>* If 'block_numer' is provided in combination with 'from_block' and / or 'to_block', 'block_number' will will be used<br/> |  |  | "" |
| from_block | str | The minimum block number from which to get the logs<br/>* Provide the param 'block_numer' or ('from_block' and / or 'to_block')<br/>* If 'block_numer' is provided in combination with 'from_block' and / or 'to_block', 'block_number' will will be used<br/> |  |  | "" |
| to_block | str | The maximum block number from which to get the logs<br/>* Provide the param 'block_numer' or ('from_block' and / or 'to_block')<br/>* If 'block_numer' is provided in combination with 'from_block' and / or 'to_block', 'block_number' will will be used<br/> |  |  | "" |
| from_date | str | The start date from which to get the logs (any format that is accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/>* If 'from_date' and the block params are provided, the block params will be used. Please refer to the blocks params sections (block_number,from_block and to_block) on how to use them<br/> |  |  | "" |
| to_date | str | Get the logs up to this date (any format that is accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/>* If 'to_date' and the block params are provided, the block params will be used. Please refer to the blocks params sections (block_number,from_block and to_block) on how to use them<br/> |  |  | "" |
| topic0 | str | topic0 |  |  | "" |
| topic1 | str | topic1 |  |  | "" |
| topic2 | str | topic2 |  |  | "" |
| topic3 | str | topic3 |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |





