# evm API:

> `streams.evm`

- [add_address_to_stream](#add_address_to_stream)
- [create_stream](#create_stream)
- [delete_address_from_stream](#delete_address_from_stream)
- [delete_stream](#delete_stream)
- [get_addresses](#get_addresses)
- [get_stream](#get_stream)
- [get_streams](#get_streams)
- [update_stream](#update_stream)
- [update_stream_status](#update_stream_status)


---
## add_address_to_stream

> `streams.evm.add_address_to_stream()`

Adds an address to a Stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
}
body = {
    "address": "", 
}

result = streams.evm.add_address_to_stream(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | The id of the stream to add the address to | Yes |  | "" |


### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address or a list of addresses to be added to the Stream. | Yes |  | "" |


---
## create_stream

> `streams.evm.create_stream()`

Creates a new evm stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
body = {
    "webhookUrl": "", 
    "description": "", 
    "tag": "", 
    "topic0": [], 
    "allAddresses": True, 
    "includeNativeTxs": True, 
    "includeContractLogs": True, 
    "includeInternalTxs": True, 
    "abi": [], 
    "advancedOptions": [], 
    "chainIds": [], 
}

result = streams.evm.create_stream(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| webhookUrl | str | Webhook URL where moralis will send the POST request. | Yes |  | "" |
| description | str | A description for this stream | Yes |  | "" |
| tag | str | A user-provided tag that will be send along the webhook, the user can use this tag to identify the specific stream if multiple streams are present | Yes |  | "" |
| topic0 | List of str | An Array of topic0's in hex, required if the type : log | Yes |  | [] |
| allAddresses | bool | Include events for all addresses (only applied when abi and topic0 is provided) | Yes |  | True |
| includeNativeTxs | bool | Include or not native transactions defaults to false (only applied when type:contract) | Yes |  | True |
| includeContractLogs | bool | Include or not logs of contract interactions defaults to false | Yes |  | True |
| includeInternalTxs | bool | Include or not include internal transactions defaults to false | Yes |  | True |
| abi | List of object: <br/> - anonymous: bool<br/> - constant: bool<br/> - inputs: List of AbiInput<br/> - name: str<br/> - outputs: List of AbiOutput<br/> - payable: bool<br/> - stateMutability: str<br/> - type: str<br/> - gas: float |  | Yes |  | [] |
| advancedOptions | List of object: <br/> - topic0: str<br/> - filter: object: <br/><br/> - includeNativeTxs: bool |  | Yes |  | [] |
| chainIds | List of str | The ids of the chains for this stream in hex Ex: ["0x1","0x38"] | Yes |  | [] |


---
## delete_address_from_stream

> `streams.evm.delete_address_from_stream()`

Deletes an address from a Stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
}
body = {
    "address": "", 
}

result = streams.evm.delete_address_from_stream(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | The id of the stream to delete the address from | Yes |  | "" |


### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address or a list of addresses to be removed from the Stream. | Yes |  | "" |


---
## delete_stream

> `streams.evm.delete_stream()`

Delete a specific evm stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
}

result = streams.evm.delete_stream(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | The id of the stream to delete | Yes |  | "" |



---
## get_addresses

> `streams.evm.get_addresses()`

Get all addresses associated with a specific stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
    "limit": 1.2, 
    "cursor": "", 
}

result = streams.evm.get_addresses(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | the id of the stream to get the addresses from | Yes |  | "" |
| limit | float | Limit response results max value 100 | Yes |  | 1.2 |
| cursor | str | Cursor for fetching next page |  |  | "" |



---
## get_stream

> `streams.evm.get_stream()`

Get a specific evm stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
}

result = streams.evm.get_stream(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | The id of the stream to get | Yes |  | "" |



---
## get_streams

> `streams.evm.get_streams()`

Get all the evm streams for the current project based on the project api-key.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "limit": 1.2, 
    "cursor": "", 
}

result = streams.evm.get_streams(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| limit | float | Limit response results max value 100 | Yes |  | 1.2 |
| cursor | str | Cursor for fetching next page |  |  | "" |



---
## update_stream

> `streams.evm.update_stream()`

Updates a specific evm stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
}
body = {
    "webhookUrl": "", 
    "description": "", 
    "tag": "", 
    "topic0": [], 
    "allAddresses": True, 
    "includeNativeTxs": True, 
    "includeContractLogs": True, 
    "includeInternalTxs": True, 
    "abi": [], 
    "advancedOptions": [], 
    "chainIds": [], 
}

result = streams.evm.update_stream(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | The id of the stream to update | Yes |  | "" |


### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| webhookUrl | str | Webhook URL where moralis will send the POST request. | Yes |  | "" |
| description | str | A description for this stream | Yes |  | "" |
| tag | str | A user-provided tag that will be send along the webhook, the user can use this tag to identify the specific stream if multiple streams are present | Yes |  | "" |
| topic0 | List of str | An Array of topic0's in hex, required if the type : log | Yes |  | [] |
| allAddresses | bool | Include events for all addresses (only applied when abi and topic0 is provided) | Yes |  | True |
| includeNativeTxs | bool | Include or not native transactions defaults to false (only applied when type:contract) | Yes |  | True |
| includeContractLogs | bool | Include or not logs of contract interactions defaults to false | Yes |  | True |
| includeInternalTxs | bool | Include or not include internal transactions defaults to false | Yes |  | True |
| abi | List of object: <br/> - anonymous: bool<br/> - constant: bool<br/> - inputs: List of AbiInput<br/> - name: str<br/> - outputs: List of AbiOutput<br/> - payable: bool<br/> - stateMutability: str<br/> - type: str<br/> - gas: float |  | Yes |  | [] |
| advancedOptions | List of object: <br/> - topic0: str<br/> - filter: object: <br/><br/> - includeNativeTxs: bool |  | Yes |  | [] |
| chainIds | List of str | The ids of the chains for this stream in hex Ex: ["0x1","0x38"] | Yes |  | [] |


---
## update_stream_status

> `streams.evm.update_stream_status()`

Updates the status of specific evm stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
}
body = {
    "status": "", 
}

result = streams.evm.update_stream_status(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | The id of the stream to update | Yes |  | "" |


### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| status | enum[str]: <br/>- "active"<br/>- "paused"<br/>- "error"<br/>- "terminated" | The status of the stream. | Yes |  | "" |




