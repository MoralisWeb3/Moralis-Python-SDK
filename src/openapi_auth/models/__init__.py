# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_auth.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_auth.model.address_info_dto import AddressInfoDto
from openapi_auth.model.aptos_challenge_request_dto import AptosChallengeRequestDto
from openapi_auth.model.aptos_challenge_response_dto import AptosChallengeResponseDto
from openapi_auth.model.aptos_complete_challenge_request_dto import AptosCompleteChallengeRequestDto
from openapi_auth.model.aptos_complete_challenge_response_dto import AptosCompleteChallengeResponseDto
from openapi_auth.model.bind_remove_dto import BindRemoveDto
from openapi_auth.model.bind_remove_response_dto import BindRemoveResponseDto
from openapi_auth.model.bind_request_dto import BindRequestDto
from openapi_auth.model.bind_request_response_dto import BindRequestResponseDto
from openapi_auth.model.bind_verify_remove_dto import BindVerifyRemoveDto
from openapi_auth.model.bind_verify_remove_response_dto import BindVerifyRemoveResponseDto
from openapi_auth.model.bind_verify_request_dto import BindVerifyRequestDto
from openapi_auth.model.bind_verify_request_response_dto import BindVerifyRequestResponseDto
from openapi_auth.model.evm_challenge_request_dto import EvmChallengeRequestDto
from openapi_auth.model.evm_challenge_response_dto import EvmChallengeResponseDto
from openapi_auth.model.evm_complete_challenge_request_dto import EvmCompleteChallengeRequestDto
from openapi_auth.model.evm_complete_challenge_response_dto import EvmCompleteChallengeResponseDto
from openapi_auth.model.solana_challenge_request_dto import SolanaChallengeRequestDto
from openapi_auth.model.solana_challenge_response_dto import SolanaChallengeResponseDto
from openapi_auth.model.solana_complete_challenge_request_dto import SolanaCompleteChallengeRequestDto
from openapi_auth.model.solana_complete_challenge_response_dto import SolanaCompleteChallengeResponseDto
from openapi_auth.model.verification_dto import VerificationDto
