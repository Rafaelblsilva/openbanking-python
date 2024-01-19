# RiskPensionEnumContributionPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contribution_payment_method** | **str** | Forma de pagamento da contribuição.  - CARTAO_CREDITO  - DEBITO_CONTA  - DEBITO_CONTA_POUPANCA  - BOLETO_BANCARIO  - PIX  - TED_DOC  - CONSIGNACAO_FOLHA_PAGAMENTO  - PONTOS_PROGRAMA_BENEFICIO  - OUTROS  - NA  | 
**contribution_payment_method_additional_info** | **str** | Campo livre para preenchimento das informações adicionais referente ao contributionPaymentMethod.  [Restrição] Obrigatório quando &#x27;contributionPaymentMethod&#x27; for igual &#x27;OUTROS&#x27;.   | [optional] 
**contribution_periodicity** | **str** | Periodicidade de pagamento da contribuição. - MENSAL - UNICA - ANUAL - TRIMESTRAL - SEMESTRAL - BIMESTRAL - OUTROS - NA  | 
**contribution_periodicity_additional_info** | **str** | Campo livre para preenchimento das informações adicionais referente ao contributionPaymentMethod.  [Restrição] Obrigatório quando &#x27;contributionPeriodicity&#x27; for igual &#x27;OUTROS&#x27;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

