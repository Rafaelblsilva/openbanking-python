# GetRiskPensionContractData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant** | [**Participant**](Participant.md) |  | 
**society** | [**GetRiskPensionContractDataSociety**](GetRiskPensionContractDataSociety.md) |  | 
**name** | **str** | Nome comercial do produto, pelo qual é identificado nos canais de distribuição e atendimento da sociedade. | 
**code** | **str** | Código único a ser definido pela sociedade. | 
**modality** | [**EnumProductModality**](EnumProductModality.md) |  | [optional] 
**coverages** | [**list[Coverage]**](Coverage.md) |  | 
**assistance_types** | [**list[EnumAssistanceType]**](EnumAssistanceType.md) |  | 
**assistance_types_additional_infos** | **list[str]** | Lista a ser preenchida pelas participantes quando houver &#x27;Outros&#x27; no campo &#x27;Tipo de Assistência&#x27;. | [optional] 
**additionals** | [**list[EnumAdditional]**](EnumAdditional.md) |  | 
**terms_and_conditions** | [**list[TermsAndConditions]**](TermsAndConditions.md) |  | 
**pmbac_remuneration** | [**InsurancePensionEnumPmbacRemuneration**](InsurancePensionEnumPmbacRemuneration.md) |  | [optional] 
**age_adjustment** | [**AgeAdjustment**](AgeAdjustment.md) |  | [optional] 
**financial_regime_contract_types** | [**list[InsurancePensionEnumFinancialRegime]**](InsurancePensionEnumFinancialRegime.md) |  | [optional] 
**reclaim** | [**InsurancePensionReclaim**](InsurancePensionReclaim.md) |  | [optional] 
**other_guaranteed_values** | **list[str]** |  | [optional] 
**indemnity_payment_methods** | **list[str]** |  | [optional] 
**minimum_requirement** | [**RiskPensionMinimumRequirement**](RiskPensionMinimumRequirement.md) |  | [optional] 
**target_audience** | [**EnumTargetAudience**](EnumTargetAudience.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

