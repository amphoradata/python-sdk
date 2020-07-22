from logging import getLogger
logger = getLogger('amphora_file.py')

import os

from amphora.base import Base
import amphora_api_client as api
from amphora.errors import FileExistsError
"""
This class helps you manage Amphora Files
"""


class AmphoraFile(Base):
    def __init__(self, apiClient: api.ApiClient, amphora_id: str,
                 file_name: str):
        self._id = amphora_id
        self._file_name = file_name
        Base.__init__(self, apiClient)

    @property
    def name(self) -> str:
        return self._file_name

    def get_attributes(self) -> dict:
        amphora_metadata = self.amphoraeApi.amphorae_read(self._id)
        if self._file_name in amphora_metadata.file_attributes:
            return amphora_metadata.file_attributes[self._file_name]
        else:
            return None

    def pull(self, path):
        if os.path.exists(path):
            raise FileExistsError(path)
        # _preload_content=False allows binary content to not be attempted to be converted to a string
        httpResponse = self.amphoraeApi.amphorae_files_download_file(
            self._id, self._file_name, _preload_content=False)
        #open and read the file after the appending:
        f = open(path, "wb")
        f.write(httpResponse.data)
        f.close()
    
    def delete(self):
        """
        Deletes this file in the Amphora
        """
        try:
            self.amphoraeApi.amphorae_files_delete_file(self._id, self._file_name)
        except:
            print(f'Deletion of file {self._file_name} was attempted.')
