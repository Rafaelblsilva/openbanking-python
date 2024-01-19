# CustomerPhone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_main** | **bool** | Indica se o telefone informado é o principal | 
**type** | [**EnumCustomerPhoneType**](EnumCustomerPhoneType.md) |  | 
**additional_info** | **str** | Informação complementar relativa ao tipo de telefone selecionado. [Restrição] De preenchimento obrigatório quando selecionado o tipo &#x27;OUTRO&#x27;. | [optional] 
**country_calling_code** | **str** | Número de DDI (Discagem Direta Internacional) para telefone de acesso ao Cliente - se houver  [Restrição] O preenchimento é obrigatório quando for diferente de 55.   | [optional] 
**area_code** | [**EnumAreaCode**](EnumAreaCode.md) |  | 
**number** | **str** | Número de telefone do cliente | 
**phone_extension** | **str** | Número do ramal. De preenchimento obrigatório se fizer parte da identificação do número do telefone informado | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

