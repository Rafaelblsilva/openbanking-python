# OrganisationAuthorityClaim

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organisation_id** | [**OrganisationId**](OrganisationId.md) |  | [optional] 
**organisation_authority_claim_id** | [**OrganisationAuthorityClaimId**](OrganisationAuthorityClaimId.md) |  | [optional] 
**authority_id** | [**AuthorityId**](AuthorityId.md) |  | [optional] 
**status** | **str** | Is this software statement Active/Inactive | [optional] [default to 'Active']
**authorisation_domain** | **str** | Authorisation Domain for the authority | [optional] 
**role** | **str** | Roles for the Authority i.e. ASPSP, AISP, PISP, CBPII | [optional] 
**authorisations** | [**list[OrganisationAuthorityClaimAuthorisations]**](OrganisationAuthorityClaimAuthorisations.md) |  | [optional] 
**registration_id** | **str** | Registration ID for the organisation | [optional] 
**unique_technical_idenifier** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

