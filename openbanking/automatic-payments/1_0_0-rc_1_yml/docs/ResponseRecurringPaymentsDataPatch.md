# ResponseRecurringPaymentsDataPatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurring_payment_id** | **str** | Código ou identificador único informado pela instituição detentora da conta para representar a iniciação de pagamento. O &#x60;recurringPaymentId&#x60; deve ser diferente do &#x60;endToEndId&#x60;.  Este é o identificador que deverá ser utilizado na consulta ao status da iniciação de pagamento efetuada.  | 
**recurring_consent_id** | **str** | Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para &#x60;recurringConsentId&#x60; temos: - o namespace(urn) - o identificador associado ao namespace da instituição transmissora (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  [Restrição] Este campo é de preenchimento obrigatório quando o valor do campo authorisationFlow for igual a FIDO_FLOW.  | [optional] 
**end_to_end_id** | [**EndToEndId**](EndToEndId.md) |  | 
**_date** | **str** | Data em que o recurso foi criado. Uma string com a utilização de timezone UTC(UTC time format). | 
**creation_date_time** | **datetime** | Data e hora em que o pagamento foi criado.  Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339),  sempre com a utilização de timezone UTC(UTC time format).  | 
**status_update_date_time** | **datetime** | Data e hora em que o pagamento teve o status atualizado.  Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339),  sempre com a utilização de timezone UTC(UTC time format).  | 
**ibge_town_code** | **str** | O campo ibgeTownCode no arranjo Pix tem o mesmo comportamento que o campo codMun descrito no item 1.6.6 do manual do Pix.  1. Caso a informação referente ao município não seja enviada, o PSP do recebedor assumirá que não existem feriados estaduais e municipais no período em questão;  | 
**status** | [**EnumPaymentStatusType**](EnumPaymentStatusType.md) |  | 
**rejection_reason** | [**RejectionReason**](RejectionReason.md) |  | [optional] 
**cnpj_initiator** | **str** | CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix. | 
**payment** | [**PaymentPix**](PaymentPix.md) |  | 
**remittance_information** | **str** | Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.  | [optional] 
**creditor_account** | [**CreditorAccount**](CreditorAccount.md) |  | [optional] 
**debtor_account** | [**DebtorAccount**](DebtorAccount.md) |  | [optional] 
**cancellation** | [**PixPaymentCancellation**](PixPaymentCancellation.md) |  | [optional] 
**authorisation_flow** | **str** | Campo condicional utilizado para identificar o fluxo de autorização em que o pagamento foi solicitado.  [Restrição] Se CIBA ou FIDO, preenchimento obrigatório. Caso o campo não esteja presente no payload, subentende-se que o fluxo de autorização utilizado é o HYBRID_FLOW.  | [optional] 
**transaction_identification** | **str** | Trata-se de um identificador de transação que deve ser retransmitido intacto pelo PSP do pagador ao gerar a ordem de pagamento.  Essa informação permitirá ao recebedor identificar e correlacionar a transferência, quando recebida, com a apresentação das instruções ao pagador.  Os caracteres permitidos no contexto do Pix para o campo txid (EMV 62-05) são:Letras minúsculas, de &#x27;a&#x27; a &#x27;z&#x27; Letras maiúsculas, de &#x27;A&#x27; a &#x27;z&#x27; Dígitos decimais, de &#x27;0&#x27; a &#x27;9&#x27;.  | [optional] 
**document** | [**CreateRecurringPixPaymentDataDocument**](CreateRecurringPixPaymentDataDocument.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

