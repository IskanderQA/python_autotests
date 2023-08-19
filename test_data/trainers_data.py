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
     }, {'trainer_token': '9bd189a8403bc75b51d64f3e84e73754'},
     {'id': '2006', 'message': 'Информация о тренере обновлена'})
]

UPDATING_INFO_WITH_ERRORS = [
    ({
         "name": "",
         "city": "Tokyo"
     }, {'trainer_token': '9bd189a8403bc75b51d64f3e84e73754'},
     {'message': 'Отсутствует имя тренера(name)'}),
    ({
         "name": "Ash",
         "city": ""
     }, {'trainer_token': '9bd189a8403bc75b51d64f3e84e73754'},
     {'message': 'Отсутствует город пользователя(city)', 'status': 'error'}),
    ({
         "name": "Ash",
         "city": "New York"
     }, {'trainer_token': '9bd189a8403bc764f3e84e73754'},
     {'message': 'Неверный токен', 'status': 'error'}),
    ({
         "name": "Ash",
         "city": "New York"
     }, {'trainer_token': ''},
     {'message': 'токен отсутствует', 'status': 'error'}),
]

error_message_token = {"message": "токен отсутствует", "status": "error"}
error_message_trainer_not_found = {'message': 'Тренер отсутствует', 'status': 'error'}
