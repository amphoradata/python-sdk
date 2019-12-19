# amphora_client.OrganisationRestrictionApi

All URIs are relative to *https://appsvc62a56562.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisation_restriction_create**](OrganisationRestrictionApi.md#organisation_restriction_create) | **POST** /api/organisations/{id}/restrictions | Restricts an organisation from accessing data.
[**organisation_restriction_delete**](OrganisationRestrictionApi.md#organisation_restriction_delete) | **DELETE** /api/organisations/{id}/restrictions/{targetOrganisationId} | Deletes a restriction


# **organisation_restriction_create**
> Restriction organisation_restriction_create(id, restriction, x_amphoradata_version=x_amphoradata_version)

Restricts an organisation from accessing data.

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

# Defining host is optional and default to https://appsvc62a56562.azurewebsites.net
configuration.host = "https://appsvc62a56562.azurewebsites.net"
# Create an instance of the API class
api_instance = amphora_client.OrganisationRestrictionApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Your organisation id
restriction = amphora_client.Restriction() # Restriction | Restriction to create
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Restricts an organisation from accessing data.
    api_response = api_instance.organisation_restriction_create(id, restriction, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationRestrictionApi->organisation_restriction_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Your organisation id | 
 **restriction** | [**Restriction**](Restriction.md)| Restriction to create | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**Restriction**](Restriction.md)

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

# **organisation_restriction_delete**
> GenericResponse organisation_restriction_delete(id, target_organisation_id, x_amphoradata_version=x_amphoradata_version)

Deletes a restriction

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

# Defining host is optional and default to https://appsvc62a56562.azurewebsites.net
configuration.host = "https://appsvc62a56562.azurewebsites.net"
# Create an instance of the API class
api_instance = amphora_client.OrganisationRestrictionApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Your organisation id
target_organisation_id = 'target_organisation_id_example' # str | Organisation Id for which you want to delete a restriction
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Deletes a restriction
    api_response = api_instance.organisation_restriction_delete(id, target_organisation_id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationRestrictionApi->organisation_restriction_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Your organisation id | 
 **target_organisation_id** | **str**| Organisation Id for which you want to delete a restriction | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**GenericResponse**](GenericResponse.md)

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

