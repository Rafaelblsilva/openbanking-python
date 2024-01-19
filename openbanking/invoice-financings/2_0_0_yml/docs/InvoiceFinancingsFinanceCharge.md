# InvoiceFinancingsFinanceCharge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_type** | [**EnumContractFinanceChargeType**](EnumContractFinanceChargeType.md) |  | 
**charge_additional_info** | **str** | Campo para informações adicionais.  [Restrição] Obrigatório se selecionada a opção &#x27;OUTROS&#x27; em Tipo de encargo pactuado no contrato.  | [optional] 
**charge_rate** | **str** | Representa o valor do encargo em percentual pactuado no contrato.    O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros  (representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

