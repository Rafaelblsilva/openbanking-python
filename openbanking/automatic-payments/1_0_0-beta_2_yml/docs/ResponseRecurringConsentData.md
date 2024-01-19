# ResponseRecurringConsentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurring_consent_id** | **str** | Identificador único do consentimento de longa duração criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://datatracker.ietf.org/doc/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para &#x60;recurringConsentId&#x60; temos:   - o namespace(urn)   - o identificador associado ao namespace da instituição transmissora (bancoex)   - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://datatracker.ietf.org/doc/html/rfc8141).  | 
**status_update_date_time** | **datetime** | Data e hora em que o consentimento teve o status atualizado. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format).  | 
**logged_user** | [**LoggedUser**](LoggedUser.md) |  | 
**business_entity** | [**BusinessEntity**](BusinessEntity.md) |  | 
**status** | [**EnumAuthorisationStatusType**](EnumAuthorisationStatusType.md) |  | 
**creditors** | [**Creditors**](Creditors.md) |  | 
**start_date_time** | **datetime** | Data e hora em que o consentimento deve passar a ser válido. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format). | 
**creation_date_time** | **datetime** | Data e hora em que o consentimento foi criado. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format). | 
**expiration_date_time** | **datetime** | Data e hora em que o consentimento deve deixar de ser válido. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format). | 
**additional_information** | **str** | Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional no consentimento | [optional] 
**debtor_account** | [**ConsentsDebtorAccount**](ConsentsDebtorAccount.md) |  | [optional] 
**rejection** | [**Rejection**](Rejection.md) |  | [optional] 
**revocation** | [**ResponsePostRecurringConsentDataRevocation**](ResponsePostRecurringConsentDataRevocation.md) |  | [optional] 
**recurring_configuration** | [**RecurringConfiguration**](RecurringConfiguration.md) |  | 
**ibge_town_code** | **str** | Campo utilizado pela iniciadora para cálculo do dia útil de liquidação do pagamento (vide especificação do endToEndId) baseado no munícipio de cadastro do usuário pagador no detentor.  [Restrições] - Campo obrigatório que deverá ser retornado quando o consentimento estiver ou passar pelo status AUTHORISED; - Campo obrigatório quando o oneOf utilizado do recurringConfiguration for “automatic”.  | [optional] 
**risk_signals** | [**RiskSignalsConsents**](RiskSignalsConsents.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

