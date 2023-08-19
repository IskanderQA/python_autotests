from common.api.put_trainers import PutTrainersApi
from test_data.trainers_data import UPDATING_INFO_SUCCESS, UPDATING_INFO_WITH_ERRORS
import pytest


@pytest.mark.parametrize('request_body, token, message', UPDATING_INFO_SUCCESS)
def test_updating_info_about_trainer_success(request_body, token, message):
    response = PutTrainersApi().put_trainers(request_body=request_body, headers=token)
    assert response.response.json() == message


@pytest.mark.parametrize('request_body, token, message', UPDATING_INFO_WITH_ERRORS)
def test_updating_info_about_trainer_with_errors(request_body, token, message):
    response = PutTrainersApi().put_trainers(request_body=request_body, headers=token)
    assert response.response.json() == message
