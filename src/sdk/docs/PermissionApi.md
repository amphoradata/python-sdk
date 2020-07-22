# amphora_api_client.PermissionApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permission_get_permissions**](PermissionApi.md#permission_get_permissions) | **POST** /api/permissions | The permission level for each object id in the request.


# **permission_get_permissions**
> PermissionsResponse permission_get_permissions(permissions_request)

The permission level for each object id in the request.

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
api_instance = amphora_api_client.PermissionApi(amphora_api_client.ApiClient(configuration))
permissions_request = amphora_api_client.PermissionsRequest() # PermissionsRequest | A request object containing the list of ids to check.

try:
    # The permission level for each object id in the request.
    api_response = api_instance.permission_get_permissions(permissions_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionApi->permission_get_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissions_request** | [**PermissionsRequest**](PermissionsRequest.md)| A request object containing the list of ids to check. | 

### Return type

[**PermissionsResponse**](PermissionsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A dictionary with permission levels associated to the ids. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

