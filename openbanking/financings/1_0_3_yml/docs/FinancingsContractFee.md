# FinancingsContractFee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_name** | **str** | Denominação da Tarifa pactuada | 
**fee_code** | **str** | Sigla identificadora da tarifa pactuada | 
**fee_charge_type** | **str** | Tipo de cobrança para a tarifa pactuada no contrato. | 
**fee_charge** | **str** | \&quot;Forma de cobrança relativa a tarifa pactuada no contrato. (Vide Enum) - Mínimo - Máximo - Fixo - Percentual\&quot;  | 
**fee_amount** | **float** | \&quot;Valor monetário da tarifa pactuada no contrato. Preenchimento obrigatório quando a forma de cobrança for: Mínimo, Máximo ou Fixo\&quot;  | 
**fee_rate** | **float** | É o valor da tarifa em percentual pactuada no contrato.  [Restrição] Preenchimento obrigatório quando a forma de cobrança for Percentual. Exemplo: 0.0150 &#x3D; 1,5%.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

