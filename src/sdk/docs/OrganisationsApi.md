# amphora_api_client.OrganisationsApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_get_plan**](OrganisationsApi.md#account_get_plan) | **GET** /api/Organisations/{id}/Account/Plan | Get&#39;s an Organisation&#39;s plan information.
[**account_read**](OrganisationsApi.md#account_read) | **GET** /api/Organisations/{id}/Account | Get&#39;s an Organisation&#39;s account information.
[**organisations_create**](OrganisationsApi.md#organisations_create) | **POST** /api/Organisations | Creates a new Organisation. This will assign the logged in user to the organisation.
[**organisations_delete**](OrganisationsApi.md#organisations_delete) | **DELETE** /api/Organisations/{id} | Deletes an organisation.
[**organisations_read**](OrganisationsApi.md#organisations_read) | **GET** /api/Organisations/{id} | Gets an organisation&#39;s details.
[**organisations_read_invitations**](OrganisationsApi.md#organisations_read_invitations) | **GET** /api/Organisations/{id}/Invitations | Gets an organisation&#39;s invitations.
[**organisations_terms_of_use_read**](OrganisationsApi.md#organisations_terms_of_use_read) | **GET** /api/Organisations/{id}/TermsOfUse | Get&#39;s a list of an Organisation&#39;s Terms of Use.
[**organisations_update**](OrganisationsApi.md#organisations_update) | **PUT** /api/Organisations/{id} | Updates an organisation.


# **account_get_plan**
> PlanInformation account_get_plan(id)

Get's an Organisation's plan information.

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
api_instance = amphora_api_client.OrganisationsApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id.

try:
    # Get's an Organisation's plan information.
    api_response = api_instance.account_get_plan(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->account_get_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | 

### Return type

[**PlanInformation**](PlanInformation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Organisation&#39;s plan.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_read**
> Account account_read(id)

Get's an Organisation's account information.

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
api_instance = amphora_api_client.OrganisationsApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id.

try:
    # Get's an Organisation's account information.
    api_response = api_instance.account_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->account_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | 

### Return type

[**Account**](Account.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Organisation&#39;s account metadata.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisations_create**
> Organisation organisations_create(organisation)

Creates a new Organisation. This will assign the logged in user to the organisation.

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
api_instance = amphora_api_client.OrganisationsApi(amphora_api_client.ApiClient(configuration))
organisation = amphora_api_client.Organisation() # Organisation | Information of the new Organisation.

try:
    # Creates a new Organisation. This will assign the logged in user to the organisation.
    api_response = api_instance.organisations_create(organisation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation** | [**Organisation**](Organisation.md)| Information of the new Organisation. | 

### Return type

[**Organisation**](Organisation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Organisation metadata.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisations_delete**
> str organisations_delete(id)

Deletes an organisation.

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
api_instance = amphora_api_client.OrganisationsApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id.

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
 **id** | **str**| Organisation Id. | 

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
**200** | A Message.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisations_read**
> Organisation organisations_read(id)

Gets an organisation's details.

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
api_instance = amphora_api_client.OrganisationsApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id.

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
 **id** | **str**| Organisation Id. | 

### Return type

[**Organisation**](Organisation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organisation metadata.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisations_read_invitations**
> list[Invitation] organisations_read_invitations(id)

Gets an organisation's invitations.

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
api_instance = amphora_api_client.OrganisationsApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id.

try:
    # Gets an organisation's invitations.
    api_response = api_instance.organisations_read_invitations(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_read_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | 

### Return type

[**list[Invitation]**](Invitation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of invitations.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisations_terms_of_use_read**
> list[TermsOfUse] organisations_terms_of_use_read(id)

Get's a list of an Organisation's Terms of Use.

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
api_instance = amphora_api_client.OrganisationsApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | The Id of the Organisation.

try:
    # Get's a list of an Organisation's Terms of Use.
    api_response = api_instance.organisations_terms_of_use_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_terms_of_use_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the Organisation. | 

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
**200** | The Terms.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisations_update**
> file organisations_update(id, organisation)

Updates an organisation.

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
api_instance = amphora_api_client.OrganisationsApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id.
organisation = amphora_api_client.Organisation() # Organisation | Organisation Information. All fields are updated.

try:
    # Updates an organisation.
    api_response = api_instance.organisations_update(id, organisation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | 
 **organisation** | [**Organisation**](Organisation.md)| Organisation Information. All fields are updated. | 

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
**200** | The organisation metadaa.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

