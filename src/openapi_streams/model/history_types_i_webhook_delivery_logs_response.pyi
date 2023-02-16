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


class HistoryTypesIWebhookDeliveryLogsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "result",
            "total",
        }
        
        class properties:
            
            
            class result(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['IWebhookDeliveryLogsModel']:
                        return IWebhookDeliveryLogsModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['IWebhookDeliveryLogsModel'], typing.List['IWebhookDeliveryLogsModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'result':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'IWebhookDeliveryLogsModel':
                    return super().__getitem__(i)
            total = schemas.Float64Schema
            cursor = schemas.StrSchema
            __annotations__ = {
                "result": result,
                "total": total,
                "cursor": cursor,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    result: MetaOapg.properties.result
    total: MetaOapg.properties.total
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cursor"]) -> MetaOapg.properties.cursor: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["result"], typing_extensions.Literal["total"], typing_extensions.Literal["cursor"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cursor"]) -> typing.Union[MetaOapg.properties.cursor, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["result"], typing_extensions.Literal["total"], typing_extensions.Literal["cursor"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        result: typing.Union[MetaOapg.properties.result, list, tuple, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, ],
        cursor: typing.Union[MetaOapg.properties.cursor, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'HistoryTypesIWebhookDeliveryLogsResponse':
        return super().__new__(
            cls,
            *args,
            result=result,
            total=total,
            cursor=cursor,
            _configuration=_configuration,
        )

from openapi_streams.model.i_webhook_delivery_logs_model import IWebhookDeliveryLogsModel
