# bind API:

> `auth.bind`

- [remove_bind](#remove_bind)
- [request_bind](#request_bind)
- [verify_remove_bind](#verify_remove_bind)
- [verify_request_bind](#verify_request_bind)


---
## remove_bind

> `auth.bind.remove_bind()`

Request to remove bind of an address from a profile

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "blockchainType": "evm", 
    "address": "0x57af6B90c2237d2F888bf4CAe56f25FE1b14e531", 
    "profileId": "0xbfbcfab169c67072ff418133124480fea02175f1402aaa497daa4fd09026b0e1", 
}

result = auth.bind.remove_bind(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| blockchainType | enum[str]: <br/>- "evm"<br/>- "solana" | The chain in which the address belongs to | Yes |  | "evm" |
| address | str | Unique identifier with a length of 66 characters | Yes |  | "0x57af6B90c2237d2F888bf4CAe56f25FE1b14e531" |
| profileId | str | Unique identifier with a length of 66 characters | Yes |  | "0xbfbcfab169c67072ff418133124480fea02175f1402aaa497daa4fd09026b0e1" |


---
## request_bind

> `auth.bind.request_bind()`

Request for message to bind profile that is belong to the two addresses<br>
        All profiles under the addresses will be bound and new profile will be generated.


### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "addresses": [], 
}

result = auth.bind.request_bind(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| addresses | List of object: <br/> - blockchainType: enum[str]: <br/>- "evm"<br/>- "solana"<br/> - address: str | An array of addresses that needs to be bind | Yes |  | [] |


---
## verify_remove_bind

> `auth.bind.verify_remove_bind()`

Verify remove bind request

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "message": "Please sign this message to unbind:<br/>Address: 0x6ed338bcB610640e81465FCfb9894DDfA354Cc91<br/>from<br/>Profile Id:<br/>- 0x0b2bbac1251651c0cbbdbbb29fed5a03adc8b05a2a9eb10a02aaa489b9c1f8ff<br/>Nonce: 5pXWu7aGkY2J7II0X", 
    "signature": "0xc4f2f59d80e036ecab4eaaac5d4ee713ab94264ca584839c98b5743c4f6777322038225a4bc1e0f13b8382166816737369f26bd66f0479cfa80d4c52c02eb2cb1b", 
}

result = auth.bind.verify_remove_bind(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| message | str | Message that needs to be signed by the end user | Yes |  | "Please sign this message to unbind:<br/>Address: 0x6ed338bcB610640e81465FCfb9894DDfA354Cc91<br/>from<br/>Profile Id:<br/>- 0x0b2bbac1251651c0cbbdbbb29fed5a03adc8b05a2a9eb10a02aaa489b9c1f8ff<br/>Nonce: 5pXWu7aGkY2J7II0X" |
| signature | str | EIP-191 compliant signature signed by the Ethereum account address requesting authentication. | Yes |  | "0xc4f2f59d80e036ecab4eaaac5d4ee713ab94264ca584839c98b5743c4f6777322038225a4bc1e0f13b8382166816737369f26bd66f0479cfa80d4c52c02eb2cb1b" |


---
## verify_request_bind

> `auth.bind.verify_request_bind()`

Verify bind request

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "verifications": [], 
}

result = auth.bind.verify_request_bind(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| verifications | List of object: <br/> - message: str<br/> - signature: str | Message that needs to be signed by the end user | Yes |  | [] |




