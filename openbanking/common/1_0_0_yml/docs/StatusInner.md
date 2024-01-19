# StatusInner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Enum com Status da API. OK (a implementação é totalmente funcional). PARTIAL_FAILURE (um ou mais endpoints estão indisponíveis). UNAVAILABLE (a implementação completa está indisponível). SCHEDULED_OUTAGE (uma interrupção anunciada está em vigor) | [optional] 
**explanation** | **str** | Fornece uma explicação da interrupção atual que pode ser exibida para um cliente final. Obrigatório se a propriedade status tiver algum valor que não seja OK | [optional] 
**detection_time** | **str** | A data e hora em que a interrupção atual foi detectada. Só deve estar presente se a propriedade status for PARTIAL_FAILURE ou UNAVAILABLE | [optional] 
**expected_resolution_time** | **str** | A data e hora em que o serviço completo deve continuar (se conhecido). Não deve estar presente se a propriedade status tiver um valor OK. | [optional] 
**update_time** | **str** | A data e hora em que esse status foi atualizado pela última vez pelo titular dos dados. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

