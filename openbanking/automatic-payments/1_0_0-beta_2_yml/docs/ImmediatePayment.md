# ImmediatePayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EnumPaymentType**](EnumPaymentType.md) |  | 
**_date** | **date** | Define a data alvo da liquidação do pagamento. O fuso horário de Brasília deve ser utilizado para criação e racionalização sobre os dados deste campo.  | 
**currency** | **str** | Código da moeda nacional segundo modelo ISO-4217, ou seja, &#x27;BRL&#x27;. Todos os valores monetários informados estão representados com a moeda vigente do Brasil.  | 
**amount** | **str** | Valor da transação com 2 casas decimais.  | 
**remittance_information** | **str** | Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.  | [optional] 
**creditor_account** | [**PostCreditorAccount**](PostCreditorAccount.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

