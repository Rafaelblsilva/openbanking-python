# Organisation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organisation_id** | [**OrganisationId**](OrganisationId.md) |  | [optional] 
**status** | **str** | Status of the directory registration of an organisation | [optional] [default to 'Active']
**organisation_name** | **str** | Name of the organisation. | [optional] 
**created_on** | **str** | JSONDatetime of organisation creation. | [optional] 
**legal_entity_name** | **str** | Legal Entity name for the org. Usually the same as org name | [optional] 
**country_of_registration** | **str** | Country of registration for the org | [optional] 
**company_register** | **str** | Legal company register for the country, i.e. Companies House | [optional] 
**registration_number** | **str** | Company registration number from company register i.e. Companies House registration number | [optional] 
**registration_id** | **str** | Registered ID for the organisation i.e. Legal Entity identifier number | [optional] 
**registered_name** | **str** |  | [optional] 
**address_line1** | **str** | Address line 1 | [optional] 
**address_line2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | [optional] 
**postcode** | **str** | Postcode | [optional] 
**country** | **str** | Country | [optional] 
**parent_organisation_reference** | **str** | Parent Organisation Reference | [optional] 
**requires_signing** | **bool** | true - one of the attached tncs has to be signed. false - no tnc present | [optional] 
**tn_c_updated** | **bool** | true - attached tnc has been update. false - no tnc present | [optional] 
**tn_cs_to_be_signed** | [**TnCsToBeSigned**](TnCsToBeSigned.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

