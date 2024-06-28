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


class WalletHistoryNftTransfer(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "contract_type",
            "amount",
            "possible_spam",
            "token_id",
            "verified",
            "token_address",
            "transaction_type",
            "from_address",
            "log_index",
            "value",
            "direction",
        }
        
        class properties:
            token_address = schemas.StrSchema
            token_id = schemas.StrSchema
            from_address = schemas.StrSchema
            value = schemas.StrSchema
            amount = schemas.StrSchema
            contract_type = schemas.StrSchema
            transaction_type = schemas.StrSchema
            log_index = schemas.IntSchema
            possible_spam = schemas.BoolSchema
            direction = schemas.StrSchema
            
            
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
            operator = schemas.StrSchema
            verified_collection = schemas.BoolSchema
            collection_logo = schemas.StrSchema
            collection_banner_image = schemas.StrSchema
        
            @staticmethod
            def normalized_metadata() -> typing.Type['NormalizedMetadata']:
                return NormalizedMetadata
            __annotations__ = {
                "token_address": token_address,
                "token_id": token_id,
                "from_address": from_address,
                "value": value,
                "amount": amount,
                "contract_type": contract_type,
                "transaction_type": transaction_type,
                "log_index": log_index,
                "possible_spam": possible_spam,
                "direction": direction,
                "from_address_label": from_address_label,
                "to_address": to_address,
                "to_address_label": to_address_label,
                "operator": operator,
                "verified_collection": verified_collection,
                "collection_logo": collection_logo,
                "collection_banner_image": collection_banner_image,
                "normalized_metadata": normalized_metadata,
            }

    
    contract_type: MetaOapg.properties.contract_type
    amount: MetaOapg.properties.amount
    possible_spam: MetaOapg.properties.possible_spam
    token_id: MetaOapg.properties.token_id
    verified: schemas.AnyTypeSchema
    token_address: MetaOapg.properties.token_address
    transaction_type: MetaOapg.properties.transaction_type
    from_address: MetaOapg.properties.from_address
    log_index: MetaOapg.properties.log_index
    value: MetaOapg.properties.value
    direction: MetaOapg.properties.direction
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_id"]) -> MetaOapg.properties.token_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_type"]) -> MetaOapg.properties.contract_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_type"]) -> MetaOapg.properties.transaction_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["log_index"]) -> MetaOapg.properties.log_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direction"]) -> MetaOapg.properties.direction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address_label"]) -> MetaOapg.properties.from_address_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address_label"]) -> MetaOapg.properties.to_address_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verified_collection"]) -> MetaOapg.properties.verified_collection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection_logo"]) -> MetaOapg.properties.collection_logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection_banner_image"]) -> MetaOapg.properties.collection_banner_image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalized_metadata"]) -> 'NormalizedMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["token_address", "token_id", "from_address", "value", "amount", "contract_type", "transaction_type", "log_index", "possible_spam", "direction", "from_address_label", "to_address", "to_address_label", "operator", "verified_collection", "collection_logo", "collection_banner_image", "normalized_metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_id"]) -> MetaOapg.properties.token_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_type"]) -> MetaOapg.properties.contract_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_type"]) -> MetaOapg.properties.transaction_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["log_index"]) -> MetaOapg.properties.log_index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["direction"]) -> MetaOapg.properties.direction: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address_label"]) -> typing.Union[MetaOapg.properties.from_address_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address"]) -> typing.Union[MetaOapg.properties.to_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address_label"]) -> typing.Union[MetaOapg.properties.to_address_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> typing.Union[MetaOapg.properties.operator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verified_collection"]) -> typing.Union[MetaOapg.properties.verified_collection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection_logo"]) -> typing.Union[MetaOapg.properties.collection_logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection_banner_image"]) -> typing.Union[MetaOapg.properties.collection_banner_image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalized_metadata"]) -> typing.Union['NormalizedMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token_address", "token_id", "from_address", "value", "amount", "contract_type", "transaction_type", "log_index", "possible_spam", "direction", "from_address_label", "to_address", "to_address_label", "operator", "verified_collection", "collection_logo", "collection_banner_image", "normalized_metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        contract_type: typing.Union[MetaOapg.properties.contract_type, str, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        possible_spam: typing.Union[MetaOapg.properties.possible_spam, bool, ],
        token_id: typing.Union[MetaOapg.properties.token_id, str, ],
        verified: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        token_address: typing.Union[MetaOapg.properties.token_address, str, ],
        transaction_type: typing.Union[MetaOapg.properties.transaction_type, str, ],
        from_address: typing.Union[MetaOapg.properties.from_address, str, ],
        log_index: typing.Union[MetaOapg.properties.log_index, decimal.Decimal, int, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        direction: typing.Union[MetaOapg.properties.direction, str, ],
        from_address_label: typing.Union[MetaOapg.properties.from_address_label, None, str, schemas.Unset] = schemas.unset,
        to_address: typing.Union[MetaOapg.properties.to_address, str, schemas.Unset] = schemas.unset,
        to_address_label: typing.Union[MetaOapg.properties.to_address_label, None, str, schemas.Unset] = schemas.unset,
        operator: typing.Union[MetaOapg.properties.operator, str, schemas.Unset] = schemas.unset,
        verified_collection: typing.Union[MetaOapg.properties.verified_collection, bool, schemas.Unset] = schemas.unset,
        collection_logo: typing.Union[MetaOapg.properties.collection_logo, str, schemas.Unset] = schemas.unset,
        collection_banner_image: typing.Union[MetaOapg.properties.collection_banner_image, str, schemas.Unset] = schemas.unset,
        normalized_metadata: typing.Union['NormalizedMetadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletHistoryNftTransfer':
        return super().__new__(
            cls,
            *args,
            contract_type=contract_type,
            amount=amount,
            possible_spam=possible_spam,
            token_id=token_id,
            verified=verified,
            token_address=token_address,
            transaction_type=transaction_type,
            from_address=from_address,
            log_index=log_index,
            value=value,
            direction=direction,
            from_address_label=from_address_label,
            to_address=to_address,
            to_address_label=to_address_label,
            operator=operator,
            verified_collection=verified_collection,
            collection_logo=collection_logo,
            collection_banner_image=collection_banner_image,
            normalized_metadata=normalized_metadata,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.normalized_metadata import NormalizedMetadata
