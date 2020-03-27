import os
from amphora.client import AmphoraDataRepositoryClient, Credentials

# provide your login credentials
credentials = Credentials(username=os.environ['username'], password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# create an amphora
amphora = client.create_amphora("My New Data Store", "This is a description of my new Amphora")
# update the amphora
amphora.update(price=10, labels = ["custom", "labels"])
# delete the amphora
amphora.delete()
