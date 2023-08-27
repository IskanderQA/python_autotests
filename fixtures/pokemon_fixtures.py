import pytest
from config import token
from tests.conftest import create_pokemon_api, kill_all_pokemons_api, get_pokemon_api

@pytest.fixture
def create_pokemon_before_and_kill_all_after(create_pokemon_api, kill_all_pokemons_api, get_pokemon_api):
    create_pokemon_api.post_create_pokemon(request_body={
         "name": "Бульбазавр",
         "photo": "https://dolnikov.ru/pokemons/albums/001.png"
     }, headers={'trainer_token': token})

    yield

    kill_all_pokemons_api.kill_all_pokemons(kill_all_pokemons_api, get_pokemon_api)