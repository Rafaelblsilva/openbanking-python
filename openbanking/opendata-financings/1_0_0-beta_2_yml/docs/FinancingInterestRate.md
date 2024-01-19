# FinancingInterestRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referential_rate_indexer** | **str** | Tipos de taxas referenciais ou indexadores, conforme Anexo 5: Taxa referencial ou Indexador (Indx), do Documento 3040 | 
**rate** | **str** | Percentual que incide sobre a composição das taxas de juros remuneratórios. (representa uma porcentagem Ex: 0.15 (O valor ao lado representa 15%. O valor &#x27;1 &#x27;representa 100%) A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  | 
**applications** | [**list[ApplicationRate]**](ApplicationRate.md) |  | 
**minimum_rate** | **str** | Percentual mínimo cobrado (taxa efetiva) no mês de referência, para o Financiamento contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%) | 
**maximum_rate** | **str** | Percentual máximo cobrado (taxa efetiva) no mês de referência, para o Financiamento contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

