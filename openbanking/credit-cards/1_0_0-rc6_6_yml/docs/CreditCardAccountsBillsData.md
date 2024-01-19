# CreditCardAccountsBillsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill_id** | **str** | Informação que identifica a fatura | 
**due_date** | **date** | Data de vencimento da Fatura, que aparece para pagamento pelo cliente | 
**bill_total_amount** | **float** | Valor total da fatura | 
**bill_total_amount_currency** | **str** | Moeda referente ao valor de pagamento total da fatura, segundo modelo ISO-4217. p.ex. &#x27;BRL&#x27; Todos os valores informados estão representados com a moeda vigente do Brasil | 
**bill_minimum_amount** | **float** | Valor do pagamento minimo da fatura | 
**bill_minimum_amount_currency** | **str** | Moeda referente ao valor de pagamento minimo da fatura, segundo modelo ISO-4217. p.ex. &#x27;BRL&#x27; Todos os valores informados estão representados com a moeda vigente do Brasil | 
**is_instalment** | **bool** | Indica se a fatura permite parcelamento (true) ou não (false). | 
**finance_charges** | [**list[CreditCardAccountsBillsFinanceCharge]**](CreditCardAccountsBillsFinanceCharge.md) | Lista dos encargos cobrados na fatura | 
**payments** | [**list[CreditCardAccountsBillsPayment]**](CreditCardAccountsBillsPayment.md) | Lista que traz os valores relativos aos pagamentos da Fatura da conta de pagamento pós-paga | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

