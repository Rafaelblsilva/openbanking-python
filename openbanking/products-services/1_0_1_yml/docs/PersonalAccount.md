# PersonalAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AccountType**](AccountType.md) |  | 
**fees** | [**AccountFee**](AccountFee.md) |  | 
**service_bundles** | [**list[ServiceBundle]**](ServiceBundle.md) | Lista dos Pacotes de serviços | 
**opening_closing_channels** | [**list[OpeningClosingChannels]**](OpeningClosingChannels.md) | Lista dos canais para aberturas e encerramento | 
**additional_info** | **str** | Texto livre para complementar informação relativa ao Canal disponível, quando no campo &#x27;&#x27;openingClosingChannels&#x27;&#x27; estiver preenchida a opção &#x27;&#x27;Outros&#x27;&#x27; Restrição: Campo de preenchimento obrigatório se &#x27;&#x27;openingCloseChannels&#x27;&#x27; estiver preenchida a opção &#x27;&#x27;OUTROS&#x27;&#x27;  | [optional] 
**transaction_methods** | [**list[TransactionMethods]**](TransactionMethods.md) | Lista de formas de movimentação | 
**terms_conditions** | [**AccountsTermsConditions**](AccountsTermsConditions.md) |  | 
**income_rate** | [**AccountsIncomeRate**](AccountsIncomeRate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

