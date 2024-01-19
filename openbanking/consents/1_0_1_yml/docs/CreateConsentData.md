# CreateConsentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logged_user** | [**LoggedUser**](LoggedUser.md) |  | 
**business_entity** | [**BusinessEntity**](BusinessEntity.md) |  | [optional] 
**permissions** | **list[str]** |  | 
**expiration_date_time** | **datetime** | Data e hora de expiração da permissão. De preenchimento obrigatório, reflete a data limite de validade do consentimento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). | 
**transaction_from_date_time** | **datetime** | Data e hora da transação inicial. Se não for preenchido, a transação terá a data aberta e a data será retornada com a primeira transação disponível. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). | [optional] 
**transaction_to_date_time** | **datetime** | Data e hora final da transação. Se não for preenchido, a transação terá a data aberta e a data será retornada com a ultima transação disponível. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

