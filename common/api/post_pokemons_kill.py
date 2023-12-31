from common.api.basic_methods import Api
from config import token, trainer_id


class PostKillPokemonApi(Api):

    def post_kill_pokemon(self, request_body={}, headers={}):
        url = f'{self.url}/pokemons/kill'
        return self.post(url=url, json_body=request_body, headers=headers)

    def kill_all_pokemons(self, kill_all_pokemons_api, get_pokemon_api):
        get_pokemons_from_trainer = get_pokemon_api.get_pokemons(trainer_id=trainer_id)
        for i in range(len(get_pokemons_from_trainer.response.json())):
            pokemon_id = get_pokemons_from_trainer.response.json()[i]['id']
            kill_all_pokemons_api.post_kill_pokemon(request_body={
                "pokemon_id": pokemon_id
            }, headers={'trainer_token': token})
