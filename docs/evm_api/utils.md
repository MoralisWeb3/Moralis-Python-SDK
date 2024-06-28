# utils API:

> `evm_api.utils`

- [endpoint_weights](#endpoint_weights)
- [review_contracts](#review_contracts)
- [run_contract_function](#run_contract_function)
- [web3_api_version](#web3_api_version)


---
## endpoint_weights

> `evm_api.utils.endpoint_weights()`

Get the cost and rate limit for each API endpoint.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"

result = evm_api.utils.endpoint_weights(
    api_key=api_key,
)

print(result)

```


---
## review_contracts

> `evm_api.utils.review_contracts()`

Review contracts as spam or not spam


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "chain": "eth", 
}
body = {
    "contracts": [{'contract_address': '0xa4991609c508b6d4fb7156426db0bd49fe298bd8', 'report_type': 'spam', 'contract_type': 'ERC20', 'reason': 'The contract contains shady code'}], 
}

result = evm_api.utils.review_contracts(
    api_key=api_key,
    params=params,
    body=body,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |


### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| contracts | List of object: <br/> - contract_address: str<br/> - reason: str<br/> - report_type: enum[str]: <br/>- "spam"<br/>- "not_spam"<br/> - contract_type: enum[str]: <br/>- "ERC20"<br/>- "NFT" | The contracts to be reported | Yes |  | [{'contract_address': '0xa4991609c508b6d4fb7156426db0bd49fe298bd8', 'report_type': 'spam', 'contract_type': 'ERC20', 'reason': 'The contract contains shady code'}] |


---
## run_contract_function

> `evm_api.utils.run_contract_function()`

Run a given function of a contract ABI and retrieve readonly data. [Try it with Swagger](https://deep-index.moralis.io/api-docs-2.1/#/Utils/runContractFunction).


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "function_name": "", 
    "chain": "eth", 
}
body = {
    "abi": [], 
    "params": {}, 
}

result = evm_api.utils.run_contract_function(
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
| function_name | str | The function name of the contract | Yes |  | "" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |


### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| abi | List of object | The contract ABI | Yes |  | [] |
| params | object | The params for the given function | Yes |  | {} |


---
## web3_api_version

> `evm_api.utils.web3_api_version()`

Get the current version of the Moralis Web3 API.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"

result = evm_api.utils.web3_api_version(
    api_key=api_key,
)

print(result)

```




