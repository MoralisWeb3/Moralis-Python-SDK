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


class WalletHistoryTransaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "gas_price",
            "summary",
            "receipt_status",
            "receipt_cumulative_gas_used",
            "block_hash",
            "block_number",
            "native_transfers",
            "transaction_index",
            "nonce",
            "erc20_transfers",
            "nft_transfers",
            "receipt_gas_used",
            "block_timestamp",
            "category",
            "from_address",
            "value",
            "hash",
        }
        
        class properties:
            hash = schemas.StrSchema
            nonce = schemas.StrSchema
            transaction_index = schemas.StrSchema
            from_address = schemas.StrSchema
            value = schemas.StrSchema
            gas_price = schemas.StrSchema
            receipt_cumulative_gas_used = schemas.StrSchema
            receipt_gas_used = schemas.StrSchema
            receipt_status = schemas.StrSchema
            block_timestamp = schemas.StrSchema
            block_number = schemas.StrSchema
            block_hash = schemas.StrSchema
        
            @staticmethod
            def category() -> typing.Type['ETransactionCategory']:
                return ETransactionCategory
            summary = schemas.StrSchema
            
            
            class nft_transfers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WalletHistoryNftTransfer']:
                        return WalletHistoryNftTransfer
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WalletHistoryNftTransfer'], typing.List['WalletHistoryNftTransfer']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nft_transfers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WalletHistoryNftTransfer':
                    return super().__getitem__(i)
            
            
            class erc20_transfers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WalletHistoryErc20Transfer']:
                        return WalletHistoryErc20Transfer
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WalletHistoryErc20Transfer'], typing.List['WalletHistoryErc20Transfer']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'erc20_transfers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WalletHistoryErc20Transfer':
                    return super().__getitem__(i)
            
            
            class native_transfers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NativeTransfer']:
                        return NativeTransfer
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['NativeTransfer'], typing.List['NativeTransfer']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'native_transfers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NativeTransfer':
                    return super().__getitem__(i)
            from_address_entity = schemas.StrSchema
            from_address_entity_logo = schemas.StrSchema
            
            
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
            to_address_entity = schemas.StrSchema
            to_address_entity_logo = schemas.StrSchema
            
            
            class to_address(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'to_address':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
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
            gas = schemas.StrSchema
            input = schemas.StrSchema
            
            
            class receipt_contract_address(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'receipt_contract_address':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            transaction_fee = schemas.StrSchema
            
            
            class internal_transactions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['InternalTransaction']:
                        return InternalTransaction
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['InternalTransaction'], typing.List['InternalTransaction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'internal_transactions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'InternalTransaction':
                    return super().__getitem__(i)
        
            @staticmethod
            def contract_interactions() -> typing.Type['ResolveContractInteractionResponse']:
                return ResolveContractInteractionResponse
            possible_spam = schemas.BoolSchema
            method_label = schemas.StrSchema
            
            
            class logs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LogVerbose']:
                        return LogVerbose
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['LogVerbose'], typing.List['LogVerbose']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'logs':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LogVerbose':
                    return super().__getitem__(i)
            __annotations__ = {
                "hash": hash,
                "nonce": nonce,
                "transaction_index": transaction_index,
                "from_address": from_address,
                "value": value,
                "gas_price": gas_price,
                "receipt_cumulative_gas_used": receipt_cumulative_gas_used,
                "receipt_gas_used": receipt_gas_used,
                "receipt_status": receipt_status,
                "block_timestamp": block_timestamp,
                "block_number": block_number,
                "block_hash": block_hash,
                "category": category,
                "summary": summary,
                "nft_transfers": nft_transfers,
                "erc20_transfers": erc20_transfers,
                "native_transfers": native_transfers,
                "from_address_entity": from_address_entity,
                "from_address_entity_logo": from_address_entity_logo,
                "from_address_label": from_address_label,
                "to_address_entity": to_address_entity,
                "to_address_entity_logo": to_address_entity_logo,
                "to_address": to_address,
                "to_address_label": to_address_label,
                "gas": gas,
                "input": input,
                "receipt_contract_address": receipt_contract_address,
                "transaction_fee": transaction_fee,
                "internal_transactions": internal_transactions,
                "contract_interactions": contract_interactions,
                "possible_spam": possible_spam,
                "method_label": method_label,
                "logs": logs,
            }
    
    gas_price: MetaOapg.properties.gas_price
    summary: MetaOapg.properties.summary
    receipt_status: MetaOapg.properties.receipt_status
    receipt_cumulative_gas_used: MetaOapg.properties.receipt_cumulative_gas_used
    block_hash: MetaOapg.properties.block_hash
    block_number: MetaOapg.properties.block_number
    native_transfers: MetaOapg.properties.native_transfers
    transaction_index: MetaOapg.properties.transaction_index
    nonce: MetaOapg.properties.nonce
    erc20_transfers: MetaOapg.properties.erc20_transfers
    nft_transfers: MetaOapg.properties.nft_transfers
    receipt_gas_used: MetaOapg.properties.receipt_gas_used
    block_timestamp: MetaOapg.properties.block_timestamp
    category: 'ETransactionCategory'
    from_address: MetaOapg.properties.from_address
    value: MetaOapg.properties.value
    hash: MetaOapg.properties.hash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gas_price"]) -> MetaOapg.properties.gas_price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_cumulative_gas_used"]) -> MetaOapg.properties.receipt_cumulative_gas_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_gas_used"]) -> MetaOapg.properties.receipt_gas_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_status"]) -> MetaOapg.properties.receipt_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> 'ETransactionCategory': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nft_transfers"]) -> MetaOapg.properties.nft_transfers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["erc20_transfers"]) -> MetaOapg.properties.erc20_transfers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["native_transfers"]) -> MetaOapg.properties.native_transfers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address_entity"]) -> MetaOapg.properties.from_address_entity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address_entity_logo"]) -> MetaOapg.properties.from_address_entity_logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address_label"]) -> MetaOapg.properties.from_address_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address_entity"]) -> MetaOapg.properties.to_address_entity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address_entity_logo"]) -> MetaOapg.properties.to_address_entity_logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address_label"]) -> MetaOapg.properties.to_address_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gas"]) -> MetaOapg.properties.gas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input"]) -> MetaOapg.properties.input: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_contract_address"]) -> MetaOapg.properties.receipt_contract_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_fee"]) -> MetaOapg.properties.transaction_fee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internal_transactions"]) -> MetaOapg.properties.internal_transactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_interactions"]) -> 'ResolveContractInteractionResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["method_label"]) -> MetaOapg.properties.method_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logs"]) -> MetaOapg.properties.logs: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hash", "nonce", "transaction_index", "from_address", "value", "gas_price", "receipt_cumulative_gas_used", "receipt_gas_used", "receipt_status", "block_timestamp", "block_number", "block_hash", "category", "summary", "nft_transfers", "erc20_transfers", "native_transfers", "from_address_entity", "from_address_entity_logo", "from_address_label", "to_address_entity", "to_address_entity_logo", "to_address", "to_address_label", "gas", "input", "receipt_contract_address", "transaction_fee", "internal_transactions", "contract_interactions", "possible_spam", "method_label", "logs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gas_price"]) -> MetaOapg.properties.gas_price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_cumulative_gas_used"]) -> MetaOapg.properties.receipt_cumulative_gas_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_gas_used"]) -> MetaOapg.properties.receipt_gas_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_status"]) -> MetaOapg.properties.receipt_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> 'ETransactionCategory': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nft_transfers"]) -> MetaOapg.properties.nft_transfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["erc20_transfers"]) -> MetaOapg.properties.erc20_transfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["native_transfers"]) -> MetaOapg.properties.native_transfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address_entity"]) -> typing.Union[MetaOapg.properties.from_address_entity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address_entity_logo"]) -> typing.Union[MetaOapg.properties.from_address_entity_logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address_label"]) -> typing.Union[MetaOapg.properties.from_address_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address_entity"]) -> typing.Union[MetaOapg.properties.to_address_entity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address_entity_logo"]) -> typing.Union[MetaOapg.properties.to_address_entity_logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address"]) -> typing.Union[MetaOapg.properties.to_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address_label"]) -> typing.Union[MetaOapg.properties.to_address_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gas"]) -> typing.Union[MetaOapg.properties.gas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input"]) -> typing.Union[MetaOapg.properties.input, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_contract_address"]) -> typing.Union[MetaOapg.properties.receipt_contract_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_fee"]) -> typing.Union[MetaOapg.properties.transaction_fee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internal_transactions"]) -> typing.Union[MetaOapg.properties.internal_transactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_interactions"]) -> typing.Union['ResolveContractInteractionResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["possible_spam"]) -> typing.Union[MetaOapg.properties.possible_spam, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["method_label"]) -> typing.Union[MetaOapg.properties.method_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logs"]) -> typing.Union[MetaOapg.properties.logs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hash", "nonce", "transaction_index", "from_address", "value", "gas_price", "receipt_cumulative_gas_used", "receipt_gas_used", "receipt_status", "block_timestamp", "block_number", "block_hash", "category", "summary", "nft_transfers", "erc20_transfers", "native_transfers", "from_address_entity", "from_address_entity_logo", "from_address_label", "to_address_entity", "to_address_entity_logo", "to_address", "to_address_label", "gas", "input", "receipt_contract_address", "transaction_fee", "internal_transactions", "contract_interactions", "possible_spam", "method_label", "logs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        gas_price: typing.Union[MetaOapg.properties.gas_price, str, ],
        summary: typing.Union[MetaOapg.properties.summary, str, ],
        receipt_status: typing.Union[MetaOapg.properties.receipt_status, str, ],
        receipt_cumulative_gas_used: typing.Union[MetaOapg.properties.receipt_cumulative_gas_used, str, ],
        block_hash: typing.Union[MetaOapg.properties.block_hash, str, ],
        block_number: typing.Union[MetaOapg.properties.block_number, str, ],
        native_transfers: typing.Union[MetaOapg.properties.native_transfers, list, tuple, ],
        transaction_index: typing.Union[MetaOapg.properties.transaction_index, str, ],
        nonce: typing.Union[MetaOapg.properties.nonce, str, ],
        erc20_transfers: typing.Union[MetaOapg.properties.erc20_transfers, list, tuple, ],
        nft_transfers: typing.Union[MetaOapg.properties.nft_transfers, list, tuple, ],
        receipt_gas_used: typing.Union[MetaOapg.properties.receipt_gas_used, str, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, str, ],
        category: 'ETransactionCategory',
        from_address: typing.Union[MetaOapg.properties.from_address, str, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        hash: typing.Union[MetaOapg.properties.hash, str, ],
        from_address_entity: typing.Union[MetaOapg.properties.from_address_entity, str, schemas.Unset] = schemas.unset,
        from_address_entity_logo: typing.Union[MetaOapg.properties.from_address_entity_logo, str, schemas.Unset] = schemas.unset,
        from_address_label: typing.Union[MetaOapg.properties.from_address_label, None, str, schemas.Unset] = schemas.unset,
        to_address_entity: typing.Union[MetaOapg.properties.to_address_entity, str, schemas.Unset] = schemas.unset,
        to_address_entity_logo: typing.Union[MetaOapg.properties.to_address_entity_logo, str, schemas.Unset] = schemas.unset,
        to_address: typing.Union[MetaOapg.properties.to_address, None, str, schemas.Unset] = schemas.unset,
        to_address_label: typing.Union[MetaOapg.properties.to_address_label, None, str, schemas.Unset] = schemas.unset,
        gas: typing.Union[MetaOapg.properties.gas, str, schemas.Unset] = schemas.unset,
        input: typing.Union[MetaOapg.properties.input, str, schemas.Unset] = schemas.unset,
        receipt_contract_address: typing.Union[MetaOapg.properties.receipt_contract_address, None, str, schemas.Unset] = schemas.unset,
        transaction_fee: typing.Union[MetaOapg.properties.transaction_fee, str, schemas.Unset] = schemas.unset,
        internal_transactions: typing.Union[MetaOapg.properties.internal_transactions, list, tuple, schemas.Unset] = schemas.unset,
        contract_interactions: typing.Union['ResolveContractInteractionResponse', schemas.Unset] = schemas.unset,
        possible_spam: typing.Union[MetaOapg.properties.possible_spam, bool, schemas.Unset] = schemas.unset,
        method_label: typing.Union[MetaOapg.properties.method_label, str, schemas.Unset] = schemas.unset,
        logs: typing.Union[MetaOapg.properties.logs, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletHistoryTransaction':
        return super().__new__(
            cls,
            *args,
            gas_price=gas_price,
            summary=summary,
            receipt_status=receipt_status,
            receipt_cumulative_gas_used=receipt_cumulative_gas_used,
            block_hash=block_hash,
            block_number=block_number,
            native_transfers=native_transfers,
            transaction_index=transaction_index,
            nonce=nonce,
            erc20_transfers=erc20_transfers,
            nft_transfers=nft_transfers,
            receipt_gas_used=receipt_gas_used,
            block_timestamp=block_timestamp,
            category=category,
            from_address=from_address,
            value=value,
            hash=hash,
            from_address_entity=from_address_entity,
            from_address_entity_logo=from_address_entity_logo,
            from_address_label=from_address_label,
            to_address_entity=to_address_entity,
            to_address_entity_logo=to_address_entity_logo,
            to_address=to_address,
            to_address_label=to_address_label,
            gas=gas,
            input=input,
            receipt_contract_address=receipt_contract_address,
            transaction_fee=transaction_fee,
            internal_transactions=internal_transactions,
            contract_interactions=contract_interactions,
            possible_spam=possible_spam,
            method_label=method_label,
            logs=logs,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.e_transaction_category import ETransactionCategory
from openapi_evm_api.model.internal_transaction import InternalTransaction
from openapi_evm_api.model.log_verbose import LogVerbose
from openapi_evm_api.model.native_transfer import NativeTransfer
from openapi_evm_api.model.resolve_contract_interaction_response import ResolveContractInteractionResponse
from openapi_evm_api.model.wallet_history_erc20_transfer import WalletHistoryErc20Transfer
from openapi_evm_api.model.wallet_history_nft_transfer import WalletHistoryNftTransfer