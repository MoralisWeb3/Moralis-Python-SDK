import os
from pathlib import Path

root_path = Path(__file__).parent.parent
temp_path = (root_path / "temp")
swaggers_path = (temp_path / "swagger")
generated_api_path = (temp_path / "generated-api")
docs_path = root_path / 'docs'


# Make temp folder
def make_temp_folder():
    print("⏳ Making temp folder...")
    if not os.path.exists(temp_path):
        os.makedirs(temp_path)
        os.makedirs(swaggers_path)
        os.makedirs(generated_api_path)
    print("✅ Making temp folder done")


def make_docs_folder():
    if not docs_path.exists():
        os.mkdir(docs_path)


def prepare():
    make_temp_folder()
    make_docs_folder()
