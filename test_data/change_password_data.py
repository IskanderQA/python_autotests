PASSWORD_CASES = [
    ({'email': "biketrial666@yandex.ru", "password_old": "123", "password_new": "123"},
     {'trainer_token': '083c977e6f1218a0b727e97a489c43a1'},
     {"message": "Пароль должен иметь хотя-бы одну заглавную букву", "status": "error"}),  # valid params
    ({'email': "biketrial666@yandex.ru", "password_old": "123", "password_new": "ASD"},
     {'trainer_token': '083c977e6f1218a0b727e97a489c43a1'},
     {"message": "Пароль не должен быть пустым и иметь минимум 6 символов, 1 заглавную букву и 1 цифру",
      "status": "error"}),
    ({'email': "biketrial666@yandex.ru", "password_old": "123", "password_new": "ФФЫВфывЫФВ1"},
     {'trainer_token': '083c977e6f1218a0b727e97a489c43a1'},
     {'message': 'Неверные логин или пароль', 'status': 'error'}),
    ({'email': "", "password_old": "123", "password_new": "ФФЫВфывЫФВ1"},
     {'trainer_token': '083c977e6f1218a0b727e97a489c43a1'},
     {'message': 'Неверные логин или пароль', 'status': 'error'}),
    ({'email': "biketrial666@yandex.ru", "password_old": "Lotus_elise1", "password_new": "ФФЫВфывЫФВ1"},
     {'trainer_token': '083c977e6f1asdasd218a0b727e97a489c43a1'},
     {'message': 'Неверный токен', 'status': 'error'}),
    ({'email': "biketrial666@yandex.ru", "password_old": "Lotus_elise1", "password_new": "ФФЫВфывЫФВ1"},
     {'trainer_token': ''},
     {'message': 'токен отсутствует', 'status': 'error'}),
]

valid_message = {"id": "2006", "message": "Успешная смена пароля"}
