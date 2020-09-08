# amphora_api_client.TermsOfUseApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terms_of_use_accept**](TermsOfUseApi.md#terms_of_use_accept) | **POST** /api/TermsOfUse/{id}/Accepts | Accepts a Terms of Use.
[**terms_of_use_create**](TermsOfUseApi.md#terms_of_use_create) | **POST** /api/TermsOfUse | Creates a Terms of Use object.
[**terms_of_use_delete**](TermsOfUseApi.md#terms_of_use_delete) | **DELETE** /api/TermsOfUse/{id} | Deletes a Terms of Use object.
[**terms_of_use_list**](TermsOfUseApi.md#terms_of_use_list) | **GET** /api/TermsOfUse | Returns all Terms of Use.
[**terms_of_use_read**](TermsOfUseApi.md#terms_of_use_read) | **GET** /api/TermsOfUse/{id} | Returns all Terms of Use.


# **terms_of_use_accept**
> terms_of_use_accept(id)

Accepts a Terms of Use.

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
api_instance = amphora_api_client.TermsOfUseApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | The Terms of Use id.

try:
    # Accepts a Terms of Use.
    api_instance.terms_of_use_accept(id)
except ApiException as e:
    print("Exception when calling TermsOfUseApi->terms_of_use_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Terms of Use id. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_of_use_create**
> TermsOfUse terms_of_use_create(create_terms_of_use)

Creates a Terms of Use object.

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
api_instance = amphora_api_client.TermsOfUseApi(amphora_api_client.ApiClient(configuration))
create_terms_of_use = amphora_api_client.CreateTermsOfUse() # CreateTermsOfUse | The terms of use to create.

try:
    # Creates a Terms of Use object.
    api_response = api_instance.terms_of_use_create(create_terms_of_use)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsOfUseApi->terms_of_use_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_terms_of_use** | [**CreateTermsOfUse**](CreateTermsOfUse.md)| The terms of use to create. | 

### Return type

[**TermsOfUse**](TermsOfUse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The terms of use object.  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_of_use_delete**
> terms_of_use_delete(id)

Deletes a Terms of Use object.

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
api_instance = amphora_api_client.TermsOfUseApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | The terms of use id to delete.

try:
    # Deletes a Terms of Use object.
    api_instance.terms_of_use_delete(id)
except ApiException as e:
    print("Exception when calling TermsOfUseApi->terms_of_use_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The terms of use id to delete. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_of_use_list**
> list[TermsOfUse] terms_of_use_list(take=take, skip=skip)

Returns all Terms of Use.

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
api_instance = amphora_api_client.TermsOfUseApi(amphora_api_client.ApiClient(configuration))
take = 56 # int | Gets or sets how many items to return. Defaults to 64. (optional)
skip = 56 # int | Gets or sets how many items to skip before returning. Defaults to 0. (optional)

try:
    # Returns all Terms of Use.
    api_response = api_instance.terms_of_use_list(take=take, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsOfUseApi->terms_of_use_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| Gets or sets how many items to return. Defaults to 64. | [optional] 
 **skip** | **int**| Gets or sets how many items to skip before returning. Defaults to 0. | [optional] 

### Return type

[**list[TermsOfUse]**](TermsOfUse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Terms of Use. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_of_use_read**
> TermsOfUse terms_of_use_read(id)

Returns all Terms of Use.

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
api_instance = amphora_api_client.TermsOfUseApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Returns all Terms of Use.
    api_response = api_instance.terms_of_use_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsOfUseApi->terms_of_use_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TermsOfUse**](TermsOfUse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Terms of Use. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

