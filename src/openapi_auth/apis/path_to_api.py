import typing_extensions

from openapi_auth.paths import PathValues
from openapi_auth.apis.paths.challenge_request_evm import ChallengeRequestEvm
from openapi_auth.apis.paths.challenge_verify_evm import ChallengeVerifyEvm
from openapi_auth.apis.paths.challenge_request_solana import ChallengeRequestSolana
from openapi_auth.apis.paths.challenge_verify_solana import ChallengeVerifySolana
from openapi_auth.apis.paths.challenge_request_aptos import ChallengeRequestAptos
from openapi_auth.apis.paths.challenge_verify_aptos import ChallengeVerifyAptos
from openapi_auth.apis.paths.profile_profile_id_addresses import ProfileProfileIdAddresses
from openapi_auth.apis.paths.bind_request import BindRequest
from openapi_auth.apis.paths.bind_request_verify import BindRequestVerify
from openapi_auth.apis.paths.bind_remove import BindRemove
from openapi_auth.apis.paths.bind_remove_verify import BindRemoveVerify

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CHALLENGE_REQUEST_EVM: ChallengeRequestEvm,
        PathValues.CHALLENGE_VERIFY_EVM: ChallengeVerifyEvm,
        PathValues.CHALLENGE_REQUEST_SOLANA: ChallengeRequestSolana,
        PathValues.CHALLENGE_VERIFY_SOLANA: ChallengeVerifySolana,
        PathValues.CHALLENGE_REQUEST_APTOS: ChallengeRequestAptos,
        PathValues.CHALLENGE_VERIFY_APTOS: ChallengeVerifyAptos,
        PathValues.PROFILE_PROFILE_ID_ADDRESSES: ProfileProfileIdAddresses,
        PathValues.BIND_REQUEST: BindRequest,
        PathValues.BIND_REQUEST_VERIFY: BindRequestVerify,
        PathValues.BIND_REMOVE: BindRemove,
        PathValues.BIND_REMOVE_VERIFY: BindRemoveVerify,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CHALLENGE_REQUEST_EVM: ChallengeRequestEvm,
        PathValues.CHALLENGE_VERIFY_EVM: ChallengeVerifyEvm,
        PathValues.CHALLENGE_REQUEST_SOLANA: ChallengeRequestSolana,
        PathValues.CHALLENGE_VERIFY_SOLANA: ChallengeVerifySolana,
        PathValues.CHALLENGE_REQUEST_APTOS: ChallengeRequestAptos,
        PathValues.CHALLENGE_VERIFY_APTOS: ChallengeVerifyAptos,
        PathValues.PROFILE_PROFILE_ID_ADDRESSES: ProfileProfileIdAddresses,
        PathValues.BIND_REQUEST: BindRequest,
        PathValues.BIND_REQUEST_VERIFY: BindRequestVerify,
        PathValues.BIND_REMOVE: BindRemove,
        PathValues.BIND_REMOVE_VERIFY: BindRemoveVerify,
    }
)
