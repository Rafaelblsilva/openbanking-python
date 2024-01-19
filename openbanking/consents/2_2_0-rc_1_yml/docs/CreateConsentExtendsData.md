# CreateConsentExtendsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_date_time** | **datetime** | Data e hora de expiração da permissão. De preenchimento obrigatório, reflete a data limite de validade do consentimento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). Para consentimentos com prazo indeterminado, preencher com valor &#x27;2300-01-01T00:00:00Z&#x27;. Esse valor deve ser refletido no expirationDateTime do consentimento relacionado. | 
**logged_user** | [**LoggedUserExtends**](LoggedUserExtends.md) |  | 
**business_entity** | [**BusinessEntityExtends**](BusinessEntityExtends.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

