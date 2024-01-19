# ResponsePaymentConsentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_id** | **str** | Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
**creation_date_time** | **datetime** | Data e hora em que o consentimento foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format). | 
**expiration_date_time** | **datetime** | Data e hora em que o consentimento da iniciação de pagamento expira, devendo ser sempre o creationDateTime mais 5 minutos. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC (UTC time format).  O consentimento é criado com o status AWAITING_AUTHORISATION, e deve assumir o status AUTHORIZED, REJECTED ou CONSUMED antes do tempo de expiração - 5 minutos.   Caso não assuma, o status permanece como AWAITING_AUTHORISATION e será necessária a criação de um novo consentimento.   Para o cenário em que o status assumiu AUTHORISED, o tempo máximo (do token FAPI Hybrid Flow) é de 60 minutos, sem refresh,  e este é o tempo para consumir o consentimento autorizado, mudando seu status para CONSUMED. Não é possível prorrogar este tempo e a criação de um novo consentimento será necessária para os cenários de insucesso.  | 
**status_update_date_time** | **datetime** | Data e hora em que o recurso foi atualizado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).  | 
**status** | **str** | Retorna o estado do consentimento, o qual no momento de sua criação será AWAITING_AUTHORISATION. Este estado será alterado depois da autorização do consentimento na detentora da conta do pagador (Debtor) para AUTHORISED ou REJECTED.  O consentimento fica no estado CONSUMED após ocorrer a iniciação do pagamento referente ao consentimento.   Em caso de consentimento expirado a detentora deverá retornar o status REJECTED.   Estados possíveis:   AWAITING_AUTHORISATION - Aguardando autorização   AUTHORISED - Autorizado    REJECTED - Rejeitado   CONSUMED - Consumido   | 
**logged_user** | [**LoggedUser**](LoggedUser.md) |  | 
**business_entity** | [**BusinessEntity**](BusinessEntity.md) |  | [optional] 
**creditor** | [**Identification**](Identification.md) |  | 
**payment** | [**PaymentConsent**](PaymentConsent.md) |  | 
**debtor_account** | [**DebtorAccount**](DebtorAccount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

