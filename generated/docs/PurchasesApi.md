# amphora_client.PurchasesApi

All URIs are relative to *https://beta.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchases_purchase**](PurchasesApi.md#purchases_purchase) | **POST** /api/Amphorae/{id}/Purchases | Purchases an Amphora as the logged in user.


# **purchases_purchase**
> str purchases_purchase(id, x_amphoradata_version=x_amphoradata_version)

Purchases an Amphora as the logged in user.

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
api_instance = amphora_client.PurchasesApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Purchases an Amphora as the logged in user.
    api_response = api_instance.purchases_purchase(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchasesApi->purchases_purchase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

