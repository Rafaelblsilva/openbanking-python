# CreditCardAccountsTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Código ou identificador único prestado pela instituição que mantém a conta para representar a transação individual.  O ideal é que o &#x60;transactionId&#x60; seja imutável.  No entanto, para casos em que a transação ainda está em processamento, é esperado que o &#x60;transactionId&#x60; intermediário seja estável, mudando apenas quando a transação sofrer uma mudança em seu estado.  Para transações processadas, é esperado que o &#x60;transactionld&#x60; e demais dados da transação sejam imutáveis.  O &#x60;transactionId&#x60; deve obedecer, no mínimo, as regras de imutabilidade propostas conforme a tabela “Data de imutabilidade por tipo de transação” presente nas orientações desta API  | 
**identification_number** | **str** | Número de identificação do cartão: corresponde aos 4 últimos dígitos do cartão para PF, ou então, preencher com um identificador para PJ, com as caracteristicas definidas para os IDs no Open Finance.  | 
**transaction_name** | **str** | Literal usada na instituição financeira para identificar a transação. A informação apresentada precisa ser a mesma utilizada nos canais eletrônicos da instituição (extrato e fatura). | 
**bill_id** | **str** | Informação que identifica a fatura onde consta a transação informada. Preencher apenas para casos de transação em fatura fechada, ou seja, este campo não é esperado em casos de transação em fatura aberta. | [optional] 
**credit_debit_type** | [**EnumCreditDebitIndicator**](EnumCreditDebitIndicator.md) |  | 
**transaction_type** | [**EnumCreditCardTransactionType**](EnumCreditCardTransactionType.md) |  | 
**transactional_additional_info** | **str** | Campo livre, de preenchimento obrigatório quando selecionado tipo de transação \&quot;OUTROS\&quot; | [optional] 
**payment_type** | [**EnumCreditCardAccountsPaymentType**](EnumCreditCardAccountsPaymentType.md) |  | [optional] 
**fee_type** | [**EnumCreditCardAccountFee**](EnumCreditCardAccountFee.md) |  | [optional] 
**fee_type_additional_info** | **str** | Campo livre, de preenchimento obrigatório quando selecionada tipo de tarifa \&quot;OUTRA\&quot; | [optional] 
**other_credits_type** | [**EnumCreditCardAccountsOtherCreditType**](EnumCreditCardAccountsOtherCreditType.md) |  | [optional] 
**other_credits_additional_info** | **str** | Campo livre para preenchimento de dados adicionais de outros tipos de crédito contratados no cartão.  [Restrição] Preenchimento obrigatório quando selecionado no campo outros tipos de crédito \&quot;OUTROS\&quot;.  | [optional] 
**charge_identificator** | **float** | Número da parcela que está sendo informada. | 
**charge_number** | **float** | Quantidade de parcelas.    [Restrição] O campo deve ser preenchido quando houverem parcelas relacionadas a transação.  | [optional] 
**brazilian_amount** | [**CreditCardAccountsTransactionBrazilianAmount**](CreditCardAccountsTransactionBrazilianAmount.md) |  | 
**amount** | [**CreditCardAccountsTransactionAmount**](CreditCardAccountsTransactionAmount.md) |  | 
**transaction_date_time** | **datetime** | Data e hora original da transação.  No primeiro momento, as instituições poderão complementar informações faltantes com 0 (Por exemplo: 2016-01-29T00:00:00.000Z)  A partir de 31/01/2024 é esperado que o campo seja preenchido com informações reais.  | 
**bill_post_date** | **date** | Data em que a transação foi inserida na fatura | 
**payee_mcc** | **float** | O MCC ou o código da categoria do estabelecimento comercial. Os MCCs são agrupados segundo suas similaridades. O MCC é usado para classificar o negócio pelo tipo fornecido de bens ou serviços. Os MCCs são atribuídos por tipo de comerciante (por exemplo, um para hotéis, um para lojas de materiais de escritório, etc.) ou por nome de comerciante (por exemplo, 3000 para a United Airlines).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

