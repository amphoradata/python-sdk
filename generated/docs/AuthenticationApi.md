# amphora_client.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_authentication_request_post**](AuthenticationApi.md#api_authentication_request_post) | **POST** /api/authentication/request | Returns a JWT (JSON Web Token).


# **api_authentication_request_post**
> str api_authentication_request_post(token_request=token_request)

Returns a JWT (JSON Web Token).

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.AuthenticationApi()
token_request = amphora_client.TokenRequest() # TokenRequest |  (optional)

try:
    # Returns a JWT (JSON Web Token).
    api_response = api_instance.api_authentication_request_post(token_request=token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->api_authentication_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**TokenRequest**](TokenRequest.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

