# UnarrangedAccountOverdraftContractedFee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_name** | **str** | Denominação da Tarifa pactuada | 
**fee_code** | **str** | Sigla identificadora da tarifa pactuada | 
**fee_charge_type** | [**EnumContractFeeChargeType**](EnumContractFeeChargeType.md) |  | 
**fee_charge** | [**EnumContractFeeCharge**](EnumContractFeeCharge.md) |  | 
**fee_amount** | **float** | Valor monetário da tarifa pactuada no contrato. Preenchimento obrigatório quando a forma de cobrança for: Mínimo, Máximo ou Fixo.  | 
**fee_rate** | **float** | É o valor da tarifa em percentual pactuada no contrato. Deve-se informar 4 casas decimais, mesmo que preenchidas com zeros. Exemplo: 0.2000 [Restrição] Preenchimento obrigatório quando a forma de cobrança for Percentual. Exemplo: 0.0150 &#x3D; 1,5%.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

