# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.2
    Generated by: https://openapi-generator.tech
"""

from openapi_evm_api.paths.wallets_address_chains.get import GetWalletActiveChains
from openapi_evm_api.paths.wallets_address_stats.get import GetWalletStats


class WalletsApi(
    GetWalletActiveChains,
    GetWalletStats,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
