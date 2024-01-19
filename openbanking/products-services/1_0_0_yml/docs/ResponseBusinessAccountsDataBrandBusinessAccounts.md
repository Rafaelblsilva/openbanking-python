# ResponseBusinessAccountsDataBrandBusinessAccounts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Tipos de contas ofertadas para pessoas jurídicas, conforme Resolução 3.919 do Bacen. | 
**fees** | [**list[ResponseBusinessAccountsDataBrandFees]**](ResponseBusinessAccountsDataBrandFees.md) |  | 
**service_bundles** | [**list[ResponseBusinessAccountsDataBrandServiceBundles]**](ResponseBusinessAccountsDataBrandServiceBundles.md) |  | 
**opening_closing_channels** | **str** | Canais disponíveis para abertura e encerramento de contas | 
**additional_info** | **str** | Texto livre para complementar informação relativa ao Canal disponível, quando no campo &#x27;openingClosingChannels&#x27; estiver preenchida a opção &#x27;Outros&#x27; | [optional] 
**transaction_methods** | **str** | Lista de formas de movimentação possíveis para a conta | 
**terms_conditions** | [**AccountsTermsConditions**](AccountsTermsConditions.md) |  | 
**income_rates** | [**list[ResponseBusinessAccountsDataBrandIncomeRates]**](ResponseBusinessAccountsDataBrandIncomeRates.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

