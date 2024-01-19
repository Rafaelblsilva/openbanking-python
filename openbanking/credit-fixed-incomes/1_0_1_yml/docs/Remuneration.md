# Remuneration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_fixed_rate** | **str** | Valor da taxa de emissão do contrato.          [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver &#x27;PRE_FIXADO&#x27; no campo &#x27;indexer&#x27; ou quando se tratar de produto com remuneração híbrida.  | [optional] 
**post_fixed_indexer_percentage** | **str** | Percentual do indexador de emissão do contrato.     [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;indexer&#x27; for preenchido de forma diferente de &#x27;PRE_FIXADO&#x27; ou quando se tratar de produto com remuneração híbrida.  | [optional] 
**rate_type** | [**EnumRateType**](EnumRateType.md) |  | [optional] 
**rate_periodicity** | [**EnumRatePeriodicity**](EnumRatePeriodicity.md) |  | [optional] 
**calculation** | [**EnumCalculation**](EnumCalculation.md) |  | [optional] 
**indexer** | [**EnumIndexer**](EnumIndexer.md) |  | 
**indexer_additional_info** | **str** | Informações adicionais do indexador   [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver &#x27;Outros&#x27; no campo &#x27;indexer&#x27;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

