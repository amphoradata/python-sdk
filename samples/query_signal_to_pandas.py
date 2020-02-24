import os
from datetime import datetime, timedelta

import amphora_client as a10a
from amphora_client.rest import ApiException
from amphora_client.configuration import Configuration

# Import this to convert to Pandas.DataFrame
import amphora_extensions.pandas as a10a_pd

configuration = Configuration()
configuration.host = "https://beta.amphoradata.com"

# Create an instance of the auth API class
auth_api = a10a.AuthenticationApi(a10a.ApiClient(configuration))

token_request = a10a.TokenRequest(username=os.environ['username'], password=os.environ['password'] ) 

# https://beta.amphoradata.com/Amphorae/Detail?id=57d6593f-1889-410a-b1fb-631b6f9c9c85
id = "57d6593f-1889-410a-b1fb-631b6f9c9c85" 

try:
    # Gets a token
    res = auth_api.authentication_request_token(token_request = token_request )
    configuration.api_key["Authorization"] = "Bearer " + res

    amphora_api = a10a.AmphoraeApi(a10a.ApiClient(configuration))
    print(f'Getting signals for: {amphora_api.amphorae_read(id).name}')
    signals = amphora_api.amphorae_signals_get_signals(id)
    properties=list((s._property for s in signals))

    ts_api = a10a.TimeSeriesApi(a10a.ApiClient(configuration)) # the API for interacting with time series
    tomorrow = datetime.now() + timedelta(hours=24)
    # Create a DateTimeRange to describe over what period we want data.
    time_range = a10a.DateTimeRange(_from = datetime.now(), to= tomorrow)
    # Create a variable object for getting temperature data
    temperatureVariable = a10a.NumericVariable( kind="numeric", 
        value=a10a.Tsx(tsx="$event.temperature"), 
        aggregation=a10a.Tsx(tsx = "it doesn't matter"))

    get_series = a10a.GetSeries([id], search_span= time_range, inline_variables={"temperature": temperatureVariable})
    time_series_data = ts_api.time_series_query_time_series( a10a.QueryRequest(get_series= get_series))

    print(f'Got {len(time_series_data.timestamps)} datapoints and {len(time_series_data.properties)} properties')

    # Convert to a pandas dataframe!
    df = a10a_pd.to_df(time_series_data)
    print(df)

except ApiException as e:
    print("Exception when calling API: %s\n" % e)


