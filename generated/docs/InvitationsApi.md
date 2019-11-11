# amphora_client.InvitationsApi

All URIs are relative to *https://appsvc19cba94a.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invitations_accept_invitation**](InvitationsApi.md#invitations_accept_invitation) | **POST** /api/invitations/{orgId} | Accepts an invitation sent to me
[**invitations_get_my_invitations**](InvitationsApi.md#invitations_get_my_invitations) | **GET** /api/invitations | Returns all the invitations sent to me
[**invitations_invite_new_user**](InvitationsApi.md#invitations_invite_new_user) | **POST** /api/invitations | Invite a new email address to Amphora Data


# **invitations_accept_invitation**
> AcceptInvitationDto invitations_accept_invitation(org_id, accept_invitation_dto)

Accepts an invitation sent to me

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

# Defining host is optional and default to https://appsvc19cba94a.azurewebsites.net
configuration.host = "https://appsvc19cba94a.azurewebsites.net"
# Create an instance of the API class
api_instance = amphora_client.InvitationsApi(amphora_client.ApiClient(configuration))
org_id = 'org_id_example' # str | Organisation to accept invitation for
accept_invitation_dto = amphora_client.AcceptInvitationDto() # AcceptInvitationDto | Invitation to accept

try:
    # Accepts an invitation sent to me
    api_response = api_instance.invitations_accept_invitation(org_id, accept_invitation_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->invitations_accept_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organisation to accept invitation for | 
 **accept_invitation_dto** | [**AcceptInvitationDto**](AcceptInvitationDto.md)| Invitation to accept | 

### Return type

[**AcceptInvitationDto**](AcceptInvitationDto.md)

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

# **invitations_get_my_invitations**
> file invitations_get_my_invitations()

Returns all the invitations sent to me

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

# Defining host is optional and default to https://appsvc19cba94a.azurewebsites.net
configuration.host = "https://appsvc19cba94a.azurewebsites.net"
# Create an instance of the API class
api_instance = amphora_client.InvitationsApi(amphora_client.ApiClient(configuration))

try:
    # Returns all the invitations sent to me
    api_response = api_instance.invitations_get_my_invitations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->invitations_get_my_invitations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitations_invite_new_user**
> InvitationDto invitations_invite_new_user(invitation_dto)

Invite a new email address to Amphora Data

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

# Defining host is optional and default to https://appsvc19cba94a.azurewebsites.net
configuration.host = "https://appsvc19cba94a.azurewebsites.net"
# Create an instance of the API class
api_instance = amphora_client.InvitationsApi(amphora_client.ApiClient(configuration))
invitation_dto = amphora_client.InvitationDto() # InvitationDto | Invitation details

try:
    # Invite a new email address to Amphora Data
    api_response = api_instance.invitations_invite_new_user(invitation_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->invitations_invite_new_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_dto** | [**InvitationDto**](InvitationDto.md)| Invitation details | 

### Return type

[**InvitationDto**](InvitationDto.md)

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

