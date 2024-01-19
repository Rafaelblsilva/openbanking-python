# AccountTransactionsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Código ou identificador único prestado pela instituição que mantém a conta para representar a transação individual.  O ideal é que o &#x60;transactionId&#x60; seja imutável.  No entanto, o &#x60;transactionId&#x60; deve obedecer, no mínimo, as regras de imutabilidade propostas conforme tabela “Data de imutabilidade por tipo de transação” presente nas orientações desta API.  | 
**completed_authorised_payment_type** | [**EnumCompletedAuthorisedPaymentIndicator**](EnumCompletedAuthorisedPaymentIndicator.md) |  | 
**credit_debit_type** | [**EnumCreditDebitIndicator**](EnumCreditDebitIndicator.md) |  | 
**transaction_name** | **str** | Literal usada na instituição financeira para identificar a transação. A informação apresentada precisa ser a mesma utilizada nos canais eletrônicos da instituição (extrato). | 
**type** | [**EnumTransactionTypes**](EnumTransactionTypes.md) |  | 
**transaction_amount** | [**AccountTransactionsDataAmount**](AccountTransactionsDataAmount.md) |  | 
**transaction_date_time** | **str** | Data e hora original da transação.  | 
**partie_cnpj_cpf** | **str** | Identificação da pessoa envolvida na transação: pagador ou recebedor (Preencher com o CPF ou CNPJ, sem formatação). Com a IN BCB nº 371, a partir de 02/05/23, o envio das informações de identificação de contraparte tornou-se obrigatória para transações de pagamento. Para maiores detalhes, favor consultar a página &#x60;Orientações - Contas&#x60;.  | [optional] 
**partie_person_type** | [**EnumPartiePersonType**](EnumPartiePersonType.md) |  | [optional] 
**partie_compe_code** | **str** | Código identificador atribuído pelo Banco Central do Brasil às instituições participantes do STR (Sistema de Transferência de reservas) referente à pessoa envolvida na transação. O número-código substituiu o antigo código COMPE. Todos os participantes do STR, exceto as Infraestruturas do Mercado Financeiro (IMF) e a Secretaria do Tesouro Nacional, possuem um número-código independentemente de participarem da Centralizadora da Compensação de Cheques (Compe). O campo tem a anotação “n/a” (“não se aplica”) para os participantes do STR aos quais não é atribuído um número-código | [optional] 
**partie_branch_code** | **str** | Código da Agência detentora da conta da pessoa envolvida na transação. (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória) | [optional] 
**partie_number** | **str** | Número da conta da pessoa envolvida na transação | [optional] 
**partie_check_digit** | **str** | Dígito da conta da pessoa envolvida na transação | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

