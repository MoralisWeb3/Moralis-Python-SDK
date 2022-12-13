#  Create build artifacts, required for CI and manual publishing
rm -rf dist
rm -rf build
python3 setup.py sdist bdist_wheel