# insurances_1_0_0-rc3_0_yml.SegurosApi

All URIs are relative to *https://api.banco.com.br/open-banking/opendata-insurance/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_personal_insurance**](SegurosApi.md#get_personal_insurance) | **GET** /personals | Conjunto de informações referentes a seguros pessoais de uma instituição

# **get_personal_insurance**
> OKResponsePersonalInsuranceList get_personal_insurance(page=page, page_size=page_size)

Conjunto de informações referentes a seguros pessoais de uma instituição

Método para obter a lista de todos os seguros pessoais de uma instituição

### Example
```python
from __future__ import print_function
import time
import insurances_1_0_0-rc3_0_yml
from insurances_1_0_0-rc3_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = insurances_1_0_0-rc3_0_yml.SegurosApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Conjunto de informações referentes a seguros pessoais de uma instituição
    api_response = api_instance.get_personal_insurance(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegurosApi->get_personal_insurance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**OKResponsePersonalInsuranceList**](OKResponsePersonalInsuranceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

