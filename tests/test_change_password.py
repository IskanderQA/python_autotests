import pytest
from test_data.change_password_data import PASSWORD_CASES_SUCCESS, PASSWORD_CASES_WITH_ERRORS


@pytest.mark.parametrize('cases, headers, message', PASSWORD_CASES_SUCCESS)
def test_change_password_success(password_api, cases, headers, message):

    response = password_api.put_change_password(request_body=cases, headers=headers)
    assert response.response.json()["message"] == message


@pytest.mark.parametrize('cases, headers, message', PASSWORD_CASES_WITH_ERRORS)
def test_change_password_errors(password_api, cases, headers, message):

    response = password_api.put_change_password(request_body=cases, headers=headers)
    assert response.response.json() == message
