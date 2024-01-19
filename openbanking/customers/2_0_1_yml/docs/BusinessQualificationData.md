# BusinessQualificationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_date_time** | **datetime** | Data e hora da atualização dos campos \\&lt;_endpoint_\\&gt;, conforme especificação RFC-3339, formato UTC. Quando não existente uma data vinculada especificamente ao bloco, assumir a data e hora de atualização do cadastro como um todo.  | 
**economic_activities** | [**list[EconomicActivity]**](EconomicActivity.md) | Lista dos demais códigos relativos às demais atividades econômicas da empresa, segundo padrão CNAE (Classificação Nacional de Atividades Econômicas). De preenchimento obrigatório, se houver | [optional] 
**informed_revenue** | [**InformedRevenue**](InformedRevenue.md) |  | [optional] 
**informed_patrimony** | [**BusinessInformedPatrimony**](BusinessInformedPatrimony.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

