# AccountBalancesData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_amount** | [**AccountBalancesDataAvailableAmount**](AccountBalancesDataAvailableAmount.md) |  | 
**blocked_amount** | [**AccountBalancesDataBlockedAmount**](AccountBalancesDataBlockedAmount.md) |  | 
**automatically_invested_amount** | [**AccountBalancesDataAutomaticallyInvestedAmount**](AccountBalancesDataAutomaticallyInvestedAmount.md) |  | 
**update_date_time** | **datetime** | Data e hora da última atualização do saldo. É esperado que a instituição informe a última vez que capturou o saldo para compartilhamento no Open Finance. Dessa forma, é possível que: - Caso a instituição capture dados de forma síncrona essa informação seja de poucos momentos; - Caso a instituição capture dados de forma assíncrona essa informação seja de horas ou dias no passado; - Quando não existente uma data vinculada especificamente ao bloco, se assume a data e hora de atualização do cadastro como um todo.  De toda forma, é preciso continuar respeitando o prazo máximo de tempestividade da API de Contas.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

