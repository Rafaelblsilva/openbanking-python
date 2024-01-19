# RiskSignalsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | ID único do dispositivo gerado pela plataforma. | 
**is_rooted_device** | **bool** | Indica se o dispositivo sofreu processo de “root”. | 
**screen_brightness** | **int** | Indica o nível de brilho da tela do dispositivo. | 
**elapsed_time_since_boot** | **int** | Indica por quanto tempo o dispositivo está ligado. | 
**os_version** | **str** | Versão do sistema operacional. | 
**user_time_zone** | **str** | Detalha o fuso horário em que o dispositivo está definido. | 
**language** | **str** | Idioma configurado no dispositivo. | 
**screen_dimensions** | **str** | Tamanho de tela do dispositivo | 
**account_tenure** | **str** | Tempo que o cliente fez cadastro no ITP. | 
**latitude_longitude** | **str** | Latitude (2 casas decimais) e Longitude.  [Restrição] Caso o sinal de risco esteja disponível (cliente permitiu que fosse coletado), o mesmo deverá ser enviado  | [optional] 
**is_calling_progress** | **bool** | Indica chamada ativa no momento do vínculo.  [Restrição] Caso o sinal de risco esteja disponível (cliente permitiu que fosse coletado), o mesmo deverá ser enviado  | [optional] 
**is_dev_mode_enabled** | **bool** | Indica se o dispositivo está em modo de desenvolvedor. | [optional] 
**is_mock_gps** | **bool** | Indica se o dispositivo está usando um GPS falso. | [optional] 
**is_emulated** | **bool** | Indica se o dispositivo é emulado ou real. | [optional] 
**is_monkey_runner** | **bool** | Indica o uso do MonkeyRunner. | [optional] 
**is_charging** | **bool** | Indica se a bateria do dispositivo está sendo carregada. | [optional] 
**antenna_information** | **str** | Indica em qual antena o dispositivo está conectado. | [optional] 
**is_usb_connected** | **bool** | Indica se o dispositivo está conectado em um USB de um computador. | [optional] 
**integrity** | [**RiskSignalsDataIntegrity**](RiskSignalsDataIntegrity.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

