# amphora_client.OrganisationsApi

All URIs are relative to *https://appsvc50a3d34f.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisations_create**](OrganisationsApi.md#organisations_create) | **POST** /api/organisations | Creates a new Organisation. This will assign the logged in user to the organisation.
[**organisations_delete**](OrganisationsApi.md#organisations_delete) | **DELETE** /api/organisations/{id} | Deletes an organisation.
[**organisations_read**](OrganisationsApi.md#organisations_read) | **GET** /api/organisations/{id} | Gets an organisation&#39;s details.
[**organisations_update**](OrganisationsApi.md#organisations_update) | **PUT** /api/organisations/{id} | Updates an organisation.


# **organisations_create**
> OrganisationDto organisations_create(organisation_dto)

Creates a new Organisation. This will assign the logged in user to the organisation.

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

# Defining host is optional and default to https://appsvc50a3d34f.azurewebsites.net
configuration.host = "https://appsvc50a3d34f.azurewebsites.net"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
organisation_dto = amphora_client.OrganisationDto() # OrganisationDto | Information of the new Organisation

try:
    # Creates a new Organisation. This will assign the logged in user to the organisation.
    api_response = api_instance.organisations_create(organisation_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_dto** | [**OrganisationDto**](OrganisationDto.md)| Information of the new Organisation | 

### Return type

[**OrganisationDto**](OrganisationDto.md)

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

# **organisations_delete**
> str organisations_delete(id)

Deletes an organisation.

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

# Defining host is optional and default to https://appsvc50a3d34f.azurewebsites.net
configuration.host = "https://appsvc50a3d34f.azurewebsites.net"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id

try:
    # Deletes an organisation.
    api_response = api_instance.organisations_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id | 

### Return type

**str**

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

# **organisations_read**
> OrganisationDto organisations_read(id)

Gets an organisation's details.

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

# Defining host is optional and default to https://appsvc50a3d34f.azurewebsites.net
configuration.host = "https://appsvc50a3d34f.azurewebsites.net"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id

try:
    # Gets an organisation's details.
    api_response = api_instance.organisations_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id | 

### Return type

[**OrganisationDto**](OrganisationDto.md)

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

# **organisations_update**
> file organisations_update(id, organisation_dto)

Updates an organisation.

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

# Defining host is optional and default to https://appsvc50a3d34f.azurewebsites.net
configuration.host = "https://appsvc50a3d34f.azurewebsites.net"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id
organisation_dto = amphora_client.OrganisationDto() # OrganisationDto | Organisation Information. All fields are updated.

try:
    # Updates an organisation.
    api_response = api_instance.organisations_update(id, organisation_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id | 
 **organisation_dto** | [**OrganisationDto**](OrganisationDto.md)| Organisation Information. All fields are updated. | 

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

