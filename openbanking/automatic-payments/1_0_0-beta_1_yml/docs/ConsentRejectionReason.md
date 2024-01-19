# ConsentRejectionReason

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Código indicador do motivo de rejeição. - NAO_INFORMADO - FALHA_INFRAESTRUTURA - TEMPO_EXPIRADO_AUTORIZACAO - REJEITADO_USUARIO - CONTAS_ORIGEM_DESTINO_IGUAIS - CONTA_NAO_PERMITE_PAGAMENTO - SALDO_INSUFICIENTE - VALOR_ACIMA_LIMITE  | 
**detail** | **str** | Detalhe sobre o motivo de rejeição indicado no campo &#x60;/data/rejection/reason/code&#x60; - NAO_INFORMADO: Não informada pela detentora de conta; - FALHA_INFRAESTRUTURA: [Descrição de qual falha na infraestrutura inviabilizou o processamento]; - TEMPO_EXPIRADO_AUTORIZACAO: Consentimento expirou antes que o usuário pudesse confirmá-lo; - REJEITADO_USUARIO: O usuário rejeitou a autorização do consentimento; - CONTAS_ORIGEM_DESTINO_IGUAIS: A conta selecionada é igual à conta destino e não permite realizar esse pagamento; - CONTA_NAO_PERMITE_PAGAMENTO: A conta selecionada é do tipo [salario/investimento/liquidação/outros] e não permite realizar esse pagamento; - SALDO_INSUFICIENTE: A conta selecionada não possui saldo suficiente para realizar o pagamento; - VALOR_ACIMA_LIMITE: O valor ultrapassa o limite estabelecido para permitir a realização de transações pelo cliente;  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

