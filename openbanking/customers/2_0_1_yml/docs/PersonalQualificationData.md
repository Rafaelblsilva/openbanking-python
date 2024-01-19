# PersonalQualificationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_date_time** | **datetime** | Data e hora da atualização dos campos \\&lt;_endpoint_\\&gt;, conforme especificação RFC-3339, formato UTC. Quando não existente uma data vinculada especificamente ao bloco, assumir a data e hora de atualização do cadastro como um todo.  | 
**company_cnpj** | **str** | Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica.  Deve-se ter apenas os números do CNPJ, sem máscara  | 
**occupation_code** | [**EnumOccupationMainCodeType**](EnumOccupationMainCodeType.md) |  | [optional] 
**occupation_description** | **str** | Campo livre, de preenchimento obrigatório. Se selecionada a opção *occupationCode* \&quot;RECEITA_FEDERAL\&quot; ou \&quot;CBO\&quot;, informar o código desta lista padronizada.    Se selecionada *occupationCode* \&quot;OUTRO\&quot;, informar o descritivo da ocupação quando a IF não segue a lista padronizada da Receita Federal e nem da CBO.  | [optional] 
**informed_income** | [**InformedIncome**](InformedIncome.md) |  | [optional] 
**informed_patrimony** | [**PersonalInformedPatrimony**](PersonalInformedPatrimony.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

