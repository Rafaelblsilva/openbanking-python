# ResponsePixPaymentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | Código ou identificador único informado pela instituição detentora da conta para representar a iniciação de pagamento individual. O &#x60;paymentId&#x60; deve ser diferente do &#x60;endToEndId&#x60;. Este é o identificador que deverá ser utilizado na consulta ao status da iniciação de pagamento efetuada.  | 
**end_to_end_id** | [**EndToEndId**](EndToEndId.md) |  | 
**consent_id** | **str** | Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
**creation_date_time** | **datetime** | Data e hora em que o recurso foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).  | 
**status_update_date_time** | **datetime** | Data e hora da última atualização da iniciação de pagamento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).  | 
**proxy** | **str** | Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória. No caso de telefone celular deve ser informado no padrão E.1641. Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres. No caso de CPF deverá ser informado com 11 números, sem pontos ou traços. Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços. No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223. Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT, QRDN ou QRES e validar o campo creditorAccount. Esta validação é opcional caso o localInstrument for igual a INIC. [Restrição] Se localInstrument for igual a MANU, o campo proxy não deve ser preenchido. Se localInstrument for igual INIC, DICT, QRDN ou QRES, o campo proxy deve ser sempre preenchido com a chave Pix.  | [optional] 
**ibge_town_code** | **str** | O campo ibgetowncode no arranjo PIX, tem o mesmo comportamento que o campo codMun descrito no item 1.6.6 do manual do PIX, conforme segue:  1. Caso a informação referente ao município não seja enviada; o PSP do recebedor assumirá que não existem feriados estaduais e municipais no período em questão;  | [optional] 
**status** | [**EnumPaymentStatusType**](EnumPaymentStatusType.md) |  | 
**rejection_reason** | [**RejectionReason**](RejectionReason.md) |  | [optional] 
**local_instrument** | [**EnumLocalInstrument**](EnumLocalInstrument.md) |  | 
**cnpj_initiator** | **str** | CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix. | 
**payment** | [**PaymentPix**](PaymentPix.md) |  | 
**transaction_identification** | **str** | Trata-se de um identificador de transação que deve ser retransmitido intacto pelo PSP do pagador ao gerar a ordem de pagamento.  [Restrição] A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora, caso ele tenha sido enviado na requisição da iniciação do pagamento.  | [optional] 
**remittance_information** | **str** | Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.  | [optional] 
**creditor_account** | [**CreditorAccount**](CreditorAccount.md) |  | 
**cancellation** | [**PixPaymentCancellation**](PixPaymentCancellation.md) |  | [optional] 
**debtor_account** | [**DebtorAccount**](DebtorAccount.md) |  | 
**authorisation_flow** | **str** | Campo condicional utilizado para identificar o fluxo de autorização em que o pagamento foi solicitado.  [Restrição] Se CIBA ou FIDO, preenchimento obrigatório. Caso o campo não esteja presente no payload, subentende-se que o fluxo de autorização utilizado é o HYBRID_FLOW.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

