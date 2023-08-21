from common.api.basic_methods import Api


class GetPokemonApi(Api):

    def get_pokemons(self, page: int = None, trainer_id: int = None, status: str = None, pokemon_id: str = None,
                     in_pokeball: int = None):
        # if in_pokeball == 0 -  то придёт ответ со списком покемоном БЕЗ покебола
        # if in_pokeball == 1 -  то придёт ответ со списком покемоном В покеболе;
        # if in_pokeball == любое другое значение, то придёт ответ со списком всех покемонов находящихся и В покеболе и БЕЗ покебола.

        url = f'{self.url}/pokemons'
        return self.get(url=url,
                        params={'page': page, 'trainer_id': trainer_id, 'status': status, 'pokemon_id': pokemon_id,
                                'in_pokeball': in_pokeball})
