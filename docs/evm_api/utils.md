# utils API:

> `evm_api.utils`

- [endpoint_weights](#endpoint_weights)
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
    "subdomain": "", 
    "providerUrl": "", 
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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152"<br/>- "arbitrum"<br/>- "0xa4b1" | The chain to query |  | "eth" | "eth" |
| subdomain | str | The subdomain of the Moralis server to use (only use when selecting local devchain as chain) |  |  | "" |
| providerUrl | str | The web3 provider URL to use when using local dev chain |  |  | "" |


### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| abi | object | The contract ABI | Yes |  | [] |
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




