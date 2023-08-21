from common.api.basic_methods import Api


class TrainersApi(Api):

    def get_trainers(self, trainer_id: int = None, page: int = None):
        url = f'{self.url}/trainers'
        return self.get(url=url, params={'trainer_id': trainer_id, 'page': page})

    def put_change_password(self, request_body={}, headers={}):

        url = f'{self.url}/trainers/re'
        return self.put(url=url, json_body=request_body, headers=headers)
