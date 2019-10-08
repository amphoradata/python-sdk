# openapi_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_users_post**](UsersApi.md#api_users_post) | **POST** /api/users | 
[**api_users_self_get**](UsersApi.md#api_users_self_get) | **GET** /api/users/self | 
[**api_users_username_delete**](UsersApi.md#api_users_username_delete) | **DELETE** /api/users/{username} | 


# **api_users_post**
> api_users_post(onboarding_id=onboarding_id, user_dto=user_dto)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.UsersApi()
onboarding_id = '' # str |  (optional) (default to '')
user_dto = openapi_client.UserDto() # UserDto |  (optional)

try:
    api_instance.api_users_post(onboarding_id=onboarding_id, user_dto=user_dto)
except ApiException as e:
    print("Exception when calling UsersApi->api_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **onboarding_id** | **str**|  | [optional] [default to &#39;&#39;]
 **user_dto** | [**UserDto**](UserDto.md)|  | [optional] 

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

# **api_users_self_get**
> api_users_self_get()



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.UsersApi()

try:
    api_instance.api_users_self_get()
except ApiException as e:
    print("Exception when calling UsersApi->api_users_self_get: %s\n" % e)
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

# **api_users_username_delete**
> api_users_username_delete(username)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.UsersApi()
username = '' # str |  (default to '')

try:
    api_instance.api_users_username_delete(username)
except ApiException as e:
    print("Exception when calling UsersApi->api_users_username_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [default to &#39;&#39;]

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

