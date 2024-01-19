# opendata-loans_1_0_0-beta_2_yml.LoansApi

All URIs are relative to *http://api.banco.com.br/open-banking/opendata-loans/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_loans**](LoansApi.md#get_business_loans) | **GET** /business-loans | Obtém dados sobre empréstimos pessoa jurídica
[**get_personal_loans**](LoansApi.md#get_personal_loans) | **GET** /personal-loans | Obtém dados sobre empréstimos pessoa natural

# **get_business_loans**
> ResponseBusinessLoans get_business_loans(page=page, page_size=page_size)

Obtém dados sobre empréstimos pessoa jurídica

Obtém dados sobre empréstimos pessoa jurídica

### Example
```python
from __future__ import print_function
import time
import opendata-loans_1_0_0-beta_2_yml
from opendata-loans_1_0_0-beta_2_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendata-loans_1_0_0-beta_2_yml.LoansApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém dados sobre empréstimos pessoa jurídica
    api_response = api_instance.get_business_loans(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->get_business_loans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponseBusinessLoans**](ResponseBusinessLoans.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_loans**
> ResponsePersonalLoans get_personal_loans(page=page, page_size=page_size)

Obtém dados sobre empréstimos pessoa natural

Obtém dados sobre empréstimos pessoa natural

### Example
```python
from __future__ import print_function
import time
import opendata-loans_1_0_0-beta_2_yml
from opendata-loans_1_0_0-beta_2_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendata-loans_1_0_0-beta_2_yml.LoansApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém dados sobre empréstimos pessoa natural
    api_response = api_instance.get_personal_loans(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->get_personal_loans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponsePersonalLoans**](ResponsePersonalLoans.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

