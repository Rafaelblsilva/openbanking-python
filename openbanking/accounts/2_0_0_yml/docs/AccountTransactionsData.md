# AccountTransactionsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Código ou identificador único prestado pela instituição que mantém a conta para representar a transação individual. | [optional] 
**completed_authorised_payment_type** | [**EnumCompletedAuthorisedPaymentIndicator**](EnumCompletedAuthorisedPaymentIndicator.md) |  | 
**credit_debit_type** | [**EnumCreditDebitIndicator**](EnumCreditDebitIndicator.md) |  | 
**transaction_name** | **str** | Campo livre que corresponde ao identificador da transação na instituição financeira | 
**type** | [**EnumTransactionTypes**](EnumTransactionTypes.md) |  | 
**transaction_amount** | [**AccountTransactionsDataAmount**](AccountTransactionsDataAmount.md) |  | 
**transaction_date** | **str** | Se indicador de transação: TRANSACAO_EFETIVADA - corresponde a data de lançamento da transação LANCAMENTO_FUTURO - corresponde a data prevista de efetivação da transação  | 
**partie_cnpj_cpf** | **str** | Identificação da pessoa envolvida na transação: pagador ou recebedor (Preencher com o CPF ou CNPJ, sem formatação)  | [optional] 
**partie_person_type** | [**EnumPartiePersonType**](EnumPartiePersonType.md) |  | [optional] 
**partie_compe_code** | **str** | Código identificador atribuído pelo Banco Central do Brasil às instituições participantes do STR (Sistema de Transferência de reservas) referente à pessoa envolvida na transação. O número-código substituiu o antigo código COMPE. Todos os participantes do STR, exceto as Infraestruturas do Mercado Financeiro (IMF) e a Secretaria do Tesouro Nacional, possuem um número-código independentemente de participarem da Centralizadora da Compensação de Cheques (Compe). O campo tem a anotação “n/a” (“não se aplica”) para os participantes do STR aos quais não é atribuído um número-código | [optional] 
**partie_branch_code** | **str** | Código da Agência detentora da conta da pessoa envolvida na transação. (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória) | [optional] 
**partie_number** | **str** | Número da conta da pessoa envolvida na transação | [optional] 
**partie_check_digit** | **str** | Dígito da conta da pessoa envolvida na transação | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

