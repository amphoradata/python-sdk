# amphora_api_client.InvitationsApi

All URIs are relative to *https://app.amphoradata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invitations_accept_invitation**](InvitationsApi.md#invitations_accept_invitation) | **POST** /api/invitations/{orgId} | Accepts or rejects an invitation sent to the user.
[**invitations_invite_new_user**](InvitationsApi.md#invitations_invite_new_user) | **POST** /api/invitations | Invite a new email address to Amphora Data.
[**invitations_read_my_invitations**](InvitationsApi.md#invitations_read_my_invitations) | **GET** /api/invitations | Returns all the invitations sent to me.


# **invitations_accept_invitation**
> HandleInvitation invitations_accept_invitation(org_id, handle_invitation)

Accepts or rejects an invitation sent to the user.

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
api_instance = amphora_api_client.InvitationsApi(amphora_api_client.ApiClient(configuration))
org_id = 'org_id_example' # str | Organisation to accept invitation for.
handle_invitation = amphora_api_client.HandleInvitation() # HandleInvitation | Invitation information to accept or reject.

try:
    # Accepts or rejects an invitation sent to the user.
    api_response = api_instance.invitations_accept_invitation(org_id, handle_invitation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->invitations_accept_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organisation to accept invitation for. | 
 **handle_invitation** | [**HandleInvitation**](HandleInvitation.md)| Invitation information to accept or reject. | 

### Return type

[**HandleInvitation**](HandleInvitation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invitation information that was submitted.  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitations_invite_new_user**
> Invitation invitations_invite_new_user(invitation)

Invite a new email address to Amphora Data.

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
api_instance = amphora_api_client.InvitationsApi(amphora_api_client.ApiClient(configuration))
invitation = amphora_api_client.Invitation() # Invitation | Invitation details.

try:
    # Invite a new email address to Amphora Data.
    api_response = api_instance.invitations_invite_new_user(invitation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->invitations_invite_new_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation** | [**Invitation**](Invitation.md)| Invitation details. | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Invitation Object.  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitations_read_my_invitations**
> list[Invitation] invitations_read_my_invitations()

Returns all the invitations sent to me.

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
api_instance = amphora_api_client.InvitationsApi(amphora_api_client.ApiClient(configuration))

try:
    # Returns all the invitations sent to me.
    api_response = api_instance.invitations_read_my_invitations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationsApi->invitations_read_my_invitations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Invitation]**](Invitation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of invitations. |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

