# ConsentAuthorizationDataRiskSignals

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geolocation** | [**ConsentAuthorizationDataRiskSignalsGeolocation**](ConsentAuthorizationDataRiskSignalsGeolocation.md) |  | [optional] 
**device_id** | **str** | Identificador do dispositivo. | [optional] 
**is_rooted_device** | **bool** | Indica se o usuário possui permissão root no dispositivo. | [optional] 
**screen_brightness** | **int** | Indica o nível de brilho da tela do dispositivo. | [optional] 
**elapsed_time_since_boot** | **int** | Indica por quanto tempo o dispositivo está ligado desde a última inicialização. | [optional] 
**is_call_in_progress** | **bool** | Indica se há uma chamada em curso | [optional] 
**is_dev_mode_enabled** | **bool** | Indica se o modo desenvolvedor está ativado no dispositivo. | [optional] 
**is_mock_gps** | **bool** | Indica se o dispositivo está utilizando geolocalização fictícia. | [optional] 
**is_emulated** | **bool** | Indica se o dispositivo é emulado. | [optional] 
**is_monkey_runner** | **bool** | Indica se o dispositivo está sob controle de uma ferramenta de automação. | [optional] 
**is_charging** | **bool** | Indica se a bateria do dispositivo está em carregamento. | [optional] 
**antenna_information** | **str** | Indica o tipo de conexão com a rede de celular do dispositivo. | [optional] 
**is_usb_connected** | **bool** | Indica se existe ao menos uma conexão USB ao dispositivo. | [optional] 
**user_time_zone** | **str** | Indica a configuração de fuso horário do dispositivo no formato UTC offset: ±hh[:mm] | [optional] 
**language** | **str** | Indica o idioma do dispositivo no formato ISO 639-1. | [optional] 
**screen_dimensions** | [**ConsentAuthorizationDataRiskSignalsScreenDimensions**](ConsentAuthorizationDataRiskSignalsScreenDimensions.md) |  | [optional] 
**account_tenure** | **int** | Indica há quanto tempo o cliente realizou seu cadastro na iniciadora. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

