'''
Schema for trainer
'''

from voluptuous import Schema, PREVENT_EXTRA

trainer_valid_structure = Schema(
    {
        "city": str,
         "get_history_battle": str,
         "id": str,
        "level": str,
         "photo": str,
         "pokemons": list,
         "pokemons_alive": list,
         "pokemons_in_pokeballs": list,
         "trainer_name": str
    },
    extra=PREVENT_EXTRA,
    required=True

)

trainer_not_found = Schema(
    {
        "message": "Тренер отсутствует",
        "status": "error"
    },
    extra=PREVENT_EXTRA,
    required=True

)