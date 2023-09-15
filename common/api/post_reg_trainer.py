from common.api.basic_methods import Api


class CreateTrainerApi(Api):

    def post_reg_trainer(self, headers={}, request_body={}):
        url=f'{self.url}/trainers/reg'
        return self.post(url=url, headers=request_body, json_body=request_body)