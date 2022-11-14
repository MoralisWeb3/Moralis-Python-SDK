import shutil
from pathlib import Path

root_path = Path(__file__).parent.parent
temp_path = (root_path / "temp")


# Remove temp files
def cleanup():
    print("⏳ Removing temp folder...")
    if temp_path.exists() and temp_path.is_dir():
        shutil.rmtree(temp_path)
    print("✅ Removing temp folder done")
