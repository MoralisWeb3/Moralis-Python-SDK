# sol_api: nft

- [get_nft_metadata](#get_nft_metadata)


---
## `get_nft_metadata()`
Get the global NFT metadata for a given network and contract (mint, standard, name, symbol, metaplex).


### Example
```python
from moralis import sol_api

api_key = "YOUR_API_KEY"
params = {
    "address": "", 
    "network": "", 
}

result = sol_api.nft.get_nft_metadata(
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





