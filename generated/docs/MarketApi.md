# amphora_client.MarketApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_location_fuzzy_get**](MarketApi.md#api_location_fuzzy_get) | **GET** /api/location/fuzzy | Executes a fuzzy location search.
[**api_market_get**](MarketApi.md#api_market_get) | **GET** /api/market | Finds Amphora using a fuzzy search
[**api_market_purchase_post**](MarketApi.md#api_market_purchase_post) | **POST** /api/market/purchase | Purchases an Amphora as the logged in user.


# **api_location_fuzzy_get**
> FuzzySearchResponse api_location_fuzzy_get(query=query)

Executes a fuzzy location search.

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.MarketApi()
query = '' # str | Search Text (optional) (default to '')

try:
    # Executes a fuzzy location search.
    api_response = api_instance.api_location_fuzzy_get(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_location_fuzzy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search Text | [optional] [default to &#39;&#39;]

### Return type

[**FuzzySearchResponse**](FuzzySearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_market_get**
> list[AmphoraDto] api_market_get(query=query)

Finds Amphora using a fuzzy search

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.MarketApi()
query = '' # str | Amphora Id (optional) (default to '')

try:
    # Finds Amphora using a fuzzy search
    api_response = api_instance.api_market_get(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_market_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Amphora Id | [optional] [default to &#39;&#39;]

### Return type

[**list[AmphoraDto]**](AmphoraDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_market_purchase_post**
> api_market_purchase_post(id=id)

Purchases an Amphora as the logged in user.

### Example

```python
from __future__ import print_function
import time
import amphora_client
from amphora_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amphora_client.MarketApi()
id = '' # str | Amphora Id (optional) (default to '')

try:
    # Purchases an Amphora as the logged in user.
    api_instance.api_market_purchase_post(id=id)
except ApiException as e:
    print("Exception when calling MarketApi->api_market_purchase_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id | [optional] [default to &#39;&#39;]

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

