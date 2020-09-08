# amphora_api_client.SearchApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_search_amphora**](SearchApi.md#search_search_amphora) | **GET** /api/search-v2/amphorae | Searches for Amphorae.
[**search_search_organisations**](SearchApi.md#search_search_organisations) | **GET** /api/search-v2/organisations | Searches for Organisations with fuzzy search.


# **search_search_amphora**
> SearchResponseOfBasicAmphora search_search_amphora(term=term, labels=labels, org_id=org_id, lat=lat, lon=lon, dist=dist, take=take, skip=skip)

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
term = 'term_example' # str | Gets or sets the free text search term. (optional)
labels = 'labels_example' # str | Gets or sets the comma separated labels that must be included in results. (optional)
org_id = 'org_id_example' # str | Gets or sets the Organisation ID for the Amphora. (optional)
lat = 3.4 # float | Gets or sets the latitude (center of search area). (optional)
lon = 3.4 # float | Gets or sets the longitude (center of search area). (optional)
dist = 3.4 # float | Gets or sets the distance from center of search area (describing a circle). (optional)
take = 56 # int | Gets or sets how many items to return. Defaults to 64. (optional)
skip = 56 # int | Gets or sets how many items to skip before returning. Defaults to 0. (optional)

try:
    # Searches for Amphorae.
    api_response = api_instance.search_search_amphora(term=term, labels=labels, org_id=org_id, lat=lat, lon=lon, dist=dist, take=take, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_search_amphora: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Gets or sets the free text search term. | [optional] 
 **labels** | **str**| Gets or sets the comma separated labels that must be included in results. | [optional] 
 **org_id** | **str**| Gets or sets the Organisation ID for the Amphora. | [optional] 
 **lat** | **float**| Gets or sets the latitude (center of search area). | [optional] 
 **lon** | **float**| Gets or sets the longitude (center of search area). | [optional] 
 **dist** | **float**| Gets or sets the distance from center of search area (describing a circle). | [optional] 
 **take** | **int**| Gets or sets how many items to return. Defaults to 64. | [optional] 
 **skip** | **int**| Gets or sets how many items to skip before returning. Defaults to 0. | [optional] 

### Return type

[**SearchResponseOfBasicAmphora**](SearchResponseOfBasicAmphora.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A search response of Amphora.  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_search_organisations**
> SearchResponseOfOrganisation search_search_organisations(term=term, take=take, skip=skip)

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
term = 'term_example' # str | Gets or sets the free text search term. (optional)
take = 56 # int | Gets or sets how many items to return. Defaults to 64. (optional)
skip = 56 # int | Gets or sets how many items to skip before returning. Defaults to 0. (optional)

try:
    # Searches for Organisations with fuzzy search.
    api_response = api_instance.search_search_organisations(term=term, take=take, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_search_organisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Gets or sets the free text search term. | [optional] 
 **take** | **int**| Gets or sets how many items to return. Defaults to 64. | [optional] 
 **skip** | **int**| Gets or sets how many items to skip before returning. Defaults to 0. | [optional] 

### Return type

[**SearchResponseOfOrganisation**](SearchResponseOfOrganisation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Organisations.  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

