# amphora_client.VersionApi

All URIs are relative to *https://appsvc62a56562.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_get_current_version**](VersionApi.md#version_get_current_version) | **GET** /api/version | Get&#39;s the current server version


# **version_get_current_version**
> str version_get_current_version(x_amphoradata_version=x_amphoradata_version)

Get's the current server version

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint
configuration = amphora_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://appsvc62a56562.azurewebsites.net
configuration.host = "https://appsvc62a56562.azurewebsites.net"
# Create an instance of the API class
api_instance = amphora_client.VersionApi(amphora_client.ApiClient(configuration))
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Get's the current server version
    api_response = api_instance.version_get_current_version(x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->version_get_current_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

