# FinancingsInstalments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_number_of_instalments** | **str** | Tipo de prazo total do contrato referente à modalidade de crédito informada. | 
**total_number_of_instalments** | **float** | Prazo Total segundo o tipo (dia, semana, mês, ano) referente à Modalidade de Crédito informada.  [Restrição] Obrigatoriamente deve ser preenchido caso o typeNumberOfInstalments seja diferente de SEM_PRAZO_TOTAL.  | [optional] 
**type_contract_remaining** | **str** | Tipo de prazo remanescente do contrato referente à modalidade de crédito informada.  | 
**contract_remaining_number** | **float** | Prazo Remanescente segundo o tipo (dia, semana, mês, ano) referente à Modalidade de Crédito informada.  [Restrição] Obrigatoriamente deve ser preenchido caso o typeContractRemaining seja diferente de SEM_PRAZO_REMANESCENTE.  | [optional] 
**paid_instalments** | **float** | Quantidade de prestações pagas. (No caso de modalidades que não possuam parcelas, o número de prestações é igual a zero) | 
**due_instalments** | **float** | Quantidade de prestações a vencer.  [Restrição] Obrigatório para modalidades que possuam parcelas.  | [optional] 
**past_due_instalments** | **float** | Quantidade de prestações vencidas.  [Restrição] Obrigatório para modalidades que possuam parcelas.  | [optional] 
**balloon_payments** | [**list[FinancingsBalloonPayment]**](FinancingsBalloonPayment.md) | Lista que traz as datas de vencimento e valor das parcelas não regulares do contrato da modalidade de crédito consultada | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

