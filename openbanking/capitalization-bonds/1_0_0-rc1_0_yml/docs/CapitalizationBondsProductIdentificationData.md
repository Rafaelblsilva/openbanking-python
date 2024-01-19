# CapitalizationBondsProductIdentificationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant** | [**Participant**](Participant.md) |  | 
**society** | [**CapitalizationBondsProductIdentificationDataSociety**](CapitalizationBondsProductIdentificationDataSociety.md) |  | 
**name** | **str** | Nome comercial do produto, pelo qual é identificado nos canais de distribuição e atendimento da sociedade. | 
**code** | **str** | Código único a ser definido pela sociedade. | 
**modality** | [**EnumCapitalizationBondsProductModality**](EnumCapitalizationBondsProductModality.md) |  | 
**cost_type** | [**EnumCapitalizationBondsProductCostType**](EnumCapitalizationBondsProductCostType.md) |  | 
**terms_and_conditions** | [**TermsAndConditions**](TermsAndConditions.md) |  | 
**quotas** | [**list[CapitalizationBondsProductQuota]**](CapitalizationBondsProductQuota.md) | Informações relativas às taxas da Quotas praticadas para cada Parcela | 
**validity** | **int** | Período entre a data de início e a data final para constituição do capital a ser pago ao(s) titular(es) do direito de resgate. Prazo de vigência do título de capitalização em meses (Resolução CNSP 384/20). Em meses. | [optional] 
**serie_size** | **int** | Os títulos de capitalização que prevejam sorteio devem ser estruturados em séries, ou seja, em sequências ou em grupos de títulos submetidos às mesmas condições e características, à exceção do valor do pagamento. | [optional] 
**capitalization_period** | [**CapitalizationBondsProductCapitalizationPeriod**](CapitalizationBondsProductCapitalizationPeriod.md) |  | 
**late_payment** | [**LatePayment**](LatePayment.md) |  | 
**contribution_payment** | [**ContributionPayment**](ContributionPayment.md) |  | 
**redemption_percentage_end_term** | **str** | Percentual mínimo da soma das contribuições efetuadas que poderá ser resgatado ao final da vigência, tendo como condição os pagamentos das parcelas nos respectivos vencimentos. | 
**final_redemption_rate** | **str** | Valor percentual (%) de resgate final permitido. | 
**draws** | [**list[CapitalizationBondsProductPrizeDraw]**](CapitalizationBondsProductPrizeDraw.md) | Informações relativas aos Sorteios | 
**additional_info** | **str** | Campo aberto (possibilidade de incluir URL) Observação: As URLs são limitadas a 2048 caracteres mas, para o contexto do Open Insurance , foi adotado a metade deste tamanho (1024). tamanho p.ex.  ‘https://ACME.exemplo/capitalizacao/tradicional/pdf/condicoes_gerais. | 
**minimum_requirement_details** | **str** | Campo aberto (possibilidade de incluir URL). Observação: As URLs são limitadas a 2048 caracteres mas, para o contexto do Open Insurance , foi adotado a metade deste tamanho (1024). tamanho. p.ex. ‘https://ACME.exemplo/capitalizacao/tradicional/pdf/condicoes_gerais.’  | [optional] 
**target_audience** | **str** | A considerar os domínios abaixo:    1. Pessoa Natural   2. Pessoa Jurídica   3. Ambas (Pessoa Natural e Jurídica)  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

