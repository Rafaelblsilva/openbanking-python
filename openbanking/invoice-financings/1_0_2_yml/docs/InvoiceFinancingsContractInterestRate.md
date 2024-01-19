# InvoiceFinancingsContractInterestRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_type** | **str** | \&quot;Tipo de Taxa (vide  Enum) - NOMINAL (taxa nominal é uma taxa de juros em que a unidade referencial não coincide com a unidade de tempo da capitalização. Ela é sempre fornecida em termos anuais, e seus períodos de capitalização podem ser diários, mensais, trimestrais ou semestrais. p.ex. Uma taxa de 12% ao ano com capitalização mensal) - EFETIVA (É a taxa de juros em que a unidade referencial coincide com a unidade de tempo da capitalização. Como as unidades de medida de tempo da taxa de juros e dos períodos de capitalização são iguais, usa-se exemplos simples como 1% ao mês, 60% ao ano)\&quot;  | 
**interest_rate_type** | [**EnumContractInterestRateType**](EnumContractInterestRateType.md) |  | 
**tax_periodicity** | [**EnumContractTaxPeriodicity**](EnumContractTaxPeriodicity.md) |  | 
**calculation** | [**EnumContractCalculation**](EnumContractCalculation.md) |  | 
**referential_rate_indexer_type** | [**EnumContractReferentialRateIndexerType**](EnumContractReferentialRateIndexerType.md) |  | 
**referential_rate_indexer_sub_type** | [**EnumContractReferentialRateIndexerSubType**](EnumContractReferentialRateIndexerSubType.md) |  | [optional] 
**referential_rate_indexer_additional_info** | **str** | Campo livre para complementar a informação relativa ao Tipo de taxa referencial ou indexador. [Restrição] Obrigatório para complementar a informação relativa ao Tipo de taxa referencial ou indexador, quando selecionada o tipo ou subtipo OUTRO.  | [optional] 
**pre_fixed_rate** | **float** | Taxa pré fixada aplicada sob o contrato da modalidade crédito. p.ex. 0.0045. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  | 
**post_fixed_rate** | **float** | Taxa pós fixada aplicada sob o contrato da modalidade crédito. p.ex. 0.0045 .O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  | 
**additional_info** | **str** | Texto com informações adicionais sobre a composição das taxas de juros pactuadas | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

