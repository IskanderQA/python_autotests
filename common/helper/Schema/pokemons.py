'''
Schema for pokemons
'''

from voluptuous import Schema, PREVENT_EXTRA

pokemons_valid_structure = Schema(
    {
        "attack": str,
        "id": str,
        "in_pokeball": str,
        "name": str,
        "photo": str,
        "stage": str,
        "status": str,
        "trainer_id": str
    },
    extra=PREVENT_EXTRA,
    required=True
)