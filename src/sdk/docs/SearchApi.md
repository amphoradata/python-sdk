# amphora_api_client.SearchApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_search_amphorae**](SearchApi.md#search_search_amphorae) | **GET** /api/search/amphorae | Searches for Amphorae.
[**search_search_amphorae_by_location**](SearchApi.md#search_search_amphorae_by_location) | **GET** /api/search/amphorae/byLocation | Searches for Amphorae by loction.
[**search_search_amphorae_by_organisation**](SearchApi.md#search_search_amphorae_by_organisation) | **GET** /api/search/amphorae/byOrganisation | Searches for Amphorae in an Organisation.
[**search_search_organisations**](SearchApi.md#search_search_organisations) | **GET** /api/search/organisations | Searches for Organisations with fuzzy search.


# **search_search_amphorae**
> list[BasicAmphora] search_search_amphorae(term=term, labels=labels, lat=lat, lon=lon, dist=dist, x_amphoradata_version=x_amphoradata_version)

Searches for Amphorae.

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
api_instance = amphora_api_client.SearchApi(amphora_api_client.ApiClient(configuration))
term = 'term_example' # str | General search term for text comparison. (optional)
labels = 'labels_example' # str | Comma separated labels that must be included in results. (optional)
lat = 3.4 # float | Latitude (center of search area). (optional)
lon = 3.4 # float | Longitude (center of search area). (optional)
dist = 3.4 # float | Distance from center of search area (describing a circle). (optional)
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Searches for Amphorae.
    api_response = api_instance.search_search_amphorae(term=term, labels=labels, lat=lat, lon=lon, dist=dist, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_search_amphorae: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| General search term for text comparison. | [optional] 
 **labels** | **str**| Comma separated labels that must be included in results. | [optional] 
 **lat** | **float**| Latitude (center of search area). | [optional] 
 **lon** | **float**| Longitude (center of search area). | [optional] 
 **dist** | **float**| Distance from center of search area (describing a circle). | [optional] 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**list[BasicAmphora]**](BasicAmphora.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Amphora.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_search_amphorae_by_location**
> list[BasicAmphora] search_search_amphorae_by_location(lat=lat, lon=lon, dist=dist, x_amphoradata_version=x_amphoradata_version)

Searches for Amphorae by loction.

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
api_instance = amphora_api_client.SearchApi(amphora_api_client.ApiClient(configuration))
lat = 3.4 # float | Latitude. (optional)
lon = 3.4 # float | Longitude. (optional)
dist = 10.0 # float | Distance from Latitude and Longitude in which to search. (optional) (default to 10.0)
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
 **lat** | **float**| Latitude. | [optional] 
 **lon** | **float**| Longitude. | [optional] 
 **dist** | **float**| Distance from Latitude and Longitude in which to search. | [optional] [default to 10.0]
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**list[BasicAmphora]**](BasicAmphora.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Amphora. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_search_amphorae_by_organisation**
> list[BasicAmphora] search_search_amphorae_by_organisation(org_id=org_id, x_amphoradata_version=x_amphoradata_version)

Searches for Amphorae in an Organisation.

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
api_instance = amphora_api_client.SearchApi(amphora_api_client.ApiClient(configuration))
org_id = 'org_id_example' # str | Organisation Id. (optional)
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
 **org_id** | **str**| Organisation Id. | [optional] 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**list[BasicAmphora]**](BasicAmphora.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Amphora.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_search_organisations**
> list[Organisation] search_search_organisations(term=term, x_amphoradata_version=x_amphoradata_version)

Searches for Organisations with fuzzy search.

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
api_instance = amphora_api_client.SearchApi(amphora_api_client.ApiClient(configuration))
term = 'term_example' # str | Search Term. (optional)
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Searches for Organisations with fuzzy search.
    api_response = api_instance.search_search_organisations(term=term, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_search_organisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Search Term. | [optional] 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**list[Organisation]**](Organisation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Organisations.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

