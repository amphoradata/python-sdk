# openapi_client.OrganisationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_organisations_id_delete**](OrganisationsApi.md#api_organisations_id_delete) | **DELETE** /api/organisations/{id} | 
[**api_organisations_id_get**](OrganisationsApi.md#api_organisations_id_get) | **GET** /api/organisations/{id} | 
[**api_organisations_id_invitations_get**](OrganisationsApi.md#api_organisations_id_invitations_get) | **GET** /api/organisations/{id}/invitations | 
[**api_organisations_id_invitations_post**](OrganisationsApi.md#api_organisations_id_invitations_post) | **POST** /api/organisations/{id}/invitations | 
[**api_organisations_id_put**](OrganisationsApi.md#api_organisations_id_put) | **PUT** /api/organisations/{id} | 
[**api_organisations_post**](OrganisationsApi.md#api_organisations_post) | **POST** /api/organisations | 


# **api_organisations_id_delete**
> api_organisations_id_delete(id)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.OrganisationsApi()
id = '' # str |  (default to '')

try:
    api_instance.api_organisations_id_delete(id)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_id_delete: %s\n" % e)
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

# **api_organisations_id_get**
> api_organisations_id_get(id)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.OrganisationsApi()
id = '' # str |  (default to '')

try:
    api_instance.api_organisations_id_get(id)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_id_get: %s\n" % e)
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

# **api_organisations_id_invitations_get**
> api_organisations_id_invitations_get(id)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.OrganisationsApi()
id = '' # str |  (default to '')

try:
    api_instance.api_organisations_id_invitations_get(id)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_id_invitations_get: %s\n" % e)
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

# **api_organisations_id_invitations_post**
> api_organisations_id_invitations_post(id, invitation=invitation)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.OrganisationsApi()
id = '' # str |  (default to '')
invitation = openapi_client.Invitation() # Invitation |  (optional)

try:
    api_instance.api_organisations_id_invitations_post(id, invitation=invitation)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_id_invitations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [default to &#39;&#39;]
 **invitation** | [**Invitation**](Invitation.md)|  | [optional] 

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

# **api_organisations_id_put**
> api_organisations_id_put(id, organisation_dto=organisation_dto)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.OrganisationsApi()
id = '' # str |  (default to '')
organisation_dto = openapi_client.OrganisationDto() # OrganisationDto |  (optional)

try:
    api_instance.api_organisations_id_put(id, organisation_dto=organisation_dto)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [default to &#39;&#39;]
 **organisation_dto** | [**OrganisationDto**](OrganisationDto.md)|  | [optional] 

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

# **api_organisations_post**
> api_organisations_post(organisation_model=organisation_model)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.OrganisationsApi()
organisation_model = openapi_client.OrganisationModel() # OrganisationModel |  (optional)

try:
    api_instance.api_organisations_post(organisation_model=organisation_model)
except ApiException as e:
    print("Exception when calling OrganisationsApi->api_organisations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_model** | [**OrganisationModel**](OrganisationModel.md)|  | [optional] 

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

