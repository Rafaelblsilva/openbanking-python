# InvoiceFinancingsInstalments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_number_of_instalments** | **str** | Tipo de prazo total do contrato referente à modalidade de crédito informada. | 
**total_number_of_instalments** | **float** | Prazo Total segundo o tipo (dia, semana, mês, ano) referente à Modalidade de Crédito informada. | 
**type_contract_remaining** | **str** | Tipo de prazo remanescente do contrato referente à modalidade de crédito informada.  | 
**contract_remaining_number** | **float** | Prazo Remanescente segundo o tipo (dia, semana, mês, ano) referente à Modalidade de Crédito informada. | 
**paid_instalments** | **float** | Quantidade de prestações pagas. (No caso de modalidades que não possuam parcelas, o número de prestações é igual a zero) | 
**due_instalments** | **float** | Quantidade de prestações a vencer.(No caso de modalidades que não possuam parcelas, o número de prestações é igual a zero) | 
**past_due_instalments** | **float** | Quantidade de prestações vencidas. (No caso de modalidades que não possuam parcelas, o número de prestações é igual a zero) | 
**balloon_payments** | [**list[InvoiceFinancingsBalloonPayment]**](InvoiceFinancingsBalloonPayment.md) | Lista que traz as datas de vencimento e valor das parcelas não regulares do contrato da modalidade de crédito consultada | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

