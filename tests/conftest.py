import pytest
from common.api.get_trainers import TrainersApi
from common.api.get_battles import BattlesApi
from common.api.post_change_avatar import AvatarsApi
from common.api.post_create_pokemon import PostCreatePokemonApi
from common.api.get_pokemons import GetPokemonApi
from common.api.post_pokemons_kill import PostKillPokemonApi


@pytest.fixture(scope="session")
def api():
    pokemon_api = TrainersApi().get_trainers()
    yield pokemon_api


@pytest.fixture(scope="session")
def battles_api():
    battles = BattlesApi().get_battles()
    yield battles


@pytest.fixture(scope="session")
def password_api():
    password = TrainersApi().put_change_password()
    yield password


@pytest.fixture(scope="session")
def avatar_api():
    avatar = AvatarsApi().post_change_avatar()
    yield avatar


@pytest.fixture(scope="session")
def create_pokemon_api():
    create_pokemon = PostCreatePokemonApi().post_create_pokemon()
    yield create_pokemon


@pytest.fixture(scope="session")
def get_pokemon_api():
    get_pokemons = GetPokemonApi().get_pokemons()
    yield get_pokemons


@pytest.fixture(scope="session")
def kill_all_pokemons_api():
    kill_pokemon = PostKillPokemonApi().post_kill_pokemon()
    yield kill_pokemon
