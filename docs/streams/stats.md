# stats API:

> `Moralis.streams.stats`

- [get_stats](#get_stats)
- [get_stats_by_stream_id](#get_stats_by_stream_id)


---
## get_stats

> `Moralis.streams.stats.get_stats()`

Get the global stats for the account.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"

result = streams.stats.get_stats(
    api_key=api_key,
)

print(result)

```


---
## get_stats_by_stream_id

> `Moralis.streams.stats.get_stats_by_stream_id()`

Get the stats for the streamId specified


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "streamId": "", 
}

result = streams.stats.get_stats_by_stream_id(
    api_key=api_key,
    params=params,
)

print(result)

```

### Parameters

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| streamId | str | The id of the stream to get the stats | Yes |  | "" |





