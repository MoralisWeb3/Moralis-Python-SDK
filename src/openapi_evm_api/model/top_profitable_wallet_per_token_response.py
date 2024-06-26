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


class TopProfitableWalletPerTokenResponse(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "count_of_trades",
            "avg_sell_price_usd",
            "total_tokens_bought",
            "total_usd_invested",
            "address",
            "realized_profit_usd",
            "realized_profit_percentage",
            "avg_buy_price_usd",
            "total_tokens_sold",
            "avg_cost_of_quantity_sold",
            "total_sold_usd",
        }
        
        class properties:
            avg_buy_price_usd = schemas.StrSchema
            avg_cost_of_quantity_sold = schemas.StrSchema
            avg_sell_price_usd = schemas.StrSchema
            count_of_trades = schemas.NumberSchema
            realized_profit_percentage = schemas.NumberSchema
            realized_profit_usd = schemas.StrSchema
            total_sold_usd = schemas.StrSchema
            total_tokens_bought = schemas.StrSchema
            total_tokens_sold = schemas.StrSchema
            total_usd_invested = schemas.StrSchema
            address = schemas.StrSchema
            __annotations__ = {
                "avg_buy_price_usd": avg_buy_price_usd,
                "avg_cost_of_quantity_sold": avg_cost_of_quantity_sold,
                "avg_sell_price_usd": avg_sell_price_usd,
                "count_of_trades": count_of_trades,
                "realized_profit_percentage": realized_profit_percentage,
                "realized_profit_usd": realized_profit_usd,
                "total_sold_usd": total_sold_usd,
                "total_tokens_bought": total_tokens_bought,
                "total_tokens_sold": total_tokens_sold,
                "total_usd_invested": total_usd_invested,
                "address": address,
            }

    
    count_of_trades: MetaOapg.properties.count_of_trades
    avg_sell_price_usd: MetaOapg.properties.avg_sell_price_usd
    total_tokens_bought: MetaOapg.properties.total_tokens_bought
    total_usd_invested: MetaOapg.properties.total_usd_invested
    address: MetaOapg.properties.address
    realized_profit_usd: MetaOapg.properties.realized_profit_usd
    realized_profit_percentage: MetaOapg.properties.realized_profit_percentage
    avg_buy_price_usd: MetaOapg.properties.avg_buy_price_usd
    total_tokens_sold: MetaOapg.properties.total_tokens_sold
    avg_cost_of_quantity_sold: MetaOapg.properties.avg_cost_of_quantity_sold
    total_sold_usd: MetaOapg.properties.total_sold_usd
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avg_buy_price_usd"]) -> MetaOapg.properties.avg_buy_price_usd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avg_cost_of_quantity_sold"]) -> MetaOapg.properties.avg_cost_of_quantity_sold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avg_sell_price_usd"]) -> MetaOapg.properties.avg_sell_price_usd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count_of_trades"]) -> MetaOapg.properties.count_of_trades: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realized_profit_percentage"]) -> MetaOapg.properties.realized_profit_percentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realized_profit_usd"]) -> MetaOapg.properties.realized_profit_usd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_sold_usd"]) -> MetaOapg.properties.total_sold_usd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_tokens_bought"]) -> MetaOapg.properties.total_tokens_bought: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_tokens_sold"]) -> MetaOapg.properties.total_tokens_sold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_usd_invested"]) -> MetaOapg.properties.total_usd_invested: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["avg_buy_price_usd", "avg_cost_of_quantity_sold", "avg_sell_price_usd", "count_of_trades", "realized_profit_percentage", "realized_profit_usd", "total_sold_usd", "total_tokens_bought", "total_tokens_sold", "total_usd_invested", "address", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avg_buy_price_usd"]) -> MetaOapg.properties.avg_buy_price_usd: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avg_cost_of_quantity_sold"]) -> MetaOapg.properties.avg_cost_of_quantity_sold: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avg_sell_price_usd"]) -> MetaOapg.properties.avg_sell_price_usd: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count_of_trades"]) -> MetaOapg.properties.count_of_trades: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realized_profit_percentage"]) -> MetaOapg.properties.realized_profit_percentage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realized_profit_usd"]) -> MetaOapg.properties.realized_profit_usd: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_sold_usd"]) -> MetaOapg.properties.total_sold_usd: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_tokens_bought"]) -> MetaOapg.properties.total_tokens_bought: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_tokens_sold"]) -> MetaOapg.properties.total_tokens_sold: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_usd_invested"]) -> MetaOapg.properties.total_usd_invested: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["avg_buy_price_usd", "avg_cost_of_quantity_sold", "avg_sell_price_usd", "count_of_trades", "realized_profit_percentage", "realized_profit_usd", "total_sold_usd", "total_tokens_bought", "total_tokens_sold", "total_usd_invested", "address", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        count_of_trades: typing.Union[MetaOapg.properties.count_of_trades, decimal.Decimal, int, float, ],
        avg_sell_price_usd: typing.Union[MetaOapg.properties.avg_sell_price_usd, str, ],
        total_tokens_bought: typing.Union[MetaOapg.properties.total_tokens_bought, str, ],
        total_usd_invested: typing.Union[MetaOapg.properties.total_usd_invested, str, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        realized_profit_usd: typing.Union[MetaOapg.properties.realized_profit_usd, str, ],
        realized_profit_percentage: typing.Union[MetaOapg.properties.realized_profit_percentage, decimal.Decimal, int, float, ],
        avg_buy_price_usd: typing.Union[MetaOapg.properties.avg_buy_price_usd, str, ],
        total_tokens_sold: typing.Union[MetaOapg.properties.total_tokens_sold, str, ],
        avg_cost_of_quantity_sold: typing.Union[MetaOapg.properties.avg_cost_of_quantity_sold, str, ],
        total_sold_usd: typing.Union[MetaOapg.properties.total_sold_usd, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TopProfitableWalletPerTokenResponse':
        return super().__new__(
            cls,
            *args,
            count_of_trades=count_of_trades,
            avg_sell_price_usd=avg_sell_price_usd,
            total_tokens_bought=total_tokens_bought,
            total_usd_invested=total_usd_invested,
            address=address,
            realized_profit_usd=realized_profit_usd,
            realized_profit_percentage=realized_profit_percentage,
            avg_buy_price_usd=avg_buy_price_usd,
            total_tokens_sold=total_tokens_sold,
            avg_cost_of_quantity_sold=avg_cost_of_quantity_sold,
            total_sold_usd=total_sold_usd,
            _configuration=_configuration,
            **kwargs,
        )
