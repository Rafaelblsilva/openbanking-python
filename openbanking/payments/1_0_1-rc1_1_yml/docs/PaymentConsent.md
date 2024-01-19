# PaymentConsent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EnumPaymentType**](EnumPaymentType.md) |  | 
**_date** | **date** | Data do pagamento, conforme especificação RFC-3339. | 
**currency** | **str** | Código da moeda nacional segundo modelo ISO-4217, ou seja, &#x27;BRL&#x27;. Todos os valores monetários informados estão representados com a moeda vigente do Brasil.  | 
**amount** | **str** | Valor da transação com 2 casas decimais.  | 
**ibge_town_code** | **str** | Traz o código da cidade segundo o IBGE (Instituto Brasileiro de Geografia e Estatística). Para o preenchimento deste campo, o Iniciador de Pagamentos deve seguir a orientação do arranjo da forma de pagamento. O preenchimento do campo tanto em pix/payments quanto /consents deve ser igual. Caso haja divergência dos valores, a instituição deve retornar HTTP 422 com o código de erro PAGAMENTO_DIVERGENTE_DO_CONSENTIMENTO. Este campo faz referência ao campo CodMun do arranjo Pix.  | [optional] 
**details** | [**Details**](Details.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

