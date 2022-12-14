# coding: utf-8

"""
    Solana API

    Moralis Solana API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from openapi_sol_api.paths.account_network_address_balance.get import Balance
from openapi_sol_api.paths.account_network_address_nft.get import GetNfts
from openapi_sol_api.paths.account_network_address_portfolio.get import GetPortfolio
from openapi_sol_api.paths.account_network_address_tokens.get import GetSpl


class AccountApi(
    Balance,
    GetNfts,
    GetPortfolio,
    GetSpl,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
