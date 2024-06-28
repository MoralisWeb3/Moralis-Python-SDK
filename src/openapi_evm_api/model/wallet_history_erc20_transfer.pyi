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


class WalletHistoryErc20Transfer(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "address",
            "possible_spam",
            "verified_contract",
            "value_formatted",
            "token_logo",
            "token_name",
            "token_decimals",
            "token_symbol",
            "transaction_index",
            "from_address",
            "log_index",
            "value",
        }
        
        class properties:
            token_name = schemas.StrSchema
            token_symbol = schemas.StrSchema
            token_logo = schemas.StrSchema
            token_decimals = schemas.StrSchema
            address = schemas.StrSchema
            from_address = schemas.StrSchema
            value = schemas.StrSchema
            value_formatted = schemas.StrSchema
            log_index = schemas.IntSchema
            possible_spam = schemas.BoolSchema
            verified_contract = schemas.BoolSchema
            block_timestamp = schemas.StrSchema
            to_address = schemas.StrSchema
            
            
            class to_address_label(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'to_address_label':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class from_address_label(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'from_address_label':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "token_name": token_name,
                "token_symbol": token_symbol,
                "token_logo": token_logo,
                "token_decimals": token_decimals,
                "address": address,
                "from_address": from_address,
                "value": value,
                "value_formatted": value_formatted,
                "log_index": log_index,
                "possible_spam": possible_spam,
                "verified_contract": verified_contract,
                "block_timestamp": block_timestamp,
                "to_address": to_address,
                "to_address_label": to_address_label,
                "from_address_label": from_address_label,
            }

    
    address: MetaOapg.properties.address
    possible_spam: MetaOapg.properties.possible_spam
    verified_contract: MetaOapg.properties.verified_contract
    value_formatted: MetaOapg.properties.value_formatted
    token_logo: MetaOapg.properties.token_logo
    token_name: MetaOapg.properties.token_name
    token_decimals: MetaOapg.properties.token_decimals
    token_symbol: MetaOapg.properties.token_symbol
    transaction_index: schemas.AnyTypeSchema
    from_address: MetaOapg.properties.from_address
    log_index: MetaOapg.properties.log_index
    value: MetaOapg.properties.value
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_name"]) -> MetaOapg.properties.token_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_decimals"]) -> MetaOapg.properties.token_decimals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value_formatted"]) -> MetaOapg.properties.value_formatted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["log_index"]) -> MetaOapg.properties.log_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verified_contract"]) -> MetaOapg.properties.verified_contract: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address_label"]) -> MetaOapg.properties.to_address_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address_label"]) -> MetaOapg.properties.from_address_label: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["token_name", "token_symbol", "token_logo", "token_decimals", "address", "from_address", "value", "value_formatted", "log_index", "possible_spam", "verified_contract", "block_timestamp", "to_address", "to_address_label", "from_address_label", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_name"]) -> MetaOapg.properties.token_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_decimals"]) -> MetaOapg.properties.token_decimals: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value_formatted"]) -> MetaOapg.properties.value_formatted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["log_index"]) -> MetaOapg.properties.log_index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verified_contract"]) -> MetaOapg.properties.verified_contract: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> typing.Union[MetaOapg.properties.block_timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address"]) -> typing.Union[MetaOapg.properties.to_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address_label"]) -> typing.Union[MetaOapg.properties.to_address_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address_label"]) -> typing.Union[MetaOapg.properties.from_address_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token_name", "token_symbol", "token_logo", "token_decimals", "address", "from_address", "value", "value_formatted", "log_index", "possible_spam", "verified_contract", "block_timestamp", "to_address", "to_address_label", "from_address_label", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        possible_spam: typing.Union[MetaOapg.properties.possible_spam, bool, ],
        verified_contract: typing.Union[MetaOapg.properties.verified_contract, bool, ],
        value_formatted: typing.Union[MetaOapg.properties.value_formatted, str, ],
        token_logo: typing.Union[MetaOapg.properties.token_logo, str, ],
        token_name: typing.Union[MetaOapg.properties.token_name, str, ],
        token_decimals: typing.Union[MetaOapg.properties.token_decimals, str, ],
        token_symbol: typing.Union[MetaOapg.properties.token_symbol, str, ],
        transaction_index: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        from_address: typing.Union[MetaOapg.properties.from_address, str, ],
        log_index: typing.Union[MetaOapg.properties.log_index, decimal.Decimal, int, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, str, schemas.Unset] = schemas.unset,
        to_address: typing.Union[MetaOapg.properties.to_address, str, schemas.Unset] = schemas.unset,
        to_address_label: typing.Union[MetaOapg.properties.to_address_label, None, str, schemas.Unset] = schemas.unset,
        from_address_label: typing.Union[MetaOapg.properties.from_address_label, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletHistoryErc20Transfer':
        return super().__new__(
            cls,
            *args,
            address=address,
            possible_spam=possible_spam,
            verified_contract=verified_contract,
            value_formatted=value_formatted,
            token_logo=token_logo,
            token_name=token_name,
            token_decimals=token_decimals,
            token_symbol=token_symbol,
            transaction_index=transaction_index,
            from_address=from_address,
            log_index=log_index,
            value=value,
            block_timestamp=block_timestamp,
            to_address=to_address,
            to_address_label=to_address_label,
            from_address_label=from_address_label,
            _configuration=_configuration,
            **kwargs,
        )
