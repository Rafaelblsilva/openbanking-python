# ResponseFundsTransactionsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Código ou identificador único prestado pela instituição que mantém a representação individual do movimento na posição do fundo. | 
**type** | [**EnumFundsTransactionsType**](EnumFundsTransactionsType.md) |  | 
**transaction_type** | [**EnumFundsTransactionsTransactionType**](EnumFundsTransactionsTransactionType.md) |  | 
**transaction_type_additional_info** | **str** | Informação adicional do tipo do motivo, para preenchimento no caso de movimentações não delimitadas no domínio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;transactionType&#x27; for preenchido com o valor &#x27;OUTROS&#x27;.  | [optional] 
**transaction_conversion_date** | **date** | Data da conversão da transação de movimentação do fundo de investimento. | 
**transaction_quota_price** | [**ResponseFundsTransactionsDataTransactionQuotaPrice**](ResponseFundsTransactionsDataTransactionQuotaPrice.md) |  | 
**transaction_quota_quantity** | **str** | Número de cotas convertidas na data da movimentação.  | 
**transaction_value** | [**ResponseFundsTransactionsDataTransactionValue**](ResponseFundsTransactionsDataTransactionValue.md) |  | 
**transaction_gross_value** | [**ResponseFundsTransactionsDataTransactionGrossValue**](ResponseFundsTransactionsDataTransactionGrossValue.md) |  | 
**income_tax** | [**ResponseFundsTransactionsDataIncomeTax**](ResponseFundsTransactionsDataIncomeTax.md) |  | [optional] 
**financial_transaction_tax** | [**ResponseFundsTransactionsDataFinancialTransactionTax**](ResponseFundsTransactionsDataFinancialTransactionTax.md) |  | [optional] 
**transaction_exit_fee** | [**ResponseFundsTransactionsDataTransactionExitFee**](ResponseFundsTransactionsDataTransactionExitFee.md) |  | [optional] 
**transaction_net_value** | [**ResponseFundsTransactionsDataTransactionNetValue**](ResponseFundsTransactionsDataTransactionNetValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

