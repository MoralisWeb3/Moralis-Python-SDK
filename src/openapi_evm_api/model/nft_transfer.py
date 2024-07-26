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


class NftTransfer(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "contract_type",
            "possible_spam",
            "token_id",
            "block_timestamp",
            "block_hash",
            "block_number",
            "token_address",
            "log_index",
            "transaction_hash",
        }
        
        class properties:
            token_address = schemas.StrSchema
            token_id = schemas.StrSchema
            contract_type = schemas.StrSchema
            block_number = schemas.StrSchema
            block_timestamp = schemas.StrSchema
            block_hash = schemas.StrSchema
            transaction_hash = schemas.StrSchema
            log_index = schemas.IntSchema
            possible_spam = schemas.BoolSchema
            from_address_entity = schemas.StrSchema
            from_address_entity_logo = schemas.StrSchema
            from_address = schemas.StrSchema
            
            
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
            value = schemas.StrSchema
            amount = schemas.StrSchema
            transaction_type = schemas.StrSchema
            transaction_index = schemas.IntSchema
            operator = schemas.StrSchema
            verified_collection = schemas.BoolSchema
            
            
            class last_sale(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                class MetaOapg:
                    required = {
                        "buyer_address",
                        "price",
                        "block_timestamp",
                        "payment_token",
                        "seller_address",
                        "transaction_hash",
                        "price_formatted",
                    }
                    
                    class properties:
                        transaction_hash = schemas.StrSchema
                        block_timestamp = schemas.StrSchema
                        price = schemas.StrSchema
                        price_formatted = schemas.StrSchema
                        usd_price = schemas.StrSchema
                        buyer_address = schemas.StrSchema
                        seller_address = schemas.StrSchema
                        
                        
                        class payment_token(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "token_logo",
                                    "token_name",
                                    "token_address",
                                    "token_decimals",
                                    "token_symbol",
                                }
                                
                                class properties:
                                    token_name = schemas.StrSchema
                                    token_symbol = schemas.StrSchema
                                    token_logo = schemas.StrSchema
                                    token_decimals = schemas.StrSchema
                                    token_address = schemas.StrSchema
                                    __annotations__ = {
                                        "token_name": token_name,
                                        "token_symbol": token_symbol,
                                        "token_logo": token_logo,
                                        "token_decimals": token_decimals,
                                        "token_address": token_address,
                                    }
                            
                            token_logo: MetaOapg.properties.token_logo
                            token_name: MetaOapg.properties.token_name
                            token_address: MetaOapg.properties.token_address
                            token_decimals: MetaOapg.properties.token_decimals
                            token_symbol: MetaOapg.properties.token_symbol
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["token_name"]) -> MetaOapg.properties.token_name: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["token_decimals"]) -> MetaOapg.properties.token_decimals: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["token_name", "token_symbol", "token_logo", "token_decimals", "token_address", ], str]):
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
                            def get_item_oapg(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token_name", "token_symbol", "token_logo", "token_decimals", "token_address", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                token_logo: typing.Union[MetaOapg.properties.token_logo, str, ],
                                token_name: typing.Union[MetaOapg.properties.token_name, str, ],
                                token_address: typing.Union[MetaOapg.properties.token_address, str, ],
                                token_decimals: typing.Union[MetaOapg.properties.token_decimals, str, ],
                                token_symbol: typing.Union[MetaOapg.properties.token_symbol, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'payment_token':
                                return super().__new__(
                                    cls,
                                    *args,
                                    token_logo=token_logo,
                                    token_name=token_name,
                                    token_address=token_address,
                                    token_decimals=token_decimals,
                                    token_symbol=token_symbol,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "transaction_hash": transaction_hash,
                            "block_timestamp": block_timestamp,
                            "price": price,
                            "price_formatted": price_formatted,
                            "usd_price": usd_price,
                            "buyer_address": buyer_address,
                            "seller_address": seller_address,
                            "payment_token": payment_token,
                        }
            
                
                buyer_address: MetaOapg.properties.buyer_address
                price: MetaOapg.properties.price
                block_timestamp: MetaOapg.properties.block_timestamp
                payment_token: MetaOapg.properties.payment_token
                seller_address: MetaOapg.properties.seller_address
                transaction_hash: MetaOapg.properties.transaction_hash
                price_formatted: MetaOapg.properties.price_formatted
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["price_formatted"]) -> MetaOapg.properties.price_formatted: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["usd_price"]) -> MetaOapg.properties.usd_price: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["buyer_address"]) -> MetaOapg.properties.buyer_address: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["seller_address"]) -> MetaOapg.properties.seller_address: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["payment_token"]) -> MetaOapg.properties.payment_token: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "block_timestamp", "price", "price_formatted", "usd_price", "buyer_address", "seller_address", "payment_token", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["price_formatted"]) -> MetaOapg.properties.price_formatted: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["usd_price"]) -> typing.Union[MetaOapg.properties.usd_price, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["buyer_address"]) -> MetaOapg.properties.buyer_address: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["seller_address"]) -> MetaOapg.properties.seller_address: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["payment_token"]) -> MetaOapg.properties.payment_token: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "block_timestamp", "price", "price_formatted", "usd_price", "buyer_address", "seller_address", "payment_token", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, None, ],
                    usd_price: typing.Union[MetaOapg.properties.usd_price, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'last_sale':
                    return super().__new__(
                        cls,
                        *args,
                        usd_price=usd_price,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "token_address": token_address,
                "token_id": token_id,
                "contract_type": contract_type,
                "block_number": block_number,
                "block_timestamp": block_timestamp,
                "block_hash": block_hash,
                "transaction_hash": transaction_hash,
                "log_index": log_index,
                "possible_spam": possible_spam,
                "from_address_entity": from_address_entity,
                "from_address_entity_logo": from_address_entity_logo,
                "from_address": from_address,
                "from_address_label": from_address_label,
                "to_address_entity": to_address_entity,
                "to_address_entity_logo": to_address_entity_logo,
                "to_address": to_address,
                "to_address_label": to_address_label,
                "value": value,
                "amount": amount,
                "transaction_type": transaction_type,
                "transaction_index": transaction_index,
                "operator": operator,
                "verified_collection": verified_collection,
                "last_sale": last_sale,
            }

    
    contract_type: MetaOapg.properties.contract_type
    possible_spam: MetaOapg.properties.possible_spam
    token_id: MetaOapg.properties.token_id
    block_timestamp: MetaOapg.properties.block_timestamp
    block_hash: MetaOapg.properties.block_hash
    block_number: MetaOapg.properties.block_number
    token_address: MetaOapg.properties.token_address
    log_index: MetaOapg.properties.log_index
    transaction_hash: MetaOapg.properties.transaction_hash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_id"]) -> MetaOapg.properties.token_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_type"]) -> MetaOapg.properties.contract_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["log_index"]) -> MetaOapg.properties.log_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address_entity"]) -> MetaOapg.properties.from_address_entity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address_entity_logo"]) -> MetaOapg.properties.from_address_entity_logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_type"]) -> MetaOapg.properties.transaction_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verified_collection"]) -> MetaOapg.properties.verified_collection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_sale"]) -> MetaOapg.properties.last_sale: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["token_address", "token_id", "contract_type", "block_number", "block_timestamp", "block_hash", "transaction_hash", "log_index", "possible_spam", "from_address_entity", "from_address_entity_logo", "from_address", "from_address_label", "to_address_entity", "to_address_entity_logo", "to_address", "to_address_label", "value", "amount", "transaction_type", "transaction_index", "operator", "verified_collection", "last_sale", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_id"]) -> MetaOapg.properties.token_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_type"]) -> MetaOapg.properties.contract_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["log_index"]) -> MetaOapg.properties.log_index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address_entity"]) -> typing.Union[MetaOapg.properties.from_address_entity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address_entity_logo"]) -> typing.Union[MetaOapg.properties.from_address_entity_logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address"]) -> typing.Union[MetaOapg.properties.from_address, schemas.Unset]: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_type"]) -> typing.Union[MetaOapg.properties.transaction_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_index"]) -> typing.Union[MetaOapg.properties.transaction_index, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> typing.Union[MetaOapg.properties.operator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verified_collection"]) -> typing.Union[MetaOapg.properties.verified_collection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_sale"]) -> typing.Union[MetaOapg.properties.last_sale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token_address", "token_id", "contract_type", "block_number", "block_timestamp", "block_hash", "transaction_hash", "log_index", "possible_spam", "from_address_entity", "from_address_entity_logo", "from_address", "from_address_label", "to_address_entity", "to_address_entity_logo", "to_address", "to_address_label", "value", "amount", "transaction_type", "transaction_index", "operator", "verified_collection", "last_sale", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        contract_type: typing.Union[MetaOapg.properties.contract_type, str, ],
        possible_spam: typing.Union[MetaOapg.properties.possible_spam, bool, ],
        token_id: typing.Union[MetaOapg.properties.token_id, str, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, str, ],
        block_hash: typing.Union[MetaOapg.properties.block_hash, str, ],
        block_number: typing.Union[MetaOapg.properties.block_number, str, ],
        token_address: typing.Union[MetaOapg.properties.token_address, str, ],
        log_index: typing.Union[MetaOapg.properties.log_index, decimal.Decimal, int, ],
        transaction_hash: typing.Union[MetaOapg.properties.transaction_hash, str, ],
        from_address_entity: typing.Union[MetaOapg.properties.from_address_entity, str, schemas.Unset] = schemas.unset,
        from_address_entity_logo: typing.Union[MetaOapg.properties.from_address_entity_logo, str, schemas.Unset] = schemas.unset,
        from_address: typing.Union[MetaOapg.properties.from_address, str, schemas.Unset] = schemas.unset,
        from_address_label: typing.Union[MetaOapg.properties.from_address_label, None, str, schemas.Unset] = schemas.unset,
        to_address_entity: typing.Union[MetaOapg.properties.to_address_entity, str, schemas.Unset] = schemas.unset,
        to_address_entity_logo: typing.Union[MetaOapg.properties.to_address_entity_logo, str, schemas.Unset] = schemas.unset,
        to_address: typing.Union[MetaOapg.properties.to_address, str, schemas.Unset] = schemas.unset,
        to_address_label: typing.Union[MetaOapg.properties.to_address_label, None, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        transaction_type: typing.Union[MetaOapg.properties.transaction_type, str, schemas.Unset] = schemas.unset,
        transaction_index: typing.Union[MetaOapg.properties.transaction_index, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        operator: typing.Union[MetaOapg.properties.operator, str, schemas.Unset] = schemas.unset,
        verified_collection: typing.Union[MetaOapg.properties.verified_collection, bool, schemas.Unset] = schemas.unset,
        last_sale: typing.Union[MetaOapg.properties.last_sale, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NftTransfer':
        return super().__new__(
            cls,
            *args,
            contract_type=contract_type,
            possible_spam=possible_spam,
            token_id=token_id,
            block_timestamp=block_timestamp,
            block_hash=block_hash,
            block_number=block_number,
            token_address=token_address,
            log_index=log_index,
            transaction_hash=transaction_hash,
            from_address_entity=from_address_entity,
            from_address_entity_logo=from_address_entity_logo,
            from_address=from_address,
            from_address_label=from_address_label,
            to_address_entity=to_address_entity,
            to_address_entity_logo=to_address_entity_logo,
            to_address=to_address,
            to_address_label=to_address_label,
            value=value,
            amount=amount,
            transaction_type=transaction_type,
            transaction_index=transaction_index,
            operator=operator,
            verified_collection=verified_collection,
            last_sale=last_sale,
            _configuration=_configuration,
            **kwargs,
        )
