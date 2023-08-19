from common.api.basic_methods import Api


class PostCreatePokemonApi(Api):

    def post_create_pokemon(self, request_body={}, headers={}):
        url = f'{self.url}/pokemons'
        return self.post(url=url, json_body=request_body, headers=headers)


    def create_five_pokemons(self, create_pokemon_api):
        token = '9bd189a8403bc75b51d64f3e84e73754'
        for i in range(5):
            create_pokemon_api.post_create_pokemon(request_body={
                "name": "Бульбазавр",
                "photo": "https://dolnikov.ru/pokemons/albums/001.png"
            }, headers={'trainer_token': token})
