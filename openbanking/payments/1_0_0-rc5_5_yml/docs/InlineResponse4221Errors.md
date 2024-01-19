# InlineResponse4221Errors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Códigos de erros previstos na criação da iniciação de pagamento:   • SALDO_INSUFICIENTE – Esta conta não possui saldo suficiente para realizar o pagamento.   • BENEFICIARIO_INCOMPATIVEL – O beneficiário informado no consentimento não é o mesmo do esperado pelo DICT.   • VALOR_INCOMPATIVEL – O valor informado no consentimento não é o mesmo valor do informado no payload de pagamento.   • VALOR_ACIMA_LIMITE – O valor (ou quantidade de transações) ultrapassa a faixa de limite parametrizada na detentora para permitir a realização de transações pelo cliente.   • VALOR_INVALIDO – O valor enviado não é válido para o QR Code informado.   • COBRANCA_INVALIDA – Validação de expiração, validação de vencimento, Status Válido.   • CONSENTIMENTO_INVALIDO – Consentimento inválido (status não é \&quot;authorised\&quot; ou está expirado).   • JANELA_OPER_INVALIDA – Requisição está fora da janela de funcionamento.   • NAO_INFORMADO – Não informada pela detentora de conta.    | 
**title** | **str** | Título específico do erro reportado, de acordo com o código enviado:   • SALDO_INSUFICIENTE: Saldo insuficiente.   • BENEFICIARIO_INCOMPATIVEL: Beneficiário incompatível.   • VALOR_INCOMPATIVEL: Valor da transação incompatível.   • VALOR_ACIMA_LIMITE: Acima do limite estabelecido.   • VALOR_INVALIDO: Valor inválido.   • COBRANCA_INVALIDA: Cobrança inválida.   • CONSENTIMENTO_INVALIDO: Consentimento inválido.   • JANELA_OPER_INVALIDA: Janela de operação inválida.   • NAO_INFORMADO: Não informado.    | 
**detail** | **str** | Descrição específica do erro de acordo com o código reportado:   • SALDO_INSUFICIENTE: A conta selecionada não possui saldo suficiente para realizar o pagamento.   • BENEFICIARIO_INCOMPATIVEL: O beneficiário informado no consentimento não é o mesmo do esperado pelo DICT.   • VALOR_INCOMPATIVEL: O valor informado no consentimento não é o mesmo valor do informado no payload de pagamento.   • VALOR_ACIMA_LIMITE: O valor (ou quantidade de transações) ultrapassa a faixa de limite parametrizada na detentora para permitir a realização de transações pelo cliente.   • VALOR_INVALIDO: O valor enviado não é válido para o QR Code informado.   • COBRANCA_INVALIDA: Validação de expiração, validação de vencimento ou Status Válido.   • CONSENTIMENTO_INVALIDO: Consentimento inválido (status diferente de \&quot;AUTHORISED\&quot; ou está expirado).   • JANELA_OPER_INVALIDA: Requisição está fora da janela de funcionamento.   • NAO_INFORMADO: Não reportado/identificado pela instituição detentora de conta.    | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
