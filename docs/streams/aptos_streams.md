# aptos_streams API:

> `streams.aptos_streams`

- [aptos_streams_add_addresses](#aptos_streams_add_addresses)
- [aptos_streams_create](#aptos_streams_create)
- [aptos_streams_delete](#aptos_streams_delete)
- [aptos_streams_delete_addresses](#aptos_streams_delete_addresses)
- [aptos_streams_get](#aptos_streams_get)
- [aptos_streams_get_addresses](#aptos_streams_get_addresses)
- [aptos_streams_get_all](#aptos_streams_get_all)
- [aptos_streams_update](#aptos_streams_update)
- [aptos_streams_update_status](#aptos_streams_update_status)


---
## aptos_streams_add_addresses

> `streams.aptos_streams.aptos_streams_add_addresses()`

Adds addresses to an existing aptos stream


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
}
body = ""

result = streams.aptos_streams.aptos_streams_add_addresses(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | the id of the aptos stream to get the addresses from | Yes |  | "" |


### Body

| Type | Description | Required |
|------|-------------|----------|
| object: <br/> - address: str | - | Yes |


---
## aptos_streams_create

> `streams.aptos_streams.aptos_streams_create()`

Creates a new aptos stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
body = {
    "webhookUrl": "", 
    "tag": "", 
    "functions": [], 
    "events": [], 
    "network": [], 
    "includePayload": True, 
    "includeEvents": True, 
    "includeChanges": True, 
    "description": "", 
    "demo": True, 
    "allAddresses": True, 
}

result = streams.aptos_streams.aptos_streams_create(
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
| tag | str | A user-provided tag that will be send along the webhook, the user can use this tag to identify the specific stream if multiple streams are present | Yes |  | "" |
| functions | List of str | An Array of events in string-signature format ex: ['0x1::aptos_account::transfer'] | Yes |  | [] |
| events | List of str | An Array of events in string-signature format ex: ['0x1::coin::WithdrawEvent'] | Yes |  | [] |
| network | List of enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to listen to | Yes |  | [] |
| includePayload | bool | Include or not payload for every transaction in webhook defaults to false | Yes |  | True |
| includeEvents | bool | Include or not events in webhook defaults to false | Yes |  | True |
| includeChanges | bool | Include or not raw changes for every transaction in webhook defaults to false | Yes |  | True |
| description | str | A description for this stream | Yes |  | "" |
| demo | bool | Indicator if it is a demo stream | Yes |  | True |
| allAddresses | bool | Include events for all addresses (only applied when at least one event or function is provided) | Yes |  | True |


---
## aptos_streams_delete

> `streams.aptos_streams.aptos_streams_delete()`

Deletes a aptos stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
}

result = streams.aptos_streams.aptos_streams_delete(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | the id of the aptos stream to delete | Yes |  | "" |



---
## aptos_streams_delete_addresses

> `streams.aptos_streams.aptos_streams_delete_addresses()`

Deletes addresses of an existing aptos stream


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
}
body = ""

result = streams.aptos_streams.aptos_streams_delete_addresses(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | the id of the aptos stream to get the addresses from | Yes |  | "" |


### Body

| Type | Description | Required |
|------|-------------|----------|
| object: <br/> - address: str | Provide a list of valid Aptos addresses, or a single address | Yes |


---
## aptos_streams_get

> `streams.aptos_streams.aptos_streams_get()`

Get a specific aptos stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
}

result = streams.aptos_streams.aptos_streams_get(
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
## aptos_streams_get_addresses

> `streams.aptos_streams.aptos_streams_get_addresses()`

Get all addresses associated with a specific aptos stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
    "limit": 1.2, 
    "cursor": "", 
}

result = streams.aptos_streams.aptos_streams_get_addresses(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | the id of the aptos stream to get the addresses from | Yes |  | "" |
| limit | float | Limit response results max value 100 | Yes |  | 1.2 |
| cursor | str | Cursor for fetching next page |  |  | "" |



---
## aptos_streams_get_all

> `streams.aptos_streams.aptos_streams_get_all()`

Get all aptos streams.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "limit": 1.2, 
    "cursor": "", 
}

result = streams.aptos_streams.aptos_streams_get_all(
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
## aptos_streams_update

> `streams.aptos_streams.aptos_streams_update()`

Updates a new aptos stream.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "id": "", 
}
body = {
    "allAddresses": True, 
    "demo": True, 
    "description": "", 
    "includeChanges": True, 
    "includeEvents": True, 
    "includePayload": True, 
    "network": [], 
    "events": [], 
    "functions": [], 
    "tag": "", 
    "webhookUrl": "", 
}

result = streams.aptos_streams.aptos_streams_update(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str |  | Yes |  | "" |


### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| allAddresses | bool | Include events for all addresses (only applied when at least one event or function is provided) | Yes |  | True |
| demo | bool | Indicator if it is a demo stream | Yes |  | True |
| description | str | A description for this stream | Yes |  | "" |
| includeChanges | bool | Include or not raw changes for every transaction in webhook defaults to false | Yes |  | True |
| includeEvents | bool | Include or not events in webhook defaults to false | Yes |  | True |
| includePayload | bool | Include or not payload for every transaction in webhook defaults to false | Yes |  | True |
| network | List of enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to listen to | Yes |  | [] |
| events | List of str | An Array of events in string-signature format ex: ['0x1::coin::WithdrawEvent'] | Yes |  | [] |
| functions | List of str | An Array of events in string-signature format ex: ['0x1::aptos_account::transfer'] | Yes |  | [] |
| tag | str | A user-provided tag that will be send along the webhook, the user can use this tag to identify the specific stream if multiple streams are present | Yes |  | "" |
| webhookUrl | str | Webhook URL where moralis will send the POST request. | Yes |  | "" |


---
## aptos_streams_update_status

> `streams.aptos_streams.aptos_streams_update_status()`

Update a Stream Status


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

result = streams.aptos_streams.aptos_streams_update_status(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| id | str | the id of the aptos stream to update the status | Yes |  | "" |


### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| status | enum[str]: <br/>- "active"<br/>- "paused"<br/>- "error"<br/>- "terminated" | The status of the stream. | Yes |  | "" |




