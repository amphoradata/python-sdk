# Application

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name of your application. Will be shown on the consent page. | [optional] 
**logout_url** | **str** | Gets or sets a url for front channel HTTP logouts. | [optional] 
**allowed_scopes** | **list[str]** | Gets or sets the allowed scopes for the app. openid is not required, and will be automatically included. Options include: [&#39;amphora&#39;, &#39;amphora.purchase&#39;, &#39;profile&#39;, &#39;email&#39;, &#39;web_api&#39;]. | [optional] 
**id** | **str** |  | [optional] 
**locations** | [**list[AppLocation]**](AppLocation.md) | Gets or sets a collection of locations your application will run. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


