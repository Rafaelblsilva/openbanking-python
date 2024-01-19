# InlineResponse4221Errors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Códigos de erros previstos na criação da iniciação de pagamento.   • 01 – Saldo insuficiente;   • 02 – Beneficiário incompatível;   • 03 – Valor da transação incompatível;   • 04 – Acima do limite estabelecido;   • 05 – Valor inválido;   • 06 – Cobrança inválida;   • 07 – Consentimento inválido;   • 10 – Janela de operação inválida;      • 99 – Desconhecido.    | 
**title** | **str** | Título específico do erro reportado, de acordo com o código enviado:   • 01: Saldo insuficiente;   • 02: Beneficiário incompatível;   • 03: Valor da transação incompatível;   • 04: Acima do limite estabelecido;   • 05: Valor inválido;   • 06: Cobrança inválida;   • 07: Consentimento inválido;   • 10: Janela de operação inválida;      • 99: Desconhecido.    | 
**detail** | **str** | Descrição específica do erro de acordo com o código reportado.   • 01: A conta selecionada não possui saldo suficiente para realizar o pagamento.   • 02: O beneficiário informado no consentimento não é o mesmo do esperado pelo DICT.   • 03: O valor informado no consentimento não é o mesmo valor do informado no payload de pagamento.     • 04: O valor (ou quantidade de transações) ultrapassa a faixa de limite parametrizada na detentora para permitir a realização de transações pelo cliente.   • 05: O valor enviado não é válido para o QR Code informado.   • 06: Validação de expiração, validação de vencimento ou Status Válido.   • 07: Consentimento inválido (status diferente de \&quot;AUTHORISED\&quot; ou está expirado).   • 10: Requisição está fora da janela de funcionamento.         • 99: Não informada pela instituição detentora da conta.   | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

