# account API:

> `sol_api.account`

- [balance](#balance)
- [get_nfts](#get_nfts)
- [get_portfolio](#get_portfolio)
- [get_spl](#get_spl)


---
## balance

> `sol_api.account.balance()`

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
| network | enum[str]: <br/>- "mainnet"<br/>- "devnet" | The network to query | Yes | "mainnet" | "" |
| address | str | The address for which the native balance will be checked | Yes |  | "" |



---
## get_nfts

> `sol_api.account.get_nfts()`

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
| network | enum[str]: <br/>- "mainnet"<br/>- "devnet" | The network to query | Yes | "mainnet" | "" |
| address | str | The address of the contract | Yes |  | "" |



---
## get_portfolio

> `sol_api.account.get_portfolio()`

Gets the portfolio for a given network and address.


### Example
```python
from moralis import sol_api

api_key = "YOUR_API_KEY"
params = {
    "network": "", 
    "address": "", 
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
| network | enum[str]: <br/>- "mainnet"<br/>- "devnet" | The network to query | Yes | "mainnet" | "" |
| address | str | The wallet address | Yes |  | "" |



---
## get_spl

> `sol_api.account.get_spl()`

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
| network | enum[str]: <br/>- "mainnet"<br/>- "devnet" | The network to query | Yes | "mainnet" | "" |
| address | str | The address for which token balances will be checked | Yes |  | "" |





