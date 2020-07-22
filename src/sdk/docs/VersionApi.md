# amphora_api_client.VersionApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_get_current_version**](VersionApi.md#version_get_current_version) | **GET** /api/version | Get&#39;s the current server version.


# **version_get_current_version**
> str version_get_current_version()

Get's the current server version.

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
api_instance = amphora_api_client.VersionApi(amphora_api_client.ApiClient(configuration))

try:
    # Get's the current server version.
    api_response = api_instance.version_get_current_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->version_get_current_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | The current version string. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

