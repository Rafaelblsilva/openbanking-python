# UnarrangedAccountOverdraftRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fees** | [**list[FeeReferentialRateIndexer]**](FeeReferentialRateIndexer.md) | Lista de tipos de taxas referenciais ou indexadores | 
**applications** | [**list[ApplicationRate]**](ApplicationRate.md) | Lista  das faixas de cobrança da taxa efetiva de remuneração. | 
**minimum_rate** | **str** | Percentual mínimo cobrado (taxa efetiva) no mês de referência, para o crédito contratado A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  | 
**maximum_rate** | **str** | Percentual máximo cobrado (taxa efetiva) no mês de referência, para o crédito contratado A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  | 
**customers** | [**list[Customer]**](Customer.md) | Lista percentual de cliente por faixa referente a  taxa remuneratória. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

