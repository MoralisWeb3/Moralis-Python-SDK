import os
import sys

# This demo is only for testing purposes.
sys.path.insert(0, '../../src')

from dotenv import load_dotenv
from moralis import evm_api

load_dotenv()
api_key = str(os.getenv("MORALIS_API_KEY"))

block_response = evm_api.block.get_block(api_key, {
    'block_number_or_hash': '1000000'
})

print(block_response)

ens_domain_response = evm_api.resolve.resolve_ens_domain(api_key, {
    'domain': 'nick.eth'
})

print(ens_domain_response)
