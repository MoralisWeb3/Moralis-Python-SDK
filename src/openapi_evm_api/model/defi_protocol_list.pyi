# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.2
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_evm_api import schemas  # noqa: F401


class DefiProtocolList(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def UNISWAPV2(cls):
        return cls("uniswap-v2")
    
    @schemas.classproperty
    def UNISWAPV3(cls):
        return cls("uniswap-v3")
    
    @schemas.classproperty
    def PANCAKESWAPV2(cls):
        return cls("pancakeswap-v2")
    
    @schemas.classproperty
    def PANCAKESWAPV3(cls):
        return cls("pancakeswap-v3")
    
    @schemas.classproperty
    def QUICKSWAPV2(cls):
        return cls("quickswap-v2")
    
    @schemas.classproperty
    def SUSHISWAPV2(cls):
        return cls("sushiswap-v2")
    
    @schemas.classproperty
    def AAVEV2(cls):
        return cls("aave-v2")
    
    @schemas.classproperty
    def AAVEV3(cls):
        return cls("aave-v3")
    
    @schemas.classproperty
    def FRAXSWAPV1(cls):
        return cls("fraxswap-v1")
    
    @schemas.classproperty
    def FRAXSWAPV2(cls):
        return cls("fraxswap-v2")
    
    @schemas.classproperty
    def LIDO(cls):
        return cls("lido")
    
    @schemas.classproperty
    def MAKERDAO(cls):
        return cls("makerdao")
    
    @schemas.classproperty
    def EIGENLAYER(cls):
        return cls("eigenlayer")
    
    @schemas.classproperty
    def PENDLE(cls):
        return cls("pendle")
    
    @schemas.classproperty
    def ETHERFI(cls):
        return cls("etherfi")
    
    @schemas.classproperty
    def ROCKETPOOL(cls):
        return cls("rocketpool")
    
    @schemas.classproperty
    def SPARKFI(cls):
        return cls("sparkfi")
