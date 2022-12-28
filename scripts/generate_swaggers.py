# Generate all input openApi files

from pathlib import Path
import json
import urllib3
import re

http = urllib3.PoolManager()

root_path = Path(__file__).parent.parent
temp_path = (root_path / "temp")
swaggers_path = (temp_path / "swagger")


# Get swagger
def get_swagger(swagger_url):
    print("⏳ Fetching swagger...")
    response = http.request('GET', swagger_url)
    data = response.data.decode("utf-8")
    print("✅ Fetching swagger done")
    return data


# process swagger
def process_swagger(data):
    print("⏳ Processing swagger...")
    # Remove original 'tags'
    data = re.sub('"tags":\[.*?\]', '', data)
    # Remove traling commas and double commas (caused by previous step)
    data = re.sub(',}', '}', data)
    data = re.sub(',,', ',', data)
    # Convert x-tag-sdk to tags
    data = re.sub('"x-tag-sdk":"(.*?)"', r'"tags": ["\1"]', data)
    print("✅ Processing swagger done")
    return data


# Save swagger to temp folder
def save_swagger(data, api_name):
    print("⏳ Saving swagger...")
    json_out_file = (swaggers_path / (api_name + ".json"))
    with open(json_out_file, "w") as outfile:
        try:
            json.dump(json.loads(data), outfile, indent=4)
        except BaseException as error:
            print("An exception occured parsing the swagger for " + api_name + ": " + data)
            raise Exception("An exception occured parsing the swagger for " +api_name+ ": " + str(error))
    print("✅ Saving swagger done")


# Create openapi client

def makeapi(swagger_url, api_name):
    print(f"⏳ Making api generation for {api_name}...")

    data = get_swagger(swagger_url)
    data = process_swagger(data)
    save_swagger(data, api_name)

    print(f"⏳ Finished api generation for {api_name}")


def generate_swaggers():
    print("⏳ Generating all api clients...")
    apis = json.load(open(root_path / 'api-config.json'))
    for api in apis:
        makeapi(api["swagger"], api["name"])
    print('🏁 Finished generating all api clients\n')
