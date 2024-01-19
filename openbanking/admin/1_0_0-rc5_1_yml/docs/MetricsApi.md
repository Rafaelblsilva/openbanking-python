# admin_1_0_0-rc5_1_yml.MetricsApi

All URIs are relative to *http://api.banco.com.br/open-banking/admin/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics**](MetricsApi.md#get_metrics) | **GET** /metrics | Obtém as métricas de disponibilidade das APIs

# **get_metrics**
> ResponseMetricsList get_metrics(page=page, page_size=page_size, period=period)

Obtém as métricas de disponibilidade das APIs

Obtém as métricas de disponibilidade das APIs

### Example
```python
from __future__ import print_function
import time
import admin_1_0_0-rc5_1_yml
from admin_1_0_0-rc5_1_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = admin_1_0_0-rc5_1_yml.MetricsApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
period = 'period_example' # str | Período a ser consultado   * `CURRENT` - Métricas do dia atual.   * `ALL` - Métricas de todo o período disponível.  (optional)

try:
    # Obtém as métricas de disponibilidade das APIs
    api_response = api_instance.get_metrics(page=page, page_size=page_size, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]
 **period** | **str**| Período a ser consultado   * &#x60;CURRENT&#x60; - Métricas do dia atual.   * &#x60;ALL&#x60; - Métricas de todo o período disponível.  | [optional] 

### Return type

[**ResponseMetricsList**](ResponseMetricsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

