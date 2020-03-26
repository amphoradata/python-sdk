import os
from amphora.client import AmphoraDataRepositoryClient, Credentials

# provide your login credentials
credentials = Credentials(username=os.environ['username'], password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)
# get information about the logged in user
my_information = client.get_self()
print(my_information)

# {'about': "I'm the CTO at Amphora Data.",
#  'email': None,
#  'full_name': 'Rian Finnegan',
#  'id': 'd54505c0-2756-44e6-8b99-e7fb0fbc8711',
#  'last_modified': datetime.datetime(2020, 3, 23, 0, 3, 54, 922250, tzinfo=tzutc()),
#  'organisation_id': '7b429e6c-2885-49cf-994d-4775ae170d64',
#  'user_name': 'rian@amphoradata.com'}
