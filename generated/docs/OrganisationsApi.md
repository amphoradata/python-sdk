# amphora_client.OrganisationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_organisations_id_delete**](OrganisationsApi.md#api_organisations_id_delete) | **DELETE** /api/organisations/{id} | Deletes an organisation.
[**api_organisations_id_get**](OrganisationsApi.md#api_organisations_id_get) | **GET** /api/organisations/{id} | Gets an organisation&#39;s details.
[**api_organisations_id_invitations_get**](OrganisationsApi.md#api_organisations_id_invitations_get) | **GET** /api/organisations/{id}/invitations | Accept an invitation to an organisation.
[**api_organisations_id_invitations_post**](OrganisationsApi.md#api_organisations_id_invitations_post) | **POST** /api/organisations/{id}/invitations | Invite a user/ email address to your organisation.
[**api_organisations_id_put**](OrganisationsApi.md#api_organisations_id_put) | **PUT** /api/organisations/{id} | Updates an organisation.
[**api_organisations_post**](OrganisationsApi.md#api_organisations_post) | **POST** /api/organisations | Creates a new Organisation. This will assign the logged in user to the organisation.


# **api_organisations_id_delete**
> OrganisationDto api_organisations_id_delete(id)

Deletes an organisation.

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint
configuration = amphora_client.Configuration()
# Configure API key authorization: token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
id = '' # str | Organisation Id (default to '')

try:
    # Deletes an organisation.
    api_response = api_instance.api_organisations_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id | [default to &#39;&#39;]

### Return type

[**OrganisationDto**](OrganisationDto.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organisations_id_get**
> OrganisationDto api_organisations_id_get(id)

Gets an organisation's details.

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint
configuration = amphora_client.Configuration()
# Configure API key authorization: token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
id = '' # str | Organisation Id (default to '')

try:
    # Gets an organisation's details.
    api_response = api_instance.api_organisations_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id | [default to &#39;&#39;]

### Return type

[**OrganisationDto**](OrganisationDto.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organisations_id_invitations_get**
> OrganisationDto api_organisations_id_invitations_get(id)

Accept an invitation to an organisation.

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint
configuration = amphora_client.Configuration()
# Configure API key authorization: token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
id = '' # str | Organisation Id (default to '')

try:
    # Accept an invitation to an organisation.
    api_response = api_instance.api_organisations_id_invitations_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_id_invitations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id | [default to &#39;&#39;]

### Return type

[**OrganisationDto**](OrganisationDto.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organisations_id_invitations_post**
> api_organisations_id_invitations_post(id, invitation=invitation)

Invite a user/ email address to your organisation.

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint
configuration = amphora_client.Configuration()
# Configure API key authorization: token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
id = '' # str | Organisation Id (default to '')
invitation = amphora_client.Invitation() # Invitation |  (optional)

try:
    # Invite a user/ email address to your organisation.
    api_instance.api_organisations_id_invitations_post(id, invitation=invitation)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_id_invitations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id | [default to &#39;&#39;]
 **invitation** | [**Invitation**](Invitation.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organisations_id_put**
> api_organisations_id_put(id, organisation_dto=organisation_dto)

Updates an organisation.

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint
configuration = amphora_client.Configuration()
# Configure API key authorization: token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
id = '' # str | Organisation Id (default to '')
organisation_dto = amphora_client.OrganisationDto() # OrganisationDto |  (optional)

try:
    # Updates an organisation.
    api_instance.api_organisations_id_put(id, organisation_dto=organisation_dto)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id | [default to &#39;&#39;]
 **organisation_dto** | [**OrganisationDto**](OrganisationDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_organisations_post**
> OrganisationDto api_organisations_post(organisation_dto=organisation_dto)

Creates a new Organisation. This will assign the logged in user to the organisation.

### Example

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint
configuration = amphora_client.Configuration()
# Configure API key authorization: token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = amphora_client.OrganisationsApi(amphora_client.ApiClient(configuration))
organisation_dto = amphora_client.OrganisationDto() # OrganisationDto |  (optional)

try:
    # Creates a new Organisation. This will assign the logged in user to the organisation.
    api_response = api_instance.api_organisations_post(organisation_dto=organisation_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_dto** | [**OrganisationDto**](OrganisationDto.md)|  | [optional] 

### Return type

[**OrganisationDto**](OrganisationDto.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

