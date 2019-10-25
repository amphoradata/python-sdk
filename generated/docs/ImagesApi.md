# amphora_client.ImagesApi

All URIs are relative to *https://beta.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images_get_organisation_profile_image**](ImagesApi.md#images_get_organisation_profile_image) | **GET** /api/organisations/{id}/profile.jpg | Gets an organisations profile picture


# **images_get_organisation_profile_image**
> file images_get_organisation_profile_image(id)

Gets an organisations profile picture

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
api_instance = amphora_client.ImagesApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id

try:
    # Gets an organisations profile picture
    api_response = api_instance.images_get_organisation_profile_image(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->images_get_organisation_profile_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

