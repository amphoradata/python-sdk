# amphora_api_client.AmphoraeApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amphora_quality_get**](AmphoraeApi.md#amphora_quality_get) | **GET** /api/amphorae/{id}/quality | Gets the data quality metrics for this Amphora.
[**amphora_quality_set**](AmphoraeApi.md#amphora_quality_set) | **POST** /api/amphorae/{id}/quality | Sets the data quality metrics for this Amphora.
[**amphorae_access_controls_create_for_all**](AmphoraeApi.md#amphorae_access_controls_create_for_all) | **POST** /api/amphorae/{id}/AccessControls/ForAll | Creates an Access Control Rule for all on this Amphora.
[**amphorae_access_controls_create_for_organisation**](AmphoraeApi.md#amphorae_access_controls_create_for_organisation) | **POST** /api/amphorae/{id}/AccessControls/ForOrganisation | Creates an Access Control Rule on this Amphora.
[**amphorae_access_controls_create_for_user**](AmphoraeApi.md#amphorae_access_controls_create_for_user) | **POST** /api/amphorae/{id}/AccessControls/ForUser | Creates an Access Control rule on this Amphora.
[**amphorae_access_controls_delete**](AmphoraeApi.md#amphorae_access_controls_delete) | **DELETE** /api/amphorae/{id}/AccessControls/{ruleId} | Deletes an Access Control on this Amphora.
[**amphorae_access_controls_get_for_all_rule**](AmphoraeApi.md#amphorae_access_controls_get_for_all_rule) | **GET** /api/amphorae/{id}/AccessControls/ForAll | Gets the &#39;for all&#39; rule, if it exists, else an empty 200.
[**amphorae_access_controls_get_organisation_rules**](AmphoraeApi.md#amphorae_access_controls_get_organisation_rules) | **GET** /api/amphorae/{id}/AccessControls/ForOrganisation | Gets the list of access rules applied to organisations.
[**amphorae_access_controls_get_user_rules**](AmphoraeApi.md#amphorae_access_controls_get_user_rules) | **GET** /api/amphorae/{id}/AccessControls/ForUser | Gets the list of access rules applied to users.
[**amphorae_create**](AmphoraeApi.md#amphorae_create) | **POST** /api/amphorae | Creates a new empty Amphora in the user&#39;s organisation.
[**amphorae_delete**](AmphoraeApi.md#amphorae_delete) | **DELETE** /api/amphorae/{id} | Deletes an Amphora.
[**amphorae_files_create_file_request**](AmphoraeApi.md#amphorae_files_create_file_request) | **POST** /api/amphorae/{id}/files/{file} | Creates a file. Returns a blob URL to upload to.
[**amphorae_files_delete_file**](AmphoraeApi.md#amphorae_files_delete_file) | **DELETE** /api/amphorae/{id}/files/{file} | Gets the contents of a file. Returns application/octet-stream.
[**amphorae_files_download_file**](AmphoraeApi.md#amphorae_files_download_file) | **GET** /api/amphorae/{id}/files/{file} | Gets the contents of a file. Returns application/octet-stream.
[**amphorae_files_list_files**](AmphoraeApi.md#amphorae_files_list_files) | **GET** /api/amphorae/{id}/files | Lists an Amphora&#39;s files.
[**amphorae_files_query_files**](AmphoraeApi.md#amphorae_files_query_files) | **POST** /api/amphorae/{id}/files | Queries an Amphora&#39;s files.
[**amphorae_files_read_file_attributes**](AmphoraeApi.md#amphorae_files_read_file_attributes) | **GET** /api/amphorae/{id}/files/{file}/attributes | Gets the attributes of a file.
[**amphorae_files_write_file_attributes**](AmphoraeApi.md#amphorae_files_write_file_attributes) | **POST** /api/amphorae/{id}/files/{file}/attributes | Gets the attributes of a file.
[**amphorae_list**](AmphoraeApi.md#amphorae_list) | **GET** /api/amphorae | Gets a list of Amphora for yourself or your org, created or purchased by you (or organisation).
[**amphorae_read**](AmphoraeApi.md#amphorae_read) | **GET** /api/amphorae/{id} | Gets details of an Amphora by Id.
[**amphorae_signals_create_signal**](AmphoraeApi.md#amphorae_signals_create_signal) | **POST** /api/amphorae/{id}/signals | Associates a signal with an Amphora. Signal is created if not existing.
[**amphorae_signals_get_signal**](AmphoraeApi.md#amphorae_signals_get_signal) | **GET** /api/amphorae/{id}/signals/{property} | Gets the signals associated with an Amphora.
[**amphorae_signals_get_signals**](AmphoraeApi.md#amphorae_signals_get_signals) | **GET** /api/amphorae/{id}/signals | Gets the signals associated with an Amphora.
[**amphorae_signals_update_signal**](AmphoraeApi.md#amphorae_signals_update_signal) | **PUT** /api/amphorae/{id}/signals/{signalId} | Associates a signal with an Amphora. Signal is created if not existing.
[**amphorae_signals_upload_signal**](AmphoraeApi.md#amphorae_signals_upload_signal) | **POST** /api/amphorae/{id}/signals/values | Uploads values to an Amphora signal(s).
[**amphorae_signals_upload_signal2**](AmphoraeApi.md#amphorae_signals_upload_signal2) | **POST** /api/amphorae/{id}/signalValues | Uploads values to an Amphora signal(s).
[**amphorae_signals_upload_signal_batch**](AmphoraeApi.md#amphorae_signals_upload_signal_batch) | **POST** /api/amphorae/{id}/signals/batchvalues | Uploads values in batch to an Amphora signal(s).
[**amphorae_signals_upload_signal_batch2**](AmphoraeApi.md#amphorae_signals_upload_signal_batch2) | **POST** /api/amphorae/{id}/batchSignalValues | Uploads values in batch to an Amphora signal(s).
[**amphorae_update**](AmphoraeApi.md#amphorae_update) | **PUT** /api/amphorae/{id} | Updates the details of an Amphora by Id.
[**purchases_purchase**](AmphoraeApi.md#purchases_purchase) | **POST** /api/Amphorae/{id}/Purchases | Purchases an Amphora as the logged in user.


# **amphora_quality_get**
> Quality amphora_quality_get(id)

Gets the data quality metrics for this Amphora.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.

try:
    # Gets the data quality metrics for this Amphora.
    api_response = api_instance.amphora_quality_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphora_quality_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 

### Return type

[**Quality**](Quality.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The quality metrics. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphora_quality_set**
> Quality amphora_quality_set(id, quality)

Sets the data quality metrics for this Amphora.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
quality = amphora_api_client.Quality() # Quality | The data quality metrics.

try:
    # Sets the data quality metrics for this Amphora.
    api_response = api_instance.amphora_quality_set(id, quality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphora_quality_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **quality** | [**Quality**](Quality.md)| The data quality metrics. | 

### Return type

[**Quality**](Quality.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The quality metrics. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_access_controls_create_for_all**
> AllAccessRule amphorae_access_controls_create_for_all(id, all_access_rule)

Creates an Access Control Rule for all on this Amphora.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
all_access_rule = amphora_api_client.AllAccessRule() # AllAccessRule | The rule to create.

try:
    # Creates an Access Control Rule for all on this Amphora.
    api_response = api_instance.amphorae_access_controls_create_for_all(id, all_access_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_create_for_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **all_access_rule** | [**AllAccessRule**](AllAccessRule.md)| The rule to create. | 

### Return type

[**AllAccessRule**](AllAccessRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The same rule. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_access_controls_create_for_organisation**
> UserAccessRule amphorae_access_controls_create_for_organisation(id, organisation_access_rule)

Creates an Access Control Rule on this Amphora.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
organisation_access_rule = amphora_api_client.OrganisationAccessRule() # OrganisationAccessRule | The rule to create.

try:
    # Creates an Access Control Rule on this Amphora.
    api_response = api_instance.amphorae_access_controls_create_for_organisation(id, organisation_access_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_create_for_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **organisation_access_rule** | [**OrganisationAccessRule**](OrganisationAccessRule.md)| The rule to create. | 

### Return type

[**UserAccessRule**](UserAccessRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The same rule. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_access_controls_create_for_user**
> UserAccessRule amphorae_access_controls_create_for_user(id, user_access_rule)

Creates an Access Control rule on this Amphora.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
user_access_rule = amphora_api_client.UserAccessRule() # UserAccessRule | The rule to create.

try:
    # Creates an Access Control rule on this Amphora.
    api_response = api_instance.amphorae_access_controls_create_for_user(id, user_access_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_create_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **user_access_rule** | [**UserAccessRule**](UserAccessRule.md)| The rule to create. | 

### Return type

[**UserAccessRule**](UserAccessRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rule. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_access_controls_delete**
> Response amphorae_access_controls_delete(id, rule_id)

Deletes an Access Control on this Amphora.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
rule_id = 'rule_id_example' # str | The Id of the rule to delete.

try:
    # Deletes an Access Control on this Amphora.
    api_response = api_instance.amphorae_access_controls_delete(id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **rule_id** | **str**| The Id of the rule to delete. | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Empty 200. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_access_controls_get_for_all_rule**
> AllAccessRule amphorae_access_controls_get_for_all_rule(id)

Gets the 'for all' rule, if it exists, else an empty 200.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.

try:
    # Gets the 'for all' rule, if it exists, else an empty 200.
    api_response = api_instance.amphorae_access_controls_get_for_all_rule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_get_for_all_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 

### Return type

[**AllAccessRule**](AllAccessRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A rule, if it exists. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_access_controls_get_organisation_rules**
> list[OrganisationAccessRule] amphorae_access_controls_get_organisation_rules(id)

Gets the list of access rules applied to organisations.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.

try:
    # Gets the list of access rules applied to organisations.
    api_response = api_instance.amphorae_access_controls_get_organisation_rules(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_get_organisation_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 

### Return type

[**list[OrganisationAccessRule]**](OrganisationAccessRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**200** | A list of rules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_access_controls_get_user_rules**
> list[UserAccessRule] amphorae_access_controls_get_user_rules(id)

Gets the list of access rules applied to users.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.

try:
    # Gets the list of access rules applied to users.
    api_response = api_instance.amphorae_access_controls_get_user_rules(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_get_user_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 

### Return type

[**list[UserAccessRule]**](UserAccessRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rules. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_create**
> DetailedAmphora amphorae_create(create_amphora)

Creates a new empty Amphora in the user's organisation.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
create_amphora = amphora_api_client.CreateAmphora() # CreateAmphora | Information for the new Amphora.

try:
    # Creates a new empty Amphora in the user's organisation.
    api_response = api_instance.amphorae_create(create_amphora)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_amphora** | [**CreateAmphora**](CreateAmphora.md)| Information for the new Amphora. | 

### Return type

[**DetailedAmphora**](DetailedAmphora.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new Amphora. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_delete**
> str amphorae_delete(id)

Deletes an Amphora.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.

try:
    # Deletes an Amphora.
    api_response = api_instance.amphorae_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 

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

# **amphorae_files_create_file_request**
> UploadResponse amphorae_files_create_file_request(id, file)

Creates a file. Returns a blob URL to upload to.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
file = 'file_example' # str | The name of the file.

try:
    # Creates a file. Returns a blob URL to upload to.
    api_response = api_instance.amphorae_files_create_file_request(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_create_file_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **file** | **str**| The name of the file. | 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object with a blob URL. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_files_delete_file**
> Response amphorae_files_delete_file(id, file)

Gets the contents of a file. Returns application/octet-stream.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
file = 'file_example' # str | The name of the file.

try:
    # Gets the contents of a file. Returns application/octet-stream.
    api_response = api_instance.amphorae_files_delete_file(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **file** | **str**| The name of the file. | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 if successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_files_download_file**
> file amphorae_files_download_file(id, file)

Gets the contents of a file. Returns application/octet-stream.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
file = 'file_example' # str | The name of the file.

try:
    # Gets the contents of a file. Returns application/octet-stream.
    api_response = api_instance.amphorae_files_download_file(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **file** | **str**| The name of the file. | 

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
**200** | The file contents. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_files_list_files**
> list[str] amphorae_files_list_files(id, order_by=order_by, prefix=prefix, take=take, skip=skip)

Lists an Amphora's files.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
order_by = 'order_by_example' # str | Gets or sets the the orderBy parameter. Options are Alphabetical or LastModified. (optional)
prefix = 'prefix_example' # str | Gets or sets a prefix filter for all file names. Is case sensitive. (optional)
take = 56 # int | Gets or sets how many items to return. Defaults to 64. (optional)
skip = 56 # int | Gets or sets how many items to skip before returning. Defaults to 0. (optional)

try:
    # Lists an Amphora's files.
    api_response = api_instance.amphorae_files_list_files(id, order_by=order_by, prefix=prefix, take=take, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **order_by** | **str**| Gets or sets the the orderBy parameter. Options are Alphabetical or LastModified. | [optional] 
 **prefix** | **str**| Gets or sets a prefix filter for all file names. Is case sensitive. | [optional] 
 **take** | **int**| Gets or sets how many items to return. Defaults to 64. | [optional] 
 **skip** | **int**| Gets or sets how many items to skip before returning. Defaults to 0. | [optional] 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of file names. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_files_query_files**
> list[str] amphorae_files_query_files(id, file_query_options)

Queries an Amphora's files.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
file_query_options = amphora_api_client.FileQueryOptions() # FileQueryOptions | Option for querying the files.

try:
    # Queries an Amphora's files.
    api_response = api_instance.amphorae_files_query_files(id, file_query_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_query_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **file_query_options** | [**FileQueryOptions**](FileQueryOptions.md)| Option for querying the files. | 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of file names. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_files_read_file_attributes**
> dict(str, str) amphorae_files_read_file_attributes(id, file)

Gets the attributes of a file.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
file = 'file_example' # str | The name of the file.

try:
    # Gets the attributes of a file.
    api_response = api_instance.amphorae_files_read_file_attributes(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_read_file_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **file** | **str**| The name of the file. | 

### Return type

**dict(str, str)**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The attributes. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_files_write_file_attributes**
> dict(str, str) amphorae_files_write_file_attributes(id, file, request_body)

Gets the attributes of a file.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
file = 'file_example' # str | The name of the file.
request_body = {'key': 'request_body_example'} # dict(str, str) | A dict containing attributes for the file.

try:
    # Gets the attributes of a file.
    api_response = api_instance.amphorae_files_write_file_attributes(id, file, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_write_file_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **file** | **str**| The name of the file. | 
 **request_body** | [**dict(str, str)**](str.md)| A dict containing attributes for the file. | 

### Return type

**dict(str, str)**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The attributes. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_list**
> list[DetailedAmphora] amphorae_list(scope=scope, access_type=access_type, take=take, skip=skip)

Gets a list of Amphora for yourself or your org, created or purchased by you (or organisation).

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
scope = 'self' # str | 'self' or 'organisation'. Defaults to self. (optional) (default to 'self')
access_type = 'created' # str | 'created' or 'purchased'. Defaults to created. (optional) (default to 'created')
take = 56 # int | Gets or sets how many items to return. Defaults to 64. (optional)
skip = 56 # int | Gets or sets how many items to skip before returning. Defaults to 0. (optional)

try:
    # Gets a list of Amphora for yourself or your org, created or purchased by you (or organisation).
    api_response = api_instance.amphorae_list(scope=scope, access_type=access_type, take=take, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| &#39;self&#39; or &#39;organisation&#39;. Defaults to self. | [optional] [default to &#39;self&#39;]
 **access_type** | **str**| &#39;created&#39; or &#39;purchased&#39;. Defaults to created. | [optional] [default to &#39;created&#39;]
 **take** | **int**| Gets or sets how many items to return. Defaults to 64. | [optional] 
 **skip** | **int**| Gets or sets how many items to skip before returning. Defaults to 0. | [optional] 

### Return type

[**list[DetailedAmphora]**](DetailedAmphora.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Amphora. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_read**
> DetailedAmphora amphorae_read(id)

Gets details of an Amphora by Id.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.

try:
    # Gets details of an Amphora by Id.
    api_response = api_instance.amphorae_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 

### Return type

[**DetailedAmphora**](DetailedAmphora.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Amphora details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_create_signal**
> Signal amphorae_signals_create_signal(id, create_signal)

Associates a signal with an Amphora. Signal is created if not existing.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
create_signal = amphora_api_client.CreateSignal() # CreateSignal | Signal Details.

try:
    # Associates a signal with an Amphora. Signal is created if not existing.
    api_response = api_instance.amphorae_signals_create_signal(id, create_signal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_create_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **create_signal** | [**CreateSignal**](CreateSignal.md)| Signal Details. | 

### Return type

[**Signal**](Signal.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signal metadata. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_get_signal**
> Signal amphorae_signals_get_signal(id, _property)

Gets the signals associated with an Amphora.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
_property = '_property_example' # str | The name or id of the signal property.

try:
    # Gets the signals associated with an Amphora.
    api_response = api_instance.amphorae_signals_get_signal(id, _property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_get_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **_property** | **str**| The name or id of the signal property. | 

### Return type

[**Signal**](Signal.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of signals. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_get_signals**
> list[Signal] amphorae_signals_get_signals(id)

Gets the signals associated with an Amphora.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.

try:
    # Gets the signals associated with an Amphora.
    api_response = api_instance.amphorae_signals_get_signals(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_get_signals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 

### Return type

[**list[Signal]**](Signal.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of signals. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_update_signal**
> Signal amphorae_signals_update_signal(id, signal_id, update_signal)

Associates a signal with an Amphora. Signal is created if not existing.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
signal_id = 'signal_id_example' # str | Signal Details.
update_signal = amphora_api_client.UpdateSignal() # UpdateSignal | Signal properties to update.

try:
    # Associates a signal with an Amphora. Signal is created if not existing.
    api_response = api_instance.amphorae_signals_update_signal(id, signal_id, update_signal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_update_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **signal_id** | **str**| Signal Details. | 
 **update_signal** | [**UpdateSignal**](UpdateSignal.md)| Signal properties to update. | 

### Return type

[**Signal**](Signal.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signal metadata. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_upload_signal**
> dict(str, object) amphorae_signals_upload_signal(id, request_body)

Uploads values to an Amphora signal(s).

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
request_body = None # dict(str, object) | Signal Values.

try:
    # Uploads values to an Amphora signal(s).
    api_response = api_instance.amphorae_signals_upload_signal(id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_upload_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **request_body** | [**dict(str, object)**](object.md)| Signal Values. | 

### Return type

**dict(str, object)**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The signal values. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_upload_signal2**
> dict(str, object) amphorae_signals_upload_signal2(id, request_body)

Uploads values to an Amphora signal(s).

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
request_body = None # dict(str, object) | Signal Values.

try:
    # Uploads values to an Amphora signal(s).
    api_response = api_instance.amphorae_signals_upload_signal2(id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_upload_signal2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **request_body** | [**dict(str, object)**](object.md)| Signal Values. | 

### Return type

**dict(str, object)**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The signal values. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_upload_signal_batch**
> dict(str, object) amphorae_signals_upload_signal_batch(id, request_body)

Uploads values in batch to an Amphora signal(s).

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
request_body = None # list[dict(str, object)] | Signal Values.

try:
    # Uploads values in batch to an Amphora signal(s).
    api_response = api_instance.amphorae_signals_upload_signal_batch(id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_upload_signal_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **request_body** | [**list[dict(str, object)]**](dict.md)| Signal Values. | 

### Return type

**dict(str, object)**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of signal values. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_upload_signal_batch2**
> dict(str, object) amphorae_signals_upload_signal_batch2(id, request_body)

Uploads values in batch to an Amphora signal(s).

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
request_body = None # list[dict(str, object)] | Signal Values.

try:
    # Uploads values in batch to an Amphora signal(s).
    api_response = api_instance.amphorae_signals_upload_signal_batch2(id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_upload_signal_batch2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **request_body** | [**list[dict(str, object)]**](dict.md)| Signal Values. | 

### Return type

**dict(str, object)**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of signal values. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_update**
> DetailedAmphora amphorae_update(id, edit_amphora)

Updates the details of an Amphora by Id.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.
edit_amphora = amphora_api_client.EditAmphora() # EditAmphora | Information to update. Nulls are NOT ignored.

try:
    # Updates the details of an Amphora by Id.
    api_response = api_instance.amphorae_update(id, edit_amphora)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **edit_amphora** | [**EditAmphora**](EditAmphora.md)| Information to update. Nulls are NOT ignored. | 

### Return type

[**DetailedAmphora**](DetailedAmphora.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Amphora details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_purchase**
> Response purchases_purchase(id)

Purchases an Amphora as the logged in user.

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
api_instance = amphora_api_client.AmphoraeApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | Amphora Id.

try:
    # Purchases an Amphora as the logged in user.
    api_response = api_instance.purchases_purchase(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->purchases_purchase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Response with a message. |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

