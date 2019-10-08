# openapi_client.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_search_amphorae_by_creator_get**](SearchApi.md#api_search_amphorae_by_creator_get) | **GET** /api/search/amphorae/byCreator | 
[**api_search_amphorae_by_location_get**](SearchApi.md#api_search_amphorae_by_location_get) | **GET** /api/search/amphorae/byLocation | 
[**api_search_amphorae_by_organisation_get**](SearchApi.md#api_search_amphorae_by_organisation_get) | **GET** /api/search/amphorae/byOrganisation | 
[**api_search_amphorae_post**](SearchApi.md#api_search_amphorae_post) | **POST** /api/search/amphorae | 


# **api_search_amphorae_by_creator_get**
> api_search_amphorae_by_creator_get(user_name=user_name)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.SearchApi()
user_name = '' # str |  (optional) (default to '')

try:
    api_instance.api_search_amphorae_by_creator_get(user_name=user_name)
except ApiException as e:
    print("Exception when calling SearchApi->api_search_amphorae_by_creator_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**|  | [optional] [default to &#39;&#39;]

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

# **api_search_amphorae_by_location_get**
> api_search_amphorae_by_location_get(lat=lat, lon=lon, dist=dist)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.SearchApi()
lat = 3.4 # float |  (optional)
lon = 3.4 # float |  (optional)
dist = 10 # float |  (optional) (default to 10)

try:
    api_instance.api_search_amphorae_by_location_get(lat=lat, lon=lon, dist=dist)
except ApiException as e:
    print("Exception when calling SearchApi->api_search_amphorae_by_location_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**|  | [optional] 
 **lon** | **float**|  | [optional] 
 **dist** | **float**|  | [optional] [default to 10]

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

# **api_search_amphorae_by_organisation_get**
> api_search_amphorae_by_organisation_get(org_id=org_id)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.SearchApi()
org_id = '' # str |  (optional) (default to '')

try:
    api_instance.api_search_amphorae_by_organisation_get(org_id=org_id)
except ApiException as e:
    print("Exception when calling SearchApi->api_search_amphorae_by_organisation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | [optional] [default to &#39;&#39;]

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

# **api_search_amphorae_post**
> api_search_amphorae_post(search_parameters=search_parameters)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.SearchApi()
search_parameters = openapi_client.SearchParameters() # SearchParameters |  (optional)

try:
    api_instance.api_search_amphorae_post(search_parameters=search_parameters)
except ApiException as e:
    print("Exception when calling SearchApi->api_search_amphorae_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_parameters** | [**SearchParameters**](SearchParameters.md)|  | [optional] 

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

