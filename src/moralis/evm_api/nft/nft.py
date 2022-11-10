
import openapi_evm_api
from openapi_evm_api.apis.tags import nft_api
import json
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_evm_api.Configuration()
    configuration.api_key['ApiKeyAuth'] = api_key
    api_client = openapi_evm_api.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = nft_api.NftApi(api_client)
    api_client.close()

    return api_instance


def get_contract_nfts(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_contract_nfts(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_nft_contract_metadata(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_nft_contract_metadata(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_nft_contract_transfers(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_nft_contract_transfers(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_nft_lowest_price(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_nft_lowest_price(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_nft_metadata(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_nft_metadata(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_nft_owners(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_nft_owners(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_nft_token_id_owners(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_nft_token_id_owners(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_nft_trades(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_nft_trades(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_nft_transfers(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_nft_transfers(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_nft_transfers_by_block(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_nft_transfers_by_block(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_nft_transfers_from_to_block(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_nft_transfers_from_to_block(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_wallet_nft_collections(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_wallet_nft_collections(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_wallet_nft_transfers(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_wallet_nft_transfers(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def get_wallet_nfts(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.get_wallet_nfts(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def re_sync_metadata(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.re_sync_metadata(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def search_nfts(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.search_nfts(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)


def sync_nft_contract(api_key, **args):
    api_instance = get_api_instance(api_key)
    api_response = api_instance.sync_nft_contract(
        **args, accept_content_types='application/json; charset=utf-8', skip_deserialization=True)

    return json.loads(api_response.response.data)

