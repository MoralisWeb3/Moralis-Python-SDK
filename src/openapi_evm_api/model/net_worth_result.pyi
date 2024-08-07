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


class NetWorthResult(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "chains",
            "total_networth_usd",
        }
        
        class properties:
            total_networth_usd = schemas.StrSchema
            
            
            class chains(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ChainNetWorth']:
                        return ChainNetWorth
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ChainNetWorth'], typing.List['ChainNetWorth']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'chains':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ChainNetWorth':
                    return super().__getitem__(i)
            
            
            class unsupported_chain_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'unsupported_chain_ids':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class unavailable_chains(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UnavailableChainNetWorth']:
                        return UnavailableChainNetWorth
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UnavailableChainNetWorth'], typing.List['UnavailableChainNetWorth']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'unavailable_chains':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UnavailableChainNetWorth':
                    return super().__getitem__(i)
            __annotations__ = {
                "total_networth_usd": total_networth_usd,
                "chains": chains,
                "unsupported_chain_ids": unsupported_chain_ids,
                "unavailable_chains": unavailable_chains,
            }

    
    chains: MetaOapg.properties.chains
    total_networth_usd: MetaOapg.properties.total_networth_usd
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_networth_usd"]) -> MetaOapg.properties.total_networth_usd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chains"]) -> MetaOapg.properties.chains: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unsupported_chain_ids"]) -> MetaOapg.properties.unsupported_chain_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unavailable_chains"]) -> MetaOapg.properties.unavailable_chains: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_networth_usd", "chains", "unsupported_chain_ids", "unavailable_chains", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_networth_usd"]) -> MetaOapg.properties.total_networth_usd: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chains"]) -> MetaOapg.properties.chains: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unsupported_chain_ids"]) -> typing.Union[MetaOapg.properties.unsupported_chain_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unavailable_chains"]) -> typing.Union[MetaOapg.properties.unavailable_chains, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_networth_usd", "chains", "unsupported_chain_ids", "unavailable_chains", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        chains: typing.Union[MetaOapg.properties.chains, list, tuple, ],
        total_networth_usd: typing.Union[MetaOapg.properties.total_networth_usd, str, ],
        unsupported_chain_ids: typing.Union[MetaOapg.properties.unsupported_chain_ids, list, tuple, schemas.Unset] = schemas.unset,
        unavailable_chains: typing.Union[MetaOapg.properties.unavailable_chains, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NetWorthResult':
        return super().__new__(
            cls,
            *args,
            chains=chains,
            total_networth_usd=total_networth_usd,
            unsupported_chain_ids=unsupported_chain_ids,
            unavailable_chains=unavailable_chains,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.chain_net_worth import ChainNetWorth
from openapi_evm_api.model.unavailable_chain_net_worth import UnavailableChainNetWorth
