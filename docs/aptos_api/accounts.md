# accounts API:

> `aptos_api.accounts`

- [get_account](#get_account)
- [get_account_module](#get_account_module)
- [get_account_modules](#get_account_modules)
- [get_account_resource](#get_account_resource)
- [get_account_resources](#get_account_resources)
- [get_events_by_creation_number](#get_events_by_creation_number)
- [get_events_by_event_handle](#get_events_by_event_handle)


---
## get_account

> `aptos_api.accounts.get_account()`

Get account

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "address": "", 
    "ledger_version": "", 
}

result = aptos_api.accounts.get_account(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| address | str | Address of account with or without a 0x prefix | Yes |  | "" |
| ledger_version | str | Ledger version to get state of account.<br/>If not provided, it will be the latest version |  |  | "" |



---
## get_account_module

> `aptos_api.accounts.get_account_module()`

Get account module

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "address": "", 
    "module_name": "", 
    "ledger_version": "", 
}

result = aptos_api.accounts.get_account_module(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| address | str | Address of account with or without a 0x prefix | Yes |  | "" |
| module_name | str | Name of module to retrieve | Yes |  | "" |
| ledger_version | str | Ledger version to get state of account.<br/>If not provided, it will be the latest version |  |  | "" |



---
## get_account_modules

> `aptos_api.accounts.get_account_modules()`

Get account modules

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "address": "", 
    "ledger_version": "", 
    "limit": 1.2, 
    "start": "", 
}

result = aptos_api.accounts.get_account_modules(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| address | str | Address of account with or without a 0x prefix | Yes |  | "" |
| ledger_version | str | Ledger version to get state of account.<br/>If not provided, it will be the latest version |  |  | "" |
| limit | float | Max number of account resources to retrieve.<br/>If not provided, defaults to default page size. |  | 100 | 1.2 |
| start | str | Cursor specifying where to start for pagination<br/>This cursor cannot be derived manually client-side. Instead, you must call this endpoint once without this query parameter specified, and then use the cursor returned in the X-Aptos-Cursor header in the response. |  | "" | "" |



---
## get_account_resource

> `aptos_api.accounts.get_account_resource()`

Get account resource

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "address": "", 
    "resource_type": "", 
    "ledger_version": "", 
}

result = aptos_api.accounts.get_account_resource(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| address | str | Address of account with or without a 0x prefix | Yes |  | "" |
| resource_type | str | Name of struct to retrieve e.g. 0x1::account::Account | Yes |  | "" |
| ledger_version | str | Ledger version to get state of account.<br/>If not provided, it will be the latest version |  |  | "" |



---
## get_account_resources

> `aptos_api.accounts.get_account_resources()`

Get account resources

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "address": "", 
    "ledger_version": "", 
    "limit": 1.2, 
    "start": "", 
}

result = aptos_api.accounts.get_account_resources(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| address | str | Address of account with or without a 0x prefix | Yes |  | "" |
| ledger_version | str | Ledger version to get state of account.<br/>If not provided, it will be the latest version |  |  | "" |
| limit | float | Max number of account resources to retrieve.<br/>If not provided, defaults to default page size. |  | 100 | 1.2 |
| start | str | Cursor specifying where to start for pagination<br/>This cursor cannot be derived manually client-side. Instead, you must call this endpoint once without this query parameter specified, and then use the cursor returned in the X-Aptos-Cursor header in the response. |  | "" | "" |



---
## get_events_by_creation_number

> `aptos_api.accounts.get_events_by_creation_number()`

Get events by creation number

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "address": "", 
    "creation_number": "", 
    "limit": 1.2, 
    "start": "", 
}

result = aptos_api.accounts.get_events_by_creation_number(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| address | str | Address of account with or without a 0x prefix | Yes |  | "" |
| creation_number | str | Creation number corresponding to the event stream originating from the given account. | Yes |  | "" |
| limit | float | Max number of account resources to retrieve.<br/>If not provided, defaults to default page size. |  | 100 | 1.2 |
| start | str | Starting sequence number of events.<br/>If unspecified, by default will retrieve the most recent events |  |  | "" |



---
## get_events_by_event_handle

> `aptos_api.accounts.get_events_by_event_handle()`

Get events by event handle

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "address": "", 
    "event_handle": "", 
    "field_name": "", 
    "limit": 1.2, 
    "start": "", 
}

result = aptos_api.accounts.get_events_by_event_handle(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| address | str | Hex-encoded 32 byte Aptos account, with or without a 0x prefix, for which events are queried. This refers to the account that events were emitted to, not the account hosting the move module that emits that event type. | Yes |  | "" |
| event_handle | str | Name of struct to lookup event handle. | Yes |  | "" |
| field_name | str | Name of field to lookup event handle. | Yes |  | "" |
| limit | float | Max number of account resources to retrieve.<br/>If not provided, defaults to default page size. |  | 100 | 1.2 |
| start | str | Starting sequence number of events.<br/>If unspecified, by default will retrieve the most recent events |  |  | "" |





