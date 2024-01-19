# InvoiceFinancingsContractedFee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_name** | **str** | Denominação da Tarifa pactuada  | 
**fee_code** | **str** | Sigla identificadora da tarifa pactuada  | 
**fee_charge_type** | [**EnumContractFeeChargeType**](EnumContractFeeChargeType.md) |  | 
**fee_charge** | [**EnumContractFeeCharge**](EnumContractFeeCharge.md) |  | 
**fee_amount** | **str** | Valor monetário da tarifa pactuada no contrato.   [Restrição] Preenchimento obrigatório quando a forma de cobrança for diferente de Percentual.  | [optional] 
**fee_rate** | **str** | É o valor da tarifa em percentual pactuada no contrato.  [Restrição] Preenchimento obrigatório quando a forma de cobrança for Percentual.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

