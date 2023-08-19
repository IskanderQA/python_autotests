from common.api.basic_methods import Api


class PutTrainersApi(Api):
    """
    Updating information about trainer
    """

    def put_trainers(self, request_body={}, headers={}):
        """
        PUT /trainers
            :return:
        """

        url = f'{self.url}/trainers'
        return self.put(url=url, json_body=request_body, headers=headers)
