# amphora_client.TimeSeriesApi

All URIs are relative to *https://beta.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**time_series_query_time_series**](TimeSeriesApi.md#time_series_query_time_series) | **POST** /api/timeseries/query | Updates the details of an Amphora by Id.


# **time_series_query_time_series**
> QueryResultPage time_series_query_time_series(query_request, x_amphoradata_version=x_amphoradata_version)

Updates the details of an Amphora by Id.

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

# Defining host is optional and default to https://beta.amphoradata.com
configuration.host = "https://beta.amphoradata.com"
# Create an instance of the API class
api_instance = amphora_client.TimeSeriesApi(amphora_client.ApiClient(configuration))
query_request = amphora_client.QueryRequest() # QueryRequest | Time Series query. See https://github.com/microsoft/tsiclient/blob/master/docs/Server.md#functions .
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Updates the details of an Amphora by Id.
    api_response = api_instance.time_series_query_time_series(query_request, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->time_series_query_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**QueryRequest**](QueryRequest.md)| Time Series query. See https://github.com/microsoft/tsiclient/blob/master/docs/Server.md#functions . | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**QueryResultPage**](QueryResultPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Query Result. |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

