# LoanInterestRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fees** | [**list[InterestRateFee]**](InterestRateFee.md) | Lista das taxas referenciais ou indexadores | [optional] 
**applications** | [**list[ApplicationRate]**](ApplicationRate.md) | Lista  das faixas de cobrança da taxa efetiva aplicada pela contratação de crédito | [optional] 
**minimum_rate** | **str** | Percentual mínimo cobrado (taxa efetiva) no mês de referência, para o Empréstimo contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%) | [optional] 
**maximum_rate** | **str** | Percentual máximo cobrado (taxa efetiva) no mês de referência, para o Empréstimo contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

