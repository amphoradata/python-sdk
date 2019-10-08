# openapi_client.AmphoraeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_amphorae_id_delete**](AmphoraeApi.md#api_amphorae_id_delete) | **DELETE** /api/amphorae/{id} | 
[**api_amphorae_id_files_file_get**](AmphoraeApi.md#api_amphorae_id_files_file_get) | **GET** /api/amphorae/{id}/files/{file} | 
[**api_amphorae_id_files_file_put**](AmphoraeApi.md#api_amphorae_id_files_file_put) | **PUT** /api/amphorae/{id}/files/{file} | 
[**api_amphorae_id_files_get**](AmphoraeApi.md#api_amphorae_id_files_get) | **GET** /api/amphorae/{id}/files | 
[**api_amphorae_id_get**](AmphoraeApi.md#api_amphorae_id_get) | **GET** /api/amphorae/{id} | 
[**api_amphorae_id_put**](AmphoraeApi.md#api_amphorae_id_put) | **PUT** /api/amphorae/{id} | 
[**api_amphorae_post**](AmphoraeApi.md#api_amphorae_post) | **POST** /api/amphorae | 


# **api_amphorae_id_delete**
> api_amphorae_id_delete(id)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AmphoraeApi()
id = '' # str |  (default to '')

try:
    api_instance.api_amphorae_id_delete(id)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_delete: %s\n" % e)
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

# **api_amphorae_id_files_file_get**
> api_amphorae_id_files_file_get(id, file)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AmphoraeApi()
id = '' # str |  (default to '')
file = '' # str |  (default to '')

try:
    api_instance.api_amphorae_id_files_file_get(id, file)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_files_file_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [default to &#39;&#39;]
 **file** | **str**|  | [default to &#39;&#39;]

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

# **api_amphorae_id_files_file_put**
> api_amphorae_id_files_file_put(id, file)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AmphoraeApi()
id = '' # str |  (default to '')
file = '' # str |  (default to '')

try:
    api_instance.api_amphorae_id_files_file_put(id, file)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_files_file_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [default to &#39;&#39;]
 **file** | **str**|  | [default to &#39;&#39;]

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

# **api_amphorae_id_files_get**
> api_amphorae_id_files_get(id)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AmphoraeApi()
id = '' # str |  (default to '')

try:
    api_instance.api_amphorae_id_files_get(id)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_files_get: %s\n" % e)
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

# **api_amphorae_id_get**
> api_amphorae_id_get(id)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AmphoraeApi()
id = '' # str |  (default to '')

try:
    api_instance.api_amphorae_id_get(id)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_get: %s\n" % e)
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

# **api_amphorae_id_put**
> api_amphorae_id_put(id, amphora_extended_dto=amphora_extended_dto)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AmphoraeApi()
id = '' # str |  (default to '')
amphora_extended_dto = openapi_client.AmphoraExtendedDto() # AmphoraExtendedDto |  (optional)

try:
    api_instance.api_amphorae_id_put(id, amphora_extended_dto=amphora_extended_dto)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [default to &#39;&#39;]
 **amphora_extended_dto** | [**AmphoraExtendedDto**](AmphoraExtendedDto.md)|  | [optional] 

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

# **api_amphorae_post**
> api_amphorae_post(amphora_extended_dto=amphora_extended_dto)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AmphoraeApi()
amphora_extended_dto = openapi_client.AmphoraExtendedDto() # AmphoraExtendedDto |  (optional)

try:
    api_instance.api_amphorae_post(amphora_extended_dto=amphora_extended_dto)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amphora_extended_dto** | [**AmphoraExtendedDto**](AmphoraExtendedDto.md)|  | [optional] 

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

