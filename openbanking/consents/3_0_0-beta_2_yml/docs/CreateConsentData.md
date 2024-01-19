# CreateConsentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logged_user** | [**LoggedUser**](LoggedUser.md) |  | 
**business_entity** | [**BusinessEntity**](BusinessEntity.md) |  | [optional] 
**permissions** | **list[str]** |  | 
**expiration_date_time** | **datetime** | Data e hora de expiração da permissão. Reflete a data limite de validade do consentimento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC (UTC time format).   [Restrição] De preenchimento obrigatório nos casos em que houver validade determinada. Em casos de consentimento com prazo indeterminado o campo não deve ser enviado.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

