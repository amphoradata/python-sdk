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
> file terms_of_use_accept(id, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Accepts a Terms of Use.
    api_response = api_instance.terms_of_use_accept(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsOfUseApi->terms_of_use_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Terms of Use id. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
**200** | 200 if accepted.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_of_use_create**
> TermsOfUse terms_of_use_create(create_terms_of_use, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Creates a Terms of Use object.
    api_response = api_instance.terms_of_use_create(create_terms_of_use, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsOfUseApi->terms_of_use_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_terms_of_use** | [**CreateTermsOfUse**](CreateTermsOfUse.md)| The terms of use to create. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_of_use_delete**
> file terms_of_use_delete(id, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Deletes a Terms of Use object.
    api_response = api_instance.terms_of_use_delete(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsOfUseApi->terms_of_use_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The terms of use id to delete. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
**200** | 200 if successful.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_of_use_list**
> list[TermsOfUse] terms_of_use_list(x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Returns all Terms of Use.
    api_response = api_instance.terms_of_use_list(x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsOfUseApi->terms_of_use_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_of_use_read**
> TermsOfUse terms_of_use_read(id, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Returns all Terms of Use.
    api_response = api_instance.terms_of_use_read(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsOfUseApi->terms_of_use_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

