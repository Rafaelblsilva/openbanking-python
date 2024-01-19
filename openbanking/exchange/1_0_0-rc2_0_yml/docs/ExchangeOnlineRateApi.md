# exchange_1_0_0-rc2_0_yml.ExchangeOnlineRateApi

All URIs are relative to *https://api.banco.com.br/open-banking/opendata-exchange/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_get_online_rate**](ExchangeOnlineRateApi.md#exchange_get_online_rate) | **GET** /online-rates | Conjunto de informações de Câmbio para taxa online.

# **exchange_get_online_rate**
> OKResponseExchangeOnlineRate exchange_get_online_rate(page=page, page_size=page_size)

Conjunto de informações de Câmbio para taxa online.

As instituições autorizadas a operar em câmbio que disponibilizam em seus canais digitais a possibilidade de contratação ou a informação de taxa de câmbio devem retornar as condições no momento da consulta, sendo admitida uma defasagem máxima de atualização de 5 minutos em relação a seus canais digitais.  Já as demais instituições participantes do Open Finance autorizadas a operar em câmbio podem adotar as janelas de consulta da PTAX como frequência mínima de atualização das informações retornadas neste serviço.

### Example
```python
from __future__ import print_function
import time
import exchange_1_0_0-rc2_0_yml
from exchange_1_0_0-rc2_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = exchange_1_0_0-rc2_0_yml.ExchangeOnlineRateApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Conjunto de informações de Câmbio para taxa online.
    api_response = api_instance.exchange_get_online_rate(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeOnlineRateApi->exchange_get_online_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**OKResponseExchangeOnlineRate**](OKResponseExchangeOnlineRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

