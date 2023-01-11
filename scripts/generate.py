from generate.generate_lib import generate_lib
from generate.generate_docs import generate_docs
from generate.files import ensure_temp_folder, cleanup_temp_folder

def generate():
    print("🚀 Generating Moralis Python SDK...")
    ensure_temp_folder()
    generate_lib()
    generate_docs()
    cleanup_temp_folder()
    print("🏁 Done Moralis Python SDK...")

generate()