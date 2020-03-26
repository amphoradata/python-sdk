from datetime import datetime, timedelta

import pandas as pd
import numpy as np

import amphora.errors as errors
import amphora.utilities as utils
import amphora_api_client as api
from amphora_api_client.rest import ApiException

'''
Represents data stores as Amphora Signals
params:
    apiClient          amphora_api_client.ApiClient
    amphora_id         str
'''
class AmphoraSignals:
    def __init__(self, apiClient: api.ApiClient, amphora_id: str):
        self._id = amphora_id
        self._apiClient = apiClient
        self._amphoraApi = api.AmphoraeApi(apiClient)

    def __getitem__(self, property_name):
        for s in self.metadata:
            if s._property == property_name:
                return s
        raise ValueError(f'{property_name} not in signals')

    '''
    Get's a list of Signal metadata
    returns:
        [amphora_api_client.Signal]
    '''
    @property
    def metadata(self):
        return self._amphoraApi.amphorae_signals_get_signals(self._id)

    '''
    Downloads the data to a local object
    params:
        date_time_range [UTC] (default to 1 day)          amphora_api_client.DateTimeRange
    returns:
        amphora.SignalData
    '''
    def pull(self, date_time_range: api.DateTimeRange = None) :
        signals = self._amphoraApi.amphorae_signals_get_signals(self._id)
        if(date_time_range is None):
            date_time_range = default_date_time_range()

        ts_api = api.TimeSeriesApi(self._apiClient) # the API for interacting with time series
        
        # Create a variable object for getting temperature data
        variables = get_inline_variables(signals)
        get_series = api.GetSeries([self._id], search_span= date_time_range, inline_variables=variables)
        time_series_data = ts_api.time_series_query_time_series( api.QueryRequest(get_series= get_series))
        return SignalData(time_series_data)

    def update_attributes(self, property_name: str, attributes: dict) -> api.Signal:
        for k in attributes.keys():
            if utils.isString(k) and utils.isString(attributes[k]):
                pass
            else:
                raise errors.InvalidDataStructure(f'The attributes with key {k} must have key and value as strings')

        signal = self[property_name]
        update_signal = api.UpdateSignal(meta = attributes)
        return self._amphoraApi.amphorae_signals_update_signal(self._id, signal.id, update_signal = update_signal)


class SignalData:
    def __init__(self, data: api.QueryResultPage):
        self._data = data
    
    @property
    def data(self) -> api.QueryResultPage:
        return self._data

    def to_pandas(self, t_as_index = True, exclude_event_count = True):
        return to_df(self.data, t_as_index, exclude_event_count)


def default_date_time_range() -> api.DateTimeRange:
    yesterday = datetime.utcnow() + timedelta(hours=-24)
    return api.DateTimeRange(_from=yesterday , to= datetime.utcnow())

def get_inline_variables(signals: [api.Signal]) -> {}:
    variables = {}
    for signal in signals:
        if(signal.value_type == 'Numeric'):
            variable = api.NumericVariable( kind="numeric", 
                value=api.Tsx(tsx=f'$event.{signal._property}'), 
                aggregation=api.Tsx(tsx = "it doesn't matter"))
            variables[signal._property] = variable
        else:
            print(f'Not adding signal {signal._property} with value type {signal.value_type}')
    return variables

def to_df(query_result_page: api.QueryResultPage, t_as_index: bool, exclude_event_count: bool):
    '''
    Converts a QueryResultPage dataset to a Pandas DataFrame, using NumPy np.array
    params:
        query_result_page          amphora_client.QueryResultPage
    returns
        pd.DataFrame
    '''

    data = []
    column_names = []
    for _ in range(len(query_result_page.properties)):
        data.append(np.array(query_result_page.properties[_].values).reshape((len(query_result_page.properties[_].values))))
        column_names.append(query_result_page.properties[_].name)

    # dataframe
    df = pd.DataFrame(data).T
    if t_as_index:
        df.index =  np.array(query_result_page.timestamps)
        df.index.name = 't'
    else:
        df['t'] = np.array(query_result_page.timestamps)
        column_names.append('t')

    df.columns = column_names

    if exclude_event_count:
        del df['EventCount']

    return df