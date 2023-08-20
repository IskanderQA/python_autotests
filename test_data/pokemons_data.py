CREATE_POKEMON_SUCCESS = [
    ({
         "name": "Бульбазавр",
         "photo": "https://dolnikov.ru/pokemons/albums/001.png"
     }, {'trainer_token': '9bd189a8403bc75b51d64f3e84e73754'})

]

CREATE_POKEMON_WITH_ERRORS = [
    ({
         "name": "",
         "photo": "https://dolnikov.ru/pokemons/albums/001.png"
     }, {'trainer_token': '083c977e6f1218a0b727e97a489c43a1'},
     {'message': 'Отсутствует имя покемона(name)'}),
    ({
         "name": "0",
         "photo": "https://dolnikov.ru/pokemons/albums/001.png"
     }, {'trainer_token': '083c977e6f1218a0b727e97a489c43a1'},
     {'message': 'Имя покемона должно содержать 3 и более символов'}),
    ({
         "name": ")(*&))",
         "photo": "https://dolnikov.ru/pokemons/albums/001.png"
     }, {'trainer_token': '083c977e6f1218a0b727e97a489c43a1'},
     {'message': 'Спецсимволы использовать в имени покемона запрещено'}),
    ({
         "name": "Qwerty",
         "photo": "123.ru"
     }, {'trainer_token': '083c9776f1218a0b727e97a489c43a1'},
     {'message': 'Неверный токен', 'status': 'error'}),
    ({
         "name": "Qwerty",
         "photo": "123.ru"
     }, {'trainer_token': ''},
     {'message': 'токен отсутствует', 'status': 'error'})
]

DELETE_POKEMON_WITH_ERRORS = [
    ({"pokemon_id": ""}, {'trainer_token': '9bd189a8403bc75b51d64f3e84e73754'},
     {'message': 'Отсутствует номер покемона(pokemon_id)'}),
    ({"pokemon_id": "6328"}, {'trainer_token': '9bd189a8403bc75b51d64f3e84e73754'},
     {'message': 'Данный покемон уже мёртв'}),
    ({"pokemon_id": "6328"}, {'trainer_token': ''}, {'message': 'токен отсутствует', 'status': 'error'}),
    ({"pokemon_id": "6328"}, {'trainer_token': '9bd189a8403bc75b51d64f3e84e73'},
     {'message': 'Неверный токен', 'status': 'error'}),
    ({"pokemon_id": "6328"}, {'trainer_token': 'cf11a5c78d932d3146d9b70f38d45cc3'},
     {'message': 'Покемон вам не принадлежит!'}),
]
