# ResponsePaymentConsentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_id** | **str** | Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
**creation_date_time** | **datetime** | Data e hora em que o consentimento foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). | 
**expiration_date_time** | **datetime** | Data e hora em que o consentimento da iniciação de pagamento expira, devendo ser sempre o creationDateTime mais 5 minutos. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC (UTC time format). O consentimento é criado com o status AWAITING_AUTHORISATION, e deve assumir o status AUTHORIZED ou REJECTED antes do tempo de expiração - 5 minutos. Caso o tempo seja expirado, o status deve assumir REJECTED. Para o cenário em que o status assumiu AUTHORISED, o tempo máximo do expirationDateTime do consentimento deve assumir \&quot;now + 60 minutos\&quot;. Este é o tempo para consumir o consentimento autorizado, mudando seu status para CONSUMED. Não é possível prorrogar este tempo e a criação de um novo consentimento será necessária para os cenários de insucesso. O tempo do expirationDateTime é garantido com os 15 minutos do access token, sendo possível utilizar mais três refresh tokens até totalizar 60 minutos.  | 
**status_update_date_time** | **datetime** | Data e hora em que o recurso foi atualizado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).  | 
**status** | [**EnumAuthorisationStatusType**](EnumAuthorisationStatusType.md) |  | 
**revocation** | [**Revocation**](Revocation.md) |  | [optional] 
**logged_user** | [**LoggedUser**](LoggedUser.md) |  | 
**business_entity** | [**BusinessEntity**](BusinessEntity.md) |  | [optional] 
**creditor** | [**Identification**](Identification.md) |  | 
**payment** | [**PaymentConsent**](PaymentConsent.md) |  | 
**debtor_account** | [**DebtorAccount**](DebtorAccount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

