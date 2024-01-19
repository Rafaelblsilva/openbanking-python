# CreditCardAccountsTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Código ou identificador único prestado pela instituição que mantém a conta para representar a transação individual. | [optional] 
**identification_number** | **str** | Número de identificação do cartão: corresponde aos 4 últimos dígitos do cartão para PF, ou então, preencher com um identificador para PJ, com as caracteristicas definidas para os IDs no Open Banking.  | 
**line_name** | [**EnumCreditCardAccountsLineName**](EnumCreditCardAccountsLineName.md) |  | [optional] 
**transaction_name** | **str** | Campo de livre preenchimento. Literal usada na instituição financeira para identificar a transação | 
**bill_id** | **str** | Informação que identifica a fatura onde consta a transação informada. | [optional] 
**credit_debit_type** | [**EnumCreditDebitIndicator**](EnumCreditDebitIndicator.md) |  | 
**transaction_type** | [**EnumCreditCardTransactionType**](EnumCreditCardTransactionType.md) |  | 
**transactional_additional_info** | **str** | Campo livre, de preenchimento obrigatório quando selecionado tipo de transação \&quot;OUTROS\&quot; | 
**payment_type** | [**EnumCreditCardAccountsPaymentType**](EnumCreditCardAccountsPaymentType.md) |  | 
**fee_type** | [**EnumCreditCardAccountFee**](EnumCreditCardAccountFee.md) |  | 
**fee_type_additional_info** | **str** | Campo livre, de preenchimento obrigatório quando selecionada tipo de tarifa \&quot;OUTRA\&quot; | 
**other_credits_type** | [**EnumCreditCardAccountsOtherCreditType**](EnumCreditCardAccountsOtherCreditType.md) |  | 
**other_credits_additional_info** | **str** | Campo livre, de preenchimento obrigatório quando selecionado tipo de crédito \&quot;OUTROS\&quot; | 
**charge_identificator** | **str** | Identificador da parcela que está sendo informada. Campo de livre preenchimento | 
**charge_number** | **float** | Quantidade de parcelas | 
**brazilian_amount** | **float** | Valor da transação expresso em valor monetário com 4 casas decimais, em moeda corrente do Brasil | 
**amount** | **float** | Valor da transação efetuada no exterior e convertida em moeda nacional com 4 casas decimais. Expresso em valor monetário com 4 casas decimais | 
**currency** | **str** | Moeda referente ao valor da transação, se a operação foi efetuada em moeda  estrangeira, segundo modelo ISO-4217. Todos os valores informados estão representados com a moeda vigente do Brasil  | 
**transaction_date** | **date** | Data original da transação | 
**bill_post_date** | **date** | Data em que a transação foi inserida na fatura | 
**payee_mcc** | **float** | O MCC ou o código da categoria do estabelecimento comercial. Os MCCs são agrupados segundo suas similaridades. O MCC é usado para classificar o negócio pelo tipo fornecido de bens ou serviços. Os MCCs são atribuídos por tipo de comerciante (por exemplo, um para hotéis, um para lojas de materiais de escritório, etc.) ou por nome de comerciante (por exemplo, 3000 para a United Airlines).  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

