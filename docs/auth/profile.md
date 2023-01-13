# profile API:

> `auth.profile`

- [get_addresses](#get_addresses)


---
## get_addresses

> `auth.profile.get_addresses()`

Get addresses that are bound to the specific profileId

### Example
```python
from moralis import auth

api_key = "YOUR_API_KEY"
params = {
    "profileId": "", 
}

result = auth.profile.get_addresses(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| profileId | str | Unique identifier with a length of 66 characters | Yes |  | "" |





