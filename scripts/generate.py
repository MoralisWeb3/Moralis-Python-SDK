# Description: This script is used to generate the SDK and documentation
# Use this only in local development
# For CI we use generate_ci_1 and generate_ci_2, because the openapi-generator needs
# to run seperately as a github action

# !!Warning!!: the CI might use a different version of the open-api-generatoor than a local one
# TODO: re-use generate_ci_1 and generate_ci_2 in this script, or remove this all together
from prepare import prepare
from generate_api import generate_api
from generate_modules import generate_modules
from generate_docs import generate_docs
from cleanup import cleanup
from apply_patches import apply_patches

prepare()
generate_api()
generate_modules()
apply_patches()
generate_docs()
cleanup()
