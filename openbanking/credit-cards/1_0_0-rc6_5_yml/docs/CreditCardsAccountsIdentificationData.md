# CreditCardsAccountsIdentificationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Denominação/Identificação do nome da conta de pagamento pós-paga (cartão). Conforme CIRCULAR Nº 3.680,BCB, 2013: &#x27;conta de pagamento pós-paga: destinada à execução de transações de pagamento que independem do aporte prévio de recursos&#x27;.  | 
**product_type** | [**EnumCreditCardAccountsProductType**](EnumCreditCardAccountsProductType.md) |  | 
**product_additional_info** | **str** | Informações complementares se tipo de Cartão &#x27;OUTROS&#x27; | [optional] 
**credit_card_network** | [**EnumCreditCardAccountNetwork**](EnumCreditCardAccountNetwork.md) |  | 
**network_additional_info** | **str** | Texto livre para especificar categoria de bandeira marcada como &#x27;OUTRAS&#x27;. | [optional] 
**payment_method** | [**CreditCardsAccountPaymentMethod**](CreditCardsAccountPaymentMethod.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

