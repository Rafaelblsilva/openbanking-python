# CreditCardAccountsLimitsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_line_limit_type** | [**EnumCreditCardAccountsLineLimitType**](EnumCreditCardAccountsLineLimitType.md) |  | 
**consolidation_type** | [**EnumCreditCardAccountsConsolidationType**](EnumCreditCardAccountsConsolidationType.md) |  | 
**identification_number** | **str** | Número de identificação do cartão: corresponde aos 4 últimos dígitos do cartão para PF, ou então, preencher com um identificador para PJ, com as caracteristicas definidas para os IDs no Open Banking.  | 
**line_name** | [**EnumCreditCardAccountsLineName**](EnumCreditCardAccountsLineName.md) |  | [optional] 
**line_name_additional_info** | **str** | Campo de preenchimento obrigatório se selecionada a opção &#x27;OUTRAS&#x27; em lineName. | [optional] 
**is_limit_flexible** | **bool** | Indica se a operação de crédito é: com limite flexível (true) ou com limite (false). | 
**limit_amount_currency** | **str** | Moeda referente ao limite informado, segundo modelo ISO-4217. p.ex. &#x27;BRL.&#x27; Todos os limite informados estão representados com a moeda vigente do do Brasil.  | 
**limit_amount** | **float** | Valor total do limite informado Expresso em valor monetário com 4 casas decimais. | 
**used_amount_currency** | **str** | Moeda referente ao limite informado, segundo modelo ISO-4217. p.ex. &#x27;BRL.&#x27; Todos os saldos informados estão representados com a moeda vigente do Brasil.  | 
**used_amount** | **float** | Valor utilizado do limite informado Expresso em valor monetário com 4 casas decimais. | 
**available_amount_currency** | **str** | Moeda referente ao limite informado, segundo modelo ISO-4217. p.ex. &#x27;BRL.&#x27; Todos os saldos informados estão representados com a moeda vigente do Brasil.  | 
**available_amount** | **float** | Valor disponível do limite informado Expresso em valor monetário com 4 casas decimais. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

