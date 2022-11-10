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

from openapi_auth.model.evm_challenge_request_dto import EvmChallengeRequestDto
from openapi_auth.model.evm_challenge_response_dto import EvmChallengeResponseDto
from openapi_auth.model.evm_complete_challenge_request_dto import EvmCompleteChallengeRequestDto
from openapi_auth.model.evm_complete_challenge_response_dto import EvmCompleteChallengeResponseDto
from openapi_auth.model.solana_challenge_request_dto import SolanaChallengeRequestDto
from openapi_auth.model.solana_challenge_response_dto import SolanaChallengeResponseDto
from openapi_auth.model.solana_complete_challenge_request_dto import SolanaCompleteChallengeRequestDto
from openapi_auth.model.solana_complete_challenge_response_dto import SolanaCompleteChallengeResponseDto
