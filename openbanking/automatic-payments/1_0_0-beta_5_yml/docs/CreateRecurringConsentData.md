# CreateRecurringConsentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logged_user** | [**LoggedUser**](LoggedUser.md) |  | 
**business_entity** | [**BusinessEntity**](BusinessEntity.md) |  | [optional] 
**creditors** | [**Creditors**](Creditors.md) |  | 
**start_date_time** | **datetime** | Data e hora em que o consentimento deve passar a ser válido. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format). | 
**expiration_date_time** | **datetime** | Data e hora em que o consentimento deve deixar de ser válido. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format). | [optional] 
**additional_information** | **str** | Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional no consentimento | [optional] 
**debtor_account** | [**CreateRecurringConsentDataDebtorAccount**](CreateRecurringConsentDataDebtorAccount.md) |  | [optional] 
**recurring_configuration** | **OneOfCreateRecurringConsentDataRecurringConfiguration** | Campo destinado a configuração dos diferentes produtos de pagamentos recorrentes. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

