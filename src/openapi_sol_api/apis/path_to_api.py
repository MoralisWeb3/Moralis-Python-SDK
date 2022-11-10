import typing_extensions

from openapi_sol_api.paths import PathValues
from openapi_sol_api.apis.paths.account_network_address_balance import AccountNetworkAddressBalance
from openapi_sol_api.apis.paths.account_network_address_tokens import AccountNetworkAddressTokens
from openapi_sol_api.apis.paths.account_network_address_nft import AccountNetworkAddressNft
from openapi_sol_api.apis.paths.account_network_address_portfolio import AccountNetworkAddressPortfolio
from openapi_sol_api.apis.paths.nft_network_address_metadata import NftNetworkAddressMetadata
from openapi_sol_api.apis.paths.token_network_address_price import TokenNetworkAddressPrice

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNT_NETWORK_ADDRESS_BALANCE: AccountNetworkAddressBalance,
        PathValues.ACCOUNT_NETWORK_ADDRESS_TOKENS: AccountNetworkAddressTokens,
        PathValues.ACCOUNT_NETWORK_ADDRESS_NFT: AccountNetworkAddressNft,
        PathValues.ACCOUNT_NETWORK_ADDRESS_PORTFOLIO: AccountNetworkAddressPortfolio,
        PathValues.NFT_NETWORK_ADDRESS_METADATA: NftNetworkAddressMetadata,
        PathValues.TOKEN_NETWORK_ADDRESS_PRICE: TokenNetworkAddressPrice,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNT_NETWORK_ADDRESS_BALANCE: AccountNetworkAddressBalance,
        PathValues.ACCOUNT_NETWORK_ADDRESS_TOKENS: AccountNetworkAddressTokens,
        PathValues.ACCOUNT_NETWORK_ADDRESS_NFT: AccountNetworkAddressNft,
        PathValues.ACCOUNT_NETWORK_ADDRESS_PORTFOLIO: AccountNetworkAddressPortfolio,
        PathValues.NFT_NETWORK_ADDRESS_METADATA: NftNetworkAddressMetadata,
        PathValues.TOKEN_NETWORK_ADDRESS_PRICE: TokenNetworkAddressPrice,
    }
)
