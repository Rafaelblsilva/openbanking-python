# Model422ResponseErrorCreateConsentErrors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Códigos de erros previstos na durante o processo de extensão do consentimento:  - DEPENDE_MULTIPLA_ALCADA: Necessário aprovação de múltipla alçada.  - REFRESH_TOKEN_JWT: Refresh token não pode ser expandido.  - ESTADO_CONSENTIMENTO_INVALIDO: Estado inválido do consentimento.  - DATA_EXPIRACAO_INVALIDA: Nova data para expiração do consentimento é inválida.  | 
**title** | **str** | Título específico do erro reportado, de acordo com o código enviado: - DEPENDE_MULTIPLA_ALCADA: Necessário aprovação de múltipla alçada. - REFRESH_TOKEN_JWT: Refresh token não pode ser expandido. - ESTADO_CONSENTIMENTO_INVALIDO: Estado inválido do consentimento. - DATA_EXPIRACAO_INVALIDA: Nova data para expiração do consentimento é inválida.  | 
**detail** | **str** | Título específico do erro reportado, de acordo com o código enviado: - DEPENDE_MULTIPLA_ALCADA: O consentimento informado não pode ser renovado sem redirecionamento porque depende de múltipla alçada para aprovação. - REFRESH_TOKEN_JWT: O consentimento informado não pode ser renovado sem redirecionamento porque está vinculado a um refresh token JWT e não pode ter seu prazo de validade alterado. - ESTADO_CONSENTIMENTO_INVALIDO: O consentimento informado não pode ser renovado sem redirecionamento porque está em um estado que não permite a renovação. - DATA_EXPIRACAO_INVALIDA: O consentimento informado não pode ser renovado pois a nova data de expiração não segue a convenção do ecossistema.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

