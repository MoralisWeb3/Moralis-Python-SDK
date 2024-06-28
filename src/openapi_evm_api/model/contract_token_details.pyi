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


class ContractTokenDetails(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "address",
            "token_logo",
            "token_name",
            "token_symbol",
        }
        
        class properties:
            address = schemas.StrSchema
            token_name = schemas.StrSchema
            token_logo = schemas.StrSchema
            token_symbol = schemas.StrSchema
            
            
            class address_label(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'address_label':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "address": address,
                "token_name": token_name,
                "token_logo": token_logo,
                "token_symbol": token_symbol,
                "address_label": address_label,
            }
    
    address: MetaOapg.properties.address
    token_logo: MetaOapg.properties.token_logo
    token_name: MetaOapg.properties.token_name
    token_symbol: MetaOapg.properties.token_symbol
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_name"]) -> MetaOapg.properties.token_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_label"]) -> MetaOapg.properties.address_label: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address", "token_name", "token_logo", "token_symbol", "address_label", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_name"]) -> MetaOapg.properties.token_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_label"]) -> typing.Union[MetaOapg.properties.address_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address", "token_name", "token_logo", "token_symbol", "address_label", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        token_logo: typing.Union[MetaOapg.properties.token_logo, str, ],
        token_name: typing.Union[MetaOapg.properties.token_name, str, ],
        token_symbol: typing.Union[MetaOapg.properties.token_symbol, str, ],
        address_label: typing.Union[MetaOapg.properties.address_label, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractTokenDetails':
        return super().__new__(
            cls,
            *args,
            address=address,
            token_logo=token_logo,
            token_name=token_name,
            token_symbol=token_symbol,
            address_label=address_label,
            _configuration=_configuration,
            **kwargs,
        )