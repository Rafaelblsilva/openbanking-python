# BusinessInvoiceFinancingsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant** | [**Participant**](Participant.md) |  | [optional] 
**type** | **str** | Modalidades de direitos creditórios descontados ofertados para pessoas Jurídicas, conforme Circular 4015-Bacen. Direito creditório descontado é a antecipação de créditos relativos por ex. ao: desconto de duplicatas, desconto de cheques,antecipação de fatura de cartão de crédito | 
**fees** | [**InvoiceFinancingsFees**](InvoiceFinancingsFees.md) |  | 
**interest_rates** | [**list[BusinessInvoiceFinancingsInterestRates]**](BusinessInvoiceFinancingsInterestRates.md) | Lista que traz o conjunto de informações necessárias para demonstrar a distribuição de frequências das taxas de juros remuneratórios da Modalidade de crédito | 
**required_warranties** | [**list[RequiredWarranty]**](RequiredWarranty.md) | Lista das  garantias exigidas | 
**terms_conditions** | **str** | Campo aberto para informar as condições contratuais relativas à Modalidade de Financiamentos para pessoa jurídica informada. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Endereço eletrônico de acesso ao canal. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
