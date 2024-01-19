# ResponseCreatePixPaymentPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Valor da transação com 2 casas decimais. O valor deve ser o mesmo enviado no consentimento.   Para QR Code estático com valor pré-determinado no QR Code ou para QR Code dinâmico com indicação de que o valor não pode ser alterado: O campo amount deve ser preenchido com o valor estabelecido no QR Code.  Caso seja preenchido com valor divergente do QR Code, deve ser retornado um erro HTTP Status 422.  | 
**currency** | **str** | Código da moeda nacional segundo modelo ISO-4217, ou seja, &#x27;BRL&#x27;.   Todos os valores monetários informados estão representados com a moeda vigente do Brasil.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

