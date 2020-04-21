# amphora_api_client.OrganisationsApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_get_plan**](OrganisationsApi.md#account_get_plan) | **GET** /api/Organisations/{id}/Account/Plan | Get&#39;s an Organisation&#39;s plan information.
[**account_read**](OrganisationsApi.md#account_read) | **GET** /api/Organisations/{id}/Account | Get&#39;s an Organisation&#39;s account information.
[**organisations_create**](OrganisationsApi.md#organisations_create) | **POST** /api/organisations | Creates a new Organisation. This will assign the logged in user to the organisation.
[**organisations_delete**](OrganisationsApi.md#organisations_delete) | **DELETE** /api/organisations/{id} | Deletes an organisation.
[**organisations_read**](OrganisationsApi.md#organisations_read) | **GET** /api/organisations/{id} | Gets an organisation&#39;s details.
[**organisations_update**](OrganisationsApi.md#organisations_update) | **PUT** /api/organisations/{id} | Updates an organisation.
[**terms_and_conditions_create**](OrganisationsApi.md#terms_and_conditions_create) | **POST** /api/Organisations/{id}/TermsAndConditions | Adds new Terms and Conditions to your Organisations T/C Library.
[**terms_and_conditions_read**](OrganisationsApi.md#terms_and_conditions_read) | **GET** /api/Organisations/{id}/TermsAndConditions | Get&#39;s a list of an Organisation&#39;s Terms and Conditions.


# **account_get_plan**
> PlanInformation account_get_plan(id, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Get's an Organisation's plan information.
    api_response = api_instance.account_get_plan(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->account_get_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
> Account account_read(id, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Get's an Organisation's account information.
    api_response = api_instance.account_read(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->account_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
> Organisation organisations_create(organisation, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Creates a new Organisation. This will assign the logged in user to the organisation.
    api_response = api_instance.organisations_create(organisation, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation** | [**Organisation**](Organisation.md)| Information of the new Organisation. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
> str organisations_delete(id, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Deletes an organisation.
    api_response = api_instance.organisations_delete(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
> Organisation organisations_read(id, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Gets an organisation's details.
    api_response = api_instance.organisations_read(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

# **organisations_update**
> file organisations_update(id, organisation, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Updates an organisation.
    api_response = api_instance.organisations_update(id, organisation, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->organisations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | 
 **organisation** | [**Organisation**](Organisation.md)| Organisation Information. All fields are updated. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

# **terms_and_conditions_create**
> TermsAndConditions terms_and_conditions_create(id, terms_and_conditions, x_amphoradata_version=x_amphoradata_version)

Adds new Terms and Conditions to your Organisations T/C Library.

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
terms_and_conditions = amphora_api_client.TermsAndConditions() # TermsAndConditions | The new Terms and Conditions.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Adds new Terms and Conditions to your Organisations T/C Library.
    api_response = api_instance.terms_and_conditions_create(id, terms_and_conditions, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->terms_and_conditions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the Organisation. | 
 **terms_and_conditions** | [**TermsAndConditions**](TermsAndConditions.md)| The new Terms and Conditions. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**TermsAndConditions**](TermsAndConditions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organisation metadaa.  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_and_conditions_read**
> list[TermsAndConditions] terms_and_conditions_read(id, x_amphoradata_version=x_amphoradata_version)

Get's a list of an Organisation's Terms and Conditions.

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Get's a list of an Organisation's Terms and Conditions.
    api_response = api_instance.terms_and_conditions_read(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsApi->terms_and_conditions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the Organisation. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**list[TermsAndConditions]**](TermsAndConditions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Terms and Conditions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

