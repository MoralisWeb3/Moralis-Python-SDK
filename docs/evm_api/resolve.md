# resolve API: 

> `Moralis.evm_api.resolve`

- [resolve_domain](#resolve_domain)
- [resolve_address](#resolve_address)


---
## `resolve_domain()`
Resolve an Unstoppable domain and get the address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "domain": "brad.crypto", 
    "currency": "eth", 
}

result = evm_api.resolve.resolve_domain(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| domain | str | The domain to be resolved | Yes |  | "brad.crypto" |
| currency | enum[str]: <br/>- "eth"<br/>- "0x1" | The currency to query |  | "eth" | "eth" |



---
## `resolve_address()`
Resolve an ETH address and find the ENS name.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045", 
}

result = evm_api.resolve.resolve_address(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address to be resolved | Yes |  | "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045" |





