# Events

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_sequence_number** | **str** | Número sequência do registro do evento de câmbio no Bacen. | 
**event_type** | [**EnumExchangesEventType**](EnumExchangesEventType.md) |  | 
**event_date** | **datetime** | Data do evento relacionado com a operação. | 
**due_date** | **date** | Data em que a operação (compra ou venda), após evento, está prevista para ser liquidada. | [optional] 
**local_currency_operation_tax** | [**EventsLocalCurrencyOperationTax**](EventsLocalCurrencyOperationTax.md) |  | [optional] 
**local_currency_operation_value** | [**OperationDetailsLocalCurrencyOperationValue**](OperationDetailsLocalCurrencyOperationValue.md) |  | [optional] 
**foreign_operation_value** | [**OperationDetailsForeignOperationValue**](OperationDetailsForeignOperationValue.md) |  | [optional] 
**operation_outstanding_balance** | [**EventsOperationOutstandingBalance**](EventsOperationOutstandingBalance.md) |  | [optional] 
**vet_amount** | [**OperationDetailsVetAmount**](OperationDetailsVetAmount.md) |  | [optional] 
**local_currency_advance_percentage** | **str** | Percentual do valor de moeda nacional concedido ao cliente antecipadamente. p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%). Campos de envio obrigatório no caso de operações de câmbio com liquidação futura.  | [optional] 
**delivery_foreign_currency** | [**EnumExchangesDeliveryForeignCurrency**](EnumExchangesDeliveryForeignCurrency.md) |  | [optional] 
**operation_category_code** | **str** | Código da natureza fato do fechamento da operação. Deve respeitar os códigos de natureza referenciados na resolução 277 ou na Circular 3690, conforme se aplicar ao contrato de câmbio. | [optional] 
**foreign_partie** | [**list[OperationDetailsForeignPartie]**](OperationDetailsForeignPartie.md) | Lista para envio de informações de parte envolvida.  [Restrição] Lista de preenchimento opcional pelas participantes quando o campo &#x27;deliveryForeignCurrency &#x27; for igual EM ESPÉCIE E/OU CHEQUES DE VIAGEM.  Caso a instituição possua a informação, ela é de envio obrigatório.  Caso a informação seja atualizada posteriormente a contratação, ela deve ser enviada através de eventos.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

