# InlineResponse422Errors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Códigos de erros previstos na criação de consentimento para a iniciação de pagamentos:   • FORMA_PGTO_INVALIDA: Forma de pagamento inválida.   • DATA_PGTO_INVALIDA: Data de pagamento inválida.   • NAO_INFORMADO: Não informado.    | 
**title** | **str** | Título específico do erro reportado, de acordo com o código enviado:   • FORMA_PGTO_INVALIDA: Forma de pagamento inválida.   • DATA_PGTO_INVALIDA: Data de pagamento inválida.   • NAO_INFORMADO: Não informado.      | 
**detail** | **str** | Descrição específica do erro de acordo com o código reportado:   • FORMA_PGTO_INVALIDA – Meio de pagamento inválido.   • DATA_PGTO_INVALIDA – Data de pagamento inválida no contexto, por exemplo, data no passado. Para pagamentos únicos deve ser informada a data atual, do dia corrente.   • NAO_INFORMADO – Não reportado/identificado pela instituição detentora de conta.    | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

