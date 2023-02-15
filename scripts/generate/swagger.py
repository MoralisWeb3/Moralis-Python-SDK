import json
import re
import urllib3
from .paths import root_path
from .snake_case import to_snake, convert_abbreviations

http = urllib3.PoolManager()

def generate_swagger(swagger_url: str, api_name: str):
    print(f"⏳ Generating swagger for {api_name}...")

    swagger_content = fetch_swagger(swagger_url)
    swagger_content = process_swagger(swagger_content)

    print(f"✅ Generating swagger for {api_name} done")

    return swagger_content


def fetch_swagger(swagger_url: str):
    print("⏳ Fetching swagger...")

    # Load from local file in the root (for testing / development)
    if swagger_url.startswith("./"):
        file = open(root_path / swagger_url)
        data = file.read()
        minified = json.dumps(json.loads(data), separators=(',', ':'))

        return minified
    
    # Load from url
    response = http.request('GET', swagger_url)
    data: str = response.data.decode("utf-8")

    print("✅ Fetching swagger done")
    return data

def replace_tags(swagger_content: str):
    '''
    replace the default tags with the x-moralis-tag
    '''
    print("⏳ Replacing original tags with x-moralis-tag...")

    # Remove original 'tags'
    swagger_content = re.sub('"tags":\[.*?\]', '', swagger_content)

    # Remove trailing commas and double commas (caused by previous step)
    swagger_content = re.sub(',}', '}', swagger_content)
    swagger_content = re.sub(',,', ',', swagger_content)

    # Convert x-tag-sdk to tags
    swagger_content = re.sub('"x-tag-sdk":"(.*?)"',
                             lambda match: f'"tags": ["{to_snake(match.group(1))}"]', swagger_content)

    # We need to do this to prevent issue like getNFTByOwner -> get_nftby_owner.py, in openapi-generator
    swagger_content = re.sub('"operationId":"(.*?)"',
                             lambda match: f'"operationId": "{convert_abbreviations(match.group(1))}"', swagger_content)


    return swagger_content


def remove_invalid_attributes(swagger_json: dict):
    # 'default' is added in streams, but it's an invalid openapi specification
    if 'default' in swagger_json:
        del swagger_json['default']

    return swagger_json
    

def process_swagger(swagger_content: str):
    '''
    Process the swagger according to the needs to be used by the SDK. This includes:
    - transform "x-tag-sdk" to "tags" for every operation, this is a specific attribute,
    included to define what grouping should be used by all SDKs
    '''
    print("⏳ Processing swagger...")

    swagger_content = replace_tags(swagger_content)
    swagger_json = json.loads(swagger_content)
    swagger_json = remove_invalid_attributes(swagger_json)

    print("✅ Processing swagger done")
    return swagger_json


