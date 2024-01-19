# PersonalOtherDocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EnumPersonalOtherDocumentType**](EnumPersonalOtherDocumentType.md) |  | 
**type_additional_info** | **str** | Campo livre de preenchimento obrigatório se selecionada a opção OUTROS tipos de documentos | 
**number** | **str** | Identificação/Número do documento informado | 
**check_digit** | **str** | Dígito verificador do documento informado. De preenchimento obrigatório se o documento informado tiver dígito verificador | 
**additional_info** | **str** | Para documentos em que se aplique o uso do local de emissão o mesmo deve ser enviado mandatoriamente, com a informação de órgão e UF. Exemplo: RG, local de emissão: SSP/RS. [Restrição] Obrigatório quando o Local de Emissão do Documento for relevante.  | [optional] 
**expiration_date** | **date** | Data de validade do documento informado, conforme especificação RFC-3339. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

