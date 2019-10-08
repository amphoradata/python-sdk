# openapi_client.ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_organisations_id_profile_jpg_get**](ImagesApi.md#api_organisations_id_profile_jpg_get) | **GET** /api/organisations/{id}/profile.jpg | 


# **api_organisations_id_profile_jpg_get**
> api_organisations_id_profile_jpg_get(id)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.ImagesApi()
id = '' # str |  (default to '')

try:
    api_instance.api_organisations_id_profile_jpg_get(id)
except ApiException as e:
    print("Exception when calling ImagesApi->api_organisations_id_profile_jpg_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [default to &#39;&#39;]

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

