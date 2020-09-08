# amphora_api_client.AccountApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_invitations_invitations**](AccountApi.md#account_invitations_invitations) | **GET** /api/Account/Invitations | Gets a list of invitations to the organisation.
[**account_read**](AccountApi.md#account_read) | **GET** /api/Organisations/{id}/Account | Gets an Organisation&#39;s account information.
[**account_read2**](AccountApi.md#account_read2) | **GET** /api/Account | Gets an Organisation&#39;s account information.
[**invoices_create_invoice**](AccountApi.md#invoices_create_invoice) | **POST** /api/account/invoices | Creates a new invoice. Restricted to global administrators.
[**invoices_download_invoice**](AccountApi.md#invoices_download_invoice) | **GET** /api/account/invoices/{id}/download | Downloads an invoice in a specified format.
[**invoices_get_invoices**](AccountApi.md#invoices_get_invoices) | **GET** /api/account/invoices | Returns a list of invoices as items.
[**membership_get_memberships**](AccountApi.md#membership_get_memberships) | **GET** /api/account/memberships | Returns a collection of members of an organisational account.
[**plan_get_plan**](AccountApi.md#plan_get_plan) | **GET** /api/Account/Plan | Gets an Organisation&#39;s plan information.
[**plan_set_plan**](AccountApi.md#plan_set_plan) | **POST** /api/Account/Plan | Set&#39;s an Organisation&#39;s plan.
[**transactions_get_transactions**](AccountApi.md#transactions_get_transactions) | **GET** /api/Account/Transactions | Gets the most recent transactions of the account. Defaults to the first 50 debits and 50 credits.


# **account_invitations_invitations**
> CollectionResponseOfInvitation account_invitations_invitations(id=id)

Gets a list of invitations to the organisation.

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
api_instance = amphora_api_client.AccountApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | The organisation id. (optional)

try:
    # Gets a list of invitations to the organisation.
    api_response = api_instance.account_invitations_invitations(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_invitations_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organisation id. | [optional] 

### Return type

[**CollectionResponseOfInvitation**](CollectionResponseOfInvitation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The collection of invitations. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_read**
> AccountInformation account_read(id)

Gets an Organisation's account information.

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
api_instance = amphora_api_client.AccountApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id.

try:
    # Gets an Organisation's account information.
    api_response = api_instance.account_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | 

### Return type

[**AccountInformation**](AccountInformation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Organisation&#39;s account metadata.  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_read2**
> AccountInformation account_read2(id)

Gets an Organisation's account information.

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
api_instance = amphora_api_client.AccountApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id.

try:
    # Gets an Organisation's account information.
    api_response = api_instance.account_read2(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_read2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | 

### Return type

[**AccountInformation**](AccountInformation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Organisation&#39;s account metadata.  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_create_invoice**
> ItemResponseOfInvoice invoices_create_invoice(create_invoice)

Creates a new invoice. Restricted to global administrators.

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
api_instance = amphora_api_client.AccountApi(amphora_api_client.ApiClient(configuration))
create_invoice = amphora_api_client.CreateInvoice() # CreateInvoice | The organisation for which to create the invoice.

try:
    # Creates a new invoice. Restricted to global administrators.
    api_response = api_instance.invoices_create_invoice(create_invoice)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->invoices_create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_invoice** | [**CreateInvoice**](CreateInvoice.md)| The organisation for which to create the invoice. | 

### Return type

[**ItemResponseOfInvoice**](ItemResponseOfInvoice.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new invoice. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_download_invoice**
> file invoices_download_invoice(id, format=format)

Downloads an invoice in a specified format.

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
api_instance = amphora_api_client.AccountApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Invoice Id.
format = 'format_example' # str | Only csv is supported. (optional)

try:
    # Downloads an invoice in a specified format.
    api_response = api_instance.invoices_download_invoice(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->invoices_download_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invoice Id. | 
 **format** | **str**| Only csv is supported. | [optional] 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The invoice in the format specified. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_invoices**
> CollectionResponseOfInvoice invoices_get_invoices()

Returns a list of invoices as items.

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
api_instance = amphora_api_client.AccountApi(amphora_api_client.ApiClient(configuration))

try:
    # Returns a list of invoices as items.
    api_response = api_instance.invoices_get_invoices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->invoices_get_invoices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollectionResponseOfInvoice**](CollectionResponseOfInvoice.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of invoices. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_get_memberships**
> CollectionResponseOfMembership membership_get_memberships(id=id)

Returns a collection of members of an organisational account.

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
api_instance = amphora_api_client.AccountApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id. Defaults to your org. (optional)

try:
    # Returns a collection of members of an organisational account.
    api_response = api_instance.membership_get_memberships(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->membership_get_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. Defaults to your org. | [optional] 

### Return type

[**CollectionResponseOfMembership**](CollectionResponseOfMembership.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection response of memberships. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_get_plan**
> PlanInformation plan_get_plan()

Gets an Organisation's plan information.

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
api_instance = amphora_api_client.AccountApi(amphora_api_client.ApiClient(configuration))

try:
    # Gets an Organisation's plan information.
    api_response = api_instance.plan_get_plan()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->plan_get_plan: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PlanInformation**](PlanInformation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user&#39;s Organisation&#39;s plan.  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_set_plan**
> PlanInformation plan_set_plan(plan_type=plan_type)

Set's an Organisation's plan.

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
api_instance = amphora_api_client.AccountApi(amphora_api_client.ApiClient(configuration))
plan_type = 'plan_type_example' # str | The Plan Type. Should be PAYG or Glaze. (optional)

try:
    # Set's an Organisation's plan.
    api_response = api_instance.plan_set_plan(plan_type=plan_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->plan_set_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_type** | **str**| The Plan Type. Should be PAYG or Glaze. | [optional] 

### Return type

[**PlanInformation**](PlanInformation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Organisation&#39;s plan.  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_get_transactions**
> CollectionResponseOfTransaction transactions_get_transactions(id=id)

Gets the most recent transactions of the account. Defaults to the first 50 debits and 50 credits.

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
api_instance = amphora_api_client.AccountApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Organisation Id. (optional)

try:
    # Gets the most recent transactions of the account. Defaults to the first 50 debits and 50 credits.
    api_response = api_instance.transactions_get_transactions(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->transactions_get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organisation Id. | [optional] 

### Return type

[**CollectionResponseOfTransaction**](CollectionResponseOfTransaction.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of recent transactions.  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

