# amphora_client.AmphoraeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_amphorae_id_delete**](AmphoraeApi.md#api_amphorae_id_delete) | **DELETE** /api/amphorae/{id} | Deletes an Amphora
[**api_amphorae_id_files_file_get**](AmphoraeApi.md#api_amphorae_id_files_file_get) | **GET** /api/amphorae/{id}/files/{file} | Get&#39;s the contents of a file. Returns application/octet-stream
[**api_amphorae_id_files_file_put**](AmphoraeApi.md#api_amphorae_id_files_file_put) | **PUT** /api/amphorae/{id}/files/{file} | Set&#39;s the contents of a file. The request body becomes the content.
[**api_amphorae_id_files_get**](AmphoraeApi.md#api_amphorae_id_files_get) | **GET** /api/amphorae/{id}/files | Get&#39;s a list of an Amphora&#39;s files
[**api_amphorae_id_get**](AmphoraeApi.md#api_amphorae_id_get) | **GET** /api/amphorae/{id} | Get&#39;s details of an Amphora by Id
[**api_amphorae_id_put**](AmphoraeApi.md#api_amphorae_id_put) | **PUT** /api/amphorae/{id} | Updates the details of an Amphora by Id
[**api_amphorae_id_signals_get**](AmphoraeApi.md#api_amphorae_id_signals_get) | **GET** /api/amphorae/{id}/signals | Get&#39;s the signals associated with an Amphora.
[**api_amphorae_id_signals_post**](AmphoraeApi.md#api_amphorae_id_signals_post) | **POST** /api/amphorae/{id}/signals | Associates a signal with an Amphora. Signal is created if not existing.
[**api_amphorae_id_signals_values_post**](AmphoraeApi.md#api_amphorae_id_signals_values_post) | **POST** /api/amphorae/{id}/signals/values | Get&#39;s the signals associated with an Amphora.
[**api_amphorae_post**](AmphoraeApi.md#api_amphorae_post) | **POST** /api/amphorae | Creates a new empty Amphora in the user&#39;s organisation


# **api_amphorae_id_delete**
> api_amphorae_id_delete(id)

Deletes an Amphora

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.AmphoraeApi()
id = '' # str | Amphora Id (default to '')

try:
    # Deletes an Amphora
    api_instance.api_amphorae_id_delete(id)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_delete: %s\n" % e)
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

# **api_amphorae_id_files_file_get**
> api_amphorae_id_files_file_get(id, file)

Get's the contents of a file. Returns application/octet-stream

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.AmphoraeApi()
id = '' # str | Amphora Id (default to '')
file = '' # str | The name of the file (default to '')

try:
    # Get's the contents of a file. Returns application/octet-stream
    api_instance.api_amphorae_id_files_file_get(id, file)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_files_file_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | [default to &#39;&#39;]
 **file** | **str**| The name of the file | [default to &#39;&#39;]

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

Set's the contents of a file. The request body becomes the content.

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.AmphoraeApi()
id = '' # str | Amphora Id (default to '')
file = '' # str | The name of the file (default to '')

try:
    # Set's the contents of a file. The request body becomes the content.
    api_instance.api_amphorae_id_files_file_put(id, file)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_files_file_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | [default to &#39;&#39;]
 **file** | **str**| The name of the file | [default to &#39;&#39;]

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
> list[str] api_amphorae_id_files_get(id)

Get's a list of an Amphora's files

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.AmphoraeApi()
id = '' # str | Amphora Id (default to '')

try:
    # Get's a list of an Amphora's files
    api_response = api_instance.api_amphorae_id_files_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_files_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | [default to &#39;&#39;]

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_amphorae_id_get**
> AmphoraExtendedDto api_amphorae_id_get(id)

Get's details of an Amphora by Id

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.AmphoraeApi()
id = '' # str | Amphora Id (default to '')

try:
    # Get's details of an Amphora by Id
    api_response = api_instance.api_amphorae_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | [default to &#39;&#39;]

### Return type

[**AmphoraExtendedDto**](AmphoraExtendedDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_amphorae_id_put**
> AmphoraExtendedDto api_amphorae_id_put(id, amphora_extended_dto=amphora_extended_dto)

Updates the details of an Amphora by Id

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.AmphoraeApi()
id = '' # str | Amphora Id (default to '')
amphora_extended_dto = amphora_client.AmphoraExtendedDto() # AmphoraExtendedDto |  (optional)

try:
    # Updates the details of an Amphora by Id
    api_response = api_instance.api_amphorae_id_put(id, amphora_extended_dto=amphora_extended_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | [default to &#39;&#39;]
 **amphora_extended_dto** | [**AmphoraExtendedDto**](AmphoraExtendedDto.md)|  | [optional] 

### Return type

[**AmphoraExtendedDto**](AmphoraExtendedDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_amphorae_id_signals_get**
> list[SignalDto] api_amphorae_id_signals_get(id)

Get's the signals associated with an Amphora.

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.AmphoraeApi()
id = '' # str | Amphora Id (default to '')

try:
    # Get's the signals associated with an Amphora.
    api_response = api_instance.api_amphorae_id_signals_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_signals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | [default to &#39;&#39;]

### Return type

[**list[SignalDto]**](SignalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_amphorae_id_signals_post**
> SignalDto api_amphorae_id_signals_post(id, signal_dto=signal_dto)

Associates a signal with an Amphora. Signal is created if not existing.

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.AmphoraeApi()
id = '' # str | Amphora Id (default to '')
signal_dto = amphora_client.SignalDto() # SignalDto |  (optional)

try:
    # Associates a signal with an Amphora. Signal is created if not existing.
    api_response = api_instance.api_amphorae_id_signals_post(id, signal_dto=signal_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_signals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | [default to &#39;&#39;]
 **signal_dto** | [**SignalDto**](SignalDto.md)|  | [optional] 

### Return type

[**SignalDto**](SignalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_amphorae_id_signals_values_post**
> api_amphorae_id_signals_values_post(id, request_body=request_body)

Get's the signals associated with an Amphora.

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.AmphoraeApi()
id = '' # str | Amphora Id (default to '')
request_body = None # dict(str, object) |  (optional)

try:
    # Get's the signals associated with an Amphora.
    api_instance.api_amphorae_id_signals_values_post(id, request_body=request_body)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_id_signals_values_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | [default to &#39;&#39;]
 **request_body** | [**dict(str, object)**](object.md)|  | [optional] 

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
> AmphoraExtendedDto api_amphorae_post(create_amphora_dto=create_amphora_dto)

Creates a new empty Amphora in the user's organisation

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.AmphoraeApi()
create_amphora_dto = amphora_client.CreateAmphoraDto() # CreateAmphoraDto |  (optional)

try:
    # Creates a new empty Amphora in the user's organisation
    api_response = api_instance.api_amphorae_post(create_amphora_dto=create_amphora_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->api_amphorae_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_amphora_dto** | [**CreateAmphoraDto**](CreateAmphoraDto.md)|  | [optional] 

### Return type

[**AmphoraExtendedDto**](AmphoraExtendedDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

