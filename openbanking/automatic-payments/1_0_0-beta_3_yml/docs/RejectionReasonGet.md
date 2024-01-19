# RejectionReasonGet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**EnumRejectionReasonCodeGet**](EnumRejectionReasonCodeGet.md) |  | 
**detail** | **str** | Detalhe sobre o código identificador do motivo de rejeição.  - SALDO_INSUFICIENTE: A conta selecionada não possui saldo suficiente para realizar o pagamento; - VALOR_ACIMA_LIMITE: O valor (ou quantidade de transações) ultrapassa a faixa de limite parametrizada na detentora para permitir a realização de transações pelo cliente; - VALOR_INVALIDO: O valor enviado não é válido;  - NAO_INFORMADO: Não reportado/identificado pela instituição detentora de conta; - PAGAMENTO_DIVERGENTE_CONSENTIMENTO: Dados do pagamento divergentes dos dados do consentimento; - PAGAMENTO_RECUSADO_DETENTORA: [descrição do motivo de recusa]; - PAGAMENTO_RECUSADO_SPI: [código de erro conforme tabela de domínios reason PACS.002]; - CONSENTIMENTO_INVALIDO: Consentimento inválido (status diferente de \&quot;AUTHORISED\&quot; ou está expirado); - FALHA_INFRAESTRUTURA_SPI: Indica uma falha no Sistema de Pagamentos Instantâneos (SPI); - FALHA_INFRAESTRUTURA_ICP: Indica uma falha na Infraestrutura de Chaves Públicas (ICP); - FALHA_INFRAESTRUTURA_PSP_RECEBEDOR: Indica uma falha na infraestrutura do Prestador de Serviço de Pagamento (PSP) que recebe o pagamento; - FALHA_INFRAESTRUTURA_DETENTORA: indica uma falha na infraestrutura da instituição detentora das informações ou recursos;  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

