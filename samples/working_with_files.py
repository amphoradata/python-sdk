import os
from amphora.client import AmphoraDataRepositoryClient, Credentials

NEW_FILE_NAME = "a_new_file.jpg"

# provide your login credentials
credentials = Credentials(username=os.environ['username'],
                          password=os.environ['password'],
                          host="https://app.amphoradata.com")
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# get a reference to an Amphora
amphora = client.create_amphora(name="Various Dogs", description="Contains labelled images of various types of dog breeds.")

# pushes the dog images to the Amphora Data Repository, with attributes
amphora.push_file("data/dogs/chihuahua.jpg", attributes = {'breed': 'chihuahua', 'size': 'small', 'primaryColour': 'brown'})
amphora.push_file("data/dogs/german-shepherd.jpg", attributes = {'breed': 'german-shepherd', 'size': 'large', 'primaryColour': 'brown'})
amphora.push_file("data/dogs/golden-retriever.jpg", attributes = {'breed': 'golden-retriever', 'size': 'large', 'primaryColour': 'gold'})
amphora.push_file("data/dogs/husky.jpg", attributes = {'breed': 'husky', 'size': 'large', 'primaryColour': 'white'})
amphora.push_file("data/dogs/labrador-puppy.jpg", attributes = {'breed': 'labrador', 'size': 'small', 'primaryColour': 'brown'})


#lists the files
files = amphora.get_files()
print(f'There are {len(files)} files')
for f in files:
    print(f.name)

# query the file by attribute
large_dogs = amphora.get_files(attributes={'size': 'large'})
print(f'There are {len(large_dogs)} large dogs:')
for f in large_dogs:
    print(f.name)

# check and remove so this doesn't fail a second time
if os.path.exists(NEW_FILE_NAME):
    os.remove(NEW_FILE_NAME)

#downloads the husky
file_reference = amphora.get_file("husky.jpg")
file_reference.pull(NEW_FILE_NAME)  # downloads the file to your local machine

# TODO: enable file deletion
file_reference.delete()
