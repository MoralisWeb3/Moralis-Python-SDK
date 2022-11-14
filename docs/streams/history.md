# history API:

> `streams.history`

- [get_history](#get_history)
- [replay_history](#replay_history)


---
## get_history

> `streams.history.get_history()`

Get all history


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "limit": 1.2, 
    "cursor": "", 
    "excludePayload": True, 
}

result = streams.history.get_history(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| limit | float | - | Yes |  | 1.2 |
| cursor | str | - |  |  | "" |
| excludePayload | bool | - |  |  | True |



---
## replay_history

> `streams.history.replay_history()`

Replay a specific history.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "streamId": "", 
    "id": "", 
}

result = streams.history.replay_history(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| streamId | str | The id of the stream the history will be replayed | Yes |  | "" |
| id | str | The id of the history to replay | Yes |  | "" |





