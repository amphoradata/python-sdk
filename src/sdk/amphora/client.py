import amphora_api_client as api
from amphora.amphora import Amphora

# metadata objects
# GET
# CREATE
# UPDATE
# DELETE

# for data objects
# PUSH
# PULL

# management
# SHARE

class Credentials:

    def __init__(self, username: str, password: str):
        configuration = api.Configuration()
        authApi = api.AuthenticationApi(api.ApiClient(configuration))
        tr = api.TokenRequest(username=username, password=password)
        self.token = authApi.authentication_request_token(token_request = tr)

class AmphoraClient:

    def __init__(self, credentials: Credentials):
        configuration = api.Configuration()
        configuration.api_key["Authorization"] = "Bearer " + credentials.token
        self.client = api.ApiClient(configuration=configuration)

    """
    Gets an object to interact with the Amphora
    """
    def get_amphora(self, amphora_id: str) -> Amphora:
        return Amphora(self.client, amphora_id)

    """
    Gets the metadata of the logged in user
    """
    def get_self(self) -> api.AmphoraUser:
        usersApi = api.UsersApi(self.client)
        return usersApi.users_read_self()
