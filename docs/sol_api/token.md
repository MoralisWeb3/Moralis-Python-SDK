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
    "address": "", 
    "network": "", 
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
| address | str |  | Yes |  | "" |
| network | enum[str]: <br/>- "mainnet" |  | Yes |  | "" |





