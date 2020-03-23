import amphora_api_client as api
from amphora.amphora_file import AmphoraFile
from amphora.errors import AmphoraFileNotFoundError

"""
This class heplps you manage amphora
"""

class Amphora:
    def __init__(self, apiClient: api.ApiClient, id: str):
        self._apiClient = apiClient
        self._id = id
        self._amphoraApi = api.AmphoraeApi(apiClient)
        self._metadata = self._amphoraApi.amphorae_read(id)

    """
    Gets the metadata of the Amphora
    """
    @property
    def metadata(self) -> api.DetailedAmphora:
        return self._metadata

    def get_files(self):
        return self._amphoraApi.amphorae_files_list_files(self._id)

    def get_file(self, file_name: str) -> AmphoraFile:
        files = self._amphoraApi.amphorae_files_list_files(self._id)
        if file_name in files:
            return AmphoraFile(self._apiClient, self._id, file_name)
        else:
            raise AmphoraFileNotFoundError()
