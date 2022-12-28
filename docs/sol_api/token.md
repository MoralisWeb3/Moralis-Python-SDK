# token API:

> `sol_api.token`

- [get_token_price](#get_token_price)


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





