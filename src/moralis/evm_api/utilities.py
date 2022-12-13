from .version import __version__

print(__version__)

def get_common_headers():
    """Get the headers for the requests."""
    return {
        "x-moralis-platform": 'Python SDK',
        "x-moralis-build-target": 'python',
        "x-moralis-build-target": __version__,
    }

