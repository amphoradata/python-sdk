
# This script shows how to filter a time series query based on the write time.
# Every set of values written to an Amphora Signal contains a special property: the write time.
# The write time property (actually "wt") allows us to filter data when multiple values occur coincidentally.
# For example, in this case, there are multiple forecasts made for the same time.

import time
import os
from datetime import datetime, timedelta

from amphora.client import AmphoraDataRepositoryClient, Credentials
import amphora_api_client as a10a
from amphora_api_client.rest import ApiException
from amphora_api_client.configuration import Configuration

import json


# provide your login credentials
credentials = Credentials(username=os.environ['username'], password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# Melbourne Airport Weather
# https://beta.amphoradata.com/Amphorae/Detail?id=df92aa12-ab88-4014-a3c3-d90d01a7698d
id = "df92aa12-ab88-4014-a3c3-d90d01a7698d" 

def removeNones(a_list):
    return [i for i in a_list if i] 

try:

    amphora_api = a10a.AmphoraeApi(client.apiClient)
    print(f'Getting signals for: {amphora_api.amphorae_read(id).name}')
    print("-----------")
    signals = amphora_api.amphorae_signals_get_signals(id)
    properties=list((s._property for s in signals))

    ts_api = a10a.TimeSeriesApi(client.apiClient) # the API for interacting with time series
    one_hour_ago = datetime.utcnow() + timedelta(hours=-1)
    # Create a DateTimeRange to describe over what period we want data.
    time_range = a10a.DateTimeRange(_from = one_hour_ago , to= datetime.utcnow())
    
    # let's get the maximum write time for the period
    maxWtVar = a10a.AggregateVariable( 
        kind="aggregate", 
        aggregation=a10a.Tsx("max($event.wt)"))
    minWtVar = a10a.AggregateVariable( 
        kind="aggregate", 
        aggregation=a10a.Tsx("min($event.wt)"))
    get_aggregate = a10a.AggregateSeries([id], 
        search_span=time_range,
        interval= "PT4H",
        projected_variables=["maxWt", "minWt"],
        inline_variables={"maxWt": maxWtVar, "minWt": minWtVar})
    agg_data = ts_api.time_series_query_time_series( a10a.QueryRequest(aggregate_series= get_aggregate))

    maxWt = max(agg_data.properties[0].values) # max value from max list
    minWt = min(agg_data.properties[1].values) # min value from min list

    # Create a variable object for getting temperature data
    temperatureVariable = a10a.NumericVariable( 
        kind="numeric", 
        value=a10a.Tsx(tsx="$event.temperature"),
        aggregation=a10a.Tsx("max($value)"))

    get_series = a10a.GetSeries([id], 
        search_span= time_range, 
        projected_variables=["temp"],
        inline_variables={"temp": temperatureVariable})

    time_series_data = ts_api.time_series_query_time_series( a10a.QueryRequest(get_series= get_series))
    maxVal = max(time_series_data.properties[0].values)
    minVal = min(time_series_data.properties[0].values)
    lenVals = len(time_series_data.properties[0].values)
    print(f'Got maximum of {maxVal} and min of {minVal} from {lenVals} values')
    # access the data in time_series_data.properties
    print("-----------")

    # By filtering by the maximum write time, we get only the "most recent" forecast (and therefore probably the most accurate historically)
    temperatureVariable.filter = a10a.Tsx(tsx="$event.wt = " + str(maxWt)) # add a filter for only the maximum write time
    time_series_data = ts_api.time_series_query_time_series( a10a.QueryRequest(get_series= get_series))

    maxVal = max(removeNones(time_series_data.properties[0].values))
    minVal = min(removeNones(time_series_data.properties[0].values))
    lenVals = len(removeNones(time_series_data.properties[0].values))
    print(f'Got maximum of {maxVal} and min of {minVal} from {lenVals} values')
    # access the data in time_series_data.properties
    print("-----------")

except ApiException as e:
    print("Exception when calling API: %s\n" % e)

