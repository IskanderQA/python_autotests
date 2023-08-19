from common.api.basic_methods import Api

class AvatarsApi(Api):
    '''
    Methods for battles
    '''

    def post_change_avatar(self, request_body={}, headers={}):
        """
        PUT /trainers/re
            :return:
        """

        url = f'{self.url}/trainers/change_avatar'
        return self.post(url=url, json_body=request_body, headers=headers)
