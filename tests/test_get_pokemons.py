from common.helper.Schema.pokemons import pokemons_valid_structure
from pytest_voluptuous import S
from config import trainer_id
from fixtures.pokemon_fixtures import create_pokemon_before_and_kill_all_after


def test_get_pokemons(get_pokemon_api):
    response = get_pokemon_api.get_pokemons()
    assert len(response.response.json()) == 41
    assert S(pokemons_valid_structure) == response.response.json()[0]


def test_get_pokemons_with_trainer_id(create_pokemon_before_and_kill_all_after, get_pokemon_api):
    response = get_pokemon_api.get_pokemons(trainer_id=trainer_id)
    assert S(pokemons_valid_structure) == response.response.json()[0] and len(response.response.json()) <= 5


def test_get_pokemons_with_status(get_pokemon_api):
    response = get_pokemon_api.get_pokemons(status=1)
    assert S(pokemons_valid_structure) == response.response.json()[0]


def test_get_pokemons_with_trainer_id_and_status(create_pokemon_before_and_kill_all_after, get_pokemon_api):
    response = get_pokemon_api.get_pokemons(status=1, trainer_id=trainer_id)
    assert S(pokemons_valid_structure) == response.response.json()[0]


def test_get_pokemons_in_pokeballs_equals_0(get_pokemon_api):
    '''if in_pokeball == 0 -  то придёт ответ со списком покемоном БЕЗ покебола'''

    response = get_pokemon_api.get_pokemons(in_pokeball=0)
    assert "in_pokeball" in response.response.json()[0] and response.response.json()[0]["in_pokeball"] == '0'


def test_get_pokemons_in_pokeballs_equals_1(get_pokemon_api):
    '''if in_pokeball == 1 -  то придёт ответ со списком покемоном В покеболе'''

    response = get_pokemon_api.get_pokemons(in_pokeball=1)
    assert response.response.json()[0]["in_pokeball"] == '1'


def test_get_pokemons_in_pokeballs_any_other_value(get_pokemon_api):
    ''' in_pokeball == любое другое значение, то придёт ответ со списком всех покемонов находящихся и В покеболе и БЕЗ покебола.'''

    response = get_pokemon_api.get_pokemons(in_pokeball=666)

    assert any(
        item['in_pokeball'] == '1' for item in response.response.json()), "Отсутствуют объекты in_pokeball с ключом '1'"
    assert any(
        item['in_pokeball'] == '0' for item in response.response.json()), "Отсутствуют объекты in_pokeball с ключом '0'"


def test_get_pokemons_with_trainer_id_and_status_and_in_pokeball(create_pokemon_before_and_kill_all_after, get_pokemon_api):
    response = get_pokemon_api.get_pokemons(status=1, trainer_id=trainer_id, in_pokeball=0)
    assert S(pokemons_valid_structure) == response.response.json()[0]


def test_get_pokemons_with_pokemon_id(get_pokemon_api):
    response = get_pokemon_api.get_pokemons(pokemon_id=6207)
    assert S(pokemons_valid_structure) == response.response.json()


def test_get_pokemons_with_trainer_id_and_pokemon_id_and_status_and_in_pokeball(get_pokemon_api):
    response = get_pokemon_api.get_pokemons(status=1, trainer_id=trainer_id, in_pokeball=0, pokemon_id=6207)
    assert S(pokemons_valid_structure) == response.response.json()