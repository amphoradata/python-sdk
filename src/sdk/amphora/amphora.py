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
    def __init__(self, apiClient: api.ApiClient, amphora_id: str):
        self._apiClient = apiClient
        self._id = amphora_id
        self._amphoraApi = api.AmphoraeApi(apiClient)
        self._metadata = self._amphoraApi.amphorae_read(amphora_id)

    """
    Gets the Amphora Id
    """
    @property
    def amphora_id(self) -> str:
        return self._id
    
    """
    Gets the metadata of the Amphora
    """
    @property
    def metadata(self) -> api.DetailedAmphora:
        return self._metadata

    """
    Updates this Amphora
    params:
        id: str                         the id of the Amphora
        **kwargs:
            name: str                       the name of the Amphora
            description :str                a description of the Amphora
            price: float                    a monthly fee (in AUD)
            lat: float                      latitude
            lon: float                      longitude
            terms_and_conditions_id: str    id reference of the terms and conditions to apply
            labels: [str]                   a list (max 5) of labels
    returns:
        amphora.Amphora
    """
    def update(self, **kwargs):
        amphoraApi = api.AmphoraeApi(self._apiClient)
        model = amphoraApi.amphorae_read(self.amphora_id)
        model.name = kwargs["name"] if "name" in kwargs else model.name
        model.description = kwargs["description"] if "description" in kwargs else model.description
        model.price= kwargs["price"] if "price" in kwargs else model.price
        model.lat:float= kwargs["lat"] if "lat" in kwargs else model.lat
        model.lon:float= kwargs["lon"] if "lon" in kwargs else model.lon
        model.terms_and_conditions_id: str = kwargs["terms_and_conditions_id"] if "terms_and_conditions_id" in kwargs else model.terms_and_conditions_id
        model.labels: [str] = ",".join(kwargs["labels"]) if "labels" in kwargs else model.labels
        
        model = amphoraApi.amphorae_update(self.amphora_id, model)

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

    def push_file(self, file_path: str, file_name: str = None):
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
        print(f'Created Signal {signal._property}')
        return signal


    def get_signals(self) -> AmphoraSignals:
        return AmphoraSignals(self._apiClient, self._id)
    
    def push_signals(self, df: pd.DataFrame, auto = True):
        pusher = AmphoraSignalPusher(self._apiClient, self._id)
        signals = self.get_signals()
        if auto:
            print(f'Automatically creating signals for Amphora({self._id})')
            # create the signals
            for column_name in df:
                if not df[column_name].name:
                    raise errors.InvalidDataStructure("Column has no name")
                if is_property_in_signals(signals.metadata, df[column_name].name) or df[column_name].name == 't':
                    print(f'Signal {df[column_name].name} exists on Amphora({self._id})')
                else:
                    print(f'Auto creating Signal {df[column_name].name} on Amphora({self._id})')
                    value_type = utils.infer_value_type_from_value(df[column_name].iloc[0])
                    self.create_signal(df[column_name].name, value_type)
        pusher.push(df)

def is_property_in_signals(signals: [api.Signal], prop: str) -> bool:
    isInSignals = False
    for s in signals:
        if s._property == prop:
            isInSignals = True
            break
    return isInSignals
    