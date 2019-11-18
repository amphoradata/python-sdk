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
    t1_start = time.perf_counter()  
    res = auth_api.authentication_request_token(token_request = token_request, x_amphoradata_version="0")
    t1_stop = time.perf_counter() 
    print("Elapsed time:", t1_stop - t1_start) # print performance indicator

    configuration.api_key["Authorization"] = "Bearer " + res
    # create an instance of the Users API, now with Bearer token
    users_api = amphora_client.UsersApi(amphora_client.ApiClient(configuration))
    me = users_api.users_read_self(x_amphoradata_version="0")
    print(me)

except ApiException as e:
    print("Exception when calling AuthenticationAPI: %s\n" % e)

