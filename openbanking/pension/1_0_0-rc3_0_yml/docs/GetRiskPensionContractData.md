# GetRiskPensionContractData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant** | [**PensionParticipant**](PensionParticipant.md) |  | 
**society** | [**PensionSociety**](PensionSociety.md) |  | 
**name** | **str** | Nome comercial do produto, pelo qual é identificado nos canais de distribuição e atendimento da sociedade. | 
**code** | **str** | Código único a ser definido pela sociedade. | 
**modality** | [**EnumProductModality**](EnumProductModality.md) |  | 
**coverages** | [**list[Coverage]**](Coverage.md) |  | 
**assistance_types** | [**list[EnumAssistanceType]**](EnumAssistanceType.md) |  | [optional] 
**assistance_types_additional_infos** | **list[str]** | Lista a ser preenchida pelas participantes quando houver &#x27;Outros&#x27; no campo &#x27;Tipo de Assistência&#x27;. | [optional] 
**additional** | [**EnumAdditional**](EnumAdditional.md) |  | [optional] 
**terms_and_conditions** | [**list[TermsAndConditions]**](TermsAndConditions.md) |  | 
**pmbac_remuneration** | [**RiskPensionEnumPmbacRemuneration**](RiskPensionEnumPmbacRemuneration.md) |  | [optional] 
**premium_update_index** | [**RiskPensionEnumPremiumUpdateIndex**](RiskPensionEnumPremiumUpdateIndex.md) |  | 
**age_adjustment** | [**AgeAdjustment**](AgeAdjustment.md) |  | [optional] 
**financial_regime_contract_type** | [**RiskPensionEnumFinancialRegime**](RiskPensionEnumFinancialRegime.md) |  | [optional] 
**reclaim** | [**RiskPensionReclaim**](RiskPensionReclaim.md) |  | [optional] 
**other_guaranteed_values** | [**RiskPensionEnumOtherGuaranteedValues**](RiskPensionEnumOtherGuaranteedValues.md) |  | 
**contribution_payment** | [**RiskPensionEnumContributionPayment**](RiskPensionEnumContributionPayment.md) |  | 
**minimum_requirement** | [**RiskPensionMinimumRequirement**](RiskPensionMinimumRequirement.md) |  | 
**target_audience** | **str** | A considerar os domínios abaixo:    1. Pessoa Natural   2. Pessoa Jurídica   3. Ambas (Pessoa Natural e Jurídica)   4. NA  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

