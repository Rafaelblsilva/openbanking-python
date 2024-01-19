# NationalityOtherDocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Tipo de documento. Campo livre, de preenchimento obrigatório quando a nacionalidade for diferente de brasileira. Informar tipo e número do documento, além da, vigência e demais informações complementares para se identificar o documento de pessoa estrangeira | 
**number** | **str** | Número de identificação do documento. Campo livre, de preenchimento obrigatório quando a nacionalidade for diferente de brasileira. Informar o número do documento e demais informações complementares para se identificar o documento de pessoa estrangeira | 
**expiration_date** | **date** | Data de validade do documento informado, conforme especificação RFC-3339. | 
**issue_date** | **date** | Data de emissão do documento, conforme especificação RFC-3339. | 
**country** | **str** | Nome do país | [optional] 
**type_additional_info** | **str** | Campo livre de preenchimento obrigatório se selecionada a opção OUTROS tipos de documentos. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

