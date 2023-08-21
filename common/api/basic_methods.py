import requests
from common.helper.logger import log

class Api:

    _HEADERS = {'Content-Type': 'application/json'}
    token = {'trainer_token':'9bd189a8403bc75b51d64f3e84e73754'}
    # _TIMEOUT = 10

    def __init__(self):
        '''
        Initialization
        '''
        self.response = None
        self.url = 'https://api.pokemonbattle.me:9104'

    def get(self, url: str, params: dict = None, token: str = None):
        '''
        Basic GET-request
            :param url:
            :param params:
            :param token:
            :return:
        '''
        if token:
            self._HEADERS['trainer_token'] = token

        self.response = requests.get(url=url,
                                     params=params,
                                     headers=self._HEADERS)
        log(response=self.response)
        return self

    def post(self, url: str, params: dict = None, headers: dict = None, json_body: dict = None, token: str = None):
        '''
        Basic POST-request
            :param headers:
            :param url:
            :param params:
            :param json_body:
            :param token:
            :return:
        '''
        if token is not None:
            self._HEADERS['trainer_token'] = token

        if headers:
            self._HEADERS.update(headers)

        self.response = requests.post(url=url,
                                      headers=self._HEADERS,
                                      params=params,
                                      json=json_body)
        log(response=self.response, request_body=json_body)
        return self

    def put(self, url: str, headers: dict = None, params: dict = None, json_body: dict = None, token: str = None):
        '''
        Basic PUT-request
            :param url:
            :param params:
            :param json_body:
            :param token:
            :return:
        '''

        if token is not None:
            self._HEADERS['trainer_token'] = token

        if headers:
            self._HEADERS.update(headers)

        self.response = requests.put(url=url,
                                     headers=self._HEADERS,
                                     params=params,
                                     json=json_body)
        log(response=self.response, request_body=json_body)
        return self

    def delete(self, url: str, headers: dict = None, json_body: dict = None, token: str = None):
        """
        Basic DELETE-request
            :param url:
            :param json_body:
            :param token:
            :return:
        """
        if token:
            self._HEADERS['trainer_token'] = token

        self.response = requests.delete(url=url,
                                        headers=self._HEADERS,
                                        json=json_body)
        log(response=self.response)
        return self

    def status_code_should_be(self, expected_code: int):

        """
        Checking the status code
            :param expected_code:
            :return:
        """

        actual_code = self.response.status_code
        assert expected_code == actual_code, f'\nОжидаемый статус-код: {expected_code} ' \
                                             f'\nФактический статус-код: {actual_code}'
        return self
