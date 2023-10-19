from common.api.post_reg_trainer import CreateTrainerApi
import pytest
from test_data.reg_trainer_data import REG_TRAINER_WITH_ERRORS


@pytest.mark.parametrize('request_body, message', REG_TRAINER_WITH_ERRORS)
def test_reg_trainer_with_errors(request_body, message):
    response = CreateTrainerApi().post_reg_trainer(request_body=request_body)
    assert response.response.json() == message
