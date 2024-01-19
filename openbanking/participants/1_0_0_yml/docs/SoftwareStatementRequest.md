# SoftwareStatementRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_name** | **str** | Software Statement client name | 
**description** | **str** | Software Statement description | [optional] 
**on_behalf_of** | **str** | A reference to fourth party organisation resource on the RTS Directory if the registering Org is acting on behalf of another | [optional] 
**policy_uri** | **str** | The Software Statement compliant policy URI | 
**client_uri** | **str** | The Software Statement compliant client URI | 
**logo_uri** | **str** | The Software Statement compliant logo URI | 
**environment** | **str** | The additional check for software statement, this field can avoid environment checks. | [optional] 
**mode** | **str** | The additional check to see if the environment reflected above is live or test. | [optional] [default to 'Live']
**redirect_uri** | **list[str]** | The Software Statement redirect URIs | 
**terms_of_service_uri** | **str** | The Software Statement terms of service compliant URI | 
**version** | **float** | Software Statement version as provided by the organisation&#x27;s PTC | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

