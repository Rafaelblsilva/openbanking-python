# AccountIdentificationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compe_code** | **str** | Código identificador atribuído pelo Banco Central do Brasil às instituições participantes do STR (Sistema de Transferência de reservas). O número-código substituiu o antigo código COMPE. Todos os participantes do STR, exceto as Infraestruturas do Mercado Financeiro (IMF) e a Secretaria do Tesouro Nacional, possuem um número-código independentemente de participarem da Centralizadora da Compensação de Cheques (Compe). O campo tem a anotação “n/a” (“não se aplica”) para os participantes do STR aos quais não é atribuído um número-código | 
**branch_code** | **str** | Código da Agência detentora da conta. (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória)  | 
**number** | **str** | Número da conta  | 
**check_digit** | **str** | Dígito da conta  | 
**type** | [**EnumAccountType**](EnumAccountType.md) |  | 
**subtype** | [**EnumAccountSubType**](EnumAccountSubType.md) |  | 
**currency** | **str** | Moeda referente ao valor da transação, segundo modelo ISO-4217. p.ex. &#x27;BRL&#x27;  Todos os saldos informados estão representados com a moeda vigente do Brasil  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

