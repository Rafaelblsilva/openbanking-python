# Model422ResponseErrorCancelEnrollmentErrors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Códigos de erros previstos na criação do vínculo de conta:  • STATUS_INVALIDO: O status do vínculo de conta não permite cancelamento.  • MOTIVO_REJEICAO: A rejeição do vínculo de conta deve estar associada a um motivo de rejeição.  • REJEITADO_OUTRO_SEM_DETALHES: O uso do motivo REJEITADO_OUTRO, deve estar acompanhado de descrição (additionalInformation).  • MOTIVO_REVOGACAO: A revogação do vínculo de conta deve estar associada a um motivo de revogação.  • REVOGADO_OUTRO_SEM_DETALHES: O uso do motivo REVOGADO_OUTRO deve estar acompanhado de descrição (additionalInformation)  | 
**title** | **str** | Título específico do erro reportado, de acordo com o código enviado:  • STATUS_INVALIDO: Status inválido.  • MOTIVO_REJEICAO: Motivo de rejeição não especificado.  • REJEITADO_OUTRO_SEM_DETALHES: O campo additionalInformation é obrigatório.  • MOTIVO_REVOGACAO: Motivo de revogação não especificado.  • REVOGADO_OUTRO_SEM_DETALHES: O campo additionalInformation é obrigatório.  | 
**detail** | **str** | Descrição específica do erro de acordo com o código reportado:  • STATUS_INVALIDO: O status do vínculo de conta não permite cancelamento.  • MOTIVO_REJEICAO: A rejeição do vínculo de conta deve estar associada a um motivo de rejeição.  • REJEITADO_OUTRO_SEM_DETALHES: O uso do motivo REJEITADO_OUTRO, deve estar acompanhado de descrição (additionalInformation).  • MOTIVO_REVOGACAO: A revogação do vínculo de conta deve estar associada a um motivo de revogação.  • REVOGADO_OUTRO_SEM_DETALHES: O uso do motivo REVOGADO_OUTRO deve estar acompanhado de descrição (additionalInformation)  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

