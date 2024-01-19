# GetSurvivalPensionContractData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant** | [**PensionParticipant**](PensionParticipant.md) |  | 
**society** | [**PensionSociety**](PensionSociety.md) |  | [optional] 
**name** | **str** | Nome comercial do produto, pelo qual é identificado nos canais de distribuição e atendimento da sociedade.  | 
**code** | **str** | Código único a ser definido pela sociedade.  | 
**segment** | **str** | Segmento do qual se trata o produto contratado 1. Seguro de Pessoas 2. Previdência 3. NA  | 
**modality** | **str** | 1. Contribuição Variável; 2. Benefício Definido. 3. NA  | 
**additional_info** | **str** | Campo aberto (possibilidade de incluir URL) | [optional] 
**terms_and_conditions** | [**list[TermsAndConditions]**](TermsAndConditions.md) |  | [optional] 
**type** | [**SurvivalPensionType**](SurvivalPensionType.md) |  | [optional] 
**defferal_period** | [**SurvivalPensionDefferalPeriod**](SurvivalPensionDefferalPeriod.md) |  | 
**grant_period_benefit** | [**SurvivalPensionGrantPeriodBenefit**](SurvivalPensionGrantPeriodBenefit.md) |  | 
**costs** | [**SurvivalPensionCosts**](SurvivalPensionCosts.md) |  | 
**minimum_requirement** | [**SurvivalPensionMinimumRequirements**](SurvivalPensionMinimumRequirements.md) |  | [optional] 
**target_audience** | [**SurvivalPensionEnumTargetAudience**](SurvivalPensionEnumTargetAudience.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

