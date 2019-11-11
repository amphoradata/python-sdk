# amphora_client.AmphoraeStatisticsApi

All URIs are relative to *https://appsvc19cba94a.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amphorae_statistics_count**](AmphoraeStatisticsApi.md#amphorae_statistics_count) | **GET** /api/amphoraeStats/count | Gets ta count of all the Amphora


# **amphorae_statistics_count**
> int amphorae_statistics_count(i_frame=i_frame)

Gets ta count of all the Amphora

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

# Defining host is optional and default to https://appsvc19cba94a.azurewebsites.net
configuration.host = "https://appsvc19cba94a.azurewebsites.net"
# Create an instance of the API class
api_instance = amphora_client.AmphoraeStatisticsApi(amphora_client.ApiClient(configuration))
i_frame = True # bool |  (optional)

try:
    # Gets ta count of all the Amphora
    api_response = api_instance.amphorae_statistics_count(i_frame=i_frame)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeStatisticsApi->amphorae_statistics_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **i_frame** | **bool**|  | [optional] 

### Return type

**int**

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

