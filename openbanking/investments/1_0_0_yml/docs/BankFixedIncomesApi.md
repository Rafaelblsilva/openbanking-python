# investments_1_0_0_yml.BankFixedIncomesApi

All URIs are relative to *https://api.banco.com.br/open-banking/opendata-investments/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**investments_get_fixed_income_bank**](BankFixedIncomesApi.md#investments_get_fixed_income_bank) | **GET** /bank-fixed-incomes | Conjunto de informações de produtos de Renda Fixa Bancária (CDB, RDB, LCI e LCA)

# **investments_get_fixed_income_bank**
> OKResponseInvestmentsFixedIncomeBank investments_get_fixed_income_bank(page=page, page_size=page_size)

Conjunto de informações de produtos de Renda Fixa Bancária (CDB, RDB, LCI e LCA)

Método para obter a lista de produtos de Renda Fixa Bancária (CDB, RDB, LCI e LCA)

### Example
```python
from __future__ import print_function
import time
import investments_1_0_0_yml
from investments_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = investments_1_0_0_yml.BankFixedIncomesApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Conjunto de informações de produtos de Renda Fixa Bancária (CDB, RDB, LCI e LCA)
    api_response = api_instance.investments_get_fixed_income_bank(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankFixedIncomesApi->investments_get_fixed_income_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**OKResponseInvestmentsFixedIncomeBank**](OKResponseInvestmentsFixedIncomeBank.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

