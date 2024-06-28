# challenge API:

> `auth.challenge`

- [request_challenge_aptos](#request_challenge_aptos)
- [request_challenge_evm](#request_challenge_evm)
- [request_challenge_solana](#request_challenge_solana)
- [verify_challenge_aptos](#verify_challenge_aptos)
- [verify_challenge_evm](#verify_challenge_evm)
- [verify_challenge_solana](#verify_challenge_solana)


---
## request_challenge_aptos

> `auth.challenge.request_challenge_aptos()`

Request Aptos challenge

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "domain": "defi.finance", 
    "statement": "Please confirm", 
    "uri": "https://defi.finance/", 
    "expirationTime": "2020-01-01T00:00:00.000Z", 
    "notBefore": "2020-01-01T00:00:00.000Z", 
    "resources": ['https://docs.moralis.io/'], 
    "timeout": 15, 
    "network": "mainnet", 
    "address": "0xfb2853744bb8afd58d9386d1856afd8e08de135019961dfa3a10d8c9bf83b99d", 
    "publicKey": "0xfb2853744bb8afd58d9386d1856afd8e08de135019961dfa3a10d8c9bf83b99d", 
}

result = auth.challenge.request_challenge_aptos(
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
| statement | str | Human-readable ASCII assertion that the user will sign, and it must not contain `<br/>`. | Yes |  | "Please confirm" |
| uri | str | RFC 3986 URI referring to the resource that is the subject of the signing (as in the __subject__ of a claim). | Yes |  | "https://defi.finance/" |
| expirationTime | str | ISO 8601 datetime string that, if present, indicates when the signed authentication message is no longer valid. | Yes |  | "2020-01-01T00:00:00.000Z" |
| notBefore | str | ISO 8601 datetime string that, if present, indicates when the signed authentication message will become valid. | Yes |  | "2020-01-01T00:00:00.000Z" |
| resources | List of str | List of information or references to information the user wishes to have resolved as part of authentication by the relying party. They are expressed as RFC 3986 URIs separated by new lines. | Yes |  | ['https://docs.moralis.io/'] |
| timeout | float | Time in seconds before the challenge is expired | Yes | 15 | 15 |
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet" | The network where Contract Accounts must be resolved. | Yes |  | "mainnet" |
| address | str | Aptos address performing the signing conformant. | Yes |  | "0xfb2853744bb8afd58d9386d1856afd8e08de135019961dfa3a10d8c9bf83b99d" |
| publicKey | str | Aptos public key performing the signing conformant. | Yes |  | "0xfb2853744bb8afd58d9386d1856afd8e08de135019961dfa3a10d8c9bf83b99d" |


---
## request_challenge_evm

> `auth.challenge.request_challenge_evm()`

Request EVM challenge

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "domain": "defi.finance", 
    "statement": "Please confirm", 
    "uri": "https://defi.finance/", 
    "expirationTime": "2020-01-01T00:00:00.000Z", 
    "notBefore": "2020-01-01T00:00:00.000Z", 
    "resources": ['https://docs.moralis.io/'], 
    "timeout": 15, 
    "chainId": "1", 
    "address": "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B", 
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
| statement | str | Human-readable ASCII assertion that the user will sign, and it must not contain `<br/>`. | Yes |  | "Please confirm" |
| uri | str | RFC 3986 URI referring to the resource that is the subject of the signing (as in the __subject__ of a claim). | Yes |  | "https://defi.finance/" |
| expirationTime | str | ISO 8601 datetime string that, if present, indicates when the signed authentication message is no longer valid. | Yes |  | "2020-01-01T00:00:00.000Z" |
| notBefore | str | ISO 8601 datetime string that, if present, indicates when the signed authentication message will become valid. | Yes |  | "2020-01-01T00:00:00.000Z" |
| resources | List of str | List of information or references to information the user wishes to have resolved as part of authentication by the relying party. They are expressed as RFC 3986 URIs separated by new lines. | Yes |  | ['https://docs.moralis.io/'] |
| timeout | float | Time in seconds before the challenge is expired | Yes | 15 | 15 |
| chainId | enum[str]: <br/>- "1"<br/>- "5"<br/>- "10"<br/>- "25"<br/>- "56"<br/>- "97"<br/>- "100"<br/>- "137"<br/>- "250"<br/>- "338"<br/>- "420"<br/>- "1284"<br/>- "1285"<br/>- "1287"<br/>- "1337"<br/>- "8453"<br/>- "10200"<br/>- "43113"<br/>- "43114"<br/>- "80001"<br/>- "80002"<br/>- "84531"<br/>- "88882"<br/>- "88888"<br/>- "11155111" | EIP-155 Chain ID to which the session is bound, and the network where Contract Accounts must be resolved. | Yes |  | "1" |
| address | str | Ethereum address performing the signing conformant to capitalization encoded checksum specified in EIP-55 where applicable. | Yes |  | "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B" |


---
## request_challenge_solana

> `auth.challenge.request_challenge_solana()`

Request Solana challenge

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "domain": "defi.finance", 
    "statement": "Please confirm", 
    "uri": "https://defi.finance/", 
    "expirationTime": "2020-01-01T00:00:00.000Z", 
    "notBefore": "2020-01-01T00:00:00.000Z", 
    "resources": ['https://docs.moralis.io/'], 
    "timeout": 15, 
    "network": "mainnet", 
    "address": "26qv4GCcx98RihuK3c4T6ozB3J7L6VwCuFVc7Ta2A3Uo", 
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
| statement | str | Human-readable ASCII assertion that the user will sign, and it must not contain `<br/>`. | Yes |  | "Please confirm" |
| uri | str | RFC 3986 URI referring to the resource that is the subject of the signing (as in the __subject__ of a claim). | Yes |  | "https://defi.finance/" |
| expirationTime | str | ISO 8601 datetime string that, if present, indicates when the signed authentication message is no longer valid. | Yes |  | "2020-01-01T00:00:00.000Z" |
| notBefore | str | ISO 8601 datetime string that, if present, indicates when the signed authentication message will become valid. | Yes |  | "2020-01-01T00:00:00.000Z" |
| resources | List of str | List of information or references to information the user wishes to have resolved as part of authentication by the relying party. They are expressed as RFC 3986 URIs separated by new lines. | Yes |  | ['https://docs.moralis.io/'] |
| timeout | float | Time in seconds before the challenge is expired | Yes | 15 | 15 |
| network | enum[str]: <br/>- "mainnet"<br/>- "testnet"<br/>- "devnet" | The network where Contract Accounts must be resolved. | Yes |  | "mainnet" |
| address | str | Solana address with a length of 32 - 44 characters that is used to perform the signing | Yes |  | "26qv4GCcx98RihuK3c4T6ozB3J7L6VwCuFVc7Ta2A3Uo" |


---
## verify_challenge_aptos

> `auth.challenge.verify_challenge_aptos()`

Verify Aptos challenge

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "message": "defi.finance wants you to sign in with your Aptos account:<br/>0xfb2853744bb8afd58d9386d1856afd8e08de135019961dfa3a10d8c9bf83b99d<br/><br/><br/>URI: https://defi.finance<br/>Version: 1<br/>Chain ID: 1<br/>Nonce: Px7Nh1RPzlCLwqgOb<br/>Issued At: 2022-11-30T10:20:00.262Z", 
    "signature": "0xa8f89a58bf9b433d3100f9e41ee35b5e31fb8c7cd62547acb113162ec6f2e4140207e2dfbd4e387e1801ebc7f08a9dd105ac1d22b2e2ff0df5fa8b6d9bdcfe491c", 
}

result = auth.challenge.verify_challenge_aptos(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| message | str | Message that needs to be signed by the end user. | Yes |  | "defi.finance wants you to sign in with your Aptos account:<br/>0xfb2853744bb8afd58d9386d1856afd8e08de135019961dfa3a10d8c9bf83b99d<br/><br/><br/>URI: https://defi.finance<br/>Version: 1<br/>Chain ID: 1<br/>Nonce: Px7Nh1RPzlCLwqgOb<br/>Issued At: 2022-11-30T10:20:00.262Z" |
| signature | str | EIP-191 compliant signature signed by the Aptos account address requesting authentication. | Yes |  | "0xa8f89a58bf9b433d3100f9e41ee35b5e31fb8c7cd62547acb113162ec6f2e4140207e2dfbd4e387e1801ebc7f08a9dd105ac1d22b2e2ff0df5fa8b6d9bdcfe491c" |


---
## verify_challenge_evm

> `auth.challenge.verify_challenge_evm()`

Verify EVM challenge

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "message": "defi.finance wants you to sign in with your Ethereum account:<br/>0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B<br/><br/><br/>URI: https://defi.finance<br/>Version: 1<br/>Chain ID: 1<br/>Nonce: Px7Nh1RPzlCLwqgOb<br/>Issued At: 2022-11-30T10:20:00.262Z", 
    "signature": "0xa8f89a58bf9b433d3100f9e41ee35b5e31fb8c7cd62547acb113162ec6f2e4140207e2dfbd4e387e1801ebc7f08a9dd105ac1d22b2e2ff0df5fa8b6d9bdcfe491c", 
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
| message | str | Message that needs to be signed by the end user. | Yes |  | "defi.finance wants you to sign in with your Ethereum account:<br/>0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B<br/><br/><br/>URI: https://defi.finance<br/>Version: 1<br/>Chain ID: 1<br/>Nonce: Px7Nh1RPzlCLwqgOb<br/>Issued At: 2022-11-30T10:20:00.262Z" |
| signature | str | EIP-191 compliant signature signed by the Ethereum account address requesting authentication. | Yes |  | "0xa8f89a58bf9b433d3100f9e41ee35b5e31fb8c7cd62547acb113162ec6f2e4140207e2dfbd4e387e1801ebc7f08a9dd105ac1d22b2e2ff0df5fa8b6d9bdcfe491c" |


---
## verify_challenge_solana

> `auth.challenge.verify_challenge_solana()`

Verify Solana challenge

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "message": "defi.finance wants you to sign in with your Solana account:<br/>26qv4GCcx98RihuK3c4T6ozB3J7L6VwCuFVc7Ta2A3Uo<br/><br/>I am a third party API<br/><br/>URI: http://defi.finance<br/>Version: 1<br/>Network: mainnet<br/>Nonce: PYxxb9msdjVXsMQ9x<br/>Issued At: 2022-08-25T11:02:34.097Z<br/>Expiration Time: 2022-08-25T11:12:38.243Z<br/>Resources:<br/>- https://docs.moralis.io/", 
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
| message | str | Message that needs to be signed by the end user | Yes |  | "defi.finance wants you to sign in with your Solana account:<br/>26qv4GCcx98RihuK3c4T6ozB3J7L6VwCuFVc7Ta2A3Uo<br/><br/>I am a third party API<br/><br/>URI: http://defi.finance<br/>Version: 1<br/>Network: mainnet<br/>Nonce: PYxxb9msdjVXsMQ9x<br/>Issued At: 2022-08-25T11:02:34.097Z<br/>Expiration Time: 2022-08-25T11:12:38.243Z<br/>Resources:<br/>- https://docs.moralis.io/" |
| signature | str | Base58 signature that needs to be used to verify end user | Yes |  | "2pH9DqD5rve2qV4yBDshcAjWd2y8TqMx8BPb7f3KoNnuLEhE5JwjruYi4jaFaD4HN6wriLz2Vdr32kRBAJmHcyny" |




