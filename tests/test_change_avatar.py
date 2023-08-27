import pytest
from test_data.change_avatar_data import *


@pytest.mark.parametrize("request_body, headers, answer", CASE_AVATAR_SUCCESS)
def test_change_avatar_success(avatar_api, request_body, headers, answer):
    response = avatar_api.post_change_avatar(request_body=request_body, headers=headers)
    assert response.response.json() == answer


@pytest.mark.parametrize("request_body, headers, answer", CASE_AVATAR_WITH_ERRORS)
def test_change_avatar_errors(avatar_api, request_body, headers, answer):
    response = avatar_api.post_change_avatar(request_body=request_body, headers=headers)
    assert response.response.json() == answer
