# coding: utf-8

"""
    Streams Api

    API that provides access to Moralis Streams  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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

from openapi_streams import schemas  # noqa: F401


class StreamsTypesStreamsStatusUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "status",
        }
        
        class properties:
        
            @staticmethod
            def status() -> typing.Type['StreamsStatus']:
                return StreamsStatus
            __annotations__ = {
                "status": status,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    status: 'StreamsStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'StreamsStatus': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'StreamsStatus': ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        status: 'StreamsStatus',
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'StreamsTypesStreamsStatusUpdate':
        return super().__new__(
            cls,
            *_args,
            status=status,
            _configuration=_configuration,
        )

from openapi_streams.model.streams_status import StreamsStatus
