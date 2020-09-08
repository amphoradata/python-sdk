# amphora_api_client.FeedsApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feed_get_feed**](FeedsApi.md#feed_get_feed) | **GET** /api/feeds/v1 | Gets the feed for the logged in user.


# **feed_get_feed**
> CollectionResponseOfFeedItem feed_get_feed()

Gets the feed for the logged in user.

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
api_instance = amphora_api_client.FeedsApi(amphora_api_client.ApiClient(configuration))

try:
    # Gets the feed for the logged in user.
    api_response = api_instance.feed_get_feed()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedsApi->feed_get_feed: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollectionResponseOfFeedItem**](CollectionResponseOfFeedItem.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Feed object. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

