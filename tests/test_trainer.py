from common.helper.Schema.trainer import trainer_valid_structure, trainer_not_found
from test_data.trainers_data import CASE_TRAINERS, CASE_PAGINATION
from pytest_voluptuous import S
import pytest


class TestTrainers():

    def test_get_trainer_success(self, api):

        response = api.get_trainers(trainer_id=1927)
        api.status_code_should_be(200)

        assert S(trainer_valid_structure) == response.response.json()

    @pytest.mark.parametrize('case', CASE_TRAINERS)
    def test_get_trainer_errors(self, api, case):

        response = api.get_trainers(trainer_id=case['id'])
        api.status_code_should_be(case['status_code'])
        if response.response.status_code in [400, 404]:
            assert S(trainer_not_found) == response.response.json()
        else:
            assert S(trainer_valid_structure) == response.response.json()

    @pytest.mark.parametrize('pagination', CASE_PAGINATION)
    def test_get_trainers_check_pagination(self, pagination, api):

        response = api.get_trainers(page=pagination['page'])
        assert len(response.response.json()) == 31
