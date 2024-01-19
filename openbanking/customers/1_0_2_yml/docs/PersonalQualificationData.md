# PersonalQualificationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_date_time** | **datetime** | Data e hora da atualização do bloco, conforme especificação RFC-3339 | 
**company_cnpj** | **str** | Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica.  Deve-se ter apenas os números do CNPJ, sem máscara  | 
**occupation_code** | [**EnumOccupationMainCodeType**](EnumOccupationMainCodeType.md) |  | 
**occupation_description** | **str** | Campo livre, de preenchimento obrigatório. Traz o código da ocupação ou o descritivo da ocupação, se selecionada a opção &#x27;OUTRO&#x27; | 
**informed_income** | [**PersonalQualificationDataInformedIncome**](PersonalQualificationDataInformedIncome.md) |  | 
**informed_patrimony** | [**PersonalInformedPatrimony**](PersonalInformedPatrimony.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

