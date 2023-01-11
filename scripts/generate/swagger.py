import re
import urllib3

http = urllib3.PoolManager()

def generate_swagger(swagger_url: str, api_name: str):
    print(f"⏳ Generating swagger for {api_name}...")

    swagger_content = fetch_swagger(swagger_url)
    swagger_content = process_swagger(swagger_content)

    print(f"✅ Generating swagger for {api_name} done")

    return swagger_content


def fetch_swagger(swagger_url: str):
    print("⏳ Fetching swagger...")
    response = http.request('GET', swagger_url)
    data: str = response.data.decode("utf-8")

    print("✅ Fetching swagger done")
    return data


def rename_tag(tag):
    '''Rename tags is needed because of transform issues to snake_case in CI: evm-streams get converted to evm_streams'''
    if tag == "evm-streams":
        return "evm_streams"
    return tag


def process_swagger(swagger_content: str):
    '''
    Process the swagger according to the needs to be used by the SDK. This includes:
    - transform "x-tag-sdk" to "tags" for every operation, this is a specific attribute,
    included to define what grouping should be used by all SDKs
    '''
    print("⏳ Processing swagger...")

    # Remove original 'tags'
    swagger_content = re.sub('"tags":\[.*?\]', '', swagger_content)

    # Remove traling commas and double commas (caused by previous step)
    swagger_content = re.sub(',}', '}', swagger_content)
    swagger_content = re.sub(',,', ',', swagger_content)

    # Convert x-tag-sdk to tags
    swagger_content = re.sub('"x-tag-sdk":"(.*?)"',
                             lambda match: f'"tags": ["{rename_tag(match.group(1))}"]', swagger_content)

    print("✅ Processing swagger done")
    return swagger_content


