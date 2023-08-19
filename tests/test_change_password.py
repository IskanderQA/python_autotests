import pytest
from common.api.get_trainers import TrainersApi
from test_data.change_password_data import PASSWORD_CASES, valid_message

'''
Change password tests
'''


def test_change_password_success(password_api):
    '''
    PUT /trainers/re
    :return:
    '''

    response = password_api.put_change_password(request_body={"email": "biketrial666@yandex.ru",
                                                              "password_old": "Lotus_elise1",
                                                              "password_new": "Lotus_elise1"
                                                              },
                                                headers={'trainer_token': '083c977e6f1218a0b727e97a489c43a1'})
    assert response.response.json() == valid_message


@pytest.mark.parametrize('cases, headers, answer', PASSWORD_CASES)
def test_change_password_errors(password_api, cases, headers, answer):
    '''
    Checking error messages
    '''

    response = password_api.put_change_password(request_body=cases, headers=headers)
    assert response.response.json() == answer
