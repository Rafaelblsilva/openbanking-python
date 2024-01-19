# CapitalizationBondsProductPrizeDraw

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_interval** | **str** | Intervalo de tempo regular previsto entre os sorteios. Conforme os domínios:   - UNICO   - DIÁRIO   - SEMANAL   - QUINZENAL   - MENSAL   - BIMESTRAL   - TRIMESTRAL   - QUADRIMESTRAL   - SEMESTRAL   - ANUAL   - OUTROS   - NA  | 
**time_interval_additional_info** | **str** | Restrição: Campo obrigatório para complementar a informação quando selecionada a opção &#x27;OUTROS&#x27; | [optional] 
**quantity** | **float** | Número da quantidade de sorteios previstos ao longo da vigência. | 
**prize_multiplier** | **float** | Valor dos sorteios representado por múltiplo do valor de contribuição. Por exemplo: 5 vezes valor da contribuição | 
**early_settlement_raffle** | **bool** | Modelo de sorteio que acarreta, ao título contemplado, o seu resgate total obrigatório (Resolução Normativa 384/20). Conforme os domínios:  1. true  2. false  | [optional] 
**mandatory_contemplation** | **bool** | Possibilidade de realização de sorteio com previsão de que o título sorteado seja obrigatoriamente um título comercializado, desde que atingidos os requisitos definidos nas condições gerais do plano. Conforme os domínios:   1. true   2. false  | [optional] 
**rule_description** | **str** | Campo aberto para complementar a regra dos sorteios do produto, a ser feita para cada participante. | [optional] 
**minimum_contemplation_probability** | **str** | Número representativo da probabilidade mínima de contemplação nos sorteios, em porcentagem (%). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

