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


class Erc20Transaction(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "address",
            "block_hash",
            "block_number",
            "transaction_index",
            "log_index",
            "possible_spam",
            "verified_contract",
            "block_timestamp",
            "token_name",
            "token_decimals",
            "token_symbol",
            "from_address",
            "value",
            "transaction_hash",
            "value_decimal",
        }
        
        class properties:
            token_name = schemas.StrSchema
            token_symbol = schemas.StrSchema
            token_decimals = schemas.StrSchema
            transaction_hash = schemas.StrSchema
            address = schemas.StrSchema
            block_timestamp = schemas.StrSchema
            block_number = schemas.StrSchema
            block_hash = schemas.StrSchema
            from_address = schemas.StrSchema
            value = schemas.StrSchema
            transaction_index = schemas.IntSchema
            log_index = schemas.IntSchema
            possible_spam = schemas.BoolSchema
            verified_contract = schemas.BoolSchema
            token_logo = schemas.StrSchema
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
                "token_decimals": token_decimals,
                "transaction_hash": transaction_hash,
                "address": address,
                "block_timestamp": block_timestamp,
                "block_number": block_number,
                "block_hash": block_hash,
                "from_address": from_address,
                "value": value,
                "transaction_index": transaction_index,
                "log_index": log_index,
                "possible_spam": possible_spam,
                "verified_contract": verified_contract,
                "token_logo": token_logo,
                "to_address": to_address,
                "to_address_label": to_address_label,
                "from_address_label": from_address_label,
            }

    
    address: MetaOapg.properties.address
    block_hash: MetaOapg.properties.block_hash
    block_number: MetaOapg.properties.block_number
    transaction_index: MetaOapg.properties.transaction_index
    log_index: MetaOapg.properties.log_index
    possible_spam: MetaOapg.properties.possible_spam
    verified_contract: MetaOapg.properties.verified_contract
    block_timestamp: MetaOapg.properties.block_timestamp
    token_name: MetaOapg.properties.token_name
    token_decimals: MetaOapg.properties.token_decimals
    token_symbol: MetaOapg.properties.token_symbol
    from_address: MetaOapg.properties.from_address
    value: MetaOapg.properties.value
    transaction_hash: MetaOapg.properties.transaction_hash
    value_decimal: schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_name"]) -> MetaOapg.properties.token_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_decimals"]) -> MetaOapg.properties.token_decimals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["log_index"]) -> MetaOapg.properties.log_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verified_contract"]) -> MetaOapg.properties.verified_contract: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address_label"]) -> MetaOapg.properties.to_address_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address_label"]) -> MetaOapg.properties.from_address_label: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["token_name", "token_symbol", "token_decimals", "transaction_hash", "address", "block_timestamp", "block_number", "block_hash", "from_address", "value", "transaction_index", "log_index", "possible_spam", "verified_contract", "token_logo", "to_address", "to_address_label", "from_address_label", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_name"]) -> MetaOapg.properties.token_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_decimals"]) -> MetaOapg.properties.token_decimals: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["log_index"]) -> MetaOapg.properties.log_index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verified_contract"]) -> MetaOapg.properties.verified_contract: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_logo"]) -> typing.Union[MetaOapg.properties.token_logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address"]) -> typing.Union[MetaOapg.properties.to_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address_label"]) -> typing.Union[MetaOapg.properties.to_address_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address_label"]) -> typing.Union[MetaOapg.properties.from_address_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token_name", "token_symbol", "token_decimals", "transaction_hash", "address", "block_timestamp", "block_number", "block_hash", "from_address", "value", "transaction_index", "log_index", "possible_spam", "verified_contract", "token_logo", "to_address", "to_address_label", "from_address_label", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        block_hash: typing.Union[MetaOapg.properties.block_hash, str, ],
        block_number: typing.Union[MetaOapg.properties.block_number, str, ],
        transaction_index: typing.Union[MetaOapg.properties.transaction_index, decimal.Decimal, int, ],
        log_index: typing.Union[MetaOapg.properties.log_index, decimal.Decimal, int, ],
        possible_spam: typing.Union[MetaOapg.properties.possible_spam, bool, ],
        verified_contract: typing.Union[MetaOapg.properties.verified_contract, bool, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, str, ],
        token_name: typing.Union[MetaOapg.properties.token_name, str, ],
        token_decimals: typing.Union[MetaOapg.properties.token_decimals, str, ],
        token_symbol: typing.Union[MetaOapg.properties.token_symbol, str, ],
        from_address: typing.Union[MetaOapg.properties.from_address, str, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        transaction_hash: typing.Union[MetaOapg.properties.transaction_hash, str, ],
        value_decimal: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        token_logo: typing.Union[MetaOapg.properties.token_logo, str, schemas.Unset] = schemas.unset,
        to_address: typing.Union[MetaOapg.properties.to_address, str, schemas.Unset] = schemas.unset,
        to_address_label: typing.Union[MetaOapg.properties.to_address_label, None, str, schemas.Unset] = schemas.unset,
        from_address_label: typing.Union[MetaOapg.properties.from_address_label, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Erc20Transaction':
        return super().__new__(
            cls,
            *args,
            address=address,
            block_hash=block_hash,
            block_number=block_number,
            transaction_index=transaction_index,
            log_index=log_index,
            possible_spam=possible_spam,
            verified_contract=verified_contract,
            block_timestamp=block_timestamp,
            token_name=token_name,
            token_decimals=token_decimals,
            token_symbol=token_symbol,
            from_address=from_address,
            value=value,
            transaction_hash=transaction_hash,
            value_decimal=value_decimal,
            token_logo=token_logo,
            to_address=to_address,
            to_address_label=to_address_label,
            from_address_label=from_address_label,
            _configuration=_configuration,
            **kwargs,
        )
