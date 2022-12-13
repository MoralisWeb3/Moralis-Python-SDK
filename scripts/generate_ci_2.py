from generate_modules import generate_modules
from generate_docs import generate_docs
from cleanup import cleanup
from apply_patches import apply_patches

generate_modules()
apply_patches()
generate_docs()
cleanup()
