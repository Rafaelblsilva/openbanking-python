# BankFixedIncomesProductMovement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EnumBankFixedIncomeMovementType**](EnumBankFixedIncomeMovementType.md) |  | 
**transaction_type** | [**EnumBankFixedIncomeTransactionType**](EnumBankFixedIncomeTransactionType.md) |  | 
**transaction_type_additional_info** | **str** | Informação adicional do tipo de movimentação, para preenchimento no caso de movimentações não delimitadas no domínio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver &#x27;Outros&#x27; no campo Motivo da movimentação.  | [optional] 
**transaction_date** | **date** | Data da movimentação. | 
**transaction_unit_price** | [**BankFixedIncomesProductMovementTransactionUnitPrice**](BankFixedIncomesProductMovementTransactionUnitPrice.md) |  | 
**transaction_quantity** | **str** | Quantidade de títulos envolvidos na movimentação. | 
**transaction_gross_value** | [**BankFixedIncomesProductMovementTransactionGrossValue**](BankFixedIncomesProductMovementTransactionGrossValue.md) |  | 
**income_tax** | [**BankFixedIncomesProductMovementIncomeTax**](BankFixedIncomesProductMovementIncomeTax.md) |  | [optional] 
**financial_transaction_tax** | [**BankFixedIncomesProductMovementFinancialTransactionTax**](BankFixedIncomesProductMovementFinancialTransactionTax.md) |  | [optional] 
**transaction_net_value** | [**BankFixedIncomesProductMovementTransactionNetValue**](BankFixedIncomesProductMovementTransactionNetValue.md) |  | 
**remuneration_transaction_rate** | **str** | Taxa de remuneração da transação.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;type&#x27; for preenchido com o valor &#x27;ENTRADA&#x27;.  | [optional] 
**indexer_percentage** | **str** | Percentual máximo do indexador acordado com o cliente na contratação.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;type&#x27; for preenchido com o valor &#x27;ENTRADA&#x27;.  | [optional] 
**transaction_id** | **str** | Código ou identificador único prestado pela instituição que mantém a representação individual do movimento. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

