from common.api.post_pokemons_kill import PostKillPokemonApi
from test_data.pokemons_data import CREATE_POKEMON_SUCCESS
import pytest

@pytest.mark.parametrize("request_body, token", CREATE_POKEMON_SUCCESS)
def test_kill_pokemon_success(get_pokemon_api, create_pokemon_api, kill_all_pokemons_api, request_body, token):

    response = create_pokemon_api.post_create_pokemon(request_body=request_body, headers=token)
    assert response.response.json()["message"] == "Покемон создан"

    get_pokemons_from_trainer = get_pokemon_api.get_pokemons(trainer_id=2006)

    pokemon_id = get_pokemons_from_trainer.response.json()[0]['id']
    PostKillPokemonApi().post_kill_pokemon(request_body={
        "pokemon_id": pokemon_id
    }, headers=token)