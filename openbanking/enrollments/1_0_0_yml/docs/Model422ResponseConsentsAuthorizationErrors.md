# Model422ResponseConsentsAuthorizationErrors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Códigos de erros previstos:  • STATUS_VINCULO_INVALIDO: O vínculo de conta não possui status AUTHORISED.  • STATUS_CONSENTIMENTO_INVALIDO: O consentimento de pagamentos não possui status AWAITING_AUTHORISATION.  • RISCO: Validação síncrona dos sinais de risco impediram a ativação do consentimento.                    • FALTAM_SINAIS_OBRIGATORIOS_DA_PLATAFORMA: Os sinais obrigatórios para a plataforma do usuário não foram enviados em sua totalidade.  | 
**title** | **str** | Título específico do erro reportado, de acordo com o código enviado:  • STATUS_VINCULO_INVALIDO: Status do vínculo de conta inválido.  • STATUS_CONSENTIMENTO_INVALIDO: Status do consentimento inválido.  • RISCO: Validação síncrona dos sinais de risco impediram a ativação do consentimento.  • FALTAM_SINAIS_OBRIGATORIOS_DA_PLATAFORMA: Falta de sinais obrigatórios para a plataforma do usuário.  | 
**detail** | **str** | Descrição específica do erro de acordo com o código reportado:  • STATUS_VINCULO_INVALIDO: O vínculo de conta não possui status AUTHORISED.  • STATUS_CONSENTIMENTO_INVALIDO: O consentimento de pagamentos não possui status AWAITING_AUTHORISATION.  • RISCO: Validação síncrona dos sinais de risco impediram a ativação do consentimento.  • FALTAM_SINAIS_OBRIGATORIOS_DA_PLATAFORMA: Os sinais obrigatórios para a plataforma do usuário não foram enviados em sua totalidade.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

