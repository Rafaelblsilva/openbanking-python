# ResponseBankFixedIncomesBalancesData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_date_time** | **datetime** | data e hora da última posição consolidada disponível a que se referem os dados transacionais do cliente disponíveis nos canais eletrônicos; Na representação data deve se considerar os minutos e segundos como zero (00:00:00Z). | 
**quantity** | **str** | Quantidade de títulos detidos na data da posição do cliente | 
**updated_unit_price** | [**ResponseBankFixedIncomesBalancesDataUpdatedUnitPrice**](ResponseBankFixedIncomesBalancesDataUpdatedUnitPrice.md) |  | 
**gross_amount** | [**ResponseBankFixedIncomesBalancesDataGrossAmount**](ResponseBankFixedIncomesBalancesDataGrossAmount.md) |  | 
**net_amount** | [**ResponseBankFixedIncomesBalancesDataNetAmount**](ResponseBankFixedIncomesBalancesDataNetAmount.md) |  | 
**income_tax** | [**ResponseBankFixedIncomesBalancesDataIncomeTax**](ResponseBankFixedIncomesBalancesDataIncomeTax.md) |  | 
**financial_transaction_tax** | [**ResponseBankFixedIncomesBalancesDataFinancialTransactionTax**](ResponseBankFixedIncomesBalancesDataFinancialTransactionTax.md) |  | 
**blocked_balance** | [**ResponseBankFixedIncomesBalancesDataBlockedBalance**](ResponseBankFixedIncomesBalancesDataBlockedBalance.md) |  | 
**purchase_unit_price** | [**ResponseBankFixedIncomesBalancesDataPurchaseUnitPrice**](ResponseBankFixedIncomesBalancesDataPurchaseUnitPrice.md) |  | 
**pre_fixed_rate** | **str** | Taxa de remuneração acordada com o cliente na contratação.  Em casos de produtos progressivos, considerar taxa vigente. p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000.  Este valor representa 15%. O valor 1 representa 100%). É esperado que o preenchimento deste campo pelas participantes seja enviado de acordo com o campo preFixedRate do endpoint /investment/{investmentId}.  | [optional] 
**post_fixed_indexer_percentage** | **str** | Percentual do indexador acordado com o cliente na contratação.  Em casos de produtos progressivos, considerar taxa vigente. p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000.  Este valor representa 15%. O valor 1 representa 100%). É esperado que o preenchimento deste campo pelas participantes seja enviado de acordo com o campo postFixedIndexerPercentage do endpoint /investment/{investmentId}.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

