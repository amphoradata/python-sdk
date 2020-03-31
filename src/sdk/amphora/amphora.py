import amphora_api_client as api
from amphora.base import Base
from amphora.amphora_file import AmphoraFile
from amphora.amphora_signals import AmphoraSignals
from amphora.amphora_signal_pusher import AmphoraSignalPusher
import amphora.errors as errors
import amphora.utilities as utils

import pandas as pd


class Amphora(Base):
    """
    This class heplps you manage amphora
    """
    def __init__(self, apiClient: api.ApiClient, amphora_id: str):
        self._id = amphora_id
        Base.__init__(self, apiClient)

    @property
    def amphora_id(self) -> str:
        """
        Gets the Amphora Id
        """
        return self._id
    
    @property
    def metadata(self) -> api.DetailedAmphora:
        """
        Gets the metadata of the Amphora
        """
        return self.amphoraeApi.amphorae_read(self.amphora_id)

    def update(self, **kwargs):
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

    def delete(self):
        self.amphoraeApi.amphorae_delete(self._id)

    def get_files(self) -> [AmphoraFile]:
        """
        Gets a list of files in this Amphora
        returns:
            [amphora.AmphoraFile]
        """
        file_names = self.amphoraeApi.amphorae_files_list_files(self._id)
        res = []
        for f in file_names:
            res.append(AmphoraFile(self._apiClient, self._id, f))
        return res

    def get_file(self, file_name: str) -> AmphoraFile:
        """
        Gets a reference to a file in this Amphora
        returns:
            amphora.AmphoraFile
        """
        files = self.amphoraeApi.amphorae_files_list_files(self._id)
        if file_name in files:
            return AmphoraFile(self._apiClient, self._id, file_name)
        else:
            raise errors.AmphoraFileNotFoundError()

    def push_file(self, file_path: str, file_name: str = None):
        """
        Uploads a file to the Data Repository for this Amphora
        params:
            file_path: str              Path to the file on this machine.
            file_name: str (optional)   Overrride the file name on Data Repository.
        """
        # open the file
        if not file_name:
            file_name = utils.path_leaf(file_path)
        
        file_req = self.amphoraeApi.amphorae_files_create_file_request(self._id, file_name )
        f = open(file_path, "rb")
        body=f.read()
        hdrs = dict({
            'x-ms-blob-type' : 'BlockBlob',
            'Content-Type': 'application/octet-stream'
            })
        response = self.amphoraeApi.api_client.rest_client.PUT(file_req.url, hdrs, body=body)
        if(response.status == 201):
            print("Successfully uploaded")
        else:
            print("Error uploading")
            raise errors.ApiError(response.data)

    def pull_file(self, file_name: str, download_path: str):
        """
        Downloads a file from the Data Repository to this machine.
        params:
            file_name: str              Name of the file to download. Must exist in the Amphora.
            download_path: str          Path where to download the file on this machine.
        """
        file_ref = self.get_file(file_name)
        file_ref.pull(download_path)

    def create_signal(self, property_name: str, value_type = 'Numeric', attributes = {} ) -> api.Signal: 
        """
        Creates a Signal definition in this Amphora.
        params:
            property_name: str            Name of the property, e.g. temperature.
            value_type = 'Numeric'        Type of property, either Numeric or String. Default is Numeric.
            attributes = {str: str}       A dictionary of attributes that are associated with the signal. 

            Note: Units is a special attribute you can use to render graphs with units.
        returns:
            amphora_api_client.Signal
        """
        signal = api.Signal(_property= property_name, value_type= value_type, attributes= attributes)
        signal = self.amphoraeApi.amphorae_signals_create_signal(self._id, signal)
        print(f'Created Signal {signal._property}')
        return signal

    def get_signals(self) -> AmphoraSignals:
        """
        Gets a reference to the signals in this Amphora.
        returns:
            amphora.AmphoraSignals
        """
        return AmphoraSignals(self._apiClient, self._id)
    
    def push_signals_df(self, df: pd.DataFrame, auto = True):
        """
        Uploads data to the Data Repository as Signals in this Amphora
        params:
            df: pandas.DataFrame          A dataframe containing data to be pushed.
            auto: boolean [True]          Automatically create the Signals on the Amphora

            Note: The dataframe should have a column called 't' containing the timstamps of the time series data.
                Dataframes without a 't' column will automatically have 't' set to the current time.
                Timestamps should be in UTC
                Columns require names.
        """
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
    
    def push_signals_dict_array(self, dictionaries: [dict]):
        """
        Uploads data to the Data Repository as Signals in this Amphora
        params:
            dictionary: [dict]            An array of dictionaries containing key value pairs of data

            Note: The dictionaries should have a property called 't' containing the timstamps of the time series data.
                Dictionaries without a 't' property will automatically have 't' set to the current time.
                Timestamps should be in UTC
        """
        pusher = AmphoraSignalPusher(self._apiClient, self._id)
        pusher.push_signals_dictionaries(dictionaries)

    # Restrictions
    def create_restriction(self, organisation_id: str) -> api.Restriction:
        """
        Creates a restriction by Organisation on this Amphora
        params:
            organisation_id: str          The organisation restricted from accessing this Amphora.
        returns:
            amphora_api_client.Restriction      
        """
        restriction = api.Restriction(target_organisation_id=organisation_id)
        return self.amphoraeApi.amphorae_restrictions_create(self.amphora_id, restriction)
    
    """
    Deletes a restriction by Id on this Amphora
    params:
        restriction_id: str          The id restriction you wish to delete.
    """
    def delete_restriction_by_id(self, restriction_id: str):
        self.amphoraeApi.amphorae_restrictions_delete(self.amphora_id, restriction_id )

def is_property_in_signals(signals: [api.Signal], prop: str) -> bool:
    isInSignals = False
    for s in signals:
        if s._property == prop:
            isInSignals = True
            break
    return isInSignals
    