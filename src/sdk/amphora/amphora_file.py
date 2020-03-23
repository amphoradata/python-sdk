import amphora_api_client as api

"""
This class helps you manage Amphora Files
"""
class AmphoraFile:
    
    def __init__(self, apiClient: api.ApiClient, amphora_id: str, file_name: str):
        self._id = amphora_id
        self._file_name = file_name
        self._apiClient = apiClient
        self._amphoraApi = api.AmphoraeApi(self._apiClient)

    def get_attributes(self) -> dict:
        amphora_metadata = self._amphoraApi.amphorae_read(self._id)
        if self._file_name in amphora_metadata.file_attributes:
            return amphora_metadata.file_attributes[self._file_name]
        else:
            return None

    def download(self, path):
        content, res = self._amphoraApi.amphorae_files_download_file_with_http_info(self._id, self._file_name)
        #open and read the file after the appending:
        f = open(path, "wb")
        f.write(content)
        f.close()