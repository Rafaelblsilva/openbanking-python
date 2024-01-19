# pension_1_0_0_yml.SurvivalCoveragesApi

All URIs are relative to *https://api.banco.com.br/open-banking/opendata-pension/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pension_survival_coverages**](SurvivalCoveragesApi.md#get_pension_survival_coverages) | **GET** /survival-coverages | Informações de Previdência com Cobertura de Sobrevivência.

# **get_pension_survival_coverages**
> OKResponseSurvivalCoveragePension get_pension_survival_coverages(page=page, page_size=page_size)

Informações de Previdência com Cobertura de Sobrevivência.

Método para obter informações de Previdência de Cobertura de Sobrevivência.

### Example
```python
from __future__ import print_function
import time
import pension_1_0_0_yml
from pension_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pension_1_0_0_yml.SurvivalCoveragesApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Informações de Previdência com Cobertura de Sobrevivência.
    api_response = api_instance.get_pension_survival_coverages(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurvivalCoveragesApi->get_pension_survival_coverages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**OKResponseSurvivalCoveragePension**](OKResponseSurvivalCoveragePension.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

