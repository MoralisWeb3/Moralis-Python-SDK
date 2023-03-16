# transactions API:

> `aptos_api.transactions`

- [encode_submission](#encode_submission)
- [estimate_gas_price](#estimate_gas_price)
- [get_account_transactions](#get_account_transactions)
- [get_transaction_by_hash](#get_transaction_by_hash)
- [get_transaction_by_version](#get_transaction_by_version)
- [get_transactions](#get_transactions)
- [simulate_transaction](#simulate_transaction)
- [submit_batch_transactions](#submit_batch_transactions)
- [submit_transaction](#submit_transaction)


---
## encode_submission

> `aptos_api.transactions.encode_submission()`

Encode submission

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
}
body = {
    "sender": "", 
    "sequence_number": "", 
    "max_gas_amount": "", 
    "gas_unit_price": "", 
    "expiration_timestamp_secs": "", 
    "payload": {}, 
    "secondary_signers": [], 
}

result = aptos_api.transactions.encode_submission(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| sender | str | A hex encoded 32 byte Aptos account address. | Yes |  | "" |
| sequence_number | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| max_gas_amount | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| gas_unit_price | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| expiration_timestamp_secs | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| payload | One of:<br/>object: <br/> - type: str<br/> - function: str<br/> - type_arguments: List of str<br/> - arguments: List of str<br/>---<br/>object: <br/> - type: str<br/> - code: object<br/> - type_arguments: List of str<br/> - arguments: List of str<br/>---<br/>object: <br/> - type: str<br/> - modules: List of str<br/>---<br/> | An enum of the possible transaction payloads | Yes |  | {} |
| secondary_signers | List of str | Secondary signer accounts of the request for Multi-agent | Yes |  | [] |


---
## estimate_gas_price

> `aptos_api.transactions.estimate_gas_price()`

Estimate gas price

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
}

result = aptos_api.transactions.estimate_gas_price(
    api_key=api_key,
    params=params,
)

print(result)

```


---
## get_account_transactions

> `aptos_api.transactions.get_account_transactions()`

Get account transactions

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "address": "", 
    "limit": 1.2, 
    "start": "", 
}

result = aptos_api.transactions.get_account_transactions(
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
| limit | float | Max number of transactions to retrieve.<br/>If not provided, defaults to default page size |  | 100 | 1.2 |
| start | str | Account sequence number to start list of transactions.<br/>If not provided, defaults to showing the latest transactions |  |  | "" |



---
## get_transaction_by_hash

> `aptos_api.transactions.get_transaction_by_hash()`

Get transaction by hash

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "txn_hash": "", 
}

result = aptos_api.transactions.get_transaction_by_hash(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| txn_hash | str | Hash of transaction to retrieve | Yes |  | "" |



---
## get_transaction_by_version

> `aptos_api.transactions.get_transaction_by_version()`

Get transaction by version

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "txn_version": "", 
}

result = aptos_api.transactions.get_transaction_by_version(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| txn_version | str | Version of transaction to retrieve | Yes |  | "" |



---
## get_transactions

> `aptos_api.transactions.get_transactions()`

Get transactions

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
    "limit": 1.2, 
    "start": "", 
}

result = aptos_api.transactions.get_transactions(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network to use | No | "mainnet"  | "testnet" |
| limit | float | Max number of transactions to retrieve.<br/>If not provided, defaults to default page size |  | 100 | 1.2 |
| start | str | Account sequence number to start list of transactions.<br/>If not provided, defaults to showing the latest transactions |  |  | "" |



---
## simulate_transaction

> `aptos_api.transactions.simulate_transaction()`

Simulate transaction

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
}
body = {
    "sender": "", 
    "sequence_number": "", 
    "max_gas_amount": "", 
    "gas_unit_price": "", 
    "expiration_timestamp_secs": "", 
    "payload": {}, 
    "signature": {}, 
}

result = aptos_api.transactions.simulate_transaction(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| sender | str | A hex encoded 32 byte Aptos account address. | Yes |  | "" |
| sequence_number | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| max_gas_amount | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| gas_unit_price | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| expiration_timestamp_secs | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| payload | One of:<br/>object: <br/> - type: str<br/> - function: str<br/> - type_arguments: List of str<br/> - arguments: List of str<br/>---<br/>object: <br/> - type: str<br/> - code: object<br/> - type_arguments: List of str<br/> - arguments: List of str<br/>---<br/>object: <br/> - type: str<br/> - modules: List of str<br/>---<br/> | An enum of the possible transaction payloads | Yes |  | {} |
| signature | One of:<br/>object: <br/> - type: str<br/> - signature: str<br/> - public_key: str<br/>---<br/>object: <br/> - type: str<br/> - public_keys: List of str<br/> - signatures: List of str<br/> - threshold: float<br/> - bitmap: str<br/>---<br/>object: <br/> - type: str<br/> - sender: One of:<br/>object: <br/> - type: str<br/> - signature: str<br/> - public_key: str<br/>---<br/>object: <br/> - type: str<br/> - public_keys: List of str<br/> - signatures: List of str<br/> - threshold: float<br/> - bitmap: str<br/>---<br/><br/> - secondary_signer_addresses: List of str<br/> - secondary_signers: One of:<br/>object: <br/> - type: str<br/> - signature: str<br/> - public_key: str<br/>---<br/>object: <br/> - type: str<br/> - public_keys: List of str<br/> - signatures: List of str<br/> - threshold: float<br/> - bitmap: str<br/>---<br/><br/>---<br/> |  | Yes |  | {} |


---
## submit_batch_transactions

> `aptos_api.transactions.submit_batch_transactions()`

Submit batch transactions

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
}
body = [{
    "sender": "", 
    "sequence_number": "", 
    "max_gas_amount": "", 
    "gas_unit_price": "", 
    "expiration_timestamp_secs": "", 
    "payload": {}, 
    "signature": {}, 
}]

result = aptos_api.transactions.submit_batch_transactions(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Body
Array of objects, with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| sender | str | A hex encoded 32 byte Aptos account address. | Yes |  | "" |
| sequence_number | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| max_gas_amount | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| gas_unit_price | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| expiration_timestamp_secs | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| payload | One of:<br/>object: <br/> - type: str<br/> - function: str<br/> - type_arguments: List of str<br/> - arguments: List of str<br/>---<br/>object: <br/> - type: str<br/> - code: object<br/> - type_arguments: List of str<br/> - arguments: List of str<br/>---<br/>object: <br/> - type: str<br/> - modules: List of str<br/>---<br/> | An enum of the possible transaction payloads | Yes |  | {} |
| signature | One of:<br/>object: <br/> - type: str<br/> - signature: str<br/> - public_key: str<br/>---<br/>object: <br/> - type: str<br/> - public_keys: List of str<br/> - signatures: List of str<br/> - threshold: float<br/> - bitmap: str<br/>---<br/>object: <br/> - type: str<br/> - sender: One of:<br/>object: <br/> - type: str<br/> - signature: str<br/> - public_key: str<br/>---<br/>object: <br/> - type: str<br/> - public_keys: List of str<br/> - signatures: List of str<br/> - threshold: float<br/> - bitmap: str<br/>---<br/><br/> - secondary_signer_addresses: List of str<br/> - secondary_signers: One of:<br/>object: <br/> - type: str<br/> - signature: str<br/> - public_key: str<br/>---<br/>object: <br/> - type: str<br/> - public_keys: List of str<br/> - signatures: List of str<br/> - threshold: float<br/> - bitmap: str<br/>---<br/><br/>---<br/> |  | Yes |  | {} |


---
## submit_transaction

> `aptos_api.transactions.submit_transaction()`

Submit transaction

### Example
```python
from moralis import aptos_api

api_key = "YOUR_API_KEY"
params = {
    "network": "mainnet",
}
body = {
    "sender": "", 
    "sequence_number": "", 
    "max_gas_amount": "", 
    "gas_unit_price": "", 
    "expiration_timestamp_secs": "", 
    "payload": {}, 
    "signature": {}, 
}

result = aptos_api.transactions.submit_transaction(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| sender | str | A hex encoded 32 byte Aptos account address. | Yes |  | "" |
| sequence_number | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| max_gas_amount | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| gas_unit_price | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| expiration_timestamp_secs | str | A string containing a 64-bit unsigned integer. | Yes |  | "" |
| payload | One of:<br/>object: <br/> - type: str<br/> - function: str<br/> - type_arguments: List of str<br/> - arguments: List of str<br/>---<br/>object: <br/> - type: str<br/> - code: object<br/> - type_arguments: List of str<br/> - arguments: List of str<br/>---<br/>object: <br/> - type: str<br/> - modules: List of str<br/>---<br/> | An enum of the possible transaction payloads | Yes |  | {} |
| signature | One of:<br/>object: <br/> - type: str<br/> - signature: str<br/> - public_key: str<br/>---<br/>object: <br/> - type: str<br/> - public_keys: List of str<br/> - signatures: List of str<br/> - threshold: float<br/> - bitmap: str<br/>---<br/>object: <br/> - type: str<br/> - sender: One of:<br/>object: <br/> - type: str<br/> - signature: str<br/> - public_key: str<br/>---<br/>object: <br/> - type: str<br/> - public_keys: List of str<br/> - signatures: List of str<br/> - threshold: float<br/> - bitmap: str<br/>---<br/><br/> - secondary_signer_addresses: List of str<br/> - secondary_signers: One of:<br/>object: <br/> - type: str<br/> - signature: str<br/> - public_key: str<br/>---<br/>object: <br/> - type: str<br/> - public_keys: List of str<br/> - signatures: List of str<br/> - threshold: float<br/> - bitmap: str<br/>---<br/><br/>---<br/> |  | Yes |  | {} |




