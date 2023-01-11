from pathlib import Path

# Root directory of the project
root_path = Path(__file__).parent.parent.parent

# Project patgs
docs_path = root_path / 'docs'
docs_snippet_path = docs_path / 'code_snippets.json'
src_path = root_path / 'src'
moralis_modules_root_path = (root_path / 'src/moralis')

# Script paths
templates_path = Path(__file__).parent / 'templates'

# Temporary folders during code generation
temp_path = (root_path / "temp")
temp_swaggers_path = (temp_path / "swagger")
temp_generated_api_path = (temp_path / "generated-api")

