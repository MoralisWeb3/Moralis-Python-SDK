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


class DiscoveryTokens(
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
                    "price_usd",
                    "experienced_net_buyers_change",
                    "chain_id",
                    "fully_diluted_valuation",
                    "token_address",
                    "net_volume_change_usd",
                    "twitter_followers",
                    "market_cap",
                    "volume_change_usd",
                    "security_score",
                    "token_logo",
                    "token_name",
                    "holders_change",
                    "price_percent_change_usd",
                    "token_symbol",
                    "liquidity_change_usd",
                }
                
                class properties:
                    chain_id = schemas.StrSchema
                    token_address = schemas.StrSchema
                    
                    
                    class token_name(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'token_name':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class token_symbol(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'token_symbol':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class token_logo(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'token_logo':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class price_usd(
                        schemas.NumberBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, decimal.Decimal, int, float, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'price_usd':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class security_score(
                        schemas.NumberBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, decimal.Decimal, int, float, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'security_score':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class market_cap(
                        schemas.NumberBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, decimal.Decimal, int, float, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'market_cap':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class fully_diluted_valuation(
                        schemas.NumberBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, decimal.Decimal, int, float, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'fully_diluted_valuation':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class twitter_followers(
                        schemas.NumberBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, decimal.Decimal, int, float, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'twitter_followers':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                
                    @staticmethod
                    def holders_change() -> typing.Type['TimeFrames']:
                        return TimeFrames
                
                    @staticmethod
                    def liquidity_change_usd() -> typing.Type['TimeFrames']:
                        return TimeFrames
                
                    @staticmethod
                    def experienced_net_buyers_change() -> typing.Type['TimeFrames']:
                        return TimeFrames
                
                    @staticmethod
                    def volume_change_usd() -> typing.Type['TimeFrames']:
                        return TimeFrames
                
                    @staticmethod
                    def net_volume_change_usd() -> typing.Type['TimeFrames']:
                        return TimeFrames
                
                    @staticmethod
                    def price_percent_change_usd() -> typing.Type['TimeFrames']:
                        return TimeFrames
                    __annotations__ = {
                        "chain_id": chain_id,
                        "token_address": token_address,
                        "token_name": token_name,
                        "token_symbol": token_symbol,
                        "token_logo": token_logo,
                        "price_usd": price_usd,
                        "security_score": security_score,
                        "market_cap": market_cap,
                        "fully_diluted_valuation": fully_diluted_valuation,
                        "twitter_followers": twitter_followers,
                        "holders_change": holders_change,
                        "liquidity_change_usd": liquidity_change_usd,
                        "experienced_net_buyers_change": experienced_net_buyers_change,
                        "volume_change_usd": volume_change_usd,
                        "net_volume_change_usd": net_volume_change_usd,
                        "price_percent_change_usd": price_percent_change_usd,
                    }
        
            
            price_usd: MetaOapg.properties.price_usd
            experienced_net_buyers_change: 'TimeFrames'
            chain_id: MetaOapg.properties.chain_id
            fully_diluted_valuation: MetaOapg.properties.fully_diluted_valuation
            token_address: MetaOapg.properties.token_address
            net_volume_change_usd: 'TimeFrames'
            twitter_followers: MetaOapg.properties.twitter_followers
            market_cap: MetaOapg.properties.market_cap
            volume_change_usd: 'TimeFrames'
            security_score: MetaOapg.properties.security_score
            token_logo: MetaOapg.properties.token_logo
            token_name: MetaOapg.properties.token_name
            holders_change: 'TimeFrames'
            price_percent_change_usd: 'TimeFrames'
            token_symbol: MetaOapg.properties.token_symbol
            liquidity_change_usd: 'TimeFrames'
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["chain_id"]) -> MetaOapg.properties.chain_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["token_name"]) -> MetaOapg.properties.token_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["price_usd"]) -> MetaOapg.properties.price_usd: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["security_score"]) -> MetaOapg.properties.security_score: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["market_cap"]) -> MetaOapg.properties.market_cap: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fully_diluted_valuation"]) -> MetaOapg.properties.fully_diluted_valuation: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["twitter_followers"]) -> MetaOapg.properties.twitter_followers: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["holders_change"]) -> 'TimeFrames': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["liquidity_change_usd"]) -> 'TimeFrames': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["experienced_net_buyers_change"]) -> 'TimeFrames': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["volume_change_usd"]) -> 'TimeFrames': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["net_volume_change_usd"]) -> 'TimeFrames': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["price_percent_change_usd"]) -> 'TimeFrames': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["chain_id", "token_address", "token_name", "token_symbol", "token_logo", "price_usd", "security_score", "market_cap", "fully_diluted_valuation", "twitter_followers", "holders_change", "liquidity_change_usd", "experienced_net_buyers_change", "volume_change_usd", "net_volume_change_usd", "price_percent_change_usd", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["chain_id"]) -> MetaOapg.properties.chain_id: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["token_name"]) -> MetaOapg.properties.token_name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["price_usd"]) -> MetaOapg.properties.price_usd: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["security_score"]) -> MetaOapg.properties.security_score: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["market_cap"]) -> MetaOapg.properties.market_cap: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fully_diluted_valuation"]) -> MetaOapg.properties.fully_diluted_valuation: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["twitter_followers"]) -> MetaOapg.properties.twitter_followers: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["holders_change"]) -> 'TimeFrames': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["liquidity_change_usd"]) -> 'TimeFrames': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["experienced_net_buyers_change"]) -> 'TimeFrames': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["volume_change_usd"]) -> 'TimeFrames': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["net_volume_change_usd"]) -> 'TimeFrames': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["price_percent_change_usd"]) -> 'TimeFrames': ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["chain_id", "token_address", "token_name", "token_symbol", "token_logo", "price_usd", "security_score", "market_cap", "fully_diluted_valuation", "twitter_followers", "holders_change", "liquidity_change_usd", "experienced_net_buyers_change", "volume_change_usd", "net_volume_change_usd", "price_percent_change_usd", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                price_usd: typing.Union[MetaOapg.properties.price_usd, None, decimal.Decimal, int, float, ],
                experienced_net_buyers_change: 'TimeFrames',
                chain_id: typing.Union[MetaOapg.properties.chain_id, str, ],
                fully_diluted_valuation: typing.Union[MetaOapg.properties.fully_diluted_valuation, None, decimal.Decimal, int, float, ],
                token_address: typing.Union[MetaOapg.properties.token_address, str, ],
                net_volume_change_usd: 'TimeFrames',
                twitter_followers: typing.Union[MetaOapg.properties.twitter_followers, None, decimal.Decimal, int, float, ],
                market_cap: typing.Union[MetaOapg.properties.market_cap, None, decimal.Decimal, int, float, ],
                volume_change_usd: 'TimeFrames',
                security_score: typing.Union[MetaOapg.properties.security_score, None, decimal.Decimal, int, float, ],
                token_logo: typing.Union[MetaOapg.properties.token_logo, None, str, ],
                token_name: typing.Union[MetaOapg.properties.token_name, None, str, ],
                holders_change: 'TimeFrames',
                price_percent_change_usd: 'TimeFrames',
                token_symbol: typing.Union[MetaOapg.properties.token_symbol, None, str, ],
                liquidity_change_usd: 'TimeFrames',
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    price_usd=price_usd,
                    experienced_net_buyers_change=experienced_net_buyers_change,
                    chain_id=chain_id,
                    fully_diluted_valuation=fully_diluted_valuation,
                    token_address=token_address,
                    net_volume_change_usd=net_volume_change_usd,
                    twitter_followers=twitter_followers,
                    market_cap=market_cap,
                    volume_change_usd=volume_change_usd,
                    security_score=security_score,
                    token_logo=token_logo,
                    token_name=token_name,
                    holders_change=holders_change,
                    price_percent_change_usd=price_percent_change_usd,
                    token_symbol=token_symbol,
                    liquidity_change_usd=liquidity_change_usd,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DiscoveryTokens':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)

from openapi_evm_api.model.time_frames import TimeFrames
