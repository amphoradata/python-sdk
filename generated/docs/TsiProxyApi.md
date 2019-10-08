# openapi_client.TsiProxyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tsi_timeseries_query_post**](TsiProxyApi.md#tsi_timeseries_query_post) | **POST** /tsi/timeseries/query | 


# **tsi_timeseries_query_post**
> tsi_timeseries_query_post()



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.TsiProxyApi()

try:
    api_instance.tsi_timeseries_query_post()
except ApiException as e:
    print("Exception when calling TsiProxyApi->tsi_timeseries_query_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

