import typing_extensions

from openapi_auth.paths import PathValues
from openapi_auth.apis.paths.challenge_request_evm import ChallengeRequestEvm
from openapi_auth.apis.paths.challenge_verify_evm import ChallengeVerifyEvm
from openapi_auth.apis.paths.challenge_request_solana import ChallengeRequestSolana
from openapi_auth.apis.paths.challenge_verify_solana import ChallengeVerifySolana

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CHALLENGE_REQUEST_EVM: ChallengeRequestEvm,
        PathValues.CHALLENGE_VERIFY_EVM: ChallengeVerifyEvm,
        PathValues.CHALLENGE_REQUEST_SOLANA: ChallengeRequestSolana,
        PathValues.CHALLENGE_VERIFY_SOLANA: ChallengeVerifySolana,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CHALLENGE_REQUEST_EVM: ChallengeRequestEvm,
        PathValues.CHALLENGE_VERIFY_EVM: ChallengeVerifyEvm,
        PathValues.CHALLENGE_REQUEST_SOLANA: ChallengeRequestSolana,
        PathValues.CHALLENGE_VERIFY_SOLANA: ChallengeVerifySolana,
    }
)
