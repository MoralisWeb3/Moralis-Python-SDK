# defi API:

> `evm_api.defi`

- [get_pair_address](#get_pair_address)
- [get_pair_price](#get_pair_price)
- [get_pair_reserves](#get_pair_reserves)


---
## get_pair_address

> `evm_api.defi.get_pair_address()`

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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| to_block | str | The block number to get the reserves from |  |  | "" |
| to_date | str | Get the reserves up to this date (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |



---
## get_pair_price

> `evm_api.defi.get_pair_price()`

Get the price of a given token pair. Only Uniswap V2 based exchanges supported at the moment.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "token0_address": "0xae7ab96520de3a18e5e111b5eaab095312d7fe84", 
    "token1_address": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", 
    "chain": "eth", 
    "to_block": "", 
    "to_date": "", 
    "exchange": "", 
}

result = evm_api.defi.get_pair_price(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| token0_address | str | The token0 address | Yes |  | "0xae7ab96520de3a18e5e111b5eaab095312d7fe84" |
| token1_address | str | The token1 address | Yes |  | "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2" |
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| to_block | str | The block number to get the reserves from |  |  | "" |
| to_date | str | Get the price up to this date (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |
| exchange | str | The factory name or address of the token exchange |  |  | "" |



---
## get_pair_reserves

> `evm_api.defi.get_pair_reserves()`

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
| chain | enum[str]: <br/>- "eth"<br/>- "0x1"<br/>- "sepolia"<br/>- "0xaa36a7"<br/>- "polygon"<br/>- "0x89"<br/>- "bsc"<br/>- "0x38"<br/>- "bsc testnet"<br/>- "0x61"<br/>- "avalanche"<br/>- "0xa86a"<br/>- "fantom"<br/>- "0xfa"<br/>- "palm"<br/>- "0x2a15c308d"<br/>- "cronos"<br/>- "0x19"<br/>- "arbitrum"<br/>- "0xa4b1"<br/>- "chiliz"<br/>- "0x15b38"<br/>- "chiliz testnet"<br/>- "0x15b32"<br/>- "gnosis"<br/>- "0x64"<br/>- "gnosis testnet"<br/>- "0x27d8"<br/>- "base"<br/>- "0x2105"<br/>- "base sepolia"<br/>- "0x14a34"<br/>- "optimism"<br/>- "0xa"<br/>- "holesky"<br/>- "0x4268"<br/>- "polygon amoy"<br/>- "0x13882"<br/>- "linea"<br/>- "0xe708"<br/>- "moonbeam"<br/>- "0x504"<br/>- "moonriver"<br/>- "0x505"<br/>- "moonbase"<br/>- "0x507"<br/>- "linea sepolia"<br/>- "0xe705" | The chain to query |  | "eth" | "eth" |
| to_block | str | The block number to get the reserves from |  |  | "" |
| to_date | str | Get the reserves up to this date (format in seconds or datestring accepted by momentjs)<br/>* Provide the param 'to_block' or 'to_date'<br/>* If 'to_date' and 'to_block' are provided, 'to_block' will be used.<br/> |  |  | "" |





