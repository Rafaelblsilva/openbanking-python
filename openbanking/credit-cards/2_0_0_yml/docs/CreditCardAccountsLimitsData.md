# CreditCardAccountsLimitsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_line_limit_type** | [**EnumCreditCardAccountsLineLimitType**](EnumCreditCardAccountsLineLimitType.md) |  | 
**consolidation_type** | [**EnumCreditCardAccountsConsolidationType**](EnumCreditCardAccountsConsolidationType.md) |  | 
**identification_number** | **str** | Número de identificação do cartão: corresponde aos 4 últimos dígitos do cartão para PF, ou então, preencher com um identificador para PJ, com as caracteristicas definidas para os IDs no Open Banking.  | 
**line_name** | **str** |  | [optional] 
**line_name_additional_info** | **str** | Campo de preenchimento obrigatório se selecionada a opção &#x27;OUTRAS&#x27; em lineName. | [optional] 
**is_limit_flexible** | **bool** | Indica se a operação de crédito é: com limite flexível (true) ou com limite (false). | 
**limit_amount** | [**CreditCardsLimitAmount**](CreditCardsLimitAmount.md) |  | [optional] 
**used_amount** | [**CreditCardsUsedAmount**](CreditCardsUsedAmount.md) |  | 
**available_amount** | [**CreditCardsAvailableAmount**](CreditCardsAvailableAmount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

