# Model422ResponseErrorPatchConsentErrors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**EnumErrorsPatchConsent**](EnumErrorsPatchConsent.md) |  | 
**title** | **str** | Título específico do erro reportado, de acordo com o código enviado:   • INFORMACAO_USUARIO_REQUERIDA: Informação do usuário requerida.   • OPERACAO_NAO_PERMITIDA_STATUS: Operação não permitida.   • OPERACAO_NAO_SUPORTADA_TIPO_CONSENTIMENTO: Operação não permitida.   • TEMPO_LIMITE_REVOGACAO_EXCEDIDO: Prazo limite para revogação excedido.   • MOTIVO_REVOGACAO_NAO_PERMITIDO: Motivo de revogação não permitido.   • INFORMACAO_ADICIONAL_REVOGACAO_REQUERIDA: Informação adicional requerida.  | 
**detail** | **str** | Descrição específica do erro de acordo com o código reportado:   • INFORMACAO_USUARIO_REQUERIDA: Informação do usuário requerida.   • OPERACAO_NAO_PERMITIDA_STATUS: Operação não permitida devido ao status atual do consentimento.   • OPERACAO_NAO_SUPORTADA_TIPO_CONSENTIMENTO: Operação não suportada pelo tipo de consentimento.   • TEMPO_LIMITE_REVOGACAO_EXCEDIDO: Prazo limite para revogação excedido.   • MOTIVO_REVOGACAO_NAO_PERMITIDO: Motivo de revogação não permitido.   • INFORMACAO_ADICIONAL_REVOGACAO_REQUERIDA: Informação adicional requerida.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

