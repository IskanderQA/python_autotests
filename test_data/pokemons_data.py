from config import token

CREATE_POKEMON_SUCCESS = [
    ({
         "name": "Бульбазавр",
         "photo": "https://dolnikov.ru/pokemons/albums/001.png"
     }, {'trainer_token': token})

]

CREATE_POKEMON_WITH_ERRORS = [
    ({
         "name": "",
         "photo": "https://dolnikov.ru/pokemons/albums/001.png"
     }, {'trainer_token': token},
     {'message': 'Отсутствует имя покемона(name)'}),
    ({
         "name": "0",
         "photo": "https://dolnikov.ru/pokemons/albums/001.png"
     }, {'trainer_token': token},
     {'message': 'Имя покемона должно содержать 3 и более символов'}),
    ({
         "name": ")(*&))",
         "photo": "https://dolnikov.ru/pokemons/albums/001.png"
     }, {'trainer_token': token},
     {'message': 'Спецсимволы использовать в имени покемона запрещено'}),
    ({
         "name": "Qwerty",
         "photo": "123.ru"
     }, {'trainer_token': '02134'},
     {'message': 'Неверный токен', 'status': 'error'}),
    ({
         "name": "Qwerty",
         "photo": "123.ru"
     }, {'trainer_token': ''},
     {'message': 'токен отсутствует', 'status': 'error'})
]

DELETE_POKEMON_WITH_ERRORS = [
    ({"pokemon_id": ""}, {'trainer_token': token},
     {'message': 'Отсутствует номер покемона(pokemon_id)'}),
    ({"pokemon_id": "6328"}, {'trainer_token': token},
     {'message': 'Данный покемон уже мёртв'}),
    ({"pokemon_id": "6328"}, {'trainer_token': ''},
     {'message': 'токен отсутствует', 'status': 'error'}),
    ({"pokemon_id": "6328"}, {'trainer_token': '01234'},
     {'message': 'Неверный токен', 'status': 'error'}),
    ({"pokemon_id": "6338"}, {'trainer_token': token},
     {'message': 'Покемон вам не принадлежит!'}),
]

ADD_POKEBALL_WITH_ERRORS = [
    (
        {"pokemon_id": 6533}, {"trainer_token": token}, {'message': 'Данный покемон мёртв'}),
    ({"pokemon_id": 6300}, {"trainer_token": token}, {'message': 'Покемон вам не принадлежит!'}),
    ({"pokemon_id": 6533, }, {"trainer_token": '123'}, {'message': 'Неверный токен', 'status': 'error'}),
    ({"pokemon_id": 6533, }, {"trainer_token": ''}, {'message': 'токен отсутствует', 'status': 'error'}),
]