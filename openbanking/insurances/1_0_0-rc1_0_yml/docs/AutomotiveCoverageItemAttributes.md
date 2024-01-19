# AutomotiveCoverageItemAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_lmi** | [**CoverageItemAttributesMinLMI**](CoverageItemAttributesMinLMI.md) |  | [optional] 
**max_lmi** | [**CoverageItemAttributesMaxLMI**](CoverageItemAttributesMaxLMI.md) |  | [optional] 
**new_car** | [**NewCar**](NewCar.md) |  | [optional] 
**full_indemnity_percentage** | **str** | Será caracterizada a indenização integral quando os prejuízos resultantes de um mesmo sinistro, atingirem ou ultrapassarem a quantia apurada a partir da aplicação de percentual previamente determinado sobre o valor contratado. (Circular 269/2004). | [optional] 
**deductible_types** | [**list[EnumCoverageItemDeductibleType]**](EnumCoverageItemDeductibleType.md) | Listagem de tipo de franquia para cada tipo de cobertura do produto. | 
**full_indemnity_deductible** | **bool** | (Circular 269/2004). A considerar os domínios abaixo: 1. true 2. false  | 
**deductible_payment_by_coverage** | **bool** | Mudança do campo com a sinalização para cada cobertura se a seguradora exige pagamento de franquia.  1. true  2. false  | [optional] 
**deductible_percentage** | **str** | Percentual de Franquia | [optional] 
**mandatory_participation** | **str** | Participação Obrigatória é o valor ou percentual definido na apólice referente à responsabilidade do Segurado nos prejuízos indenizáveis decorrentes de sinistros cobertos. (Circular SUSEP 347/07). Listagem de percentual de Franquia/Percentual Participação Obrigatória do Segurado estabelecida pela sociedade para cada tipo de cobertura do  produto.  | [optional] 
**geographic_scope** | [**AutomotiveGeoGraphicScope**](AutomotiveGeoGraphicScope.md) |  | [optional] 
**contract_base** | [**ContractBase**](ContractBase.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

