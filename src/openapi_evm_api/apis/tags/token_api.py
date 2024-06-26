# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.2
    Generated by: https://openapi-generator.tech
"""

from openapi_evm_api.paths.erc20_prices.post import GetMultipleTokenPrices
from openapi_evm_api.paths.erc20_address_allowance.get import GetTokenAllowance
from openapi_evm_api.paths.erc20_metadata.get import GetTokenMetadata
from openapi_evm_api.paths.erc20_metadata_symbols.get import GetTokenMetadataBySymbol
from openapi_evm_api.paths.erc20_token_address_owners.get import GetTokenOwners
from openapi_evm_api.paths.erc20_address_price.get import GetTokenPrice
from openapi_evm_api.paths.erc20_address_stats.get import GetTokenStats
from openapi_evm_api.paths.erc20_address_transfers.get import GetTokenTransfers
from openapi_evm_api.paths.erc20_address_top_gainers.get import GetTopProfitableWalletPerToken
from openapi_evm_api.paths.address_erc20.get import GetWalletTokenBalances
from openapi_evm_api.paths.address_erc20_transfers.get import GetWalletTokenTransfers


class TokenApi(
    GetMultipleTokenPrices,
    GetTokenAllowance,
    GetTokenMetadata,
    GetTokenMetadataBySymbol,
    GetTokenOwners,
    GetTokenPrice,
    GetTokenStats,
    GetTokenTransfers,
    GetTopProfitableWalletPerToken,
    GetWalletTokenBalances,
    GetWalletTokenTransfers,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
