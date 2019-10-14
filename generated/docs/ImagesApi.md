# amphora_client.ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_organisations_id_profile_jpg_get**](ImagesApi.md#api_organisations_id_profile_jpg_get) | **GET** /api/organisations/{id}/profile.jpg | Gets an organisations profile picture


# **api_organisations_id_profile_jpg_get**
> api_organisations_id_profile_jpg_get(id)

Gets an organisations profile picture

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.ImagesApi()
id = '' # str | Amphora Id (default to '')

try:
    # Gets an organisations profile picture
    api_instance.api_organisations_id_profile_jpg_get(id)
except ApiException as e:
    print("Exception when calling ImagesApi->api_organisations_id_profile_jpg_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | [default to &#39;&#39;]

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

