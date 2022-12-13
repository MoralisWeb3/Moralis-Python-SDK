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


class NftOwner(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "block_number_minted",
            "contract_type",
            "symbol",
            "owner_of",
            "token_hash",
            "token_id",
            "last_metadata_sync",
            "name",
            "block_number",
            "token_address",
            "last_token_uri_sync",
        }
        
        class properties:
            token_address = schemas.StrSchema
            token_id = schemas.StrSchema
            contract_type = schemas.StrSchema
            owner_of = schemas.StrSchema
            block_number = schemas.StrSchema
            block_number_minted = schemas.StrSchema
            name = schemas.StrSchema
            symbol = schemas.StrSchema
            token_hash = schemas.StrSchema
            last_token_uri_sync = schemas.StrSchema
            last_metadata_sync = schemas.StrSchema
            token_uri = schemas.StrSchema
            metadata = schemas.StrSchema
        
            @staticmethod
            def normalized_metadata() -> typing.Type['NormalizedMetadata']:
                return NormalizedMetadata
            amount = schemas.StrSchema
            __annotations__ = {
                "token_address": token_address,
                "token_id": token_id,
                "contract_type": contract_type,
                "owner_of": owner_of,
                "block_number": block_number,
                "block_number_minted": block_number_minted,
                "name": name,
                "symbol": symbol,
                "token_hash": token_hash,
                "last_token_uri_sync": last_token_uri_sync,
                "last_metadata_sync": last_metadata_sync,
                "token_uri": token_uri,
                "metadata": metadata,
                "normalized_metadata": normalized_metadata,
                "amount": amount,
            }

    
    block_number_minted: MetaOapg.properties.block_number_minted
    contract_type: MetaOapg.properties.contract_type
    symbol: MetaOapg.properties.symbol
    owner_of: MetaOapg.properties.owner_of
    token_hash: MetaOapg.properties.token_hash
    token_id: MetaOapg.properties.token_id
    last_metadata_sync: MetaOapg.properties.last_metadata_sync
    name: MetaOapg.properties.name
    block_number: MetaOapg.properties.block_number
    token_address: MetaOapg.properties.token_address
    last_token_uri_sync: MetaOapg.properties.last_token_uri_sync
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_id"]) -> MetaOapg.properties.token_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_type"]) -> MetaOapg.properties.contract_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_of"]) -> MetaOapg.properties.owner_of: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number_minted"]) -> MetaOapg.properties.block_number_minted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_hash"]) -> MetaOapg.properties.token_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_token_uri_sync"]) -> MetaOapg.properties.last_token_uri_sync: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_metadata_sync"]) -> MetaOapg.properties.last_metadata_sync: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_uri"]) -> MetaOapg.properties.token_uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalized_metadata"]) -> 'NormalizedMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["token_address", "token_id", "contract_type", "owner_of", "block_number", "block_number_minted", "name", "symbol", "token_hash", "last_token_uri_sync", "last_metadata_sync", "token_uri", "metadata", "normalized_metadata", "amount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_id"]) -> MetaOapg.properties.token_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_type"]) -> MetaOapg.properties.contract_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_of"]) -> MetaOapg.properties.owner_of: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number_minted"]) -> MetaOapg.properties.block_number_minted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_hash"]) -> MetaOapg.properties.token_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_token_uri_sync"]) -> MetaOapg.properties.last_token_uri_sync: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_metadata_sync"]) -> MetaOapg.properties.last_metadata_sync: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_uri"]) -> typing.Union[MetaOapg.properties.token_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalized_metadata"]) -> typing.Union['NormalizedMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token_address", "token_id", "contract_type", "owner_of", "block_number", "block_number_minted", "name", "symbol", "token_hash", "last_token_uri_sync", "last_metadata_sync", "token_uri", "metadata", "normalized_metadata", "amount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        block_number_minted: typing.Union[MetaOapg.properties.block_number_minted, str, ],
        contract_type: typing.Union[MetaOapg.properties.contract_type, str, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        owner_of: typing.Union[MetaOapg.properties.owner_of, str, ],
        token_hash: typing.Union[MetaOapg.properties.token_hash, str, ],
        token_id: typing.Union[MetaOapg.properties.token_id, str, ],
        last_metadata_sync: typing.Union[MetaOapg.properties.last_metadata_sync, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        block_number: typing.Union[MetaOapg.properties.block_number, str, ],
        token_address: typing.Union[MetaOapg.properties.token_address, str, ],
        last_token_uri_sync: typing.Union[MetaOapg.properties.last_token_uri_sync, str, ],
        token_uri: typing.Union[MetaOapg.properties.token_uri, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, str, schemas.Unset] = schemas.unset,
        normalized_metadata: typing.Union['NormalizedMetadata', schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NftOwner':
        return super().__new__(
            cls,
            *_args,
            block_number_minted=block_number_minted,
            contract_type=contract_type,
            symbol=symbol,
            owner_of=owner_of,
            token_hash=token_hash,
            token_id=token_id,
            last_metadata_sync=last_metadata_sync,
            name=name,
            block_number=block_number,
            token_address=token_address,
            last_token_uri_sync=last_token_uri_sync,
            token_uri=token_uri,
            metadata=metadata,
            normalized_metadata=normalized_metadata,
            amount=amount,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.normalized_metadata import NormalizedMetadata
