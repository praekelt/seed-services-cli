from demands import JSONServiceClient


class StageBasedMessagingApiClient(object):
    """
    Client for Stage Based Messaging Service.

    :param str auth_token:

        An access token.

    :param str api_url:
        The full URL of the API.

    """

    def __init__(self, auth_token, api_url, session=None):
        headers = {'Authorization': 'Token ' + auth_token}
        if session is None:
            session = JSONServiceClient(url=api_url,
                                        headers=headers)
        self.session = session

    def get_schedules(self, params=None):
        return self.session.get('/schedule/', params=params)
