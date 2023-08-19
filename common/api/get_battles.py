from common.api.basic_methods import Api

class BattlesApi(Api):
    '''
    Methods for battles
    '''

    def get_battles(self, trainer_id: int = None):
        '''
        GET /battles
            :param trainer_id:
            :return:
        '''

        url = f'{self.url}/battles'
        return self.get(url=url, params={'trainer_id': trainer_id})
