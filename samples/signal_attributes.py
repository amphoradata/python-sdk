import os
import amphora_client
from amphora_client.rest import ApiException
from amphora_client.configuration import Configuration

configuration = Configuration()
# Create an instance of the API class
auth_api = amphora_client.AuthenticationApi(amphora_client.ApiClient(configuration))

token_request = amphora_client.TokenRequest(username=os.environ['username'], password=os.environ['password'] ) 

try:
    res = auth_api.authentication_request_token(token_request = token_request)
    print('got a token')
    configuration.api_key["Authorization"] = "Bearer " + res
    client = amphora_client.ApiClient(configuration)
    amphoraApi = amphora_client.AmphoraeApi(client)

    dto = amphora_client.CreateAmphora(name = "Signal Attributes Example", price = 0, 
        description="This is an Amphora created to show how to add Signal attributes Python SDK")

    amphora = amphoraApi.amphorae_create(dto)
    print('created amphora')

    signal = amphora_client.Signal(_property="sample", value_type="Numeric", attributes={'units': 'mm'} )
    signal = amphoraApi.amphorae_signals_create_signal(amphora.id, signal)

    print(signal)

except ApiException as e:
    print("Exception when calling API: %s\n" % e)

