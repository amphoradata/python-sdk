# amphora_client.AmphoraeApi

All URIs are relative to *https://beta.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amphorae_create**](AmphoraeApi.md#amphorae_create) | **POST** /api/amphorae | Creates a new empty Amphora in the user&#39;s organisation
[**amphorae_create_signal**](AmphoraeApi.md#amphorae_create_signal) | **POST** /api/amphorae/{id}/signals | Associates a signal with an Amphora. Signal is created if not existing.
[**amphorae_delete_api**](AmphoraeApi.md#amphorae_delete_api) | **DELETE** /api/amphorae/{id} | Deletes an Amphora
[**amphorae_download_file**](AmphoraeApi.md#amphorae_download_file) | **GET** /api/amphorae/{id}/files/{file} | Get&#39;s the contents of a file. Returns application/octet-stream
[**amphorae_get_signals**](AmphoraeApi.md#amphorae_get_signals) | **GET** /api/amphorae/{id}/signals | Get&#39;s the signals associated with an Amphora.
[**amphorae_list_files**](AmphoraeApi.md#amphorae_list_files) | **GET** /api/amphorae/{id}/files | Get&#39;s a list of an Amphora&#39;s files
[**amphorae_read**](AmphoraeApi.md#amphorae_read) | **GET** /api/amphorae/{id} | Get&#39;s details of an Amphora by Id
[**amphorae_update**](AmphoraeApi.md#amphorae_update) | **PUT** /api/amphorae/{id} | Updates the details of an Amphora by Id
[**amphorae_upload_signal_value**](AmphoraeApi.md#amphorae_upload_signal_value) | **POST** /api/amphorae/{id}/signals/values | 
[**amphorae_upload_to_amphora**](AmphoraeApi.md#amphorae_upload_to_amphora) | **PUT** /api/amphorae/{id}/files/{file} | Set&#39;s the contents of a file. The request body becomes the content.


# **amphorae_create**
> AmphoraExtendedDto amphorae_create(create_amphora_dto)

Creates a new empty Amphora in the user's organisation

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
api_instance = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))
create_amphora_dto = amphora_client.CreateAmphoraDto() # CreateAmphoraDto | Information for the new Amphora

try:
    # Creates a new empty Amphora in the user's organisation
    api_response = api_instance.amphorae_create(create_amphora_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_amphora_dto** | [**CreateAmphoraDto**](CreateAmphoraDto.md)| Information for the new Amphora | 

### Return type

[**AmphoraExtendedDto**](AmphoraExtendedDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_create_signal**
> SignalDto amphorae_create_signal(id, signal_dto)

Associates a signal with an Amphora. Signal is created if not existing.

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
api_instance = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id
signal_dto = amphora_client.SignalDto() # SignalDto | Signal Details

try:
    # Associates a signal with an Amphora. Signal is created if not existing.
    api_response = api_instance.amphorae_create_signal(id, signal_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_create_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | 
 **signal_dto** | [**SignalDto**](SignalDto.md)| Signal Details | 

### Return type

[**SignalDto**](SignalDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_delete_api**
> file amphorae_delete_api(id)

Deletes an Amphora

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
api_instance = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id

try:
    # Deletes an Amphora
    api_response = api_instance.amphorae_delete_api(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_delete_api: %s\n" % e)
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

# **amphorae_download_file**
> file amphorae_download_file(id, file)

Get's the contents of a file. Returns application/octet-stream

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
api_instance = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id
file = 'file_example' # str | The name of the file

try:
    # Get's the contents of a file. Returns application/octet-stream
    api_response = api_instance.amphorae_download_file(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | 
 **file** | **str**| The name of the file | 

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

# **amphorae_get_signals**
> list[SignalDto] amphorae_get_signals(id)

Get's the signals associated with an Amphora.

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
api_instance = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id

try:
    # Get's the signals associated with an Amphora.
    api_response = api_instance.amphorae_get_signals(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_get_signals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | 

### Return type

[**list[SignalDto]**](SignalDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_list_files**
> list[str] amphorae_list_files(id)

Get's a list of an Amphora's files

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
api_instance = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id

try:
    # Get's a list of an Amphora's files
    api_response = api_instance.amphorae_list_files(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_read**
> AmphoraExtendedDto amphorae_read(id)

Get's details of an Amphora by Id

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
api_instance = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id

try:
    # Get's details of an Amphora by Id
    api_response = api_instance.amphorae_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | 

### Return type

[**AmphoraExtendedDto**](AmphoraExtendedDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_update**
> AmphoraExtendedDto amphorae_update(id, amphora_extended_dto)

Updates the details of an Amphora by Id

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
api_instance = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id
amphora_extended_dto = amphora_client.AmphoraExtendedDto() # AmphoraExtendedDto | Information to update

try:
    # Updates the details of an Amphora by Id
    api_response = api_instance.amphorae_update(id, amphora_extended_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | 
 **amphora_extended_dto** | [**AmphoraExtendedDto**](AmphoraExtendedDto.md)| Information to update | 

### Return type

[**AmphoraExtendedDto**](AmphoraExtendedDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_upload_signal_value**
> file amphorae_upload_signal_value(id, request_body)



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
api_instance = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | 
request_body = None # dict(str, object) | 

try:
    api_response = api_instance.amphorae_upload_signal_value(id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_upload_signal_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**dict(str, object)**](object.md)|  | 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_upload_to_amphora**
> file amphorae_upload_to_amphora(id, file)

Set's the contents of a file. The request body becomes the content.

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
api_instance = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id
file = 'file_example' # str | The name of the file

try:
    # Set's the contents of a file. The request body becomes the content.
    api_response = api_instance.amphorae_upload_to_amphora(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_upload_to_amphora: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | 
 **file** | **str**| The name of the file | 

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

