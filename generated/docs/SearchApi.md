# amphora_client.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_search_amphorae_by_creator_get**](SearchApi.md#api_search_amphorae_by_creator_get) | **GET** /api/search/amphorae/byCreator | Searches for Amphorae by creator.
[**api_search_amphorae_by_location_get**](SearchApi.md#api_search_amphorae_by_location_get) | **GET** /api/search/amphorae/byLocation | Searches for Amphorae by loction.
[**api_search_amphorae_by_organisation_get**](SearchApi.md#api_search_amphorae_by_organisation_get) | **GET** /api/search/amphorae/byOrganisation | Searches for Amphorae in an Organisation.
[**api_search_amphorae_post**](SearchApi.md#api_search_amphorae_post) | **POST** /api/search/amphorae | Searches for Amphorae.


# **api_search_amphorae_by_creator_get**
> list[AmphoraDto] api_search_amphorae_by_creator_get(user_name=user_name)

Searches for Amphorae by creator.

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
api_instance = amphora_client.SearchApi(amphora_client.ApiClient(configuration))
user_name = '' # str | User Name of the creator (optional) (default to '')

try:
    # Searches for Amphorae by creator.
    api_response = api_instance.api_search_amphorae_by_creator_get(user_name=user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->api_search_amphorae_by_creator_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| User Name of the creator | [optional] [default to &#39;&#39;]

### Return type

[**list[AmphoraDto]**](AmphoraDto.md)

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

# **api_search_amphorae_by_location_get**
> list[AmphoraDto] api_search_amphorae_by_location_get(lat=lat, lon=lon, dist=dist)

Searches for Amphorae by loction.

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
api_instance = amphora_client.SearchApi(amphora_client.ApiClient(configuration))
lat = 3.4 # float | Latitude (optional)
lon = 3.4 # float | Longitude (optional)
dist = 10 # float | Distance from Latitude and Longitude in which to search (optional) (default to 10)

try:
    # Searches for Amphorae by loction.
    api_response = api_instance.api_search_amphorae_by_location_get(lat=lat, lon=lon, dist=dist)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->api_search_amphorae_by_location_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | [optional] 
 **lon** | **float**| Longitude | [optional] 
 **dist** | **float**| Distance from Latitude and Longitude in which to search | [optional] [default to 10]

### Return type

[**list[AmphoraDto]**](AmphoraDto.md)

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

# **api_search_amphorae_by_organisation_get**
> list[AmphoraDto] api_search_amphorae_by_organisation_get(org_id=org_id)

Searches for Amphorae in an Organisation.

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
api_instance = amphora_client.SearchApi(amphora_client.ApiClient(configuration))
org_id = '' # str | Organisation Id (optional) (default to '')

try:
    # Searches for Amphorae in an Organisation.
    api_response = api_instance.api_search_amphorae_by_organisation_get(org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->api_search_amphorae_by_organisation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organisation Id | [optional] [default to &#39;&#39;]

### Return type

[**list[AmphoraDto]**](AmphoraDto.md)

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

# **api_search_amphorae_post**
> list[AmphoraDto] api_search_amphorae_post(search_parameters=search_parameters)

Searches for Amphorae.

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
api_instance = amphora_client.SearchApi(amphora_client.ApiClient(configuration))
search_parameters = amphora_client.SearchParameters() # SearchParameters |  (optional)

try:
    # Searches for Amphorae.
    api_response = api_instance.api_search_amphorae_post(search_parameters=search_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->api_search_amphorae_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_parameters** | [**SearchParameters**](SearchParameters.md)|  | [optional] 

### Return type

[**list[AmphoraDto]**](AmphoraDto.md)

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

