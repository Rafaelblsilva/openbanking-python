# Model422ResponseErrorCreateEnrollmentErrors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Códigos de erros previstos na criação do vínculo de conta:  • PERMISSOES_INVALIDAS: As permissões associadas ao vínculo de conta não contêm \&quot;PAYMENTS_INITIATE\&quot;.  • CONTA_INVALIDA: A conta informada inexiste ou não é compatível com o fluxo de não-redirecionamento.  | 
**title** | **str** | Título específico do erro reportado, de acordo com o código enviado:  • PERMISSOES_INVALIDAS: Permissões inválidas.  • CONTA_INVALIDA: Conta inválida.  | 
**detail** | **str** | Descrição específica do erro de acordo com o código reportado:  • PERMISSOES_INVALIDAS: As permissões associadas ao vínculo de conta não contêm \&quot;PAYMENTS_INITIATE\&quot; ou contêm valores não suportados para esta operação.    • CONTA_INVALIDA: A conta informada inexiste ou não é compatível com o fluxo de não-redirecionamento.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

