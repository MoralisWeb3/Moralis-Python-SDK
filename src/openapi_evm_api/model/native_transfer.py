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


class NativeTransfer(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "internal_transaction",
            "value_formatted",
            "token_logo",
            "token_symbol",
            "from_address",
            "value",
        }
        
        class properties:
            from_address = schemas.StrSchema
            value = schemas.StrSchema
            value_formatted = schemas.StrSchema
            internal_transaction = schemas.BoolSchema
            token_symbol = schemas.StrSchema
            token_logo = schemas.StrSchema
            from_address_entity = schemas.StrSchema
            from_address_entity_logo = schemas.StrSchema
            
            
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
            to_address_entity = schemas.StrSchema
            to_address_entity_logo = schemas.StrSchema
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
            direction = schemas.StrSchema
            __annotations__ = {
                "from_address": from_address,
                "value": value,
                "value_formatted": value_formatted,
                "internal_transaction": internal_transaction,
                "token_symbol": token_symbol,
                "token_logo": token_logo,
                "from_address_entity": from_address_entity,
                "from_address_entity_logo": from_address_entity_logo,
                "from_address_label": from_address_label,
                "to_address_entity": to_address_entity,
                "to_address_entity_logo": to_address_entity_logo,
                "to_address": to_address,
                "to_address_label": to_address_label,
                "direction": direction,
            }

    
    internal_transaction: MetaOapg.properties.internal_transaction
    value_formatted: MetaOapg.properties.value_formatted
    token_logo: MetaOapg.properties.token_logo
    token_symbol: MetaOapg.properties.token_symbol
    from_address: MetaOapg.properties.from_address
    value: MetaOapg.properties.value
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value_formatted"]) -> MetaOapg.properties.value_formatted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internal_transaction"]) -> MetaOapg.properties.internal_transaction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address_entity"]) -> MetaOapg.properties.from_address_entity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address_entity_logo"]) -> MetaOapg.properties.from_address_entity_logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address_label"]) -> MetaOapg.properties.from_address_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address_entity"]) -> MetaOapg.properties.to_address_entity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address_entity_logo"]) -> MetaOapg.properties.to_address_entity_logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address_label"]) -> MetaOapg.properties.to_address_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direction"]) -> MetaOapg.properties.direction: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["from_address", "value", "value_formatted", "internal_transaction", "token_symbol", "token_logo", "from_address_entity", "from_address_entity_logo", "from_address_label", "to_address_entity", "to_address_entity_logo", "to_address", "to_address_label", "direction", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value_formatted"]) -> MetaOapg.properties.value_formatted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internal_transaction"]) -> MetaOapg.properties.internal_transaction: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address_entity"]) -> typing.Union[MetaOapg.properties.from_address_entity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address_entity_logo"]) -> typing.Union[MetaOapg.properties.from_address_entity_logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address_label"]) -> typing.Union[MetaOapg.properties.from_address_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address_entity"]) -> typing.Union[MetaOapg.properties.to_address_entity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address_entity_logo"]) -> typing.Union[MetaOapg.properties.to_address_entity_logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address"]) -> typing.Union[MetaOapg.properties.to_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address_label"]) -> typing.Union[MetaOapg.properties.to_address_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["direction"]) -> typing.Union[MetaOapg.properties.direction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["from_address", "value", "value_formatted", "internal_transaction", "token_symbol", "token_logo", "from_address_entity", "from_address_entity_logo", "from_address_label", "to_address_entity", "to_address_entity_logo", "to_address", "to_address_label", "direction", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        internal_transaction: typing.Union[MetaOapg.properties.internal_transaction, bool, ],
        value_formatted: typing.Union[MetaOapg.properties.value_formatted, str, ],
        token_logo: typing.Union[MetaOapg.properties.token_logo, str, ],
        token_symbol: typing.Union[MetaOapg.properties.token_symbol, str, ],
        from_address: typing.Union[MetaOapg.properties.from_address, str, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        from_address_entity: typing.Union[MetaOapg.properties.from_address_entity, str, schemas.Unset] = schemas.unset,
        from_address_entity_logo: typing.Union[MetaOapg.properties.from_address_entity_logo, str, schemas.Unset] = schemas.unset,
        from_address_label: typing.Union[MetaOapg.properties.from_address_label, None, str, schemas.Unset] = schemas.unset,
        to_address_entity: typing.Union[MetaOapg.properties.to_address_entity, str, schemas.Unset] = schemas.unset,
        to_address_entity_logo: typing.Union[MetaOapg.properties.to_address_entity_logo, str, schemas.Unset] = schemas.unset,
        to_address: typing.Union[MetaOapg.properties.to_address, str, schemas.Unset] = schemas.unset,
        to_address_label: typing.Union[MetaOapg.properties.to_address_label, None, str, schemas.Unset] = schemas.unset,
        direction: typing.Union[MetaOapg.properties.direction, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NativeTransfer':
        return super().__new__(
            cls,
            *args,
            internal_transaction=internal_transaction,
            value_formatted=value_formatted,
            token_logo=token_logo,
            token_symbol=token_symbol,
            from_address=from_address,
            value=value,
            from_address_entity=from_address_entity,
            from_address_entity_logo=from_address_entity_logo,
            from_address_label=from_address_label,
            to_address_entity=to_address_entity,
            to_address_entity_logo=to_address_entity_logo,
            to_address=to_address,
            to_address_label=to_address_label,
            direction=direction,
            _configuration=_configuration,
            **kwargs,
        )
