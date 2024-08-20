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


class DefiTokenBalance(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "symbol",
            "balance",
            "balance_formatted",
            "decimals",
            "name",
            "contract_address",
            "token_type",
        }
        
        class properties:
            token_type = schemas.StrSchema
            name = schemas.StrSchema
            symbol = schemas.StrSchema
            contract_address = schemas.StrSchema
            decimals = schemas.NumberSchema
            balance = schemas.StrSchema
            balance_formatted = schemas.StrSchema
            logo = schemas.StrSchema
            thumbnail = schemas.StrSchema
            usd_price = schemas.NumberSchema
            usd_value = schemas.NumberSchema
            __annotations__ = {
                "token_type": token_type,
                "name": name,
                "symbol": symbol,
                "contract_address": contract_address,
                "decimals": decimals,
                "balance": balance,
                "balance_formatted": balance_formatted,
                "logo": logo,
                "thumbnail": thumbnail,
                "usd_price": usd_price,
                "usd_value": usd_value,
            }

    
    symbol: MetaOapg.properties.symbol
    balance: MetaOapg.properties.balance
    balance_formatted: MetaOapg.properties.balance_formatted
    decimals: MetaOapg.properties.decimals
    name: MetaOapg.properties.name
    contract_address: MetaOapg.properties.contract_address
    token_type: MetaOapg.properties.token_type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_type"]) -> MetaOapg.properties.token_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_address"]) -> MetaOapg.properties.contract_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decimals"]) -> MetaOapg.properties.decimals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance_formatted"]) -> MetaOapg.properties.balance_formatted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnail"]) -> MetaOapg.properties.thumbnail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usd_price"]) -> MetaOapg.properties.usd_price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usd_value"]) -> MetaOapg.properties.usd_value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["token_type", "name", "symbol", "contract_address", "decimals", "balance", "balance_formatted", "logo", "thumbnail", "usd_price", "usd_value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_type"]) -> MetaOapg.properties.token_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_address"]) -> MetaOapg.properties.contract_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decimals"]) -> MetaOapg.properties.decimals: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance_formatted"]) -> MetaOapg.properties.balance_formatted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> typing.Union[MetaOapg.properties.logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnail"]) -> typing.Union[MetaOapg.properties.thumbnail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usd_price"]) -> typing.Union[MetaOapg.properties.usd_price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usd_value"]) -> typing.Union[MetaOapg.properties.usd_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token_type", "name", "symbol", "contract_address", "decimals", "balance", "balance_formatted", "logo", "thumbnail", "usd_price", "usd_value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        balance: typing.Union[MetaOapg.properties.balance, str, ],
        balance_formatted: typing.Union[MetaOapg.properties.balance_formatted, str, ],
        decimals: typing.Union[MetaOapg.properties.decimals, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        contract_address: typing.Union[MetaOapg.properties.contract_address, str, ],
        token_type: typing.Union[MetaOapg.properties.token_type, str, ],
        logo: typing.Union[MetaOapg.properties.logo, str, schemas.Unset] = schemas.unset,
        thumbnail: typing.Union[MetaOapg.properties.thumbnail, str, schemas.Unset] = schemas.unset,
        usd_price: typing.Union[MetaOapg.properties.usd_price, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        usd_value: typing.Union[MetaOapg.properties.usd_value, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DefiTokenBalance':
        return super().__new__(
            cls,
            *args,
            symbol=symbol,
            balance=balance,
            balance_formatted=balance_formatted,
            decimals=decimals,
            name=name,
            contract_address=contract_address,
            token_type=token_type,
            logo=logo,
            thumbnail=thumbnail,
            usd_price=usd_price,
            usd_value=usd_value,
            _configuration=_configuration,
            **kwargs,
        )