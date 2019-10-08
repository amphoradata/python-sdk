# openapi_client.SignalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_amphorae_id_signals_post**](SignalApi.md#api_amphorae_id_signals_post) | **POST** /api/amphorae/{id}/signals | 


# **api_amphorae_id_signals_post**
> api_amphorae_id_signals_post(id, body=body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.SignalApi()
id = '' # str |  (default to '')
body = None # object |  (optional)

try:
    api_instance.api_amphorae_id_signals_post(id, body=body)
except ApiException as e:
    print("Exception when calling SignalApi->api_amphorae_id_signals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [default to &#39;&#39;]
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

