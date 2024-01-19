# CreateRecurringPixPaymentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurring_consent_id** | **str** | Identificador único do consentimento de longa duração criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name.  Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.  Considerando a string urn:bancoex:C1DD33123 como exemplo para &#x60;recurringConsentId&#x60; temos: - o namespace(urn) - o identificador associado ao namespace da instituição transmissora (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  [Restrição] Este campo é de preenchimento obrigatório quando o valor do campo authorisationFlow for igual a FIDO_FLOW.  | [optional] 
**end_to_end_id** | [**EndToEndId**](EndToEndId.md) |  | 
**_date** | **date** | Data em que o recurso foi criado. Uma string com a utilização de timezone UTC(UTC time format).  | 
**payment** | [**PaymentPix**](PaymentPix.md) |  | 
**creditor_account** | [**CreditorAccountPost**](CreditorAccountPost.md) |  | [optional] 
**remittance_information** | **str** | Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.  | [optional] 
**cnpj_initiator** | **str** | CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix. | 
**ibge_town_code** | **str** | O campo ibgeTownCode no arranjo Pix tem o mesmo comportamento que o campo codMun descrito no item 1.6.6 do manual do Pix.  Caso a informação referente ao município não seja enviada, o PSP do recebedor assumirá que não existem feriados estaduais e municipais no período em questão;  | 
**authorisation_flow** | **str** | Campo condicional utilizado para identificar o fluxo de autorização em que o pagamento foi solicitado.  [Restrição] Se CIBA ou FIDO, preenchimento obrigatório. Caso o campo não esteja presente no payload, subentende-se que o fluxo de autorização utilizado é o HYBRID_FLOW.  | [optional] 
**risk_signals** | [**RiskSignalsPayments**](RiskSignalsPayments.md) |  | [optional] 
**local_instrument** | **str** | Especifica a forma de iniciação do pagamento - MANU - Inserção manual de dados da conta transacional - DICT - Inserção manual de chave Pix - INIC - Indica que o recebedor (creditor) contratou o Iniciador de Pagamentos especificamente para realizar iniciações de pagamento em que o beneficiário é previamente conhecido  | 
**proxy** | **str** | Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória.  No caso de telefone celular deve ser informado no padrão E.1641. Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres.  No caso de CPF deverá ser informado com 11 números, sem pontos ou traços. Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços.  No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na [RFC4122](https://tools.ietf.org/html/rfc4122).  Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT e validar o campo creditorAccount.  Esta validação é opcional caso o localInstrument for igual a INIC.  [Restrição] Se localInstrument for igual a DICT, o campo proxy deve ser preenchido.  | [optional] 
**transaction_identification** | **str** | Trata-se de um identificador de transação que deve ser retransmitido intacto pelo PSP do pagador ao gerar a ordem de pagamento.  Essa informação permitirá ao recebedor identificar e correlacionar a transferência, quando recebida, com a apresentação das instruções ao pagador.  Os caracteres permitidos no contexto do Pix para o campo txid (EMV 62-05) são:Letras minúsculas, de &#x27;a&#x27; a &#x27;z&#x27; Letras maiúsculas, de &#x27;A&#x27; a &#x27;z&#x27; Dígitos decimais, de &#x27;0&#x27; a &#x27;9&#x27;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
