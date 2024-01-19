# ResponseCreditFixedIncomesBalancesData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_date_time** | [**ReferenceDateTime**](ReferenceDateTime.md) |  | 
**updated_unit_price** | [**UpdatedUnitPrice**](UpdatedUnitPrice.md) |  | 
**quantity** | **str** | quantidade de títulos detidos na data da posição do cliente | 
**gross_amount** | [**GrossAmount**](GrossAmount.md) |  | 
**net_amount** | [**NetAmount**](NetAmount.md) |  | 
**income_tax** | [**IncomeTax**](IncomeTax.md) |  | 
**financial_transaction_tax** | [**FinancialTransactionTax**](FinancialTransactionTax.md) |  | 
**blocked_balance** | [**BlockedBalance**](BlockedBalance.md) |  | 
**purchase_unit_price** | [**PurchaseUnitPrice**](PurchaseUnitPrice.md) |  | 
**pre_fixed_rate** | **str** | Taxa de remuneração acordada com o cliente na contratação.  Em casos de produtos progressivos, considerar taxa vigente.  É esperado que o preenchimento deste campo pelas participantes seja enviado de acordo com o campo preFixedRate do endpoint /investment/{investmentId}.  | [optional] 
**post_fixed_indexer_percentage** | [**PostFixedIndexerPercentage**](PostFixedIndexerPercentage.md) |  | [optional] 
**fine** | [**Fine**](Fine.md) |  | [optional] 
**late_payment** | [**LatePayment**](LatePayment.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

