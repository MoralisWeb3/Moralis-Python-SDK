# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.2
    Generated by: https://openapi-generator.tech
"""

from openapi_evm_api.paths.transaction_transaction_hash_internal_transactions.get import GetInternalTransactions
from openapi_evm_api.paths.transaction_transaction_hash.get import GetTransaction
from openapi_evm_api.paths.transaction_transaction_hash_verbose.get import GetTransactionVerbose
from openapi_evm_api.paths.address.get import GetWalletTransactions
from openapi_evm_api.paths.address_verbose.get import GetWalletTransactionsVerbose


class TransactionApi(
    GetInternalTransactions,
    GetTransaction,
    GetTransactionVerbose,
    GetWalletTransactions,
    GetWalletTransactionsVerbose,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
