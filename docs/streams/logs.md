# logs API:

> `streams.logs`

- [get_logs](#get_logs)


---
## get_logs

> `streams.logs.get_logs()`

get all failed logs


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "limit": 1.2, 
    "cursor": "", 
}

result = streams.logs.get_logs(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| limit | float |  | Yes |  | 1.2 |
| cursor | str |  |  |  | "" |





