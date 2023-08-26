from common.api.basic_methods import Api
from config import token

class AddPokeballApi(Api):

    def post_add_pokeball(self, headers = {}, request_body = {}):
        url=f'{self.url}/trainers/add_pokeball'
        return self.post(url=url, headers=headers, json_body=request_body)