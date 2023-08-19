from test_data.battles_data import CASE_BATTLES
import pytest


class TestBattles():

    def test_get_all_battles_success(self, battles_api):
        '''
        GET /battles
        :return:
        '''

        response = battles_api.get_battles()
        battles_api.status_code_should_be(200)

    def test_get_battles_from_trainer_success(self, battles_api):
        '''
        GET /battles?trainer_id=
        :return:
        '''

        response = battles_api.get_battles(trainer_id=1987)
        battles_api.status_code_should_be(200)

    @pytest.mark.parametrize('case', CASE_BATTLES)
    def test_get_battles_from_trainer_errors(self, battles_api, case):
        response = battles_api.get_battles(trainer_id=case['id'])
        battles_api.status_code_should_be(case['status_code'])
