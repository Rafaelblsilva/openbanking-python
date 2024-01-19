# LoansContractInterestRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_type** | [**EnumContractTaxType**](EnumContractTaxType.md) |  | 
**interest_rate_type** | [**EnumContractInterestRateType**](EnumContractInterestRateType.md) |  | 
**tax_periodicity** | [**EnumContractTaxPeriodicity**](EnumContractTaxPeriodicity.md) |  | 
**calculation** | [**EnumContractCalculation**](EnumContractCalculation.md) |  | 
**referential_rate_indexer_type** | [**EnumContractReferentialRateIndexerType**](EnumContractReferentialRateIndexerType.md) |  | 
**referential_rate_indexer_sub_type** | [**EnumContractReferentialRateIndexerSubType**](EnumContractReferentialRateIndexerSubType.md) |  | [optional] 
**referential_rate_indexer_additional_info** | **str** | Campo livre para complementar a informação relativa ao Tipo de taxa referencial ou indexador. [Restrição] Obrigatório para complementar a informação relativa ao Tipo de taxa referencial ou indexador, quando selecionada o tipo ou subtipo OUTRO.  | [optional] 
**pre_fixed_rate** | **float** | Taxa pré fixada aplicada sob o contrato da modalidade crédito. p.ex. 0.0045. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  | 
**post_fixed_rate** | **float** | Taxa pós fixada aplicada sob o contrato da modalidade crédito. p.ex. 0.0045 .O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  | 
**additional_info** | **str** | Texto com informações adicionais sobre a composição das taxas de juros pactuadas. [Restrição] Caso a instituição não possua a informação para compartilhamento, informar NA.         | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

