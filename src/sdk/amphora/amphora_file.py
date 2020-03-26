import os

import amphora_api_client as api
from amphora.errors import FileExistsError

"""
This class helps you manage Amphora Files
"""
class AmphoraFile:
    
    def __init__(self, apiClient: api.ApiClient, amphora_id: str, file_name: str):
        self._id = amphora_id
        self._file_name = file_name
        self._apiClient = apiClient
        self._amphoraApi = api.AmphoraeApi(self._apiClient)

    @property
    def name(self) -> str:
        return self._file_name

    def get_attributes(self) -> dict:
        amphora_metadata = self._amphoraApi.amphorae_read(self._id)
        if self._file_name in amphora_metadata.file_attributes:
            return amphora_metadata.file_attributes[self._file_name]
        else:
            return None

    def pull(self, path):
        if os.path.exists(path):
            raise FileExistsError(path)
        # _preload_content=False allows binary content to not be attempted to be converted to a string
        httpResponse = self._amphoraApi.amphorae_files_download_file(self._id, self._file_name, _preload_content=False)
        #open and read the file after the appending:
        f = open(path, "wb")
        f.write(httpResponse.data)
        f.close()