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


class NftTransferCollection(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "cursor",
            "result",
            "page",
            "page_size",
        }
        
        class properties:
            page = schemas.IntSchema
            page_size = schemas.IntSchema
            cursor = schemas.StrSchema
            
            
            class result(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NftTransfer']:
                        return NftTransfer
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['NftTransfer'], typing.List['NftTransfer']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'result':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NftTransfer':
                    return super().__getitem__(i)
            block_exists = schemas.BoolSchema
            index_complete = schemas.BoolSchema
            __annotations__ = {
                "page": page,
                "page_size": page_size,
                "cursor": cursor,
                "result": result,
                "block_exists": block_exists,
                "index_complete": index_complete,
            }

    
    cursor: MetaOapg.properties.cursor
    result: MetaOapg.properties.result
    page: MetaOapg.properties.page
    page_size: MetaOapg.properties.page_size
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page_size"]) -> MetaOapg.properties.page_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cursor"]) -> MetaOapg.properties.cursor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_exists"]) -> MetaOapg.properties.block_exists: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["index_complete"]) -> MetaOapg.properties.index_complete: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["page", "page_size", "cursor", "result", "block_exists", "index_complete", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page_size"]) -> MetaOapg.properties.page_size: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cursor"]) -> MetaOapg.properties.cursor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_exists"]) -> typing.Union[MetaOapg.properties.block_exists, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["index_complete"]) -> typing.Union[MetaOapg.properties.index_complete, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["page", "page_size", "cursor", "result", "block_exists", "index_complete", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        cursor: typing.Union[MetaOapg.properties.cursor, str, ],
        result: typing.Union[MetaOapg.properties.result, list, tuple, ],
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, ],
        page_size: typing.Union[MetaOapg.properties.page_size, decimal.Decimal, int, ],
        block_exists: typing.Union[MetaOapg.properties.block_exists, bool, schemas.Unset] = schemas.unset,
        index_complete: typing.Union[MetaOapg.properties.index_complete, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NftTransferCollection':
        return super().__new__(
            cls,
            *args,
            cursor=cursor,
            result=result,
            page=page,
            page_size=page_size,
            block_exists=block_exists,
            index_complete=index_complete,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.nft_transfer import NftTransfer
