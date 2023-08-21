from common.api.basic_methods import Api


class PutTrainersApi(Api):

    def put_trainers(self, request_body={}, headers={}):
        url = f'{self.url}/trainers'
        return self.put(url=url, json_body=request_body, headers=headers)
