# CapitalizationBondsProductCapitalizationPeriod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_rate** | **str** | Taxa que remunera a parte da mensalidade destinada a formar o Capital, ou seja, a Provisão Matemática de Resgate, também chamada de saldo de capitalização. Em porcentagem ao mês (% a.m.). | 
**update_index** | [**CapitalizationBondsProductUpdateIndex**](CapitalizationBondsProductUpdateIndex.md) |  | 
**update_index_additional_info** | **str** | Restrição: Campo obrigatório para complementar a informação quando selecionada a opção &#x27;OUTROS&#x27; | [optional] 
**contribution_amount** | [**list[CapitalizationPeriodContributionAmount]**](CapitalizationPeriodContributionAmount.md) |  | 
**early_redemptions** | [**list[CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions]**](CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions.md) |  | 
**redemption_percentage_end_term** | **str** | Percentual mínimo da soma das contribuições efetuadas que poderá ser resgatado ao final da vigência, tendo como condição os pagamentos das parcelas nos respectivos vencimentos. | 
**grace_period_redemption** | **float** | Intervalo de tempo mínimo entre contratação e resgate do direito, em meses. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

