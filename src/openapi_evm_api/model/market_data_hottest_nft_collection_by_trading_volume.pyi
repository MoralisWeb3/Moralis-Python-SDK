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


class MarketDataHottestNFTCollectionByTradingVolume(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class items(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "collection_image",
                    "floor_price_usd",
                    "collection_title",
                    "market_cap_24hr_percent_change",
                    "volume_24hr_percent_change",
                    "collection_address",
                    "rank",
                    "volume_usd",
                    "market_cap_usd",
                    "floor_price_24hr_percent_change",
                }
                
                class properties:
                    rank = schemas.IntSchema
                    collection_title = schemas.StrSchema
                    collection_image = schemas.StrSchema
                    floor_price_usd = schemas.StrSchema
                    floor_price_24hr_percent_change = schemas.StrSchema
                    volume_usd = schemas.StrSchema
                    volume_24hr_percent_change = schemas.StrSchema
                    average_price_usd = schemas.StrSchema
                    collection_address = schemas.StrSchema
                    average_price = schemas.StrSchema
                    floor_price = schemas.StrSchema
                    floor_price_usd_24hr_percent_change = schemas.StrSchema
                    floor_price_7d_percent_change = schemas.StrSchema
                    floor_price_usd_7d_percent_change = schemas.StrSchema
                    floor_price_30d_percent_change = schemas.StrSchema
                    floor_price_usd_30d_percent_change = schemas.StrSchema
                    __annotations__ = {
                        "rank": rank,
                        "collection_title": collection_title,
                        "collection_image": collection_image,
                        "floor_price_usd": floor_price_usd,
                        "floor_price_24hr_percent_change": floor_price_24hr_percent_change,
                        "volume_usd": volume_usd,
                        "volume_24hr_percent_change": volume_24hr_percent_change,
                        "average_price_usd": average_price_usd,
                        "collection_address": collection_address,
                        "average_price": average_price,
                        "floor_price": floor_price,
                        "floor_price_usd_24hr_percent_change": floor_price_usd_24hr_percent_change,
                        "floor_price_7d_percent_change": floor_price_7d_percent_change,
                        "floor_price_usd_7d_percent_change": floor_price_usd_7d_percent_change,
                        "floor_price_30d_percent_change": floor_price_30d_percent_change,
                        "floor_price_usd_30d_percent_change": floor_price_usd_30d_percent_change,
                    }
        
            
            collection_image: MetaOapg.properties.collection_image
            floor_price_usd: MetaOapg.properties.floor_price_usd
            collection_title: MetaOapg.properties.collection_title
            market_cap_24hr_percent_change: schemas.AnyTypeSchema
            volume_24hr_percent_change: MetaOapg.properties.volume_24hr_percent_change
            collection_address: MetaOapg.properties.collection_address
            rank: MetaOapg.properties.rank
            volume_usd: MetaOapg.properties.volume_usd
            market_cap_usd: schemas.AnyTypeSchema
            floor_price_24hr_percent_change: MetaOapg.properties.floor_price_24hr_percent_change
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["rank"]) -> MetaOapg.properties.rank: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["collection_title"]) -> MetaOapg.properties.collection_title: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["collection_image"]) -> MetaOapg.properties.collection_image: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["floor_price_usd"]) -> MetaOapg.properties.floor_price_usd: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["floor_price_24hr_percent_change"]) -> MetaOapg.properties.floor_price_24hr_percent_change: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["volume_usd"]) -> MetaOapg.properties.volume_usd: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["volume_24hr_percent_change"]) -> MetaOapg.properties.volume_24hr_percent_change: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["average_price_usd"]) -> MetaOapg.properties.average_price_usd: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["collection_address"]) -> MetaOapg.properties.collection_address: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["average_price"]) -> MetaOapg.properties.average_price: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["floor_price"]) -> MetaOapg.properties.floor_price: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["floor_price_usd_24hr_percent_change"]) -> MetaOapg.properties.floor_price_usd_24hr_percent_change: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["floor_price_7d_percent_change"]) -> MetaOapg.properties.floor_price_7d_percent_change: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["floor_price_usd_7d_percent_change"]) -> MetaOapg.properties.floor_price_usd_7d_percent_change: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["floor_price_30d_percent_change"]) -> MetaOapg.properties.floor_price_30d_percent_change: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["floor_price_usd_30d_percent_change"]) -> MetaOapg.properties.floor_price_usd_30d_percent_change: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["rank", "collection_title", "collection_image", "floor_price_usd", "floor_price_24hr_percent_change", "volume_usd", "volume_24hr_percent_change", "average_price_usd", "collection_address", "average_price", "floor_price", "floor_price_usd_24hr_percent_change", "floor_price_7d_percent_change", "floor_price_usd_7d_percent_change", "floor_price_30d_percent_change", "floor_price_usd_30d_percent_change", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["rank"]) -> MetaOapg.properties.rank: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["collection_title"]) -> MetaOapg.properties.collection_title: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["collection_image"]) -> MetaOapg.properties.collection_image: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["floor_price_usd"]) -> MetaOapg.properties.floor_price_usd: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["floor_price_24hr_percent_change"]) -> MetaOapg.properties.floor_price_24hr_percent_change: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["volume_usd"]) -> MetaOapg.properties.volume_usd: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["volume_24hr_percent_change"]) -> MetaOapg.properties.volume_24hr_percent_change: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["average_price_usd"]) -> typing.Union[MetaOapg.properties.average_price_usd, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["collection_address"]) -> MetaOapg.properties.collection_address: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["average_price"]) -> typing.Union[MetaOapg.properties.average_price, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["floor_price"]) -> typing.Union[MetaOapg.properties.floor_price, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["floor_price_usd_24hr_percent_change"]) -> typing.Union[MetaOapg.properties.floor_price_usd_24hr_percent_change, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["floor_price_7d_percent_change"]) -> typing.Union[MetaOapg.properties.floor_price_7d_percent_change, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["floor_price_usd_7d_percent_change"]) -> typing.Union[MetaOapg.properties.floor_price_usd_7d_percent_change, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["floor_price_30d_percent_change"]) -> typing.Union[MetaOapg.properties.floor_price_30d_percent_change, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["floor_price_usd_30d_percent_change"]) -> typing.Union[MetaOapg.properties.floor_price_usd_30d_percent_change, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["rank", "collection_title", "collection_image", "floor_price_usd", "floor_price_24hr_percent_change", "volume_usd", "volume_24hr_percent_change", "average_price_usd", "collection_address", "average_price", "floor_price", "floor_price_usd_24hr_percent_change", "floor_price_7d_percent_change", "floor_price_usd_7d_percent_change", "floor_price_30d_percent_change", "floor_price_usd_30d_percent_change", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                collection_image: typing.Union[MetaOapg.properties.collection_image, str, ],
                floor_price_usd: typing.Union[MetaOapg.properties.floor_price_usd, str, ],
                collection_title: typing.Union[MetaOapg.properties.collection_title, str, ],
                market_cap_24hr_percent_change: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                volume_24hr_percent_change: typing.Union[MetaOapg.properties.volume_24hr_percent_change, str, ],
                collection_address: typing.Union[MetaOapg.properties.collection_address, str, ],
                rank: typing.Union[MetaOapg.properties.rank, decimal.Decimal, int, ],
                volume_usd: typing.Union[MetaOapg.properties.volume_usd, str, ],
                market_cap_usd: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                floor_price_24hr_percent_change: typing.Union[MetaOapg.properties.floor_price_24hr_percent_change, str, ],
                average_price_usd: typing.Union[MetaOapg.properties.average_price_usd, str, schemas.Unset] = schemas.unset,
                average_price: typing.Union[MetaOapg.properties.average_price, str, schemas.Unset] = schemas.unset,
                floor_price: typing.Union[MetaOapg.properties.floor_price, str, schemas.Unset] = schemas.unset,
                floor_price_usd_24hr_percent_change: typing.Union[MetaOapg.properties.floor_price_usd_24hr_percent_change, str, schemas.Unset] = schemas.unset,
                floor_price_7d_percent_change: typing.Union[MetaOapg.properties.floor_price_7d_percent_change, str, schemas.Unset] = schemas.unset,
                floor_price_usd_7d_percent_change: typing.Union[MetaOapg.properties.floor_price_usd_7d_percent_change, str, schemas.Unset] = schemas.unset,
                floor_price_30d_percent_change: typing.Union[MetaOapg.properties.floor_price_30d_percent_change, str, schemas.Unset] = schemas.unset,
                floor_price_usd_30d_percent_change: typing.Union[MetaOapg.properties.floor_price_usd_30d_percent_change, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    collection_image=collection_image,
                    floor_price_usd=floor_price_usd,
                    collection_title=collection_title,
                    market_cap_24hr_percent_change=market_cap_24hr_percent_change,
                    volume_24hr_percent_change=volume_24hr_percent_change,
                    collection_address=collection_address,
                    rank=rank,
                    volume_usd=volume_usd,
                    market_cap_usd=market_cap_usd,
                    floor_price_24hr_percent_change=floor_price_24hr_percent_change,
                    average_price_usd=average_price_usd,
                    average_price=average_price,
                    floor_price=floor_price,
                    floor_price_usd_24hr_percent_change=floor_price_usd_24hr_percent_change,
                    floor_price_7d_percent_change=floor_price_7d_percent_change,
                    floor_price_usd_7d_percent_change=floor_price_usd_7d_percent_change,
                    floor_price_30d_percent_change=floor_price_30d_percent_change,
                    floor_price_usd_30d_percent_change=floor_price_usd_30d_percent_change,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MarketDataHottestNFTCollectionByTradingVolume':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
