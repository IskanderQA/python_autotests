from common.api.basic_methods import Api


class PatchTrainersApi(Api):

    def patch_trainers(self, request_body={}, headers={}):
        url = f'{self.url}/trainers'
        return self.patch(url=url, json_body=request_body, headers=headers)
