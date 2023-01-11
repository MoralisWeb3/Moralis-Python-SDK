import json
import os
import shutil
from pathlib import Path
from .paths import temp_path, temp_swaggers_path, temp_generated_api_path

def remove_folder(path: Path):
    if path.exists() and path.is_dir():
        print(f'⏳ Removing already existing path {path.as_posix()}...')
        shutil.rmtree(path)

def ensure_empty_folder(path: Path):
    remove_folder(path)
    os.makedirs(path)

def ensure_temp_folder():
    print(f"⏳ Ensuring empty temp folder at {temp_path}")

    ensure_empty_folder(temp_path)

    os.makedirs(temp_swaggers_path)
    os.makedirs(temp_generated_api_path)

    print("✅ Empty temp folder ensured")

def cleanup_temp_folder():
    remove_folder(temp_swaggers_path)


def save_json(content: str, path: Path, name: str):
    print(f"⏳ Saving file {name}.json...")
    out_file = (path / (name + ".json"))

    with open(out_file, "w") as outfile:
        try:
            json.dump(json.loads(content), outfile, indent=4)
        except BaseException as error:
            print("An exception occured parsing the json for " +
                  name + ": " + content)
            raise Exception(
                "An exception occured parsing the swagger for " + name + ": " + str(error))
    print("✅ Saving file done")

def save_py(content:str, path: Path):
    print(f"⏳ Saving file {path.as_posix()}...")
    with open(path, "w") as outfile:
        outfile.write(content)

    print("✅ Saving file done")





def copy_and_replace_folder(src_path: Path, dest_path: Path):
    print(f"⏳ Moving folder from {src_path.as_posix()} to {dest_path.as_posix()}...")
    remove_folder(dest_path)
    shutil.copytree(src_path, dest_path)
    print(f"✅ Done moving folder")

