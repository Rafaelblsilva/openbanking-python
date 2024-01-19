# ResponsePersonalFinancingsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant** | [**Participant**](Participant.md) |  | [optional] 
**type** | **str** | Modalidades de financiamentos ofertados para pessoas naturais, conforme Circular 4015-Bacen. Segundo cartilha do Bacen: Financiamento é um contrato entre o cliente e uma instituição financeira, mas com, destinação específica como para a aquisição de veículo ou de bem imóvel, que funcionam como garantia para o crédito concedido | 
**fees** | [**PersonalFinancingFee**](PersonalFinancingFee.md) |  | 
**interest_rates** | [**list[FinancingInterestRate]**](FinancingInterestRate.md) | Lista que traz o conjunto de informações necessárias para demonstrar a distribuição de frequências das taxas de juros remuneratórios da Modalidade de crédito | 
**required_warranties** | [**list[RequiredWarranty]**](RequiredWarranty.md) |  | 
**terms_conditions** | **str** | Campo aberto para informar as condições contratuais relativas ao produto ou serviço informado. Pode ser informada a URL referente ao endereço onde constam as condições informadas. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

