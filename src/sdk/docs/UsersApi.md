# amphora_api_client.UsersApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_create**](UsersApi.md#users_create) | **POST** /api/users | Creates a new User. Returns the password.
[**users_read_self**](UsersApi.md#users_read_self) | **GET** /api/users/self | Gets logged in users information.


# **users_create**
> AmphoraUser users_create(create_amphora_user)

Creates a new User. Returns the password.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import amphora_api_client
from amphora_api_client.rest import ApiException
from pprint import pprint
configuration = amphora_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://app.amphoradata.com
configuration.host = "https://app.amphoradata.com"
# Create an instance of the API class
api_instance = amphora_api_client.UsersApi(amphora_api_client.ApiClient(configuration))
create_amphora_user = amphora_api_client.CreateAmphoraUser() # CreateAmphoraUser | User parameters.

try:
    # Creates a new User. Returns the password.
    api_response = api_instance.users_create(create_amphora_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_amphora_user** | [**CreateAmphoraUser**](CreateAmphoraUser.md)| User parameters. | 

### Return type

[**AmphoraUser**](AmphoraUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The info for the created user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_read_self**
> AmphoraUser users_read_self()

Gets logged in users information.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import amphora_api_client
from amphora_api_client.rest import ApiException
from pprint import pprint
configuration = amphora_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://app.amphoradata.com
configuration.host = "https://app.amphoradata.com"
# Create an instance of the API class
api_instance = amphora_api_client.UsersApi(amphora_api_client.ApiClient(configuration))

try:
    # Gets logged in users information.
    api_response = api_instance.users_read_self()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_read_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AmphoraUser**](AmphoraUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Your own details.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

