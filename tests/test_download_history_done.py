from common.api.post_trainers_download_history_done import DownloadHistoryDoneApi
import pytest
from test_data.download_history_done_data import DOWNLOAD_HISTORY_DONE_ERRORS


# TBD для создания успешного теста необходимо добавить тест в связке с Selenium, чтобы для начала запросить задачу на фронте


@pytest.mark.parametrize('headers, user_id, message', DOWNLOAD_HISTORY_DONE_ERRORS)
def test_download_history_done_errors(headers, user_id, message):
    response = DownloadHistoryDoneApi().post_trainers_download_history_done(headers=headers, request_body=user_id)
    assert response.response.json() == message
