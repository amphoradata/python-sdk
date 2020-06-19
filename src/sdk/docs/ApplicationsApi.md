# amphora_api_client.ApplicationsApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_create_application**](ApplicationsApi.md#applications_create_application) | **POST** /api/applications | Creates a new application. Applications are external websites that Amphora users can sign in to.
[**applications_create_application2**](ApplicationsApi.md#applications_create_application2) | **GET** /api/applications/{id} | Gets an application by Id, if it exists.
[**applications_delete_application**](ApplicationsApi.md#applications_delete_application) | **DELETE** /api/applications/{id} | Deletes an application. Must be done by an Organisation administrator.


# **applications_create_application**
> Application applications_create_application(create_application, x_amphoradata_version=x_amphoradata_version)

Creates a new application. Applications are external websites that Amphora users can sign in to.

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
api_instance = amphora_api_client.ApplicationsApi(amphora_api_client.ApiClient(configuration))
create_application = amphora_api_client.CreateApplication() # CreateApplication | An application to create.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Creates a new application. Applications are external websites that Amphora users can sign in to.
    api_response = api_instance.applications_create_application(create_application, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_application** | [**CreateApplication**](CreateApplication.md)| An application to create. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Application information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_create_application2**
> Application applications_create_application2(id, x_amphoradata_version=x_amphoradata_version)

Gets an application by Id, if it exists.

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
api_instance = amphora_api_client.ApplicationsApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the application to get.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Gets an application by Id, if it exists.
    api_response = api_instance.applications_create_application2(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_create_application2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the application to get. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Application information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_delete_application**
> Application applications_delete_application(id, x_amphoradata_version=x_amphoradata_version)

Deletes an application. Must be done by an Organisation administrator.

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
api_instance = amphora_api_client.ApplicationsApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | The application id to delete.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Deletes an application. Must be done by an Organisation administrator.
    api_response = api_instance.applications_delete_application(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_delete_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application id to delete. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 if successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

