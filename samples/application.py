import os
from amphora.client import AmphoraDataRepositoryClient, Credentials
from amphora_api_client import ApplicationsApi, CreateApplication, AppLocation

# provide your login credentials
credentials = Credentials(username=os.environ['username'],
                          password=os.environ['password'])
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

# create an amphora
appApi = ApplicationsApi(client.apiClient)
appLocations = [
    AppLocation(origin="http://localhost:3000", allowed_redirect_paths=["/#/callback"])
]

app = appApi.applications_create_application(
    CreateApplication(
    name="react-amphora-dev", 
    locations=appLocations, 
    logout_url="http://localhost:3000/logout" ))

print(f'Your Application ID is {app.id}')

