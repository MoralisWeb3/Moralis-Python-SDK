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


class IWebhookDeliveryLogsModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "createdAt",
            "retries",
            "chain",
            "streamId",
            "blockNumber",
            "errorMessage",
            "id",
            "tag",
            "type",
            "deliveryStatus",
            "webhookUrl",
        }
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['UUID']:
                return UUID
            streamId = schemas.StrSchema
            chain = schemas.StrSchema
            webhookUrl = schemas.StrSchema
            tag = schemas.StrSchema
            retries = schemas.Float64Schema
            
            
            class deliveryStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("failed")
                
                @schemas.classproperty
                def SUCCESS(cls):
                    return cls("success")
            blockNumber = schemas.Float64Schema
            errorMessage = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EVM(cls):
                    return cls("evm")
                
                @schemas.classproperty
                def APTOS(cls):
                    return cls("aptos")
            createdAt = schemas.DateTimeSchema
            __annotations__ = {
                "id": id,
                "streamId": streamId,
                "chain": chain,
                "webhookUrl": webhookUrl,
                "tag": tag,
                "retries": retries,
                "deliveryStatus": deliveryStatus,
                "blockNumber": blockNumber,
                "errorMessage": errorMessage,
                "type": type,
                "createdAt": createdAt,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    createdAt: MetaOapg.properties.createdAt
    retries: MetaOapg.properties.retries
    chain: MetaOapg.properties.chain
    streamId: MetaOapg.properties.streamId
    blockNumber: MetaOapg.properties.blockNumber
    errorMessage: MetaOapg.properties.errorMessage
    id: 'UUID'
    tag: MetaOapg.properties.tag
    type: MetaOapg.properties.type
    deliveryStatus: MetaOapg.properties.deliveryStatus
    webhookUrl: MetaOapg.properties.webhookUrl
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retries"]) -> MetaOapg.properties.retries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chain"]) -> MetaOapg.properties.chain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["streamId"]) -> MetaOapg.properties.streamId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blockNumber"]) -> MetaOapg.properties.blockNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorMessage"]) -> MetaOapg.properties.errorMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'UUID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deliveryStatus"]) -> MetaOapg.properties.deliveryStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookUrl"]) -> MetaOapg.properties.webhookUrl: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["createdAt"], typing_extensions.Literal["retries"], typing_extensions.Literal["chain"], typing_extensions.Literal["streamId"], typing_extensions.Literal["blockNumber"], typing_extensions.Literal["errorMessage"], typing_extensions.Literal["id"], typing_extensions.Literal["tag"], typing_extensions.Literal["type"], typing_extensions.Literal["deliveryStatus"], typing_extensions.Literal["webhookUrl"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retries"]) -> MetaOapg.properties.retries: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chain"]) -> MetaOapg.properties.chain: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["streamId"]) -> MetaOapg.properties.streamId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blockNumber"]) -> MetaOapg.properties.blockNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorMessage"]) -> MetaOapg.properties.errorMessage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'UUID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deliveryStatus"]) -> MetaOapg.properties.deliveryStatus: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookUrl"]) -> MetaOapg.properties.webhookUrl: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["createdAt"], typing_extensions.Literal["retries"], typing_extensions.Literal["chain"], typing_extensions.Literal["streamId"], typing_extensions.Literal["blockNumber"], typing_extensions.Literal["errorMessage"], typing_extensions.Literal["id"], typing_extensions.Literal["tag"], typing_extensions.Literal["type"], typing_extensions.Literal["deliveryStatus"], typing_extensions.Literal["webhookUrl"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, datetime, ],
        retries: typing.Union[MetaOapg.properties.retries, decimal.Decimal, int, float, ],
        chain: typing.Union[MetaOapg.properties.chain, str, ],
        streamId: typing.Union[MetaOapg.properties.streamId, str, ],
        blockNumber: typing.Union[MetaOapg.properties.blockNumber, decimal.Decimal, int, float, ],
        errorMessage: typing.Union[MetaOapg.properties.errorMessage, str, ],
        id: 'UUID',
        tag: typing.Union[MetaOapg.properties.tag, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        deliveryStatus: typing.Union[MetaOapg.properties.deliveryStatus, str, ],
        webhookUrl: typing.Union[MetaOapg.properties.webhookUrl, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IWebhookDeliveryLogsModel':
        return super().__new__(
            cls,
            *args,
            createdAt=createdAt,
            retries=retries,
            chain=chain,
            streamId=streamId,
            blockNumber=blockNumber,
            errorMessage=errorMessage,
            id=id,
            tag=tag,
            type=type,
            deliveryStatus=deliveryStatus,
            webhookUrl=webhookUrl,
            _configuration=_configuration,
        )

from openapi_streams.model.uuid import UUID
