# Status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Condição atual da API:   * &#x60;OK&#x60; - A implementação é totalmente funcional   * &#x60;PARTIAL_FAILURE&#x60; - Um ou mais endpoints estão indisponíveis   * &#x60;UNAVAILABLE&#x60; - A implementação completa está indisponível   * &#x60;SCHEDULED_OUTAGE&#x60; - Uma interrupção anunciada está em vigor  | 
**explanation** | **str** | Fornece uma explicação da interrupção atual que pode ser exibida para um cliente final. Será obrigatoriamente preenchido se code tiver algum valor que não seja OK | 
**detection_time** | **str** | A data e hora em que a interrupção atual foi detectada. Será obrigatoriamente preenchido se a propriedade code for PARTIAL_FAILURE ou UNAVAILABLE | [optional] 
**expected_resolution_time** | **str** | A data e hora em que o serviço completo deve continuar (se conhecido). Será obrigatoriamente preenchido se code tiver algum valor que não seja OK | [optional] 
**update_time** | **str** | A data e hora em que esse status foi atualizado pela última vez pelo titular dos dados. | [optional] 
**unavailable_endpoints** | **list[str]** | Endpoints com indisponibilidade | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

