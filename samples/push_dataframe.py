import os
from datetime import datetime
from amphora.client import AmphoraDataRepositoryClient, Credentials
import pandas as pd

# create a dataframe of some random data
data = [
    [datetime(2020, 10, 6), 20], 
    [datetime(2020, 10, 7), 15], 
    [datetime(2020, 10, 8), 16],
    [datetime(2020, 10, 9), 17],
    [datetime(2020, 10, 10), 18],
    ]

# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['t', 'temperature']) 
print(df)
# provide your login credentials
credentials = Credentials(username=os.environ['username'],
                          password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# create an amphora
amphora = client.create_amphora("My New Signal Store", "This is a description of a new Amphora")

amphora.push_signals_df(df)
print("Signals pushed!")
# delete the amphora
amphora.delete()
print("Amphora deleted.")