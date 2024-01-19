# PhoneChannelIdentification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  Tipo de canal telefônico de atendimento:  * &#x60;CENTRAL_TELEFONICA&#x60;  * &#x60;SAC&#x60;  * &#x60;OUVIDORIA&#x60;  * &#x60;OUTROS&#x60; | 
**additional_info** | **str** | Campo de texto livre para descrever informações complementateres sobre canais telefônicos. De preenchimento obrigatório quando o tipo de canal de atendimento telefônico selecionado for \&quot;OUTROS\&quot; | [optional] 
**phones** | [**list[PhoneChannelPhone]**](PhoneChannelPhone.md) | Lista de telefones do Canal de Atendimento | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

