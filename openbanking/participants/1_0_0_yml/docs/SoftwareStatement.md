# SoftwareStatement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Is this software statement Active/Inactive | [optional] [default to 'Active']
**client_id** | **str** | Software Statement client Id | [optional] 
**client_name** | **str** | Software Statement client name | [optional] 
**description** | **str** | Software Statement description | [optional] 
**environment** | **str** | The additional check for software statement, this field can avoid | [optional] 
**organisation_id** | [**OrganisationId**](OrganisationId.md) |  | [optional] 
**software_statement_id** | [**SoftwareStatementId**](SoftwareStatementId.md) |  | [optional] 
**mode** | **str** | Software Statement mode | [optional] [default to 'Live']
**rts_client_created** | **bool** | Client created flag | [optional] 
**on_behalf_of** | **str** | A reference to fourth party organisation resource on the RTS Directory if the registering Org is acting on behalf of another | [optional] 
**policy_uri** | **str** | The Software Statement policy compliant URI | [optional] 
**client_uri** | **str** | The Software Statement client compliant URI | [optional] 
**logo_uri** | **str** | The Software Statement logo compliant URI | [optional] 
**redirect_uri** | **list[str]** | The Software Statement redirect compliant URI | [optional] 
**terms_of_service_uri** | **str** | The Software Statement terms of service compliant URI | [optional] 
**version** | **float** | Software Statement version as provided by the organisation&#x27;s PTC | [optional] 
**locked** | **bool** | Flag shows if assertion has been generated on the software statement - will be set to true when assertion is generated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

