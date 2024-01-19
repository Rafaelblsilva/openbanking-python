# HomeInsuranceData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant** | [**Participant**](Participant.md) |  | 
**society** | [**Society**](Society.md) |  | 
**name** | **str** | Nome comercial do produto, pelo qual é identificado nos canais de distribuição e atendimento da sociedade. | 
**code** | **str** | Código único a ser definido pela sociedade. | 
**coverages** | [**list[HomeCoverageItem]**](HomeCoverageItem.md) |  | 
**property_characteristics** | [**list[HomePropertyCharacteristics]**](HomePropertyCharacteristics.md) |  | 
**property_postal_code** | **str** | O conjunto de dados de Produtos que vai retornar está condicionado ao input do valor de CEP (Filtro). Nesse contexto será necessário que o CEP de consulta seja inserido. Código de Endereçamento Postal: Composto por um conjunto numérico de oito dígitos, o objetivo principal do CEP é orientar e acelerar o encaminhamento, o tratamento e a entrega de objetos postados nos Correios, por meio da sua atribuição a localidades, logradouros, unidades dos Correios, serviços, órgãos públicos, empresas e edifícios. p.ex. &#x27;01311000&#x27; | [optional] 
**protective** | **bool** | Indicativo de exigência de itens protecionais (por exemplo, alarmes) a considerar os seguintes domínios abaixo:   1. true   2. false  | [optional] 
**additionals** | [**list[EnumInsuranceAdditionalType]**](EnumInsuranceAdditionalType.md) |  | [optional] 
**additional_info** | **str** | Texto livre para complementar informação relativa ao additional, quando for selecionada a opção &#x27;Outros&#x27; | [optional] 
**assistance_services** | [**list[AssistanceServicesItem]**](AssistanceServicesItem.md) |  | [optional] 
**terms_and_conditions** | [**list[TermsAndConditionsItem]**](TermsAndConditionsItem.md) |  | 
**terms** | [**list[EnumInsuranceTermType]**](EnumInsuranceTermType.md) |  | 
**terms_additional_info** | **str** | Texto livre para complementar informação relativa ao campo terms, quando for selecionada a opção &#x27;Outros&#x27; | [optional] 
**customer_service** | [**EnumCustomerServiceType**](EnumCustomerServiceType.md) |  | [optional] 
**premium_payment** | [**PremiumPayment**](PremiumPayment.md) |  | [optional] 
**minimum_requirement** | [**InsuranceMinimumRequirement**](InsuranceMinimumRequirement.md) |  | 
**target_audience** | [**EnumTargetAudience**](EnumTargetAudience.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

