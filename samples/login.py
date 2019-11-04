from __future__ import print_function
import time
import os
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint
from amphora_client.configuration import Configuration

# Defining host is optional and default to http://localhost
configuration = Configuration()
configuration.host = "https://beta.amphoradata.com"
# Create an instance of the API class
auth_api = amphora_client.AuthenticationApi(amphora_client.ApiClient(configuration))

token_request = amphora_client.TokenRequest(username=os.environ['username'], password=os.environ['password'] ) 


try:
    # Gets a token
    res = auth_api.authentication_request_token(token_request = token_request)
    configuration.api_key["Authorization"] = "Bearer " + res
    # create an instance of the Users API, now with Bearer token
    users_api = amphora_client.UsersApi(amphora_client.ApiClient(configuration))
    me = users_api.users_read_self()
    print(me)

except ApiException as e:
    print("Exception when calling AuthenticationAPI: %s\n" % e)

