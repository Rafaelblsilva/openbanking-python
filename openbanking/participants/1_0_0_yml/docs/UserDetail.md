# UserDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**super_user** | **bool** | Is the user a super user | [optional] 
**system_user** | **bool** | Is the user a system user | [optional] 
**basic_information** | [**UserDetailBasicInformation**](UserDetailBasicInformation.md) |  | [optional] 
**org_access_details** | [**dict(str, OrgAccessDetail)**](OrgAccessDetail.md) | Map Key - Org ID, Map Value - Org Access Detail(contaning info about org admin and domain role details) | [optional] 
**directory_terms_and_conditions_details** | [**TermsAndConditionsDetails**](TermsAndConditionsDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

