from .version import __version__


def get_common_headers():
    """Get the headers for the requests."""
    return {
        "x-moralis-platform": 'Python SDK',
        "x-moralis-platform-version": __version__,
        "x-moralis-build-target": 'python',
    }
