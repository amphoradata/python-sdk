from logging import getLogger
logger = getLogger('amphora_signals.py')

from datetime import datetime, timedelta

import pandas as pd
import numpy as np

from amphora.base import Base
import amphora.errors as errors
import amphora.utilities as utils
import amphora_api_client as api
from amphora_api_client.rest import ApiException

tsi_api_get_series = "GetSeries"
tsi_api_get_events = "GetEvents"
tsi_api_aggregate_series = "AggregateSeries"


class SignalData:
    def __init__(self, data: api.QueryResultPage):
        self._data = data

    @property
    def data(self) -> api.QueryResultPage:
        return self._data

    def to_pandas(self, t_as_index=True, exclude_event_count=True):
        return to_df(self.data, t_as_index, exclude_event_count)


class AmphoraSignal(Base):
    '''
    Logically represents one Signal on an Amphora
    '''
    def __init__(self, apiClient: api.ApiClient, amphora_id: str,
                 signal_id: str):
        self._amphora_id = amphora_id
        self._id = signal_id
        Base.__init__(self, apiClient)

    @property
    def amphora_id(self):
        '''
        The Amphora ID
        '''
        return self._amphora_id

    @property
    def metadata(self):
        '''
        This signal metadata
        '''
        signals = self.amphoraeApi.amphorae_signals_get_signals(
            self._amphora_id)
        return utils.filter_by_id(signals, self._id)

    @property
    def property_name(self):
        '''
        The property name of this Signal
        '''
        self.metadata._property

    def get_attributes(self) -> dict:
        '''
        The attributes of this signal
        '''
        metadata = self.metadata
        return metadata.attributes

    def update_attributes(self, attributes: dict) -> api.Signal:
        '''
        Updates the attributes of this Signal.
        params:
            attributes: dict            Must be a dictionary of str -> str
        returns
            amphora_api_client.Signal
        '''
        for k in attributes.keys():
            if utils.isString(k) and utils.isString(attributes[k]):
                pass
            else:
                raise errors.InvalidDataStructure(
                    f'The attributes with key {k} must have key and value as strings'
                )

        update_signal = api.UpdateSignal(meta=attributes)
        return self.amphoraeApi.amphorae_signals_update_signal(
            self._amphora_id, self._id, update_signal=update_signal)

    '''
    Downloads the data to a local object
    params:
        date_time_range [UTC] (default to 1 day)                                        amphora_api_client.DateTimeRange
        include_wt (default TRUE)                                                       bool, includes the Write Time (wt)
        tsi_api (default: GetEvents, options: GetEvents, GetSeries, AggregateSeries)   str
    returns:
        amphora.SignalData
    '''

    def pull(self,
             date_time_range: api.DateTimeRange = None,
             include_wt: bool = False,
             tsi_api: str = "GetEvents") -> SignalData:
        validate_tsi_api_options(tsi_api)
        signals = self.amphoraeApi.amphorae_signals_get_signals(self._id)
        signal = utils.filter_by_id(signals,
                                    self._id)  # filter for just 1 signal
        if (date_time_range is None):
            date_time_range = default_date_time_range()

        ts_api = api.TimeSeriesApi(
            self._apiClient)  # the API for interacting with time series

        # Create a variable object for getting temperature data
        variables = get_inline_variables([signal], include_wt)
        if tsi_api == tsi_api_get_series:
            get_series = api.GetSeries([self._id],
                                       search_span=date_time_range,
                                       inline_variables=variables)
            qr = api.QueryRequest(get_series=get_series)
        elif tsi_api == tsi_api_get_events:
            get_events = api.GetEvents([self._id], search_span=date_time_range)
            qr = api.QueryRequest(get_events=get_events)
        elif tsi_api == tsi_api_aggregate_series:
            # this might not work
            aggregate_series = api.AggregateSeries([self._id],
                                                   search_span=date_time_range,
                                                   inline_variables=variables)
            qr = api.QueryRequest(aggregate_series=aggregate_series)

        time_series_data = ts_api.time_series_query_time_series(qr)
        return SignalData(time_series_data)


