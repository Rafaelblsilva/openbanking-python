# investments_1_0_0-rc2_0_yml.VariableIncomesApi

All URIs are relative to *https://api.banco.com.br/open-banking/opendata-investments/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**investments_get_variable_income**](VariableIncomesApi.md#investments_get_variable_income) | **GET** /variable-incomes | Conjunto de informações de produtos de Renda Variável (Ações e Fundos de Índices)

# **investments_get_variable_income**
> OKResponseInvestmentsVariableIncome investments_get_variable_income(page=page, page_size=page_size)

Conjunto de informações de produtos de Renda Variável (Ações e Fundos de Índices)

Método para obter a lista de informações de produtos de Renda Variável (Ações e Fundos de Índices)

### Example
```python
from __future__ import print_function
import time
import investments_1_0_0-rc2_0_yml
from investments_1_0_0-rc2_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = investments_1_0_0-rc2_0_yml.VariableIncomesApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Conjunto de informações de produtos de Renda Variável (Ações e Fundos de Índices)
    api_response = api_instance.investments_get_variable_income(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariableIncomesApi->investments_get_variable_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**OKResponseInvestmentsVariableIncome**](OKResponseInvestmentsVariableIncome.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

