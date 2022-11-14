# ipfs API:

> `evm_api.ipfs`

- [upload_folder](#upload_folder)


---
## upload_folder

> `evm_api.ipfs.upload_folder()`

Upload multiple files to IPFS and place them in a folder directory.


### Example
```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
body = [{
    "path": "moralis/logo.jpg", 
    "content": "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAApgAAAKYB3X3", 
}]

result = evm_api.ipfs.upload_folder(
    api_key=api_key,
    body=body,
)

print(result)

```

### Body
Array of objects, with the properties:

| Name | Type | Description | Required | Default | Example |
|------|------|-------------|----------|---------|---------|
| path | str | Path to the file | Yes |  | "moralis/logo.jpg" |
| content | str | Base64 or JSON | Yes |  | "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAApgAAAKYB3X3" |




