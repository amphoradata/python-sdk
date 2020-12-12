import os
from amphora.client import AmphoraDataRepositoryClient, Credentials

# provide your login credentials
credentials = Credentials(username=os.environ['username'],
                          password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# scope can be self or organisation
# access type can be created or purchased
amphoras = client.list_amphora(scope='self', access_type='purchased', take=5, skip=0)

print(amphoras)
