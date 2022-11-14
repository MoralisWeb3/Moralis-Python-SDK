# streams: project

- [get_settings](#get_settings)
- [set_settings](#set_settings)


---
## `get_settings()`
Get the settings for the current project based on the project api-key.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"

result = streams.project.get_settings(
    api_key=api_key,
)

print(result)

```


---
## `set_settings()`
Set the settings for the current project based on the project api-key.


### Example
```python
from moralis import streams

api_key = "YOUR_API_KEY"
body = {
    "region": "", 
}

result = streams.project.set_settings(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Object with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| region | enum[str]: <br/>- "us-east-1"<br/>- "us-west-2"<br/>- "eu-central-1"<br/>- "ap-southeast-1" | The region from where all the webhooks will be posted for this project | Yes |  | "" |




