from prepare import prepare
from generate_api import generate_api
from generate_modules import generate_modules
from generate_docs import generate_docs
from cleanup import cleanup
from apply_patches import apply_patches

if __name__ == "__main__":
  prepare()
  generate_api()
  generate_modules()
  apply_patches()
  generate_docs()
  cleanup()
