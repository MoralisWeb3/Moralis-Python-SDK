
from setuptools import setup, find_packages

REQUIRES = [
    "certifi >= 14.5.14",
    "frozendict ~= 2.3.4",
    "python-dateutil ~= 2.8.2",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.7",
]

setup(
    name="moralis",
    version="0.1.42",
    description="The official Moralis Python SDK",
    keywords=["Moralis", "Moralis SDK", "Moralis Python SDK", "Web3", "Crypto", "Ethereum", "Avalanche",
              "Blockchain", "Contracts", "Eth", "Evm", "Fantom", "Nft", "Dapps", "Binance", "Solana"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
