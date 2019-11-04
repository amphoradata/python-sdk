# amphora_client.OrganisationsApi

All URIs are relative to *https://beta.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisations_create_organisation**](OrganisationsApi.md#organisations_create_organisation) | **POST** /api/organisations | Creates a new Organisation. This will assign the logged in user to the organisation.
[**organisations_delete_organisation**](OrganisationsApi.md#organisations_delete_organisation) | **DELETE** /api/organisations/{id} | Deletes an organisation.
[**organisations_get_organisation**](OrganisationsApi.md#organisations_get_organisation) | **GET** /api/organisations/{id} | Gets an organisation&#39;s details.
[**organisations_update_organisation**](OrganisationsApi.md#organisations_update_organisation) | **PUT** /api/organisations/{id} | Updates an organisation.


# **organisations_create_organisation**
> OrganisationDto organisations_create_organisation(organisation_dto)

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

# Defining host is optional and default to https://beta.amphoradata.com
configuration.host = "https://beta.amphoradata.com"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
organisation_dto = amphora_client.OrganisationDto() # OrganisationDto | Information of the new Organisation

try:
    # Creates a new Organisation. This will assign the logged in user to the organisation.
    api_response = api_instance.organisations_create_organisation(organisation_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_create_organisation: %s\n" % e)
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

# **organisations_delete_organisation**
> OrganisationDto organisations_delete_organisation(id)

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

# Defining host is optional and default to https://beta.amphoradata.com
configuration.host = "https://beta.amphoradata.com"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id

try:
    # Deletes an organisation.
    api_response = api_instance.organisations_delete_organisation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_delete_organisation: %s\n" % e)
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

# **organisations_get_organisation**
> OrganisationDto organisations_get_organisation(id)

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

# Defining host is optional and default to https://beta.amphoradata.com
configuration.host = "https://beta.amphoradata.com"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id

try:
    # Gets an organisation's details.
    api_response = api_instance.organisations_get_organisation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_get_organisation: %s\n" % e)
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

# **organisations_update_organisation**
> file organisations_update_organisation(id, organisation_dto)

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

# Defining host is optional and default to https://beta.amphoradata.com
configuration.host = "https://beta.amphoradata.com"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id
organisation_dto = amphora_client.OrganisationDto() # OrganisationDto | Organisation Information. All fields are updated.

try:
    # Updates an organisation.
    api_response = api_instance.organisations_update_organisation(id, organisation_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_update_organisation: %s\n" % e)
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

