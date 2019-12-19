# amphora_client.SearchApi

All URIs are relative to *https://appsvc62a56562.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_search_amphorae**](SearchApi.md#search_search_amphorae) | **POST** /api/search/amphorae | Searches for Amphorae.
[**search_search_amphorae_by_creator**](SearchApi.md#search_search_amphorae_by_creator) | **GET** /api/search/amphorae/byCreator | Searches for Amphorae by creator.
[**search_search_amphorae_by_location**](SearchApi.md#search_search_amphorae_by_location) | **GET** /api/search/amphorae/byLocation | Searches for Amphorae by loction.
[**search_search_amphorae_by_organisation**](SearchApi.md#search_search_amphorae_by_organisation) | **GET** /api/search/amphorae/byOrganisation | Searches for Amphorae in an Organisation.


# **search_search_amphorae**
> list[AmphoraDto] search_search_amphorae(search_parameters, x_amphoradata_version=x_amphoradata_version)

Searches for Amphorae.

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
api_instance = amphora_client.SearchApi(amphora_client.ApiClient(configuration))
search_parameters = amphora_client.SearchParameters() # SearchParameters | Search parameters
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Searches for Amphorae.
    api_response = api_instance.search_search_amphorae(search_parameters, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_search_amphorae: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_parameters** | [**SearchParameters**](SearchParameters.md)| Search parameters | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**list[AmphoraDto]**](AmphoraDto.md)

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

# **search_search_amphorae_by_creator**
> list[AmphoraDto] search_search_amphorae_by_creator(user_name=user_name, x_amphoradata_version=x_amphoradata_version)

Searches for Amphorae by creator.

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
api_instance = amphora_client.SearchApi(amphora_client.ApiClient(configuration))
user_name = 'user_name_example' # str | User Name of the creator (optional)
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Searches for Amphorae by creator.
    api_response = api_instance.search_search_amphorae_by_creator(user_name=user_name, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_search_amphorae_by_creator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| User Name of the creator | [optional] 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**list[AmphoraDto]**](AmphoraDto.md)

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

# **search_search_amphorae_by_location**
> list[AmphoraDto] search_search_amphorae_by_location(lat=lat, lon=lon, dist=dist, x_amphoradata_version=x_amphoradata_version)

Searches for Amphorae by loction.

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
api_instance = amphora_client.SearchApi(amphora_client.ApiClient(configuration))
lat = 3.4 # float | Latitude (optional)
lon = 3.4 # float | Longitude (optional)
dist = 10.0 # float | Distance from Latitude and Longitude in which to search (optional) (default to 10.0)
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Searches for Amphorae by loction.
    api_response = api_instance.search_search_amphorae_by_location(lat=lat, lon=lon, dist=dist, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_search_amphorae_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | [optional] 
 **lon** | **float**| Longitude | [optional] 
 **dist** | **float**| Distance from Latitude and Longitude in which to search | [optional] [default to 10.0]
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**list[AmphoraDto]**](AmphoraDto.md)

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

# **search_search_amphorae_by_organisation**
> list[AmphoraDto] search_search_amphorae_by_organisation(org_id=org_id, x_amphoradata_version=x_amphoradata_version)

Searches for Amphorae in an Organisation.

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
api_instance = amphora_client.SearchApi(amphora_client.ApiClient(configuration))
org_id = 'org_id_example' # str | Organisation Id (optional)
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Searches for Amphorae in an Organisation.
    api_response = api_instance.search_search_amphorae_by_organisation(org_id=org_id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_search_amphorae_by_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organisation Id | [optional] 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**list[AmphoraDto]**](AmphoraDto.md)

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

