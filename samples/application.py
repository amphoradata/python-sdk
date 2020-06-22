import os
from amphora.client import AmphoraDataRepositoryClient, Credentials
from amphora_api_client import ApplicationsApi, CreateApplication, AppLocation, UpdateApplication

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

# you can also update an application's locations
# here we are adding the 'production' location for react-amphora-example
appLocations.append(AppLocation(origin="https://react-amphora-example.xtellurian.vercel.app", allowed_redirect_paths=["/#/callback"]))
updateModel = UpdateApplication(id=app.id, name=app.name, logout_url=app.logout_url, locations=appLocations)
updatedApplication = appApi.applications_update_application(app.id, update_application=updateModel)
