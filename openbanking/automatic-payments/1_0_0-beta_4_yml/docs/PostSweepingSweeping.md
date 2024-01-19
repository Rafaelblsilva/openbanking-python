# PostSweepingSweeping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Valor máximo a ser atingido pelo somatório de todas as transações que utilizam o consentimento autorizado pelo cliente. Caso o valor seja superado, a detentora de conta deve negar a transação solicitada pela iniciadora. | [optional] 
**transaction_limit** | **str** | Valor máximo para cada transação de pagamento associada a esse consentimento. Caso valor do pagamento seja maior que esse limite, a detentora de contas deve rejeitar a transação de pagamento. | [optional] 
**periodic_limits** | [**PeriodicLimits**](PeriodicLimits.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

