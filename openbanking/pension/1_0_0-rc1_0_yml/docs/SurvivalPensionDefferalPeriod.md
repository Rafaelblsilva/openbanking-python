# SurvivalPensionDefferalPeriod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_rate** | **str** | Taxa de juros mensal garantida que remunera o plano durante a fase de diferimento/acumulação. | [optional] 
**update_index** | [**UpdateIndex**](UpdateIndex.md) |  | [optional] 
**other_minimum_performance_garantees** | **str** | Para produtos do tipo PDR e VDR, indicação do índice de ampla divulgação utilizados como garantia mínima de desempenho. | [optional] 
**reversal_financial_results** | **str** | Percentual de reversão de excedente financeiro na concessão. Em %. | [optional] 
**minimum_premiums** | [**list[SurvivalPensionMinimumPremium]**](SurvivalPensionMinimumPremium.md) |  | [optional] 
**premium_payment_methods** | **list[str]** |  | 
**permission_extraordinary_contributions** | **bool** | Se ficam permitidos aportes extraordinários. A considerar os seguintes domínios: 1. true 2. false  | [optional] 
**permission_scheduled_financial_payments** | **bool** | Se ficam permitidos pagamentos financeiros programados. A considerar os seguintes domínios: 1. true 2. false  | [optional] 
**grace_period** | [**SurvivalPensionGracePeriod**](SurvivalPensionGracePeriod.md) |  | [optional] 
**redemption_payment_term** | **int** | Prazo em dias para pagamento do resgate | [optional] 
**portability_payment_term** | **float** | Prazo em dias para pagamento da portabilidade (entre empresas diferentes). | [optional] 
**investment_funds** | [**list[SurvivalPensionInvestmentFund]**](SurvivalPensionInvestmentFund.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

