import amphora_api_client as api
from amphora.amphora_file import AmphoraFile
from amphora.amphora_signals import AmphoraSignals
from amphora.amphora_signal_pusher import AmphoraSignalPusher
import amphora.errors as errors
import amphora.utilities as utils


import pandas as pd

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

    def get_files(self) -> [AmphoraFile]:
        file_names = self._amphoraApi.amphorae_files_list_files(self._id)
        res = []
        for f in file_names:
            res.append(AmphoraFile(self._apiClient, self._id, f))
        return res

    def get_file(self, file_name: str) -> AmphoraFile:
        files = self._amphoraApi.amphorae_files_list_files(self._id)
        if file_name in files:
            return AmphoraFile(self._apiClient, self._id, file_name)
        else:
            raise errors.AmphoraFileNotFoundError()

    def push_file(self, file_path: str, file_name: str):
        # open the file
        if not file_name:
            file_name = utils.path_leaf(file_path)
        
        file_req = self._amphoraApi.amphorae_files_create_file_request(self._id, file_name )
        f = open(file_path, "rb")
        body=f.read()
        hdrs = dict({
            'x-ms-blob-type' : 'BlockBlob',
            'Content-Type': 'application/octet-stream'
            })
        response = self._amphoraApi.api_client.rest_client.PUT(file_req.url, hdrs, body=body)
        if(response.status == 201):
            print("Successfully uploaded")
        else:
            print("Error uploading")
            raise errors.ApiError(response.data)

    def pull_file(self, file_name: str, download_path: str):
        file_ref = self.get_file(file_name)
        file_ref.pull(download_path)

    def create_signal(self, property_name: str, value_type = 'Numeric', attributes = {} ) -> api.Signal: 
        signal = api.Signal(_property= property_name, value_type= value_type, attributes= attributes)
        signal = self._amphoraApi.amphorae_signals_create_signal(self._id, signal)
        return signal


    def get_signals(self) -> AmphoraSignals:
        return AmphoraSignals(self._apiClient, self._id)
    
    def push_signals(self, df: pd.DataFrame, auto = True):
        pusher = AmphoraSignalPusher(self._apiClient, self._id)
        if auto:
            # create the signals
            for column in df:
                if not column.name:
                    raise errors.InvalidDataStructure("Column has no name")
                value_type = utils.infer_value_type_from_value(column.iloc[0])
                self.create_signal(column.name, value_type)
        pusher.push(df)