class AmphoraSignals(Base):
    '''
    Represents data stores as Amphora Signals
    params:
        apiClient          amphora_api_client.ApiClient
        amphora_id         str
    '''
    def __init__(self, apiClient: api.ApiClient, amphora_id: str):
        self._id = amphora_id
        Base.__init__(self, apiClient)

    def __getitem__(self, property_name) -> AmphoraSignal:
        for s in self.metadata:
            if s._property == property_name:
                return AmphoraSignal(self.apiClient, self._id, s._id)
        raise ValueError(f'{property_name} not in signals')

    @property
    def metadata(self):
        '''
        Get's a list of Signal metadata
        returns:
            [amphora_api_client.Signal]
        '''
        return self.amphoraeApi.amphorae_signals_get_signals(self._id)

    def contains_signal(self, _property: str) -> bool:
        """
        Get's a list of Signal metadata
        params:
            _property: str              The name of the property to check
        returns:
            bool                        True if a signal exists with that property.
        """
        try:
            signal = self.amphoraeApi.amphorae_signals_get_signal(
                self._id, _property=_property)
            return signal is not None
        except ApiException as e:
            logger.error(f'An Api Exception was thrown: {e}')
            return False

    def pull(self,
             date_time_range: api.DateTimeRange = None,
             include_wt: bool = False,
             tsi_api: str = "GetSeries") -> SignalData:
        '''
        Downloads the data to a local object
        params:
            date_time_range [UTC] (default to 1 day)                    amphora_api_client.DateTimeRange
            include_wt (default TRUE)                                   bool, includes the Write Time (wt)
            tsi_api (options: GetSeries, GetEvents, AggregateSeries)    str
        returns:
            amphora.SignalData
        '''
        validate_tsi_api_options(tsi_api)
        signals = self.amphoraeApi.amphorae_signals_get_signals(self._id)
        if (date_time_range is None):
            date_time_range = default_date_time_range()

        ts_api = api.TimeSeriesApi(
            self._apiClient)  # the API for interacting with time series

        # Create a variable object for getting temperature data
        variables = get_inline_variables(signals, include_wt)

        if tsi_api == tsi_api_get_series:
            get_series = api.GetSeries([self._id],
                                       search_span=date_time_range,
                                       inline_variables=variables)
            qr = api.QueryRequest(get_series=get_series)
        elif tsi_api == tsi_api_get_events:
            get_events = api.GetEvents([self._id], search_span=date_time_range)
            qr = api.QueryRequest(get_events=get_events)
        elif tsi_api == tsi_api_aggregate_series:
            # this might not work
            aggregate_series = api.AggregateSeries([self._id],
                                                   search_span=date_time_range,
                                                   inline_variables=variables)
            qr = api.QueryRequest(aggregate_series=aggregate_series)
        time_series_data = ts_api.time_series_query_time_series(qr)
        return SignalData(time_series_data)


def default_date_time_range() -> api.DateTimeRange:
    yesterday = datetime.utcnow() + timedelta(hours=-24)
    return api.DateTimeRange(_from=yesterday, to=datetime.utcnow())


def get_inline_variables(signals: [api.Signal], include_wt: bool) -> {}:
    variables = {}
    for signal in signals:
        if (signal.value_type == 'Numeric'):
            variable = api.NumericVariable(
                kind="numeric",
                # https://docs.microsoft.com/en-us/rest/api/time-series-insights/reference-time-series-expression-syntax#other-functions
                value=api.Tsx(tsx=f'coalesce($event.{signal._property}.Double, toDouble($event.{signal._property}.Long))'),
                aggregation=api.Tsx(tsx="it doesn't matter"))
            variables[signal._property] = variable
        else:
            logger.info(
                f'Not adding signal {signal._property} with value type {signal.value_type}'
            )
    if include_wt:
        variables["wt"] = variable = api.NumericVariable(
            kind="numeric",
            value=api.Tsx(tsx='$event.wt'),
            aggregation=api.Tsx(tsx="avg($value)"))
    return variables


def to_df(query_result_page: api.QueryResultPage, t_as_index: bool,
          exclude_event_count: bool):
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
        data.append(
            np.array(query_result_page.properties[_].values).reshape(
                (len(query_result_page.properties[_].values))))
        column_names.append(query_result_page.properties[_].name)

    # dataframe
    df = pd.DataFrame(data).T
    if t_as_index:
        df.index = np.array(query_result_page.timestamps)
        df.index.name = 't'
    else:
        df['t'] = np.array(query_result_page.timestamps)
        column_names.append('t')

    df.columns = column_names

    if exclude_event_count and "EventCount" in df:
        del df["EventCount"]

    return df


def validate_tsi_api_options(tsi_api: str):
    if tsi_api == tsi_api_get_series:
        pass
    elif tsi_api == tsi_api_get_events:
        pass
    elif tsi_api == tsi_api_aggregate_series:
        pass
    else:
        raise ValueError(
            "tsi_api must be one of GetSeries, GetEvents, AggregateSeries")
