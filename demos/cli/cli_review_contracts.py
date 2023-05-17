import os
import sys

# This demo is only for testing purposes.
sys.path.insert(0, '../../src')

from dotenv import load_dotenv
from moralis import evm_api
from moralis.evm_api.utils.review_contracts import Params
from openapi_evm_api.model.chain_list import ChainList
from openapi_evm_api.model.contracts_review_dto import ContractsReviewDto

load_dotenv()
api_key = str(os.getenv('MORALIS_API_KEY'))

params = Params(
    chain=ChainList.ETH
)

body = ContractsReviewDto(
    contracts=[
        {
            'reason': 'This is test',
            'report_type': 'spam',
            'contract_type': 'ERC20',
            'contract_address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
        }
    ]
)

response = evm_api.utils.review_contracts(
    api_key,
    params,
    body
)
print('👀 result: {}'.format(response['message']))
