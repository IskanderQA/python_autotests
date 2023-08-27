from common.api.post_trainers_add_pokeball import AddPokeballApi
from test_data.pokemons_data import ADD_POKEBALL_WITH_ERRORS
from test_data.trainers_data import get_pokemons_and_assignment_pokemon_id
from fixtures.pokemon_fixtures import create_pokemon_before_and_kill_all_after
from config import trainer_id
import pytest


def test_add_pokeball_success(create_pokemon_before_and_kill_all_after, get_pokemon_api):
    pokemon_id = get_pokemons_and_assignment_pokemon_id(get_pokemon_api)

    # Добавление покемона в покебол
    response = AddPokeballApi().post_add_pokeball(request_body={"pokemon_id": pokemon_id})
    assert response.response.json() == {"id": pokemon_id, "message": "Покемон пойман в покебол"}


@pytest.mark.parametrize('request_body, headers, message', ADD_POKEBALL_WITH_ERRORS)
def test_add_pokeball_with_errors(request_body, headers, message):
    response = AddPokeballApi().post_add_pokeball(request_body=request_body, headers=headers)
    assert response.response.json() == message


def test_pokemon_already_in_pokeball(create_pokemon_before_and_kill_all_after, get_pokemon_api):
    pokemon_id = get_pokemons_and_assignment_pokemon_id(get_pokemon_api)
    AddPokeballApi().post_add_pokeball(request_body={"pokemon_id": pokemon_id})
    response = AddPokeballApi().post_add_pokeball(request_body={"pokemon_id": pokemon_id})
    assert response.response.json() == {'message': 'Данный покемон уже привязан к покеболу'}


def test_pokeballs_are_full(create_pokemon_before_and_kill_all_after, get_pokemon_api, create_pokemon_api):
    AddPokeballApi().create_three_pokemon_and_add_in_pokeball(create_pokemon_api, get_pokemon_api)

    get_pokemons_from_trainer = get_pokemon_api.get_pokemons(trainer_id=trainer_id)
    pokemon_id = get_pokemons_from_trainer.response.json()[3]['id']

    response = AddPokeballApi().post_add_pokeball(request_body={"pokemon_id": pokemon_id})
    assert response.response.json() == {'message': 'Максимум 3 привязанных покемона к покеболу'}
