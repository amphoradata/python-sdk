# amphora_client.MarketApi

All URIs are relative to *https://beta.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_find**](MarketApi.md#market_find) | **GET** /api/market/search | Finds Amphora using a fuzzy search
[**market_lookup_location**](MarketApi.md#market_lookup_location) | **GET** /api/location/fuzzy | Executes a fuzzy location search.


# **market_find**
> list[AmphoraDto] market_find(x_amphoradata_version, query=query, top=top, skip=skip)

Finds Amphora using a fuzzy search

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

# Defining host is optional and default to https://beta.amphoradata.com
configuration.host = "https://beta.amphoradata.com"
# Create an instance of the API class
api_instance = amphora_client.MarketApi(amphora_client.ApiClient(configuration))
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number
query = 'query_example' # str | Amphora Id (optional)
top = 56 # int | How many results to return (optional)
skip = 56 # int | How many pages (in multiples of top) to skip (optional)

try:
    # Finds Amphora using a fuzzy search
    api_response = api_instance.market_find(x_amphoradata_version, query=query, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_amphoradata_version** | **str**| API Version Number | 
 **query** | **str**| Amphora Id | [optional] 
 **top** | **int**| How many results to return | [optional] 
 **skip** | **int**| How many pages (in multiples of top) to skip | [optional] 

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

# **market_lookup_location**
> FuzzySearchResponse market_lookup_location(x_amphoradata_version, query=query)

Executes a fuzzy location search.

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

# Defining host is optional and default to https://beta.amphoradata.com
configuration.host = "https://beta.amphoradata.com"
# Create an instance of the API class
api_instance = amphora_client.MarketApi(amphora_client.ApiClient(configuration))
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number
query = 'query_example' # str | Search Text (optional)

try:
    # Executes a fuzzy location search.
    api_response = api_instance.market_lookup_location(x_amphoradata_version, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_lookup_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_amphoradata_version** | **str**| API Version Number | 
 **query** | **str**| Search Text | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

