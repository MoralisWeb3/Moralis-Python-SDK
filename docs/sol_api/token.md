# token API:

> `sol_api.token`

- [get_token_metadata](#get_token_metadata)
- [get_token_price](#get_token_price)


---
## get_token_metadata

> `sol_api.token.get_token_metadata()`

Get the global token metadata for a given network and contract (mint, standard, name, symbol, metaplex).


### Example
```python
from moralis import sol_api

api_key = "YOUR_API_KEY"
params = {
    "network": "", 
    "address": "", 
}

result = sol_api.token.get_token_metadata(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "devnet" | The network to query | Yes | "mainnet" | "" |
| address | str | The address of the contract | Yes |  | "" |



---
## get_token_price

> `sol_api.token.get_token_price()`

Gets the token price (usd and native) for a given contract address and network.


### Example
```python
from moralis import sol_api

api_key = "YOUR_API_KEY"
params = {
    "network": "", 
    "address": "", 
}

result = sol_api.token.get_token_price(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet" | The network to query | Yes | "mainnet" | "" |
| address | str | The address of the token contract | Yes |  | "" |





