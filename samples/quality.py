import os
from amphora_api_client import Quality
from amphora.client import AmphoraDataRepositoryClient, Credentials

# provide your login credentials
credentials = Credentials(username=os.environ['username'],
                          password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# get a reference to an Amphora
amphora = client.get_amphora("e48c9a35-4696-406c-a963-8e72a8bf0131")

quality = Quality() # Quality | The data quality metrics.
quality.accuracy = 2

res = client.amphoraeApi.amphora_quality_set(amphora.amphora_id, quality)
print(res)