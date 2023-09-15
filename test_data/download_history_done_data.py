from config import token, trainer_id

DOWNLOAD_HISTORY_DONE_ERRORS = [
    ({'trainer_token': token}, {'user_id': trainer_id},
     {'message': 'Задача уже завершена', 'status': 'error'}),
    ({'trainer_token': ''}, {'user_id': trainer_id}, {'message': 'токен отсутствует', 'status': 'error'}),
    ({'trainer_token': '1234'}, {'user_id': trainer_id},
     {'message': 'Неверный токен', 'status': 'error'}),
    ({'trainer_token': token}, {'user_id': ''},
     {'message': 'Отсутствует id пользователя(user_id)'}),
    ({'trainer_token': token}, {'user_id': '0'},
     {'message': 'Пользователь вам не принадлежит', 'status': 'error'})

]