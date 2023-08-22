import pytest
from test_data.change_password_data import PASSWORD_CASES, valid_message
from config import token, email, password


def test_change_password_success(password_api):

    response = password_api.put_change_password(request_body={"email": email,
                                                              "password_old": password,
                                                              "password_new": password
                                                              },
                                                headers={'trainer_token': token})
    assert response.response.json() == valid_message


@pytest.mark.parametrize('cases, headers, answer', PASSWORD_CASES)
def test_change_password_errors(password_api, cases, headers, answer):

    response = password_api.put_change_password(request_body=cases, headers=headers)
    assert response.response.json() == answer
