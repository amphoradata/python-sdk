import os
from amphora.client import AmphoraDataRepositoryClient, Credentials

# provide your login credentials
credentials = Credentials(username=os.environ['username'], password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# get a reference to an Amphora
amphora = client.create_amphora(name="Access Controls Example", description="Used for showing Access Controls")

amphora.share_with("coyote@acme.org") # the username of the person to share with
