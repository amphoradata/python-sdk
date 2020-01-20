import os
import amphora_client
from amphora_client.rest import ApiException
from amphora_client.configuration import Configuration

configuration = Configuration()
# Create an instance of the API class
auth_api = amphora_client.AuthenticationApi(amphora_client.ApiClient(configuration))
token_request = amphora_client.TokenRequest(username=os.environ['username'], password=os.environ['password'] ) 


try:
    # Gets a token
    res = auth_api.authentication_request_token(token_request = token_request, x_amphoradata_version="0")

    configuration.api_key["Authorization"] = "Bearer " + res
    # create an instance of the Users API, now with Bearer token
    amphora_api = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))
    sydney_weather = amphora_api.amphorae_read('9ceff620-cbc8-4b60-9db3-8f6aad0a3630')
    print(sydney_weather)

except ApiException as e:
    print("Exception when calling API: %s\n" % e)

