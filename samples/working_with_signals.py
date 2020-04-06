import os
from datetime import datetime, timedelta
from amphora.client import AmphoraDataRepositoryClient, Credentials
from amphora_api_client import DateTimeRange

# provide your login credentials
credentials = Credentials(username=os.environ['username'], password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# get a reference to an Amphora
amphora = client.get_amphora("57d6593f-1889-410a-b1fb-631b6f9c9c85")

# get a reference to the Amphora's signals
signals = amphora.get_signals()

# download some signals and convert to a pandas dataframe

dt_range = DateTimeRange(_from=datetime.utcnow() + timedelta(days=-1), to=datetime.utcnow() + timedelta(days=2))
df = signals.pull( date_time_range= dt_range, include_wt=True, tsi_api="GetEvents").to_pandas()

print(df)

# update a signal
temperature_signal = signals['temperature']

# update the temperature's units
temperature_signal.update_attributes({"units": "c"})
