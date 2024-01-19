# InvoiceFinancingsContractedWarranty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Moeda referente ao valor da garantia, segundo modelo ISO-4217. p.ex. &#x27;BRL&#x27;. Todos os valores monetários informados estão representados com a moeda vigente do Brasil | 
**warranty_type** | [**EnumWarrantyType**](EnumWarrantyType.md) |  | 
**warranty_sub_type** | [**EnumWarrantySubType**](EnumWarrantySubType.md) |  | 
**warranty_amount** | **str** | Valor original da garantia. Expresso em valor monetário com no mínimo 2 casas e no máximo 4 casas decimais.  [Restrição]  Para casos em que warrantyType for igual a \&quot;GARANTIA_FIDEJUSSORIA\&quot; o valor da garantia corresponde a uma porcentagem do total garantido.  Dessa forma, os casos de garantia fidejussória para os quais não é possível determinar um valor monetário para a garantia devem ser preenchidos com 0.00.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

