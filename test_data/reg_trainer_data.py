from config import token, second_token, email, password

REG_TRAINER_WITH_ERRORS = [
    ({
         "trainer_token": token,
         "email": email,
         "password": password
     }, {"message": "Аккаунт с таким токеном уже зарегистрирован", "status": "error"}),
    ({
         "trainer_token": '12333',
         "email": email,
         "password": password
     }, {'message': 'Неверный токен', 'status': 'error'}),
    ({
         "trainer_token": '',
         "email": email,
         "password": password
     }, {'message': 'токен отсутствует', 'status': 'error'}),
    ({
         "trainer_token": second_token,
         "email": email,
         "password": ''
     }, {'message': 'Аккаунт с такой почтой уже зарегистрирован', 'status': 'error'}),
    ({
         "trainer_token": second_token,
         "email": '',
         "password": 'QWErty2'
     }, {'message': 'Почта введена некорректно(email)', 'status': 'error'}),
    ({
         "trainer_token": second_token,
         "email": 'qwe123qqweqweqweqweqwe',
         "password": 'QWErty2'
     }, {'message': 'Почта введена некорректно(email)', 'status': 'error'}),
    ({
         "trainer_token": second_token,
         "email": 'qwe123qqweqweqweqweqwe@',
         "password": 'QWErty2'
     }, {'message': 'Почта введена некорректно(email)', 'status': 'error'}),
    ({
         "trainer_token": second_token,
         "email": 'test@test.test',
         "password": ''
     }, {'message': 'Пароль не должен быть пустым и иметь минимум 6 символов, 1 '
                    'заглавную букву и 1 цифру',
         'status': 'error'}),
    ({
         "trainer_token": second_token,
         "email": 'test@test.test',
         "password": ''
     }, {'message': 'Пароль не должен быть пустым и иметь минимум 6 символов, 1 '
                    'заглавную букву и 1 цифру',
         'status': 'error'}),

]