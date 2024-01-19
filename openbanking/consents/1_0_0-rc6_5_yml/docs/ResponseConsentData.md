# ResponseConsentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_id** | **str** | Identificador único do consentimento. | 
**creation_date_time** | **datetime** | Data e hora em que o recurso foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). | 
**status** | **str** | Estado atual do consentimento cadastrado. | 
**status_update_date_time** | **datetime** | Data e hora em que o recurso foi atualizado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). | 
**permissions** | **list[str]** |  | 
**expiration_date_time** | **datetime** | Data e hora de expiração da permissão. Se não for preenchido, a permissão terá a data aberta. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). | [optional] 
**transaction_from_date_time** | **datetime** | Data e hora da transação inicial. Se não for preenchido, a transação terá a data aberta e a data será retornada com a primeira transação disponível. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). | [optional] 
**transaction_to_date_time** | **datetime** | Data e hora final da transação. Se não for preenchido, a transação terá a data aberta e a data será retornada com a ultima transação disponível. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

