# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.2
    Generated by: https://openapi-generator.tech
"""

from openapi_evm_api.paths.nft_address.get import GetContractNfts
from openapi_evm_api.paths.nft_get_multiple_nfts.post import GetMultipleNfts
from openapi_evm_api.paths.nft_metadata.post import GetNftBulkContractMetadata
from openapi_evm_api.paths.nft_address_stats.get import GetNftCollectionStats
from openapi_evm_api.paths.nft_address_metadata.get import GetNftContractMetadata
from openapi_evm_api.paths.nft_address_price.get import GetNftContractSalePrices
from openapi_evm_api.paths.nft_address_transfers.get import GetNftContractTransfers
from openapi_evm_api.paths.nft_address_lowestprice.get import GetNftLowestPrice
from openapi_evm_api.paths.nft_address_token_id.get import GetNftMetadata
from openapi_evm_api.paths.nft_address_owners.get import GetNftOwners
from openapi_evm_api.paths.nft_address_token_id_price.get import GetNftSalePrices
from openapi_evm_api.paths.nft_address_token_id_owners.get import GetNftTokenIdOwners
from openapi_evm_api.paths.nft_address_token_id_stats.get import GetNftTokenStats
from openapi_evm_api.paths.nft_address_trades.get import GetNftTrades
from openapi_evm_api.paths.nft_address_token_id_trades.get import GetNftTradesByToken
from openapi_evm_api.paths.wallets_address_nfts_trades.get import GetNftTradesByWallet
from openapi_evm_api.paths.nft_address_traits.get import GetNftTraitsByCollection
from openapi_evm_api.paths.nft_address_traits_paginate.get import GetNftTraitsByCollectionPaginate
from openapi_evm_api.paths.nft_address_token_id_transfers.get import GetNftTransfers
from openapi_evm_api.paths.block_block_number_or_hash_nft_transfers.get import GetNftTransfersByBlock
from openapi_evm_api.paths.nft_transfers.get import GetNftTransfersFromToBlock
from openapi_evm_api.paths.address_nft_collections.get import GetWalletNftCollections
from openapi_evm_api.paths.address_nft_transfers.get import GetWalletNftTransfers
from openapi_evm_api.paths.address_nft.get import GetWalletNfts
from openapi_evm_api.paths.nft_address_token_id_metadata_resync.get import ReSyncMetadata
from openapi_evm_api.paths.nft_address_traits_resync.get import ResyncNftRarity
from openapi_evm_api.paths.nft_address_sync.put import SyncNftContract


class NftApi(
    GetContractNfts,
    GetMultipleNfts,
    GetNftBulkContractMetadata,
    GetNftCollectionStats,
    GetNftContractMetadata,
    GetNftContractSalePrices,
    GetNftContractTransfers,
    GetNftLowestPrice,
    GetNftMetadata,
    GetNftOwners,
    GetNftSalePrices,
    GetNftTokenIdOwners,
    GetNftTokenStats,
    GetNftTrades,
    GetNftTradesByToken,
    GetNftTradesByWallet,
    GetNftTraitsByCollection,
    GetNftTraitsByCollectionPaginate,
    GetNftTransfers,
    GetNftTransfersByBlock,
    GetNftTransfersFromToBlock,
    GetWalletNftCollections,
    GetWalletNftTransfers,
    GetWalletNfts,
    ReSyncMetadata,
    ResyncNftRarity,
    SyncNftContract,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
