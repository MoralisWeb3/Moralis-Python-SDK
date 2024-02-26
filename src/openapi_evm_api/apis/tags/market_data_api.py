# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.2
    Generated by: https://openapi-generator.tech
"""

from openapi_evm_api.paths.market_data_nfts_hottest_collections.get import GetHottestNftCollectionsByTradingVolume
from openapi_evm_api.paths.market_data_global_market_cap.get import GetTopCryptoCurrenciesByMarketCap
from openapi_evm_api.paths.market_data_global_volume.get import GetTopCryptoCurrenciesByTradingVolume
from openapi_evm_api.paths.market_data_erc20s_top_tokens.get import GetTopErc20TokensByMarketCap
from openapi_evm_api.paths.market_data_erc20s_top_movers.get import GetTopErc20TokensByPriceMovers
from openapi_evm_api.paths.market_data_nfts_top_collections.get import GetTopNftCollectionsByMarketCap


class MarketDataApi(
    GetHottestNftCollectionsByTradingVolume,
    GetTopCryptoCurrenciesByMarketCap,
    GetTopCryptoCurrenciesByTradingVolume,
    GetTopErc20TokensByMarketCap,
    GetTopErc20TokensByPriceMovers,
    GetTopNftCollectionsByMarketCap,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
