from common.api.basic_methods import Api
from config import token, trainer_id


class DownloadHistoryDoneApi(Api):

    def post_trainers_download_history_done(self, headers = {}, request_body ={}):
        url=f'{self.url}/trainers/download_history_done'
        return self.post(url=url, headers=headers, json_body=request_body)