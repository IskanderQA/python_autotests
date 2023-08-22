import pytest
from test_data.change_avatar_data import *
from config import token, card_number, card_csv, card_actual, num

def test_change_avatar_success(avatar_api):
    response = avatar_api.post_change_avatar(request_body={"card_number": card_number,
                                                           "card_csv": card_csv,
                                                           "card_actual": card_actual,
                                                           "num": num,
                                                           "avatar_id": "1"},
                                             headers={'trainer_token': token})
    assert response.response.json() == success_message


@pytest.mark.parametrize("request_body, headers, answer", CASE_AVATAR)
def test_change_avatar_errors(avatar_api, request_body, headers, answer):
    response = avatar_api.post_change_avatar(request_body=request_body, headers=headers)
    assert response.response.json() == answer
