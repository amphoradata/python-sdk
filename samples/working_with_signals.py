import os
from amphora.client import AmphoraDataRepositoryClient, Credentials

# provide your login credentials
credentials = Credentials(username=os.environ['username'], password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# get a reference to an Amphora
amphora = client.get_amphora("e6097df0-952c-46a6-84b0-ccc29bf1b0f7")

# get a reference to the Amphora's signals
signals = amphora.get_signals()

# download some signals and convert to a pandas dataframe
df = signals.pull().to_pandas()

print(df)

# update a signal
temperature_signal = signals['temperature']

# update the temperature's units
temperature_signal.update_attributes({"units": "farenheit"})
