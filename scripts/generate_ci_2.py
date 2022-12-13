import json
from pathlib import Path
import shutil
from generate_modules import generate_modules
from generate_docs import generate_docs
from cleanup import cleanup
from apply_patches import apply_patches

root_path = Path(__file__).parent.parent
temp_path = (root_path / "temp")


def move_generated_api(api_name):
    print("⏳ Moving openapi client...")
    generated_path = (temp_path / f"generated-api/openapi_{api_name}")
    out_path = (root_path / f"src/openapi_{api_name}")
    if out_path.exists() and out_path.is_dir():
        shutil.rmtree(out_path)
    shutil.copytree(generated_path, out_path)
    docs_path = out_path / 'docs'
    if docs_path.exists() and docs_path.is_dir():
        shutil.rmtree(docs_path)
    print("✅ Moving openapi client done")

def move_generated_apis():
  print("⏳ Moving all api clients...")
  apis = json.load(open(root_path / 'api-config.json'))
  for api in apis:
      move_generated_api(api["name"])
  print('🏁 Finished moving all api clients\n')


move_generated_apis()
# generate_modules()
# apply_patches()
# generate_docs()
# cleanup()
