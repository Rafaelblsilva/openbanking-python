# ResponsePaymentConsentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_id** | **str** | Identificador único do consentimento criado para a iniciação de pagamento solicitada.  | 
**creation_date_time** | **datetime** | Data e hora em que o consentimento foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). | 
**status_update_date_time** | **datetime** | Data e hora em que o recurso foi atualizado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).  | 
**status** | **str** | Retorna o estado do consentimento, o qual no momento de sua criação será AWAITING_AUTHORISATION. Este estado será alterado depois da autorização do consentimento na detentora da conta do pagador (Debtor) para AUTHORISED ou REJECTED.  O consentimento fica no estado CONSUMED após ocorrer a iniciação do pagamento referente ao consentimento.   Em caso de consentimento expirado a detentora deverá retornar o status REJECTED.   Estados possíveis:   AWAITING_AUTHORISATION - Aguardando autorização   AUTHORISED - Autorizado    REJECTED - Rejeitado   CONSUMED - Consumido   | 
**creditor** | [**Identification**](Identification.md) |  | 
**payment** | [**PaymentConsent**](PaymentConsent.md) |  | 
**debtor_account** | [**DebtorAccount**](DebtorAccount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

