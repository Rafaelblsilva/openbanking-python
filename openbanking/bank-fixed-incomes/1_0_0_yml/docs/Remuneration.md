# Remuneration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_fixed_rate** | **str** | Taxa de remuneração pré fixada de emissão do título.  p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%).    [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver &#x27;PRE_FIXADO&#x27; no campo &#x27;indexer&#x27; ou quando se tratar de produto com remuneração híbrida.  | [optional] 
**post_fixed_indexer_percentage** | **str** | Percentual do indexador pós fixado de emissão do  título.  p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%).  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;indexer&#x27; for preenchido de forma diferente de &#x27;PRE_FIXADO&#x27; ou quando se tratar de produto com remuneração híbrida.  | [optional] 
**rate_type** | [**EnumRateType**](EnumRateType.md) |  | 
**rate_periodicity** | [**EnumRatePeriodicity**](EnumRatePeriodicity.md) |  | 
**calculation** | [**EnumCalculation**](EnumCalculation.md) |  | 
**indexer** | [**EnumBankFixedIncomeIndexer**](EnumBankFixedIncomeIndexer.md) |  | 
**indexer_additional_info** | **str** | Informações adicionais do indexador  [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver &#x27;Outros&#x27; no campo &#x27;indexer&#x27;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

