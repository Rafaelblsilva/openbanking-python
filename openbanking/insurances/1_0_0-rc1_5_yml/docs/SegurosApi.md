# insurances_1_0_0-rc1_5_yml.SegurosApi

All URIs are relative to *https://api.banco.com.br/open-banking/opendata-insurance/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_automotive_insurance**](SegurosApi.md#get_automotive_insurance) | **GET** /automotives | Conjunto de informações referentes a seguros automotivos de uma instituição
[**get_home_insurance**](SegurosApi.md#get_home_insurance) | **GET** /homes | Conjunto de informações referentes a seguros residenciais de uma instituição

# **get_automotive_insurance**
> OKResponseAutomotiveInsuranceList get_automotive_insurance(page=page, page_size=page_size)

Conjunto de informações referentes a seguros automotivos de uma instituição

Método para obter a lista de todos os seguros automotivos de uma instituição

### Example
```python
from __future__ import print_function
import time
import insurances_1_0_0-rc1_5_yml
from insurances_1_0_0-rc1_5_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = insurances_1_0_0-rc1_5_yml.SegurosApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Conjunto de informações referentes a seguros automotivos de uma instituição
    api_response = api_instance.get_automotive_insurance(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegurosApi->get_automotive_insurance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**OKResponseAutomotiveInsuranceList**](OKResponseAutomotiveInsuranceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_home_insurance**
> OKResponseHomeInsuranceList get_home_insurance(page=page, page_size=page_size)

Conjunto de informações referentes a seguros residenciais de uma instituição

Método para obter a lista de todos os seguros automotivos de uma instituição

### Example
```python
from __future__ import print_function
import time
import insurances_1_0_0-rc1_5_yml
from insurances_1_0_0-rc1_5_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = insurances_1_0_0-rc1_5_yml.SegurosApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Conjunto de informações referentes a seguros residenciais de uma instituição
    api_response = api_instance.get_home_insurance(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegurosApi->get_home_insurance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**OKResponseHomeInsuranceList**](OKResponseHomeInsuranceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

