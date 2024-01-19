# UnarrangedAccountOverdraftService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nome da Tarifa cobrada sobre Serviço que incide sobre Adiantamento a depositante, para pessoa jurídica. | [default to 'CONCESSAO_ADIANTAMENTO_DEPOSITANTE']
**code** | **str** | Sigla de identificação do serviço relacionado à Modalidade de Adiantamento a depositante, para pessoa jurídica. | [default to 'ADIANT_DEPOSITANTE']
**charging_trigger_info** | **str** | Fato gerador de cobrança que incide sobre a Modalidade de Adiantamento a depositante informada, para pessoa jurídica. | 
**prices** | [**list[Price]**](Price.md) | lista das faixas dos  valores de tarfas cobradas | 
**minimum** | [**MinimumPrice**](MinimumPrice.md) |  | 
**maximum** | [**MaximumPrice**](MaximumPrice.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

