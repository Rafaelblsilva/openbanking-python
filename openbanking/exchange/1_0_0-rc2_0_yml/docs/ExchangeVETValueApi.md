# exchange_1_0_0-rc2_0_yml.ExchangeVETValueApi

All URIs are relative to *https://api.banco.com.br/open-banking/opendata-exchange/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_get_vet_value**](ExchangeVETValueApi.md#exchange_get_vet_value) | **GET** /vet-values | Conjunto de informações de Câmbio para valor do VET.

# **exchange_get_vet_value**
> OKResponseExchangeVetValue exchange_get_vet_value(page=page, page_size=page_size)

Conjunto de informações de Câmbio para valor do VET.

Método para disponibilizar os VETs praticados pela instituição nas operações de câmbio, agrupados por tipo de operação (compra ou venda), moeda, forma de entrega, faixas de valores e público-alvo (pessoa física, pessoa jurídica ou ambos).

### Example
```python
from __future__ import print_function
import time
import exchange_1_0_0-rc2_0_yml
from exchange_1_0_0-rc2_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = exchange_1_0_0-rc2_0_yml.ExchangeVETValueApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Conjunto de informações de Câmbio para valor do VET.
    api_response = api_instance.exchange_get_vet_value(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeVETValueApi->exchange_get_vet_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**OKResponseExchangeVetValue**](OKResponseExchangeVetValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

