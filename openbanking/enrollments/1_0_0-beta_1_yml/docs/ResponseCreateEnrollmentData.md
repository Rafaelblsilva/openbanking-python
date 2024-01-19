# ResponseCreateEnrollmentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_id** | [**EnrollmentId**](EnrollmentId.md) |  | 
**creation_date_time** | **datetime** | O instante em que o vínculo de conta foi criado no ambiente da detentora. | 
**status** | [**EnumEnrollmentStatus**](EnumEnrollmentStatus.md) |  | 
**status_update_date_time** | **datetime** | O instante em que ocorreu a última alteração de status do vínculo de conta. | 
**permissions** | [**list[EnumEnrollmentPermission]**](EnumEnrollmentPermission.md) |  | 
**expiration_date_time** | **datetime** | O instante de expiração deste vínculo de conta, de acordo com a regulação vigente. | 
**logged_user** | [**LoggedUser**](LoggedUser.md) |  | 
**business_entity** | [**BusinessEntity**](BusinessEntity.md) |  | [optional] 
**debtor_account** | [**DebtorAccount**](DebtorAccount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

