from common.api.post_trainers_add_pokeball import AddPokeballApi
from common.api.post_create_pokemon import PostCreatePokemonApi
from common.api.post_pokemons_kill import PostKillPokemonApi
from test_data.pokemons_data import CREATE_POKEMON_SUCCESS
import pytest

@pytest.mark.parametrize("request_body, token", CREATE_POKEMON_SUCCESS)
def test_add_pokeball_success(get_pokemon_api, kill_all_pokemons_api, create_pokemon_api, request_body, token):
    # Запрос на отображение покемонов у тренера и присваивание id созданного покемона переменной pokemon_id
    get_pokemons_from_trainer = get_pokemon_api.get_pokemons(trainer_id=2006)
    response = create_pokemon_api.post_create_pokemon(request_body=request_body, headers=token)
    assert response.response.json()["message"] == "Покемон создан"
    pokemon_id = get_pokemons_from_trainer.response.json()[0]['id']

    # Добавление покемона в покебол
    response = AddPokeballApi().post_add_pokeball(request_body={"pokemon_id": pokemon_id})
    assert response.response.json() == {
        "id": pokemon_id,
        "message": "Покемон пойман в покебол"
    }

    # Kill all pokemons
    kill_all_pokemons_api.kill_all_pokemons(kill_all_pokemons_api, get_pokemon_api)
