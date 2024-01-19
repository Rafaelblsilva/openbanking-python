# Model422ResponseErrorFidoSignOptionsErrors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Códigos de erros previstos:  • RP_INVALIDA: O identificador da Relying Party informado não pode ser verificado.  • STATUS_VINCULO_INVALIDO: O status do vínculo de conta é tal que não permite assinatura.   • STATUS_CONSENTIMENTO_INVALIDO: O status do consentimento não permite autorização.  | 
**title** | **str** | Título específico do erro reportado, de acordo com o código enviado:  • RP_INVALIDA: Relying party inválida.  • STATUS_VINCULO_INVALIDO: Status do vínculo de conta inválido.  • STATUS_CONSENTIMENTO_INVALIDO: Status do consentimento de pagamento inválido.  | 
**detail** | **str** | Descrição específica do erro de acordo com o código reportado:  • RP_INVALIDA: O identificador da Relying Party informado não pode ser verificado.  • STATUS_VINCULO_INVALIDO: O status do vínculo de conta é tal que não permite assinatura.   • STATUS_CONSENTIMENTO_INVALIDO: O status do consentimento não permite autorização.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

