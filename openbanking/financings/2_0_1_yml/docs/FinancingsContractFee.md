# FinancingsContractFee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_name** | **str** | Denominação da Tarifa pactuada | 
**fee_code** | **str** | Sigla identificadora da tarifa pactuada | 
**fee_charge_type** | **str** | Tipo de cobrança para a tarifa pactuada no contrato. | 
**fee_charge** | **str** | \&quot;Forma de cobrança relativa a tarifa pactuada no contrato. (Vide Enum) - Mínimo - Máximo - Fixo - Percentual\&quot;  | 
**fee_amount** | **str** | Valor monetário da tarifa pactuada no contrato.   [Restrição] Preenchimento obrigatório quando a forma de cobrança for diferente de Percentual.  | [optional] 
**fee_rate** | **str** | É o valor da tarifa em percentual pactuada no contrato.  [Restrição] Preenchimento obrigatório quando a forma de cobrança for Percentual.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

