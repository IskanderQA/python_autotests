from common.api.patch_trainers import PatchTrainersApi
from test_data.trainers_data import PATCH_TRAINERS_SUCCESS, PATCH_TRAINERS_ERRORS
import pytest

'''
Частичное обновление информации по тренеру
'''


@pytest.mark.parametrize('request_body, token, message', PATCH_TRAINERS_SUCCESS)
def test_patch_trainers_success(request_body, token, message):
    response = PatchTrainersApi().patch_trainers(request_body=request_body, headers=token)
    assert response.response.json()['message'] == message


@pytest.mark.parametrize('request_body, token, message', PATCH_TRAINERS_ERRORS)
def test_patch_trainers_with_errors(request_body, token, message):
    response = PatchTrainersApi().patch_trainers(request_body=request_body, headers=token)
    assert response.response.json()['message'] == message
