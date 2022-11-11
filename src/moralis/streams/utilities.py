import pkg_resources


def get_common_headers():
    """Get the headers for the requests."""
    return {
        "x-moralis-platform": 'Python SDK',
        "x-moralis-build-target": 'python',
        "x-moralis-build-target": pkg_resources.get_distribution('moralis').version,
    }

