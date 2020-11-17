import os
from amphora.client import AmphoraDataRepositoryClient, Credentials

# provide your login credentials
credentials = Credentials(username=os.environ['username'],
                          password=os.environ['password'],
                          host="https://app.amphoradata.com")
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)
# get a reference to an Amphora
amphora = client.get_amphora("84f36667-9bc9-4da1-baba-1ef3160eae0f")

# skip = number of files to ignore
# take= the max num of files in the list
# order_by = the way to order the files. Choose Alphabetical (default) or LastModified
files = amphora.get_files(skip=90, take=30)

print(f'The client returned a list with {len(files)} names')
print(f'The first file name is {files[0].name}')

# download a file
f1 = files[0]
print(f'The first file name is {f1.name}')
f1.pull(f'./data/{f1.name}')

# alternate way to download the file
f2 = amphora.get_file(files[1].name)
print(f2.name)
f2.pull(f'./data/{f2.name}')
