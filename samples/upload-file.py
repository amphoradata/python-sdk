from __future__ import print_function
import time
import os
import amphora_client
from amphora_client.rest import ApiException
from amphora_extensions.file_uploader import FileUploader
from pprint import pprint
from amphora_client.configuration import Configuration

# Defining host is optional and default to http://localhost
configuration = Configuration()
configuration.host = "https://beta.amphoradata.com"
# Create an instance of the API class
auth_api = amphora_client.AuthenticationApi(amphora_client.ApiClient(configuration))

token_request = amphora_client.TokenRequest(username=os.environ['username'], password=os.environ['password'] ) 


try:
    res = auth_api.authentication_request_token(token_request = token_request)
    print('got a token')
    configuration.api_key["Authorization"] = "Bearer " + res
    client = amphora_client.ApiClient(configuration)

    amphoraApi = amphora_client.AmphoraeApi(client)

    dto = amphora_client.CreateAmphoraDto(name = "Create File Example", price = 0, 
        description="This is an Amphora created to show how to upload a file via the Python SDK")

    a = amphoraApi.amphorae_create(dto)
    print('created amphora')

    uploader = FileUploader(amphoraApi)
    uploader.create_and_upload_file(a.id, "./dog.jpg")

except ApiException as e:
    print("Exception when calling API: %s\n" % e)

