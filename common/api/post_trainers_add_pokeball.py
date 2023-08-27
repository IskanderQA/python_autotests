from common.api.basic_methods import Api
from config import token
from test_data.trainers_data import get_pokemons_and_assignment_pokemon_id
from tests.conftest import create_pokemon_api, get_pokemon_api

class AddPokeballApi(Api):

    def post_add_pokeball(self, headers = {}, request_body = {}):
        url=f'{self.url}/trainers/add_pokeball'
        return self.post(url=url, headers=headers, json_body=request_body)

    def create_three_pokemon_and_add_in_pokeball(self, create_pokemon_api, get_pokemon_api):
        for i in range(3):
            create_pokemon_api.post_create_pokemon(request_body={
                "name": "Бульбазавр",
                "photo": "https://dolnikov.ru/pokemons/albums/001.png"
            }, headers={'trainer_token': token})
            pokemon_id = get_pokemons_and_assignment_pokemon_id(get_pokemon_api)
            AddPokeballApi().post_add_pokeball(request_body={"pokemon_id": pokemon_id})
