# transactions API:

> `aptos_api.transactions`

- [estimate_gas_price](#estimate_gas_price)


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




