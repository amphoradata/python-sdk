from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
from openapi_client.configuration import Configuration

# Defining host is optional and default to http://localhost
configuration = Configuration()
configuration.host = "https://beta.amphoradata.com"
# Create an instance of the API class
auth_api = openapi_client.AuthenticationApi(openapi_client.ApiClient(configuration))

token_request = openapi_client.TokenRequest(username=os.environ['username'], password=os.environ['password'] ) 

try:
    # Deletes an Amphora
    res = auth_api.api_authentication_request_post(token_request = token_request)
    configuration.api_key["Authorization"] = "Bearer " + res
    # create an instance of the Users API, now with Bearer token
    users_api = openapi_client.UsersApi(openapi_client.ApiClient(configuration))
    me = users_api.api_users_self_get()
    print(me)

except ApiException as e:
    print("Exception when calling AuthenticationAPI: %s\n" % e)

