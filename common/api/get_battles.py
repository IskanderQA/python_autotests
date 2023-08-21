from common.api.basic_methods import Api

class BattlesApi(Api):

    def get_battles(self, trainer_id: int = None):

        url = f'{self.url}/battles'
        return self.get(url=url, params={'trainer_id': trainer_id})
