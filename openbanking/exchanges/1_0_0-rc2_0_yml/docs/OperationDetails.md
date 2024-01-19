# OperationDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized_institution_cnpj_number** | **str** | CNPJ da instituição autorizada a operar no mercado de câmbio. | 
**authorized_institution_name** | **str** | Nome da Instituição Financeira no Brasil. | 
**intermediary_institution_cnpj_number** | **str** | CNPJ da instituição intermediadora autorizada a operar no mercado de câmbio.  Campo de envio obrigatório nos casos em que houver instituição intermediadora.  | [optional] 
**intemediary_institution_name** | **str** | Nome da corretora interveniente autorizada a operar no mercado de câmbio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;intermediaryInstitutionCnpjNumber&#x27; for informado.  | [optional] 
**operation_number** | **str** | Número do registro da operação no Bacen. Deve ser preenchido no compartilhamento, após registro no Sistema de Câmbio e número disponível na transmissora/detentora. | [optional] 
**operation_type** | [**EnumExchangesOperationType**](EnumExchangesOperationType.md) |  | 
**operation_date** | **datetime** | Data do fechamento do contrato de câmbio. | 
**due_date** | **date** | Data em que a operação (compra ou venda) está prevista para ser liquidada. | 
**local_currency_operation_tax** | [**OperationDetailsLocalCurrencyOperationTax**](OperationDetailsLocalCurrencyOperationTax.md) |  | 
**local_currency_operation_value** | [**OperationDetailsLocalCurrencyOperationValue**](OperationDetailsLocalCurrencyOperationValue.md) |  | 
**foreign_operation_value** | [**OperationDetailsForeignOperationValue**](OperationDetailsForeignOperationValue.md) |  | 
**operation_outstanding_balance** | [**OperationDetailsOperationOutstandingBalance**](OperationDetailsOperationOutstandingBalance.md) |  | [optional] 
**vet_amount** | [**OperationDetailsVetAmount**](OperationDetailsVetAmount.md) |  | [optional] 
**local_currency_advance_percentage** | **str** | Percentual do valor de moeda nacional concedido ao cliente antecipadamente. p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%). Campos de envio obrigatório no caso de operações de câmbio com liquidação futura.  | [optional] 
**delivery_foreign_currency** | [**EnumExchangesDeliveryForeignCurrency**](EnumExchangesDeliveryForeignCurrency.md) |  | 
**operation_category_code** | **str** | Código da natureza fato do fechamento da operação. Deve respeitar os códigos de natureza referenciados na resolução 277 ou na Circular 3690, conforme se aplicar ao contrato de câmbio. | 
**relationship_code** | **str** | Código de Relação de vínculo entre o Cliente e o Pagador/Recebedor no Exterior. Deve respeitar os códigos de vínculo referenciados na resolução 277 ou na Circular 3690, conforme se aplicar ao contrato de câmbio.  [Restrição] Campo de preenchimento opcional pelas participantes quando o campo &#x27;deliveryForeignCurrency &#x27; for igual EM ESPÉCIE E/OU CHEQUES DE VIAGEM.  | [optional] 
**foreign_partie_name** | **str** | Nome do pagador ou recebedor no exterior.  [Restrição] Campo de preenchimento opcional pelas participantes quando o campo &#x27;deliveryForeignCurrency &#x27; for igual EM ESPÉCIE E/OU CHEQUES DE VIAGEM.  | [optional] 
**foreign_partie_country_code** | **str** | País do pagador ou recebedor. Código do país segundo a norma ISO 3166-1.  [Restrição] Campo de preenchimento opcional pelas participantes quando o campo &#x27;deliveryForeignCurrency &#x27; for igual EM ESPÉCIE E/OU CHEQUES DE VIAGEM.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

