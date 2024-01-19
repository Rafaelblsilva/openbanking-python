# PersonalFinancing

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Modalidades de financiamentos ofertados para pessoas físicas, conforme Circular 4015-Bacen. Segundo cartilha do Bacen: Financiamento é um contrato entre o cliente e uma instituição financeira, mas com, destinação específica como para a aquisição de veículo ou de bem imóvel, que funcionam como garantia para o crédito concedido | 
**fees** | [**list[PersonalFinancingFee]**](PersonalFinancingFee.md) |  | 
**interest_rate** | [**FinancingInterestRate**](FinancingInterestRate.md) |  | 
**required_warranties** | **list[str]** |  | 
**terms_conditions** | **str** | Campo aberto para informar as condições contratuais relativas ao produto ou serviço informado. Pode ser informada a URL referente ao endereço onde constam as condições informadas. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

