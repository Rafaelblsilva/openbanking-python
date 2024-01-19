# acquiring-services_1_0_0_yml.BusinessAcquiringServicesApi

All URIs are relative to *https://api.banco.com.br/open-banking/opendata-acquiring-services/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_acquiring_services**](BusinessAcquiringServicesApi.md#get_business_acquiring_services) | **GET** /businesses | Conjunto de informações de Credenciamento para Pessoa Jurídica.

# **get_business_acquiring_services**
> OKResponseAcquiringServices get_business_acquiring_services(page=page, page_size=page_size)

Conjunto de informações de Credenciamento para Pessoa Jurídica.

Método para disponibilizar as taxas e tarifas por serviços.

### Example
```python
from __future__ import print_function
import time
import acquiring-services_1_0_0_yml
from acquiring-services_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = acquiring-services_1_0_0_yml.BusinessAcquiringServicesApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Conjunto de informações de Credenciamento para Pessoa Jurídica.
    api_response = api_instance.get_business_acquiring_services(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessAcquiringServicesApi->get_business_acquiring_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**OKResponseAcquiringServices**](OKResponseAcquiringServices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

