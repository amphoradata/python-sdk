import time
import os
from datetime import datetime, timedelta

import amphora_api_client as a10a
from amphora_api_client.rest import ApiException
from amphora_api_client.configuration import Configuration

import json

from amphora.client import AmphoraDataRepositoryClient, Credentials

# provide your login credentials
credentials = Credentials(username=os.environ['username'],
                          password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# https://beta.amphoradata.com/Amphorae/Detail?id=57d6593f-1889-410a-b1fb-631b6f9c9c85
id = "57d6593f-1889-410a-b1fb-631b6f9c9c85"

try:
    amphora_api = a10a.AmphoraeApi(client.apiClient)
    print(f'Getting signals for: {amphora_api.amphorae_read(id).name}')
    signals = amphora_api.amphorae_signals_get_signals(id)
    properties = list((s._property for s in signals))

    ts_api = a10a.TimeSeriesApi(
        client.apiClient)  # the API for interacting with time series
    tomorrow = datetime.now() + timedelta(hours=24)
    # Create a DateTimeRange to describe over what period we want data.
    time_range = a10a.DateTimeRange(_from=datetime.now(), to=tomorrow)
    # Create a variable object for getting temperature data
    temperatureVariable = a10a.NumericVariable(
        kind="numeric",
        value=a10a.Tsx(tsx="$event.temperature"),
        aggregation=a10a.Tsx(tsx="it doesn't matter"))
    get_series = a10a.GetSeries(
        [id],
        search_span=time_range,
        inline_variables={"temperature": temperatureVariable})
    time_series_data = ts_api.time_series_query_time_series(
        a10a.QueryRequest(get_series=get_series))

    print(
        f'Got {len(time_series_data.timestamps)} datapoints and {len(time_series_data.properties)} properties'
    )
    # access the data in time_series_data.properties
    print("-----------")

    # get average of tomorrow's rainfall probablility, filtered by description = Possible shower or Mostly cloudy
    variable = a10a.AggregateVariable(
        kind="aggregate", aggregation=a10a.Tsx("avg($event.rainProb)"))
    aggregate_series = a10a.AggregateSeries(
        [id],
        search_span=time_range,
        inline_variables={"rainProbAvg": variable},
        # filter is optional, for numeric filtering use `$event.rainProb.Double > 10` etc.
        filter=a10a.Tsx(
            "$event.description.String = 'Possible shower' OR $event.description.String = 'Mostly cloudy'"
        ),
        interval="PT24H")  # 24 hour buckets
    time_series_data = ts_api.time_series_query_time_series(
        a10a.QueryRequest(aggregate_series=aggregate_series))
    event_count = next(value for value in time_series_data.properties
                       if value.name == 'EventCount')
    rain_prob_average = next(value for value in time_series_data.properties
                             if value.name == 'rainProbAvg')

    for i in range(len(time_series_data.timestamps)):
        print(f'For date: {time_series_data.timestamps[i]}')
        print(f'There has been {event_count.values[i]} events ingested')
        print(
            f'And an average rain probability of {rain_prob_average.values[i]} in 24 hour buckets'
        )
        print("----------")

except ApiException as e:
    print("Exception when calling API: %s\n" % e)
