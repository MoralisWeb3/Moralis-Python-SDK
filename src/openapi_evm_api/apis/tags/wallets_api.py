# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.2
    Generated by: https://openapi-generator.tech
"""

from openapi_evm_api.paths.wallets_address_defi_protocol_positions.get import GetDefiPositionsByProtocol
from openapi_evm_api.paths.wallets_address_defi_positions.get import GetDefiPositionsSummary
from openapi_evm_api.paths.wallets_address_defi_summary.get import GetDefiSummary
from openapi_evm_api.paths.wallets_address_chains.get import GetWalletActiveChains
from openapi_evm_api.paths.wallets_address_history.get import GetWalletHistory
from openapi_evm_api.paths.wallets_address_net_worth.get import GetWalletNetWorth
from openapi_evm_api.paths.wallets_address_profitability.get import GetWalletProfitability
from openapi_evm_api.paths.wallets_address_profitability_summary.get import GetWalletProfitabilitySummary
from openapi_evm_api.paths.wallets_address_stats.get import GetWalletStats
from openapi_evm_api.paths.wallets_address_tokens.get import GetWalletTokenBalancesPrice


class WalletsApi(
    GetDefiPositionsByProtocol,
    GetDefiPositionsSummary,
    GetDefiSummary,
    GetWalletActiveChains,
    GetWalletHistory,
    GetWalletNetWorth,
    GetWalletProfitability,
    GetWalletProfitabilitySummary,
    GetWalletStats,
    GetWalletTokenBalancesPrice,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
