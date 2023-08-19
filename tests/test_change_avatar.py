import pytest
from test_data.change_avatar_data import *

def test_change_avatar_success(avatar_api):
    response = avatar_api.post_change_avatar(request_body={"card_number": "4620869113632996",
                                                           "card_csv": "125",
                                                           "card_actual": "10/25",
                                                           "num": "56456",
                                                           "avatar_id": "1"},
                                             headers={'trainer_token': '219b5d1551fc115f532e6ac0d404ddf6'})
    assert response.response.json() == success_message


@pytest.mark.parametrize("request_body, headers, answer", CASE_AVATAR)
def test_change_avatar_errors(avatar_api, request_body, headers, answer):
    response = avatar_api.post_change_avatar(request_body=request_body, headers=headers)
    assert response.response.json() == answer
