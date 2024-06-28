# resolve API:

> `evm_api.resolve`

- [resolve_address](#resolve_address)
- [resolve_address_to_domain](#resolve_address_to_domain)
- [resolve_domain](#resolve_domain)
- [resolve_ens_domain](#resolve_ens_domain)


---
## resolve_address

> `evm_api.resolve.resolve_address()`

Reverse resolve a given ETH address to its ENS domain.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0xd8da6bf26964af9d7eed9e03e53415d37aa96045", 
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
| address | str | The address to be resolved | Yes |  | "0xd8da6bf26964af9d7eed9e03e53415d37aa96045" |



---
## resolve_address_to_domain

> `evm_api.resolve.resolve_address_to_domain()`

Resolve a specific address to its Unstoppable domain


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x94ef5300cbc0aa600a821ccbc561b057e456ab23", 
    "currency": "eth", 
}

result = evm_api.resolve.resolve_address_to_domain(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | The address to be resolved | Yes |  | "0x94ef5300cbc0aa600a821ccbc561b057e456ab23" |
| currency | enum[str]: <br/>- "eth"<br/>- "0x1" | The currency to query |  | "eth" | "eth" |



---
## resolve_domain

> `evm_api.resolve.resolve_domain()`

Resolve a specific Unstoppable domain to its address.


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
## resolve_ens_domain

> `evm_api.resolve.resolve_ens_domain()`

Resolve a specific ENS domain to its address.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "domain": "vitalik.eth", 
}

result = evm_api.resolve.resolve_ens_domain(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| domain | str | The domain to be resolved | Yes |  | "vitalik.eth" |





