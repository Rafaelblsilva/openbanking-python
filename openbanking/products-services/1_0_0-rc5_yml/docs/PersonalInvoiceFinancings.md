# PersonalInvoiceFinancings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Modalidades de direitos creditórios descontados ofertados para pessoas naturais, conforme Circular 4015-Bacen. Direito creditório descontado é a antecipação de créditos relativos por ex. ao: desconto de duplicatas, desconto de cheques,antecipação de fatura de cartão de crédito | 
**fees** | [**PersonalInvoiceFinancingsFees**](PersonalInvoiceFinancingsFees.md) |  | 
**interest_rates** | [**list[PersonalInvoiceFinancingsInterestRates]**](PersonalInvoiceFinancingsInterestRates.md) | Lista que traz o conjunto de informações necessárias para demonstrar a distribuição de frequências das taxas de juros remuneratórios da Modalidade de crédito. | 
**required_warranties** | [**list[RequiredWarranty]**](RequiredWarranty.md) | Lista das  garantias exigidas | 
**terms_conditions** | **str** | Campo aberto para informar as condições contratuais relativas à Modalidade de Financiamentos para pessoa natural informada. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Endereço eletrônico de acesso ao canal. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

