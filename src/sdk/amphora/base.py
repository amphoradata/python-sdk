from logging import getLogger
logger = getLogger('base.py')

import amphora_api_client as api


class Base:
    def __init__(self, apiClient: api.ApiClient):
        self._apiClient = apiClient

    @property
    def apiClient(self) -> api.ApiClient:
        """
        The underlying API client
        returns:
            amphora_api_client.ApiClient
        """
        return self._apiClient

    @property
    def amphoraeApi(self) -> api.AmphoraeApi:
        return api.AmphoraeApi(self.apiClient)
