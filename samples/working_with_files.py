import os
from amphora.client import AmphoraDataRepositoryClient, Credentials

# provide your login credentials
credentials = Credentials(username=os.environ['username'], password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# get a reference to an Amphora
amphora = client.get_amphora("e6097df0-952c-46a6-84b0-ccc29bf1b0f7")

# pushes the 'dog.jpg' file to the Amphora Data Repository
amphora.push_file("dog.jpg")

#lists the files
files = amphora.get_files()
print(f'There are {len(files)} files')
for f in files:
    print(f.name)

#downloads the file
file_reference = amphora.get_file("dog.jpg")
file_reference.pull("a_new_file.jpg") # downloads the file to your local machine

# TODO: enable file deletion
# file_reference.delete()