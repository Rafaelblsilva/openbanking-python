# PersonalInsuranceData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant** | [**Participant**](Participant.md) |  | 
**society** | [**PersonalInsuranceSociety**](PersonalInsuranceSociety.md) |  | 
**name** | **str** | Nome comercial do produto, pelo qual é identificado nos canais de distribuição e atendimento da sociedade. | 
**code** | **str** | Código único a ser definido pela sociedade. | 
**category** | **str** | Indicar a categoria do Produto&amp;#58;&lt;br&gt;&lt;ol&gt;&lt;li&gt;Tradicional&lt;/li&gt;&lt;li&gt;Microsseguro&lt;/li&gt;&lt;/ol&gt; | [optional] 
**modality** | [**EnumProductModality**](EnumProductModality.md) |  | 
**coverages** | [**list[PersonalCoverageItem]**](PersonalCoverageItem.md) |  | 
**assistance_types** | **list[str]** |  | [optional] 
**assistance_types_additional_infos** | **list[str]** | Lista a ser preenchido pelas participantes quando houver ‘Outros’ no campo ‘Tipo de Assistência’ | [optional] 
**additionals** | **list[str]** |  | 
**terms_and_conditions** | [**list[TermsAndConditionsItem]**](TermsAndConditionsItem.md) |  | 
**global_capital** | **bool** | A considerar os seguintes domínios:   1. true   2. false  | 
**terms** | **list[str]** |  | 
**pmbac_remuneration** | [**InsurancePensionEnumPmbacRemuneration**](InsurancePensionEnumPmbacRemuneration.md) |  | [optional] 
**benefit_recalculation** | [**BenefitRecalculation**](BenefitRecalculation.md) |  | [optional] 
**age_adjustment** | [**AgeAdjustment**](AgeAdjustment.md) |  | [optional] 
**financial_regimes** | [**list[InsurancePensionEnumFinancialRegime]**](InsurancePensionEnumFinancialRegime.md) |  | 
**reclaim** | [**PersonalInsuranceReclaim**](PersonalInsuranceReclaim.md) |  | [optional] 
**other_guaranteed_values** | [**list[EnumPersonalInsuranceOtherGuaranteedValues]**](EnumPersonalInsuranceOtherGuaranteedValues.md) |  | [optional] 
**allow_portability** | **bool** | 1. true 2. false  | 
**portability_grace_time** | [**PersonalInsurancePortabilityGraceTime**](PersonalInsurancePortabilityGraceTime.md) |  | [optional] 
**indemnity_payment_methods** | [**list[EnumPersonalInsuranceIndemnityPaymentMethod]**](EnumPersonalInsuranceIndemnityPaymentMethod.md) |  | 
**indemnity_payment_incomes** | [**list[EnumPersonalInsuranceIndemnityPaymentIncome]**](EnumPersonalInsuranceIndemnityPaymentIncome.md) |  | [optional] 
**premium_payment** | [**PersonalInsurancePremiumPayment**](PersonalInsurancePremiumPayment.md) |  | [optional] 
**minimum_requirement** | [**PersonalInsuranceMinimumRequirement**](PersonalInsuranceMinimumRequirement.md) |  | [optional] 
**target_audience** | **str** | A considerar os domínios abaixo:    1. Pessoa Natural   2. Pessoa Jurídica   3. Ambas (Pessoa Natural e Jurídica)  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

