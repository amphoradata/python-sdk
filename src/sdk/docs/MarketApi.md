# amphora_api_client.MarketApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_find**](MarketApi.md#market_find) | **GET** /api/market/search | Finds Amphora using a fuzzy search.
[**market_lookup_location**](MarketApi.md#market_lookup_location) | **GET** /api/location/fuzzy | Executes a fuzzy location search.


# **market_find**
> list[BasicAmphora] market_find(query=query, top=top, skip=skip, x_amphoradata_version=x_amphoradata_version)

Finds Amphora using a fuzzy search.

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
api_instance = amphora_api_client.MarketApi(amphora_api_client.ApiClient(configuration))
query = 'query_example' # str | A string as a search term. (optional)
top = 56 # int | How many results to return. (optional)
skip = 56 # int | How many pages (in multiples of top) to skip. (optional)
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Finds Amphora using a fuzzy search.
    api_response = api_instance.market_find(query=query, top=top, skip=skip, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| A string as a search term. | [optional] 
 **top** | **int**| How many results to return. | [optional] 
 **skip** | **int**| How many pages (in multiples of top) to skip. | [optional] 
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

# **market_lookup_location**
> FuzzySearchResponse market_lookup_location(query=query, x_amphoradata_version=x_amphoradata_version)

Executes a fuzzy location search.

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
api_instance = amphora_api_client.MarketApi(amphora_api_client.ApiClient(configuration))
query = 'query_example' # str | Search Text. (optional)
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Executes a fuzzy location search.
    api_response = api_instance.market_lookup_location(query=query, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_lookup_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search Text. | [optional] 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**FuzzySearchResponse**](FuzzySearchResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A fuzzy search response.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

