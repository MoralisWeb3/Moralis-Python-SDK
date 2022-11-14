# evm_api: defi

- [get_pair_address](#get_pair_address)
- [get_pair_reserves](#get_pair_reserves)


---
## `get_pair_address()`
Fetch the pair data of the provided token0+token1 combination.
The token0 and token1 options are interchangable (ie. there is no different outcome in "token0=WETH and token1=USDT" or "token0=USDT and token1=WETH")



### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "exchange": "uniswapv2", 
    "token0_address": "0x2b591e99afe9f32eaa6214f7b7629768c40eeb39", 
    "token1_address": "0xdac17f958d2ee523a2206206994597c13d831ec7", 
    "chain": "eth", 
    "to_block": "", 
    "to_date": "", 
}

result = evm_api.defi.get_pair_address(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| exchange | enum[str]: <br/>- "uniswapv2"<br/>- "uniswapv3"<br/>- "sushiswapv2"<br/>- "pancakeswapv2"<br/>- "pancakeswapv1"<br/>- "quickswap" | The factory name or address of the token exchange | Yes |  | "uniswapv2" |
| token0_address | str | The token0 address | Yes |  | "0x2b591e99afe9f32eaa6214f7b7629768c40eeb39" |
| token1_address | str | The token1 address | Yes |  | "0xdac17f958d2ee523a2206206994597c13d831ec7" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| to_block | str | The block number to get the reserves from |  |  | "" |
| to_date | str | Get the reserves up to this date (any format that is accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |



---
## `get_pair_reserves()`
Get the liquidity reserves for a given pair address. Only Uniswap V2 based exchanges supported at the moment.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "pair_address": "0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974", 
    "chain": "eth", 
    "to_block": "", 
    "to_date": "", 
    "provider_url": "", 
}

result = evm_api.defi.get_pair_reserves(
    api_key=api_key,
    params=params,
)

print(result)
```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| pair_address | str | The liquidity pair address | Yes |  | "0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "goerli"<br/>- "0x5"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "mumbai"<br/>- "0x13881"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "avalanche testnet"<br/>- "0xa869"<br/>- "fantom"<br/>- "0xfa"<br/>- "cronos"<br/>- "0x19"<br/>- "cronos testnet"<br/>- "0x152" | The chain to query |  | "eth" | "eth" |
| to_block | str | The block number to get the reserves from |  |  | "" |
| to_date | str | Get the reserves up to this date (any format that is accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| provider_url | str | The web3 provider URL to use when using local dev chain |  |  | "" |





