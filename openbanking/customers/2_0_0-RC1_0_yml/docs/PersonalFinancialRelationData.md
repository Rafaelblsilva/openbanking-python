# PersonalFinancialRelationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_date_time** | **datetime** | Data e hora da atualização dos campos \\&lt;_endpoint_\\&gt;, conforme especificação RFC-3339, formato UTC. Quando não existente uma data vinculada especificamente ao bloco, assumir a data e hora de atualização do cadastro como um todo.  | 
**start_date** | **datetime** | Data de início de relacionamento com a Instituição Financeira. Deve trazer o menor valor entre a informação reportada ao BACEN pelo DOC 3040 e CCS. | 
**products_services_type** | [**list[EnumProductServiceType]**](EnumProductServiceType.md) |  | 
**products_services_type_additional_info** | **str** | Informações adicionais do tipo de serviço. [Restrição] Campo obrigatório quando productsServicesType for &#x27;OUTROS&#x27;.  | [optional] 
**procurators** | [**list[PersonalProcurator]**](PersonalProcurator.md) | Lista dos representantes.  [Restrição] De preenchimento obrigatório se houver representante.  | 
**accounts** | [**list[PersonalAccount]**](PersonalAccount.md) | Lista de contas depósito à vista, poupança e pagamento pré-pagas mantidas pelo cliente na instituição transmissora.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

