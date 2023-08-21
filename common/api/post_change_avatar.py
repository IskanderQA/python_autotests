from common.api.basic_methods import Api


class AvatarsApi(Api):

    def post_change_avatar(self, request_body={}, headers={}):
        url = f'{self.url}/trainers/change_avatar'
        return self.post(url=url, json_body=request_body, headers=headers)
