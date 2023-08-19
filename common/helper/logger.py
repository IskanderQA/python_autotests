from loguru import logger
def log(response, request_body=None):
    '''
    Logging methods
        :param response:
        :param request_body:
        :return:
    '''

    logger.info(f'REQUEST METHOD: {response.request.method}')
    logger.info(f'REQUEST URL: {response.url}')
    logger.info(f'REQUEST HEADERS: {response.request.headers}')
    logger.info(f'REQUEST BODY: {request_body}')
    logger.info(f'STATUS CODE: {response.status_code}')
    logger.info(f'RESPONSE HEADERS: {response.headers}')
    logger.info(f'RESPONSE BODY: {response.text}')