# FinancingsReleases

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | Identificador de pagamento de responsabilidade de cada Instituição transmissora. | [optional] 
**is_over_parcel_payment** | **bool** | Identifica se é um pagamento pactuado (false) ou avulso (true). | 
**instalment_id** | **str** | Identificador de parcela, de responsabilidade de cada Instituição transmissora. | 
**paid_date** | **date** | Data efetiva do pagamento referente ao contrato da modalidade de crédito consultada, conforme especificação RFC-3339. p.ex. 2014-03-19 | 
**currency** | **str** | Moeda referente ao valor monetário informado, segundo modelo ISO-4217. p.ex. &#x27;BRL&#x27;. Todos os valores monetários informados estão representados com a moeda vigente do Brasil.  | 
**paid_amount** | **str** | Valor do pagamento referente ao  contrato da modalidade de crédito consultada. Expresso em valor monetário com no mínimo 2 casas e no máximo 4 casas decimais.  | 
**over_parcel** | [**FinancingsOverParcel**](FinancingsOverParcel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

