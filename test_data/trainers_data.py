from config import token, trainer_id

CASE_TRAINERS = [
    {'id': 1987, 'status_code': 200},
    {'id': -1239, 'status_code': 400},
    {'id': 19270, 'status_code': 400},
]

CASE_PAGINATION = [
    {'page': 1},
    {'page': 0},
    {'page': 5},
]

UPDATING_INFO_SUCCESS = [
    ({
         "name": "Ash",
         "city": "Tokyo"
     }, {'trainer_token': token},
     'Информация о тренере обновлена')
]

UPDATING_INFO_WITH_ERRORS = [
    ({
         "name": "",
         "city": "Tokyo"
     }, {'trainer_token': token},
     {'message': 'Отсутствует имя тренера(name)'}),
    ({
         "name": "Ash",
         "city": ""
     }, {'trainer_token': token},
     {'message': 'Отсутствует город пользователя(city)', 'status': 'error'}),
    ({
         "name": "Ash",
         "city": "New York"
     }, {'trainer_token': '012412'},
     {'message': 'Неверный токен', 'status': 'error'}),
    ({
         "name": "Ash",
         "city": "New York"
     }, {'trainer_token': ''},
     {'message': 'токен отсутствует', 'status': 'error'}),
]

error_message_token = {"message": "токен отсутствует", "status": "error"}
error_message_trainer_not_found = {'message': 'Тренер отсутствует', 'status': 'error'}


def get_pokemons_and_assignment_pokemon_id(get_pokemon_api):
    get_pokemons_from_trainer = get_pokemon_api.get_pokemons(trainer_id=trainer_id)
    return get_pokemons_from_trainer.response.json()[0]['id']


PATCH_TRAINERS_SUCCESS = [
    ({
         "name": "Ash",
     }, {'trainer_token': token},
     'Информация о тренере обновлена'),
    ({
         "city": "Tokyo"
     }, {'trainer_token': token},
     'Информация о тренере обновлена'),
    ({
         "name": "Ash",
         "city": "Tokyo"
     }, {'trainer_token': token},
     'Информация о тренере обновлена')
]

PATCH_TRAINERS_ERRORS = [
    ({"name": "Ash"},
     {'trainer_token': ''},
     'токен отсутствует'),
    ({"name": "Ash"},
     {'trainer_token': 'asdadsasd'},
     'Неверный токен'),
    ({"city": "Tokyo"},
     {'trainer_token': ''},
     'токен отсутствует'),
    ({"city": "Tokyo"},
     {'trainer_token': 'asdasdasd'},
     'Неверный токен'),
    ({
         "name": "Ash",
         "city": "Tokyo"
     },
     {'trainer_token': ''},
     'токен отсутствует'),
    ({
         "name": "Ash",
         "city": "Tokyo"
     },
     {'trainer_token': 'asdasdasd'},
     'Неверный токен')
]
