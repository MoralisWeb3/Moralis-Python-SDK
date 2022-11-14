# challenge API:

> `Moralis.auth.challenge`

- [request_challenge_evm](#request_challenge_evm)
- [request_challenge_solana](#request_challenge_solana)
- [verify_challenge_evm](#verify_challenge_evm)
- [verify_challenge_solana](#verify_challenge_solana)


---
## request_challenge_evm

> `Moralis.auth.challenge.request_challenge_evm()`

Request EVM challenge

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "domain": "defi.finance", 
    "chainId": "1", 
    "address": "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B", 
    "statement": "Please confirm", 
    "uri": "https://defi.finance/", 
    "expirationTime": "2020-01-01T00:00:00.000Z", 
    "notBefore": "2020-01-01T00:00:00.000Z", 
    "resources": ['https://docs.moralis.io/'], 
    "timeout": 15, 
}

result = auth.challenge.request_challenge_evm(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| domain | str | RFC 4501 dns authority that is requesting the signing. | Yes |  | "defi.finance" |
| chainId | enum[str]: <br/>- "1"<br/>- "5"<br/>- "25"<br/>- "56"<br/>- "97"<br/>- "137"<br/>- "250"<br/>- "338"<br/>- "1337"<br/>- "43113"<br/>- "43114"<br/>- "80001"<br/>- "11155111" | EIP-155 Chain ID to which the session is bound, and the network where Contract Accounts must be resolved. | Yes |  | "1" |
| address | str | Ethereum address performing the signing conformant to capitalization encoded checksum specified in EIP-55 where applicable. | Yes |  | "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B" |
| statement | str | Human-readable ASCII assertion that the user will sign, and it must not contain `<br/>`. | Yes |  | "Please confirm" |
| uri | str | RFC 3986 URI referring to the resource that is the subject of the signing (as in the __subject__ of a claim). | Yes |  | "https://defi.finance/" |
| expirationTime | str | ISO 8601 datetime string that, if present, indicates when the signed authentication message is no longer valid. | Yes |  | "2020-01-01T00:00:00.000Z" |
| notBefore | str | ISO 8601 datetime string that, if present, indicates when the signed authentication message will become valid. | Yes |  | "2020-01-01T00:00:00.000Z" |
| resources | List of str | List of information or references to information the user wishes to have resolved as part of authentication by the relying party. They are expressed as RFC 3986 URIs separated by `<br/>- `. | Yes |  | ['https://docs.moralis.io/'] |
| timeout | float | Time in seconds before the challenge is expired | Yes | 15 | 15 |


---
## request_challenge_solana

> `Moralis.auth.challenge.request_challenge_solana()`

Request Solana challenge

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "domain": "defi.finance", 
    "network": "mainnet", 
    "address": "26qv4GCcx98RihuK3c4T6ozB3J7L6VwCuFVc7Ta2A3Uo", 
    "statement": "Please confirm", 
    "uri": "https://defi.finance/", 
    "expirationTime": "2020-01-01T00:00:00.000Z", 
    "notBefore": "2020-01-01T00:00:00.000Z", 
    "resources": ['https://docs.moralis.io/'], 
    "timeout": 15, 
}

result = auth.challenge.request_challenge_solana(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| domain | str | RFC 4501 dns authority that is requesting the signing. | Yes |  | "defi.finance" |
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet"<br/>- "devnet" | The network where Contract Accounts must be resolved. | Yes |  | "mainnet" |
| address | str | Solana public key with a length of 32 - 44 characters that is used to perform the signing | Yes |  | "26qv4GCcx98RihuK3c4T6ozB3J7L6VwCuFVc7Ta2A3Uo" |
| statement | str | Human-readable ASCII assertion that the user will sign, and it must not contain `<br/>`. | Yes |  | "Please confirm" |
| uri | str | RFC 3986 URI referring to the resource that is the subject of the signing (as in the __subject__ of a claim). | Yes |  | "https://defi.finance/" |
| expirationTime | str | ISO 8601 datetime string that, if present, indicates when the signed authentication message is no longer valid. | Yes |  | "2020-01-01T00:00:00.000Z" |
| notBefore | str | ISO 8601 datetime string that, if present, indicates when the signed authentication message will become valid. | Yes |  | "2020-01-01T00:00:00.000Z" |
| resources | List of str | List of information or references to information the user wishes to have resolved as part of authentication by the relying party. They are expressed as RFC 3986 URIs separated by `<br/>- `. | Yes |  | ['https://docs.moralis.io/'] |
| timeout | float | Time in seconds before the challenge is expired | Yes | 15 | 15 |


---
## verify_challenge_evm

> `Moralis.auth.challenge.verify_challenge_evm()`

Verify EVM challenge

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "message": "", 
    "signature": "0x1234567890abcdef0123456789abcdef1234567890abcdef", 
}

result = auth.challenge.verify_challenge_evm(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| message | str | - | Yes |  | "" |
| signature | str | - | Yes |  | "0x1234567890abcdef0123456789abcdef1234567890abcdef" |


---
## verify_challenge_solana

> `Moralis.auth.challenge.verify_challenge_solana()`

Verify Solana challenge

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "message": "defi.finance wants you to sign in with your Solana account:
26qv4GCcx98RihuK3c4T6ozB3J7L6VwCuFVc7Ta2A3Uo

I am a third party API

URI: http://defi.finance
Version: 1
Network: mainnet
Nonce: PYxxb9msdjVXsMQ9x
Issued At: 2022-08-25T11:02:34.097Z
Expiration Time: 2022-08-25T11:12:38.243Z
Resources:
- https://docs.moralis.io/", 
    "signature": "2pH9DqD5rve2qV4yBDshcAjWd2y8TqMx8BPb7f3KoNnuLEhE5JwjruYi4jaFaD4HN6wriLz2Vdr32kRBAJmHcyny", 
}

result = auth.challenge.verify_challenge_solana(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| message | str | Message that needs to be signed by the end user | Yes |  | "defi.finance wants you to sign in with your Solana account:
26qv4GCcx98RihuK3c4T6ozB3J7L6VwCuFVc7Ta2A3Uo

I am a third party API

URI: http://defi.finance
Version: 1
Network: mainnet
Nonce: PYxxb9msdjVXsMQ9x
Issued At: 2022-08-25T11:02:34.097Z
Expiration Time: 2022-08-25T11:12:38.243Z
Resources:
- https://docs.moralis.io/" |
| signature | str | Base58 signature that needs to be used to verify end user | Yes |  | "2pH9DqD5rve2qV4yBDshcAjWd2y8TqMx8BPb7f3KoNnuLEhE5JwjruYi4jaFaD4HN6wriLz2Vdr32kRBAJmHcyny" |




