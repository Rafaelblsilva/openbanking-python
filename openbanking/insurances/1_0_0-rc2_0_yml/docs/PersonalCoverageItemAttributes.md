# PersonalCoverageItemAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indemnity_payment_methods** | **list[str]** | Listagem da forma de pagamento da indenização para cada combinação de modalidade/cobertura do produto. | 
**indemnity_payment_frequencies** | [**list[EnumPersonalIndemnityPaymentFrequencyType]**](EnumPersonalIndemnityPaymentFrequencyType.md) | Listagem de tipos de frequência de pagamento de indenização para cada combinação de modalidade/cobertura do produto. | 
**min_value** | [**InsurancePensionMinValue**](InsurancePensionMinValue.md) |  | 
**max_value** | [**InsurancePensionMaxValue**](InsurancePensionMaxValue.md) |  | 
**indemnifiable_periods** | **list[str]** | Listagem de período indenizável para cada combinação de modalidade/cobertura do produto. | 
**maximum_qty_indemnifiable_installments** | **int** | Caso o período indenizável seja relacionado a parcelas, listagem de número máximo de parcelas indenizáveis para cada combinação de modalidade/ cobertura do produto. | 
**grace_period** | [**PersonalInsuranceGracePeriod**](PersonalInsuranceGracePeriod.md) |  | 
**differentiated_grace_period** | **str** | Campo aberto para detalhamento de período de carência diferenciado, se houver. | [optional] 
**deductible_days** | **int** | Listagem de franquia em dias para cada combinação de modalidade/cobertura do produto. | 
**differentiated_deductible_days** | **int** | Detalhamento da franquia em dias diferentes para cada cobertura que exista alguma especificidade. Caso a seguradora não tenha essa diferenciação, não retornará nada no campo. | [optional] 
**deductible** | [**PersonalCoverageItemAttributesDeductible**](PersonalCoverageItemAttributesDeductible.md) |  | 
**differentiated_deductible** | [**PersonalCoverageItemAttributesDifferentiatedDeductible**](PersonalCoverageItemAttributesDifferentiatedDeductible.md) |  | [optional] 
**excluded_risks** | [**list[EnumExcludedRisks]**](EnumExcludedRisks.md) |  | 
**excluded_risks_url** | **str** | Campo aberto (possibilidade de incluir URL) | [optional] 
**allow_apart_purchase** | **bool** | Indicar se a cobertura pode ser contratada isoladamente ou não:   1. true   2. false  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

