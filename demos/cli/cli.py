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

print('🌕 block hash: {}'.format(block_response['hash']))

ens_domain_response = evm_api.resolve.resolve_ens_domain(api_key, {
    'domain': 'nick.eth'
})

print('🌞 end domain: {}'.format(ens_domain_response['address']))

nft_trades = evm_api.nft.get_nft_trades(api_key, {
    'address': '0x9c57d0278199c931cf149cc769f37bb7847091e7',
})

print('🌚 nft trade price: {}'.format(nft_trades['result'][0]['price']))
