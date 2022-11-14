# account API: 

> `Moralis.sol_api.account`

- [get_portfolio](#get_portfolio)
- [get_nfts](#get_nfts)
- [get_spl](#get_spl)
- [balance](#balance)


---
## `get_portfolio()`
Gets the portfolio for a given network and address.


### Example
```python
from moralis import sol_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "network": "", 
}

result = sol_api.account.get_portfolio(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| address | str | - | Yes |  | "" |
| network | enum[str]: <br/>- "mainnet"<br/>- "devnet" | - | Yes |  | "" |



---
## `get_nfts()`
Gets NFTs owned by a given network and address.


### Example
```python
from moralis import sol_api

api_key = "YOUR_API_KEY"
params = {
    "network": "", 
    "address": "", 
}

result = sol_api.account.get_nfts(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "devnet" | - | Yes |  | "" |
| address | str | - | Yes |  | "" |



---
## `get_spl()`
Gets the token balances owned by a given network and address.


### Example
```python
from moralis import sol_api

api_key = "YOUR_API_KEY"
params = {
    "network": "", 
    "address": "", 
}

result = sol_api.account.get_spl(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "devnet" | - | Yes |  | "" |
| address | str | - | Yes |  | "" |



---
## `balance()`
Gets the native balance owned by a given network and address.


### Example
```python
from moralis import sol_api

api_key = "YOUR_API_KEY"
params = {
    "network": "", 
    "address": "", 
}

result = sol_api.account.balance(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| network | enum[str]: <br/>- "mainnet"<br/>- "devnet" | - | Yes |  | "" |
| address | str | - | Yes |  | "" |





