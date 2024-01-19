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
**pre_fixed_rate** | **str** | Taxa de remuneração acordada com o cliente na contratação. Em casos de produtos progressivos, considerar taxa vigente.  p.ex. 0.014500. O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%).  [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver &#x27;PRE_FIXADO&#x27; no campo &#x27;indexer&#x27; ou quando se tratar de produto com remuneração híbrida.  | [optional] 
**post_fixed_indexer_percentage** | **str** | Percentual do indexador acordado com o  cliente na contratação. Em casos de produtos progressivos, considerar taxa vigente.  p.ex. 0.014500. O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%).  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;indexer&#x27; for preenchido de forma diferente de &#x27;PRE_FIXADO&#x27; ou quando se tratar de produto com remuneração híbrida.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

