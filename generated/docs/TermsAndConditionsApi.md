# amphora_client.TermsAndConditionsApi

All URIs are relative to *https://beta.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terms_and_conditions_create_terms_and_conditions**](TermsAndConditionsApi.md#terms_and_conditions_create_terms_and_conditions) | **POST** /api/Organisations/{id}/TermsAndConditions | Adds new Terms and Conditions to your Organisations T/C Library
[**terms_and_conditions_get_terms_and_conditions**](TermsAndConditionsApi.md#terms_and_conditions_get_terms_and_conditions) | **GET** /api/Organisations/{id}/TermsAndConditions | Get&#39;s a list of an Organisation&#39;s Terms and Conditions


# **terms_and_conditions_create_terms_and_conditions**
> TermsAndConditionsDto terms_and_conditions_create_terms_and_conditions(id, terms_and_conditions_dto)

Adds new Terms and Conditions to your Organisations T/C Library

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
api_instance = amphora_client.TermsAndConditionsApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | The Id of the Organisation
terms_and_conditions_dto = amphora_client.TermsAndConditionsDto() # TermsAndConditionsDto | The new Terms and Conditions

try:
    # Adds new Terms and Conditions to your Organisations T/C Library
    api_response = api_instance.terms_and_conditions_create_terms_and_conditions(id, terms_and_conditions_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsAndConditionsApi->terms_and_conditions_create_terms_and_conditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the Organisation | 
 **terms_and_conditions_dto** | [**TermsAndConditionsDto**](TermsAndConditionsDto.md)| The new Terms and Conditions | 

### Return type

[**TermsAndConditionsDto**](TermsAndConditionsDto.md)

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

# **terms_and_conditions_get_terms_and_conditions**
> list[TermsAndConditionsDto] terms_and_conditions_get_terms_and_conditions(id)

Get's a list of an Organisation's Terms and Conditions

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
api_instance = amphora_client.TermsAndConditionsApi(amphora_client.ApiClient(configuration))
id = 'id_example' # str | The Id of the Organisation

try:
    # Get's a list of an Organisation's Terms and Conditions
    api_response = api_instance.terms_and_conditions_get_terms_and_conditions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsAndConditionsApi->terms_and_conditions_get_terms_and_conditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the Organisation | 

### Return type

[**list[TermsAndConditionsDto]**](TermsAndConditionsDto.md)

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

