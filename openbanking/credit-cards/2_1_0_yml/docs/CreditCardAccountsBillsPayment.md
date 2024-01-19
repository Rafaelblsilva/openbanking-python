# CreditCardAccountsBillsPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_type** | [**EnumCreditCardAccountsBillingValueType**](EnumCreditCardAccountsBillingValueType.md) |  | 
**payment_date** | **date** | Data efetiva de quando o Pagamento da fatura foi realizado | 
**payment_mode** | [**EnumCreditCardAccountsPaymentMode**](EnumCreditCardAccountsPaymentMode.md) |  | 
**amount** | **str** | Valor pagamento segundo o valueType.   Expresso em valor monetário com no mínimo 2 casas e no máximo 4 casas decimais.    O campo não pode assumir valor negativo por se tratar de um pagamento.  | 
**currency** | **str** | Moeda referente ao valor de pagamento da fatura, segundo modelo ISO-4217. p.ex. &#x27;BRL&#x27; Todos os valores informados estão representados com a moeda vigente do Brasil  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

