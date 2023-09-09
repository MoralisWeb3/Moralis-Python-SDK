# transaction API:

> `evm_api.transaction`

- [get_internal_transactions](#get_internal_transactions)
- [get_transaction](#get_transaction)
- [get_transaction_verbose](#get_transaction_verbose)
- [get_wallet_transactions](#get_wallet_transactions)
- [get_wallet_transactions_verbose](#get_wallet_transactions_verbose)


---
## get_internal_transactions

> `evm_api.transaction.get_internal_transactions()`

Get the contents of a internal transaction by transaction hash.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "transaction_hash": "0xdc85cb1b75fd09c2f6d001fea4aba83764193cbd7881a1fa8ccde350a5681109", 
    "chain": "eth", 
}

result = evm_api.transaction.get_internal_transactions(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| transaction_hash | str | The transaction hash | Yes |  | "0xdc85cb1b75fd09c2f6d001fea4aba83764193cbd7881a1fa8ccde350a5681109" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |



---
## get_transaction

> `evm_api.transaction.get_transaction()`

Get the contents of a transaction by the given transaction hash.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "transaction_hash": "0xdc85cb1b75fd09c2f6d001fea4aba83764193cbd7881a1fa8ccde350a5681109", 
    "chain": "eth", 
    "include": "", 
}

result = evm_api.transaction.get_transaction(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| transaction_hash | str | The transaction hash | Yes |  | "0xdc85cb1b75fd09c2f6d001fea4aba83764193cbd7881a1fa8ccde350a5681109" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| include | enum[str]: <br/>- "internal_transactions" | If the result should contain the internal transactions. |  | "" | "" |



---
## get_transaction_verbose

> `evm_api.transaction.get_transaction_verbose()`

Get the contents of a transaction by the given transaction hash.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "transaction_hash": "0xdc85cb1b75fd09c2f6d001fea4aba83764193cbd7881a1fa8ccde350a5681109", 
    "chain": "eth", 
    "include": "", 
}

result = evm_api.transaction.get_transaction_verbose(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| transaction_hash | str | The transaction hash | Yes |  | "0xdc85cb1b75fd09c2f6d001fea4aba83764193cbd7881a1fa8ccde350a5681109" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| include | enum[str]: <br/>- "internal_transactions" | If the result should contain the internal transactions. |  | "" | "" |



---
## get_wallet_transactions

> `evm_api.transaction.get_wallet_transactions()`

Get native transactions ordered by block number in descending order.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xd8da6bf26964af9d7eed9e03e53415d37aa96045", 
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "from_date": "", 
    "to_date": "", 
    "cursor": "", 
    "limit": 0, 
    "include": "", 
}

result = evm_api.transaction.get_wallet_transactions(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the wallet | Yes |  | "0xd8da6bf26964af9d7eed9e03e53415d37aa96045" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the transactions<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from which to get the transactions.<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The start date from which to get the transactions (any format that is accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | Get the transactions up to this date (any format that is accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |
| include | enum[str]: <br/>- "internal_transactions" | If the result should contain the internal transactions. |  | "" | "" |



---
## get_wallet_transactions_verbose

> `evm_api.transaction.get_wallet_transactions_verbose()`

Get native transactions and logs ordered by block number in descending order.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xd8da6bf26964af9d7eed9e03e53415d37aa96045", 
    "chain": "eth", 
    "from_block": 0, 
    "to_block": 0, 
    "from_date": "", 
    "to_date": "", 
    "include": "", 
    "cursor": "", 
    "limit": 0, 
}

result = evm_api.transaction.get_wallet_transactions_verbose(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address of the wallet | Yes |  | "0xd8da6bf26964af9d7eed9e03e53415d37aa96045" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| from_block | int | The minimum block number from which to get the transactions<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | 0 |
| to_block | int | The maximum block number from which to get the transactions.<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | 0 |
| from_date | str | The start date from which to get the transactions (any format that is accepted by momentjs)<br/>* Provide the param 'from_block' or 'from_date'<br/>* If 'from_date' and 'from_block' are provided, 'from_block' will be used.<br/> |  |  | "" |
| to_date | str | Get the transactions up to this date (any format that is accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| include | enum[str]: <br/>- "internal_transactions" | If the result should contain the internal transactions. |  | "" | "" |
| cursor | str | The cursor returned in the previous response (used for getting the next page). |  |  | "" |
| limit | int | The desired page size of the result. |  |  | 0 |





