import pytest
from test_data.pokemons_data import *


@pytest.mark.parametrize("request_body, token", CREATE_POKEMON_SUCCESS)
def test_create_pokemon_success(create_pokemon_api, kill_all_pokemons_api, get_pokemon_api, request_body, token):

    # Kill all pokemons
    kill_all_pokemons_api.kill_all_pokemons(kill_all_pokemons_api, get_pokemon_api)

    # Create pokemon
    response = create_pokemon_api.post_create_pokemon(request_body=request_body, headers=token)
    assert response.response.json()["message"] == "Покемон создан"


@pytest.mark.parametrize("request_body, token, message", CREATE_POKEMON_WITH_ERRORS)
def test_create_pokemon_with_errors(create_pokemon_api, request_body, token, message):
    response = create_pokemon_api.post_create_pokemon(request_body=request_body, headers=token)
    assert response.response.json() == message


@pytest.mark.parametrize("request_body, token", CREATE_POKEMON_SUCCESS)
def test_create_more_five_pokemons(create_pokemon_api, request_body, token):
    # Create 5 pokemons for error
    create_pokemon_api.create_five_pokemons(create_pokemon_api)
    response = create_pokemon_api.post_create_pokemon(request_body=request_body, headers=token)
    assert response.response.json()["message"] == "Максимум 5 живых покемонов"
