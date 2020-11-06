import os
from amphora.client import AmphoraDataRepositoryClient, Credentials

# provide your login credentials
credentials = Credentials(username=os.environ['username'],
                          password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

results=client.search_amphora(term='Fridley Creek', labels='waterquality', take=5)

print(results.count)
print(f'There are {results.count} search results, and {len(results.items)} in items list')
if results.count > 0:
    print(results.items[0])

