# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1
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


class Erc20Price(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "usdPrice",
        }
        
        class properties:
            usdPrice = schemas.Float64Schema
        
            @staticmethod
            def nativePrice() -> typing.Type['NativeErc20Price']:
                return NativeErc20Price
            exchangeAddress = schemas.StrSchema
            exchangeName = schemas.StrSchema
            __annotations__ = {
                "usdPrice": usdPrice,
                "nativePrice": nativePrice,
                "exchangeAddress": exchangeAddress,
                "exchangeName": exchangeName,
            }

    
    usdPrice: MetaOapg.properties.usdPrice
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usdPrice"]) -> MetaOapg.properties.usdPrice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nativePrice"]) -> 'NativeErc20Price': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exchangeAddress"]) -> MetaOapg.properties.exchangeAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exchangeName"]) -> MetaOapg.properties.exchangeName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["usdPrice", "nativePrice", "exchangeAddress", "exchangeName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usdPrice"]) -> MetaOapg.properties.usdPrice: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nativePrice"]) -> typing.Union['NativeErc20Price', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exchangeAddress"]) -> typing.Union[MetaOapg.properties.exchangeAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exchangeName"]) -> typing.Union[MetaOapg.properties.exchangeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["usdPrice", "nativePrice", "exchangeAddress", "exchangeName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        usdPrice: typing.Union[MetaOapg.properties.usdPrice, decimal.Decimal, int, float, ],
        nativePrice: typing.Union['NativeErc20Price', schemas.Unset] = schemas.unset,
        exchangeAddress: typing.Union[MetaOapg.properties.exchangeAddress, str, schemas.Unset] = schemas.unset,
        exchangeName: typing.Union[MetaOapg.properties.exchangeName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Erc20Price':
        return super().__new__(
            cls,
            *args,
            usdPrice=usdPrice,
            nativePrice=nativePrice,
            exchangeAddress=exchangeAddress,
            exchangeName=exchangeName,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.native_erc20_price import NativeErc20Price
