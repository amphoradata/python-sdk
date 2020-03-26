import os
from amphora.client import AmphoraDataRepositoryClient, Credentials

# provide your login credentials
credentials = Credentials(username=os.environ['username'], password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# amphora id
amphora_id ="9ceff620-cbc8-4b60-9db3-8f6aad0a3630"
amphora = client.get_amphora(amphora_id)

print(amphora.metadata)
