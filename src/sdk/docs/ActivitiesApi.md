# amphora_api_client.ActivitiesApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activities_create_activity**](ActivitiesApi.md#activities_create_activity) | **POST** /api/activities | Creates a new activity.
[**activities_delete_activity**](ActivitiesApi.md#activities_delete_activity) | **DELETE** /api/activities/{id} | Deletes an activity.
[**activities_read_activity**](ActivitiesApi.md#activities_read_activity) | **GET** /api/activities/{id} | Gets the metadata of an activity.
[**activities_reference_amphora**](ActivitiesApi.md#activities_reference_amphora) | **PUT** /api/activities/{id}/Runs/{runId}/amphorae/{amphoraId} | References an Amphora during a run.
[**activities_start_run**](ActivitiesApi.md#activities_start_run) | **POST** /api/activities/{id}/Runs | Starts a new run of an activity.
[**activities_update_run**](ActivitiesApi.md#activities_update_run) | **POST** /api/activities/{id}/Runs/{runId} | Updates and completes a run.


# **activities_create_activity**
> Activity activities_create_activity(create_activity, x_amphoradata_version=x_amphoradata_version)

Creates a new activity.

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
api_instance = amphora_api_client.ActivitiesApi(amphora_api_client.ApiClient(configuration))
create_activity = amphora_api_client.CreateActivity() # CreateActivity | Metadata of the new activity.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Creates a new activity.
    api_response = api_instance.activities_create_activity(create_activity, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->activities_create_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_activity** | [**CreateActivity**](CreateActivity.md)| Metadata of the new activity. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**Activity**](Activity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Activity information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activities_delete_activity**
> file activities_delete_activity(id, x_amphoradata_version=x_amphoradata_version)

Deletes an activity.

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
api_instance = amphora_api_client.ActivitiesApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | The activity Id.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Deletes an activity.
    api_response = api_instance.activities_delete_activity(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->activities_delete_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The activity Id. | 
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
**200** | The Activity information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activities_read_activity**
> Activity activities_read_activity(id, x_amphoradata_version=x_amphoradata_version)

Gets the metadata of an activity.

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
api_instance = amphora_api_client.ActivitiesApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | The activity Id.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Gets the metadata of an activity.
    api_response = api_instance.activities_read_activity(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->activities_read_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The activity Id. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**Activity**](Activity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Activity information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activities_reference_amphora**
> AmphoraReference activities_reference_amphora(id, run_id, amphora_id, amphora_reference, x_amphoradata_version=x_amphoradata_version)

References an Amphora during a run.

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
api_instance = amphora_api_client.ActivitiesApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | The activity Id.
run_id = 'run_id_example' # str | The run Id.
amphora_id = 'amphora_id_example' # str | The Id of the Amphora to reference.
amphora_reference = amphora_api_client.AmphoraReference() # AmphoraReference | Information about the reference.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # References an Amphora during a run.
    api_response = api_instance.activities_reference_amphora(id, run_id, amphora_id, amphora_reference, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->activities_reference_amphora: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The activity Id. | 
 **run_id** | **str**| The run Id. | 
 **amphora_id** | **str**| The Id of the Amphora to reference. | 
 **amphora_reference** | [**AmphoraReference**](AmphoraReference.md)| Information about the reference. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**AmphoraReference**](AmphoraReference.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reference information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activities_start_run**
> Run activities_start_run(id, x_amphoradata_version=x_amphoradata_version)

Starts a new run of an activity.

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
api_instance = amphora_api_client.ActivitiesApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | The activity id in which to start a run.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Starts a new run of an activity.
    api_response = api_instance.activities_start_run(id, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->activities_start_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The activity id in which to start a run. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**Run**](Run.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Run information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activities_update_run**
> Run activities_update_run(id, run_id, update_run, x_amphoradata_version=x_amphoradata_version)

Updates and completes a run.

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
api_instance = amphora_api_client.ActivitiesApi(amphora_api_client.ApiClient(configuration))
id = 'id_example' # str | The activity Id.
run_id = 'run_id_example' # str | The run Id.
update_run = amphora_api_client.UpdateRun() # UpdateRun | Information about the update.
x_amphoradata_version = 'x_amphoradata_version_example' # str | API Version Number (optional)

try:
    # Updates and completes a run.
    api_response = api_instance.activities_update_run(id, run_id, update_run, x_amphoradata_version=x_amphoradata_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->activities_update_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The activity Id. | 
 **run_id** | **str**| The run Id. | 
 **update_run** | [**UpdateRun**](UpdateRun.md)| Information about the update. | 
 **x_amphoradata_version** | **str**| API Version Number | [optional] 

### Return type

[**Run**](Run.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Activity information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

