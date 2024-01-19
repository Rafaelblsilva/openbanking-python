# AccountBalancesData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_amount** | **float** | Saldo disponível para utilização imediata. No caso de conta de depósito a vista, sem considerar cheque especial e investimentos atrelados a conta. Admite saldo negativo. Expresso em valor monetário com 4 casas decimais. | 
**available_amount_currency** | **str** | Moeda referente ao valor do saldo disponível, segundo modelo ISO-4217. p.ex. &#x27;BRL&#x27;. Pode ser preenchido com “NA” caso a instituição não possua a informação. | 
**blocked_amount** | **float** | Saldo bloqueado, não disponível para utilização imediata, por motivo de bloqueio apresentado para o cliente nos canais eletrônicos Expresso em valor monetário com 4 casas decimais. | 
**blocked_amount_currency** | **str** | Moeda referente ao valor do saldo bloqueado, segundo modelo ISO-4217. p.ex. &#x27;BRL&#x27;. Pode ser preenchido com “NA” caso a instituição não possua a informação. | 
**automatically_invested_amount** | **float** | Saldo disponível com aplicação automática - corresponde a soma do saldo disponível acrescido do valor obtido a partir da aplicação automática Expresso em valor monetário com 4 casas decimais. | 
**automatically_invested_amount_currency** | **str** | Moeda referente ao valor do saldo disponível com aplicação automática, segundo modelo ISO-4217. p.ex. &#x27;BRL&#x27;. Pode ser preenchido com “NA” caso a instituição não possua a informação. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

