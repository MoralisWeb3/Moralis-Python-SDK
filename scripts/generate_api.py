# Generate all api clients based on the open-api swagger definitions

import os
from pathlib import Path
import shutil
import json
import urllib3
from generate_swaggers import get_swagger, process_swagger, save_swagger

http = urllib3.PoolManager()

root_path = Path(__file__).parent.parent
temp_path = (root_path / "temp")
swaggers_path = (temp_path / "swagger")


# Create openapi client
def create_api_client(api_name):
    print("⏳ Generating openapi client...")
    os.system(
        f'_JAVA_OPTIONS="--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED" openapi-generator generate -c openapi.json --skip-validate-spec -i temp/swagger/{api_name}.json -p packageName=openapi_{api_name},projectName={api_name};')
    generated_path = (temp_path / f"generated-api/openapi_{api_name}")
    out_path = (root_path / f"src/openapi_{api_name}")
    if out_path.exists() and out_path.is_dir():
        shutil.rmtree(out_path)
    shutil.copytree(generated_path, out_path)
    docs_path = out_path / 'docs'
    if docs_path.exists() and docs_path.is_dir():
        shutil.rmtree(docs_path)
    print("✅ Generating openapi client done")


def makeapi(swagger_url, api_name):
    print(f"⏳ Making api generation for {api_name}...")

    data = get_swagger(swagger_url)
    data = process_swagger(data)
    save_swagger(data, api_name)
    create_api_client(api_name)

    print(f"⏳ Finished api generation for {api_name}")


def generate_api():
    print("⏳ Generating all api clients...")
    apis = json.load(open(root_path / 'api-config.json'))
    for api in apis:
        makeapi(api["swagger"], api["name"])
    print('🏁 Finished generating all api clients\n')
