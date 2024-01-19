# ResponseCreditFixedIncomesTransactionsCurrentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Type**](Type.md) |  | 
**transaction_type** | [**TransactionType**](TransactionType.md) |  | 
**type_additional_info** | **str** | Informação adicional do tipo de movimentação, para preenchimento no caso de movimentações não delimitadas no domínio.          [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver &#x27;OUTROS&#x27; no campo &#x27;transactionType&#x27;.  | [optional] 
**transaction_date** | **date** | Data da movimentação | 
**transaction_unit_price** | [**ResponseCreditFixedIncomesTransactionsCurrentTransactionUnitPrice**](ResponseCreditFixedIncomesTransactionsCurrentTransactionUnitPrice.md) |  | 
**transaction_quantity** | **str** | Quantidade de títulos envolvidos na movimentação | 
**transaction_gross_value** | [**TransactionGrossValue**](TransactionGrossValue.md) |  | 
**income_tax** | [**ResponseCreditFixedIncomesTransactionsCurrentIncomeTax**](ResponseCreditFixedIncomesTransactionsCurrentIncomeTax.md) |  | [optional] 
**financial_transaction_tax** | [**ResponseCreditFixedIncomesTransactionsCurrentFinancialTransactionTax**](ResponseCreditFixedIncomesTransactionsCurrentFinancialTransactionTax.md) |  | [optional] 
**transaction_net_value** | [**TransactionNetValue**](TransactionNetValue.md) |  | 
**remuneration_transaction_rate** | [**RemunerationTransactionRate**](RemunerationTransactionRate.md) |  | [optional] 
**indexer_percentage** | **str** | Percentual máximo do indexador na transação acordado com o cliente na contratação.      [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;type&#x27; for preenchido com o valor &#x27;ENTRADA&#x27;.  | [optional] 
**transaction_id** | **str** | Código ou identificador único prestado pela instituição para individualizar o movimento.    | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

