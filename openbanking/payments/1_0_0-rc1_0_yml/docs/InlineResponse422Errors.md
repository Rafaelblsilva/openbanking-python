# InlineResponse422Errors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Códigos de erros previstos na criação de consentimento para a iniciação de pagamentos.   • 01 – Forma de pagamento inválida;   • 02 – Data de pagamento inválida;   • 99 – Desconhecido.    | 
**title** | **str** | Título específico do erro reportado, de acordo com o código enviado:   • 01: Forma de pagamento inválida;   • 02: Data de pagamento inválida;   • 99: Desconhecido.         | 
**detail** | **str** | Descrição específica do erro de acordo com o código reportado. • 01: Meio de pagamento inválido;   • 02: Data de pagamento inválida no contexto, por exemplo, data no passado.   Para pagamentos únicos deve ser informada a data atual, do dia corrente.     • 99: Não informada pela instituição detentora da conta.   | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

