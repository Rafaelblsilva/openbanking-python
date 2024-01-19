# AutomaticAutomatic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **str** | Identificador do contrato de transação | 
**amount** | **str** | Valor da transação com 2 casas decimais. | [optional] 
**transaction_limit** | **str** | Valor da transação com 2 casas decimais. | [optional] 
**period** | **str** | Define a periodicidade permitida para realização de transações - DIARIO - SEMANAL - MENSAL - ANUAL  | 
**day_of_month** | **int** | Dia fixo do mês que está prevista a transação.  [Restrição] Campo deve ser enviado quando o campo &#x60;/data/recurringConfiguration/automatic/period&#x60; for igual a MENSAL ou ANUAL.  | [optional] 
**day_of_week** | **str** | Dia da semana que está prevista a transação. - SEGUNDA_FEIRA - TERCA_FEIRA - QUARTA_FEIRA - QUINTA_FEIRA - SEXTA_FEIRA  [Restrição] Campo deve ser enviado quando o campo &#x60;/data/recurringConfiguration/automatic/period&#x60; for igual a SEMANAL.  | [optional] 
**month** | **str** | Mês previstos para ocorrer transações. - JANEIRO - FEVEREIRO - MARCO - ABRIL - MAIO - JUNHO - JULHO - AGOSTO - SETEMBRO - OUTUBRO - NOVEMBRO - DEZEMBRO  [Restrição] Campo deve ser enviado quando o campo &#x60;/data/recurringConfiguration/automatic/period&#x60; for igual a ANUAL  | [optional] 
**contract_debtor** | [**ContractDebtor**](ContractDebtor.md) |  | 
**immediate_payment** | [**ImmediatePayment**](ImmediatePayment.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

