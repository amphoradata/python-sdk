# amphora_api_client.AmphoraeApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amphorae_access_controls_create_for_organisation**](AmphoraeApi.md#amphorae_access_controls_create_for_organisation) | **POST** /api/amphorae/{id}/AccessControls/ForOrganisation | Creates an Access Control Rule on this Amphora.
[**amphorae_access_controls_create_for_user**](AmphoraeApi.md#amphorae_access_controls_create_for_user) | **POST** /api/amphorae/{id}/AccessControls/ForUser | Creates an Access Control rule on this Amphora.
[**amphorae_access_controls_delete**](AmphoraeApi.md#amphorae_access_controls_delete) | **DELETE** /api/amphorae/{id}/AccessControls/{ruleId} | Deletes an Access Control on this Amphora.
[**amphorae_access_controls_get_organisation_rules**](AmphoraeApi.md#amphorae_access_controls_get_organisation_rules) | **GET** /api/amphorae/{id}/AccessControls/ForOrganisation | Get&#39;s the list of access rules applied to organisations.
[**amphorae_access_controls_get_user_rules**](AmphoraeApi.md#amphorae_access_controls_get_user_rules) | **GET** /api/amphorae/{id}/AccessControls/ForUser | Get&#39;s the list of access rules applied to users.
[**amphorae_create**](AmphoraeApi.md#amphorae_create) | **POST** /api/amphorae | Creates a new empty Amphora in the user&#39;s organisation.
[**amphorae_delete**](AmphoraeApi.md#amphorae_delete) | **DELETE** /api/amphorae/{id} | Deletes an Amphora.
[**amphorae_files_create_file_request**](AmphoraeApi.md#amphorae_files_create_file_request) | **POST** /api/amphorae/{id}/files/{file} | Creates a file. Returns a blob URL to upload to.
[**amphorae_files_delete_file**](AmphoraeApi.md#amphorae_files_delete_file) | **DELETE** /api/amphorae/{id}/files/{file} | Get&#39;s the contents of a file. Returns application/octet-stream.
[**amphorae_files_download_file**](AmphoraeApi.md#amphorae_files_download_file) | **GET** /api/amphorae/{id}/files/{file} | Get&#39;s the contents of a file. Returns application/octet-stream.
[**amphorae_files_list_files**](AmphoraeApi.md#amphorae_files_list_files) | **GET** /api/amphorae/{id}/files | Get&#39;s a list of an Amphora&#39;s files.
[**amphorae_files_write_file_metadata**](AmphoraeApi.md#amphorae_files_write_file_metadata) | **POST** /api/amphorae/{id}/files/{file}/meta | 
[**amphorae_list**](AmphoraeApi.md#amphorae_list) | **GET** /api/amphorae | Gets a list of Amphora for yourself or your org, created or purchased by you (or organisation).
[**amphorae_read**](AmphoraeApi.md#amphorae_read) | **GET** /api/amphorae/{id} | Gets details of an Amphora by Id.
[**amphorae_signals_create_signal**](AmphoraeApi.md#amphorae_signals_create_signal) | **POST** /api/amphorae/{id}/signals | Associates a signal with an Amphora. Signal is created if not existing.
[**amphorae_signals_get_signal**](AmphoraeApi.md#amphorae_signals_get_signal) | **GET** /api/amphorae/{id}/signals/{property} | Get&#39;s the signals associated with an Amphora.
[**amphorae_signals_get_signals**](AmphoraeApi.md#amphorae_signals_get_signals) | **GET** /api/amphorae/{id}/signals | Get&#39;s the signals associated with an Amphora.
[**amphorae_signals_update_signal**](AmphoraeApi.md#amphorae_signals_update_signal) | **PUT** /api/amphorae/{id}/signals/{signalId} | Associates a signal with an Amphora. Signal is created if not existing.
[**amphorae_signals_upload_signal**](AmphoraeApi.md#amphorae_signals_upload_signal) | **POST** /api/amphorae/{id}/signals/values | 
[**amphorae_signals_upload_signal2**](AmphoraeApi.md#amphorae_signals_upload_signal2) | **POST** /api/amphorae/{id}/signalValues | 
[**amphorae_signals_upload_signal_batch**](AmphoraeApi.md#amphorae_signals_upload_signal_batch) | **POST** /api/amphorae/{id}/signals/batchvalues | 
[**amphorae_signals_upload_signal_batch2**](AmphoraeApi.md#amphorae_signals_upload_signal_batch2) | **POST** /api/amphorae/{id}/batchSignalValues | 
[**amphorae_update**](AmphoraeApi.md#amphorae_update) | **PUT** /api/amphorae/{id} | Updates the details of an Amphora by Id.
[**purchases_purchase**](AmphoraeApi.md#purchases_purchase) | **POST** /api/Amphorae/{id}/Purchases | Purchases an Amphora as the logged in user.


# **amphorae_access_controls_create_for_organisation**
> UserAccessRule amphorae_access_controls_create_for_organisation(id, organisation_access_rule, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Creates an Access Control Rule on this Amphora.
    api_response = api_instance.amphorae_access_controls_create_for_organisation(id, organisation_access_rule, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_create_for_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **organisation_access_rule** | [**OrganisationAccessRule**](OrganisationAccessRule.md)| The rule to create. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_access_controls_create_for_user**
> UserAccessRule amphorae_access_controls_create_for_user(id, user_access_rule, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Creates an Access Control rule on this Amphora.
    api_response = api_instance.amphorae_access_controls_create_for_user(id, user_access_rule, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_create_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **user_access_rule** | [**UserAccessRule**](UserAccessRule.md)| The rule to create. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_access_controls_delete**
> file amphorae_access_controls_delete(id, rule_id, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Deletes an Access Control on this Amphora.
    api_response = api_instance.amphorae_access_controls_delete(id, rule_id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **rule_id** | **str**| The Id of the rule to delete. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Empty 200. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_access_controls_get_organisation_rules**
> list[OrganisationAccessRule] amphorae_access_controls_get_organisation_rules(id, x_amphoradata_version=x_amphoradata_version)

Get's the list of access rules applied to organisations.

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Get's the list of access rules applied to organisations.
    api_response = api_instance.amphorae_access_controls_get_organisation_rules(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_get_organisation_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
**200** | A list of rules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_access_controls_get_user_rules**
> list[UserAccessRule] amphorae_access_controls_get_user_rules(id, x_amphoradata_version=x_amphoradata_version)

Get's the list of access rules applied to users.

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Get's the list of access rules applied to users.
    api_response = api_instance.amphorae_access_controls_get_user_rules(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_access_controls_get_user_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_create**
> DetailedAmphora amphorae_create(create_amphora, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Creates a new empty Amphora in the user's organisation.
    api_response = api_instance.amphorae_create(create_amphora, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_amphora** | [**CreateAmphora**](CreateAmphora.md)| Information for the new Amphora. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
> str amphorae_delete(id, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Deletes an Amphora.
    api_response = api_instance.amphorae_delete(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_delete: %s\n" % e)
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

# **amphorae_files_create_file_request**
> UploadResponse amphorae_files_create_file_request(id, file, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Creates a file. Returns a blob URL to upload to.
    api_response = api_instance.amphorae_files_create_file_request(id, file, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_create_file_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **file** | **str**| The name of the file. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_files_delete_file**
> file amphorae_files_delete_file(id, file, x_amphoradata_version=x_amphoradata_version)

Get's the contents of a file. Returns application/octet-stream.

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Get's the contents of a file. Returns application/octet-stream.
    api_response = api_instance.amphorae_files_delete_file(id, file, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **file** | **str**| The name of the file. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 if successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_files_download_file**
> file amphorae_files_download_file(id, file, x_amphoradata_version=x_amphoradata_version)

Get's the contents of a file. Returns application/octet-stream.

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Get's the contents of a file. Returns application/octet-stream.
    api_response = api_instance.amphorae_files_download_file(id, file, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **file** | **str**| The name of the file. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file contents. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_files_list_files**
> list[str] amphorae_files_list_files(id, order_by=order_by, x_amphoradata_version=x_amphoradata_version)

Get's a list of an Amphora's files.

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
order_by = 'order_by_example' # str | Can be alphabetical or lastModified. (optional)
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Get's a list of an Amphora's files.
    api_response = api_instance.amphorae_files_list_files(id, order_by=order_by, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **order_by** | **str**| Can be alphabetical or lastModified. | [optional] 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_files_write_file_metadata**
> dict(str, str) amphorae_files_write_file_metadata(id, file, request_body, x_amphoradata_version=x_amphoradata_version)



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
id = 'id_example' # str | 
file = 'file_example' # str | 
request_body = {'key': 'request_body_example'} # dict(str, str) | 
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    api_response = api_instance.amphorae_files_write_file_metadata(id, file, request_body, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_files_write_file_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **file** | **str**|  | 
 **request_body** | [**dict(str, str)**](str.md)|  | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_list**
> list[DetailedAmphora] amphorae_list(scope=scope, access_type=access_type, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Gets a list of Amphora for yourself or your org, created or purchased by you (or organisation).
    api_response = api_instance.amphorae_list(scope=scope, access_type=access_type, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| &#39;self&#39; or &#39;organisation&#39;. Defaults to self. | [optional] [default to &#39;self&#39;]
 **access_type** | **str**| &#39;created&#39; or &#39;purchased&#39;. Defaults to created. | [optional] [default to &#39;created&#39;]
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
> DetailedAmphora amphorae_read(id, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Gets details of an Amphora by Id.
    api_response = api_instance.amphorae_read(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
> Signal amphorae_signals_create_signal(id, signal, x_amphoradata_version=x_amphoradata_version)

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
signal = amphora_api_client.Signal() # Signal | Signal Details.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Associates a signal with an Amphora. Signal is created if not existing.
    api_response = api_instance.amphorae_signals_create_signal(id, signal, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_create_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **signal** | [**Signal**](Signal.md)| Signal Details. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_get_signal**
> Signal amphorae_signals_get_signal(id, _property, x_amphoradata_version=x_amphoradata_version)

Get's the signals associated with an Amphora.

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Get's the signals associated with an Amphora.
    api_response = api_instance.amphorae_signals_get_signal(id, _property, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_get_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **_property** | **str**| The name or id of the signal property. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
> list[Signal] amphorae_signals_get_signals(id, x_amphoradata_version=x_amphoradata_version)

Get's the signals associated with an Amphora.

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Get's the signals associated with an Amphora.
    api_response = api_instance.amphorae_signals_get_signals(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_get_signals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_update_signal**
> Signal amphorae_signals_update_signal(id, signal_id, update_signal, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Associates a signal with an Amphora. Signal is created if not existing.
    api_response = api_instance.amphorae_signals_update_signal(id, signal_id, update_signal, x_amphoradata_version=x_amphoradata_version)
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
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_upload_signal**
> amphorae_signals_upload_signal(id, request_body, x_amphoradata_version=x_amphoradata_version)



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
id = 'id_example' # str | 
request_body = None # dict(str, object) | 
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    api_instance.amphorae_signals_upload_signal(id, request_body, x_amphoradata_version=x_amphoradata_version)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_upload_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**dict(str, object)**](object.md)|  | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_upload_signal2**
> amphorae_signals_upload_signal2(id, request_body, x_amphoradata_version=x_amphoradata_version)



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
id = 'id_example' # str | 
request_body = None # dict(str, object) | 
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    api_instance.amphorae_signals_upload_signal2(id, request_body, x_amphoradata_version=x_amphoradata_version)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_upload_signal2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**dict(str, object)**](object.md)|  | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_upload_signal_batch**
> amphorae_signals_upload_signal_batch(id, request_body, x_amphoradata_version=x_amphoradata_version)



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
id = 'id_example' # str | 
request_body = None # list[dict(str, object)] | 
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    api_instance.amphorae_signals_upload_signal_batch(id, request_body, x_amphoradata_version=x_amphoradata_version)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_upload_signal_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**list[dict(str, object)]**](dict.md)|  | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_signals_upload_signal_batch2**
> amphorae_signals_upload_signal_batch2(id, request_body, x_amphoradata_version=x_amphoradata_version)



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
id = 'id_example' # str | 
request_body = None # list[dict(str, object)] | 
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    api_instance.amphorae_signals_upload_signal_batch2(id, request_body, x_amphoradata_version=x_amphoradata_version)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_signals_upload_signal_batch2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**list[dict(str, object)]**](dict.md)|  | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amphorae_update**
> DetailedAmphora amphorae_update(id, detailed_amphora, x_amphoradata_version=x_amphoradata_version)

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
detailed_amphora = amphora_api_client.DetailedAmphora() # DetailedAmphora | Information to update. Nulls are NOT ignored.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Updates the details of an Amphora by Id.
    api_response = api_instance.amphorae_update(id, detailed_amphora, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->amphorae_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Amphora Id. | 
 **detailed_amphora** | [**DetailedAmphora**](DetailedAmphora.md)| Information to update. Nulls are NOT ignored. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

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
> str purchases_purchase(id, x_amphoradata_version=x_amphoradata_version)

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
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Purchases an Amphora as the logged in user.
    api_response = api_instance.purchases_purchase(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmphoraeApi->purchases_purchase: %s\n" % e)
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

