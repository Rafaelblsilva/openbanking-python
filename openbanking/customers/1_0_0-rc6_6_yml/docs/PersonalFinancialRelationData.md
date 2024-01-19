# PersonalFinancialRelationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_date_time** | **datetime** | Data e hora da atualização do bloco de Relacionamento, conforme especificação RFC-3339, formato UTC. | 
**start_date** | **datetime** | Data de início de relacionamento com a Instituição Financeira. Deve trazer o menor valor entre a informação reportada ao BACEN pelo DOC 3040 e CCS. | 
**products_services_type** | [**list[EnumProductServiceType]**](EnumProductServiceType.md) |  | 
**products_services_type_additional_info** | **str** | Informações adicionais do tipo de serviço. [Restrição] Campo obrigatório quando productsServicesType for &#x27;OUTROS&#x27;.  | [optional] 
**procurators** | [**list[PersonalProcurator]**](PersonalProcurator.md) | Lista dos representantes. De preenchimento obrigatório se houver representante. | 
**accounts** | [**list[PersonalAccount]**](PersonalAccount.md) | Lista de contas depósito à vista, poupança e pagamento pré-pagas mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.      | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

