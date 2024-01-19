# CreditCardAccountsBillsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill_id** | **str** | Informação que identifica a fatura | 
**due_date** | **date** | Data de vencimento da Fatura, que aparece para pagamento pelo cliente | 
**bill_total_amount** | [**CreditCardsBillTotalAmount**](CreditCardsBillTotalAmount.md) |  | 
**bill_minimum_amount** | [**CreditCardAccountsBillMinimumAmount**](CreditCardAccountsBillMinimumAmount.md) |  | 
**is_instalment** | **bool** | Indica se a fatura permite parcelamento (true) ou não (false). | 
**finance_charges** | [**list[CreditCardAccountsBillsFinanceCharge]**](CreditCardAccountsBillsFinanceCharge.md) | Lista dos encargos cobrados na fatura | [optional] 
**payments** | [**list[CreditCardAccountsBillsPayment]**](CreditCardAccountsBillsPayment.md) | Lista que traz os valores relativos aos pagamentos da Fatura da conta de pagamento pós-paga | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

