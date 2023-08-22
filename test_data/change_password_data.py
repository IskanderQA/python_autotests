from config import email, password, token

PASSWORD_CASES = [
    ({'email': email, "password_old": "123", "password_new": "123"},
     {'trainer_token': token},
     {"message": "Пароль должен иметь хотя-бы одну заглавную букву", "status": "error"}),  # valid params
    ({'email': email, "password_old": "123", "password_new": "ASD"},
     {'trainer_token': token},
     {"message": "Пароль не должен быть пустым и иметь минимум 6 символов, 1 заглавную букву и 1 цифру",
      "status": "error"}),
    ({'email': email, "password_old": "123", "password_new": "ФФЫВфывЫФВ1"},
     {'trainer_token': token},
     {'message': 'Неверные логин или пароль', 'status': 'error'}),
    ({'email': "", "password_old": "123", "password_new": "ФФЫВфывЫФВ1"},
     {'trainer_token': token},
     {'message': 'Неверные логин или пароль', 'status': 'error'}),
    ({'email': email, "password_old": password, "password_new": "ФФЫВфывЫФВ1"},
     {'trainer_token': '12345'},
     {'message': 'Неверный токен', 'status': 'error'}),
    ({'email': email, "password_old": password, "password_new": "ФФЫВфывЫФВ1"},
     {'trainer_token': ''},
     {'message': 'токен отсутствует', 'status': 'error'}),
]

valid_message = {"id": "2006", "message": "Успешная смена пароля"}
