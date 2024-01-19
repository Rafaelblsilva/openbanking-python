# ResponseVariableIncomesTransactionsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EnumVariableIncomesTransactionsType**](EnumVariableIncomesTransactionsType.md) |  | 
**transaction_type** | [**EnumVariableIncomesTransactionsTransactionType**](EnumVariableIncomesTransactionsTransactionType.md) |  | 
**transaction_type_additional_info** | **str** | Informação adicional do tipo de movimentação, para preenchimento no caso de movimentações não delimitadas no domínio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;transactionType&#x27; for preenchido com o valor &#x27;OUTROS&#x27;.  | [optional] 
**transaction_date** | **date** | Data da movimentação.  [Restrição] Data do pregão: compartilhar movimentos até a data da posição.  | 
**price_factor** | **str** | Fator que indica o número de ações utilizadas para a formação do preço. Valor informado deve ser maior que zero.  | [optional] 
**transaction_unit_price** | [**ResponseVariableIncomesTransactionsDataTransactionUnitPrice**](ResponseVariableIncomesTransactionsDataTransactionUnitPrice.md) |  | [optional] 
**transaction_quantity** | **str** | Quantidade de ativos movimentados.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;transactionType&#x27; for preenchido com os valores &#x27;COMPRA&#x27; ou &#x27;VENDA&#x27;.  | [optional] 
**transaction_value** | [**ResponseVariableIncomesTransactionsDataTransactionValue**](ResponseVariableIncomesTransactionsDataTransactionValue.md) |  | 
**transaction_id** | **str** | Código ou identificador único prestado pela instituição que mantém a representação individual do movimento. | 
**broker_note_id** | **str** | Identificador da nota de negociação.  [Restrição] Informação de envio obrigatório caso o motivo da movimentação seja compra ou venda.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

