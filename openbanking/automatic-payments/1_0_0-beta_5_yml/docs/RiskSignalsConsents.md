# RiskSignalsConsents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | ID único do dispositivo gerado pela plataforma. | 
**is_rooted_device** | **bool** | Indica se o dispositivo atualmente está com permissão de “root”. | 
**screen_brightness** | **float** | Indica o nível de brilho da tela do dispositivo.   Em dispositivos Android o valor é um inteiro, entre 0 e 255, inclusive;   Em dispositivos iOS o valor é um ponto flutuante entre 0.0 e 1.0.  | 
**elapsed_time_since_boot** | **int** | Indica por quanto tempo (em milissegundos) o dispositivo está ligado. | 
**os_version** | **str** | Versão do sistema operacional. | 
**user_time_zone_offset** | **str** | Indica a configuração de fuso horário do dispositivo do usuário, com o formato UTC offset: ±hh[:mm]  | 
**language** | **str** | Indica o idioma do dispositivo no formato ISO 639-1. | 
**screen_dimensions** | [**RiskSignalsPaymentsManualScreenDimensions**](RiskSignalsPaymentsManualScreenDimensions.md) |  | 
**account_tenure** | **date** | Data de cadastro do cliente na iniciadora. | 
**geolocation** | [**RiskSignalsPaymentsManualGeolocation**](RiskSignalsPaymentsManualGeolocation.md) |  | [optional] 
**is_call_in_progress** | **bool** | Indica chamada ativa no momento do vínculo.  [Restrição] Caso o sinal de risco esteja disponível (cliente permitiu que fosse coletado), o mesmo deverá ser enviado  | [optional] 
**is_dev_mode_enabled** | **bool** | Indica se o dispositivo está em modo de desenvolvedor. | [optional] 
**is_mock_gps** | **bool** | Indica se o dispositivo está usando um GPS falso. | [optional] 
**is_emulated** | **bool** | Indica se o dispositivo é emulado ou real. | [optional] 
**is_monkey_runner** | **bool** | Indica o uso do MonkeyRunner. | [optional] 
**is_charging** | **bool** | Indica se a bateria do dispositivo está sendo carregada. | [optional] 
**antenna_information** | **str** | Indica em qual antena o dispositivo está conectado. | [optional] 
**is_usb_connected** | **bool** | Indica se o dispositivo está conectado a outro dispositivo via USB. | [optional] 
**integrity** | [**RiskSignalsPaymentsManualIntegrity**](RiskSignalsPaymentsManualIntegrity.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

