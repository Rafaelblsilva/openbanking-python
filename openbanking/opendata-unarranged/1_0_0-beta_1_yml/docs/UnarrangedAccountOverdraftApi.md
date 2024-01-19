# opendata-unarranged_1_0_0-beta_1_yml.UnarrangedAccountOverdraftApi

All URIs are relative to *http://api.banco.com.br/open-banking/opendata-unarranged/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_unarranged_account_overdraft**](UnarrangedAccountOverdraftApi.md#get_business_unarranged_account_overdraft) | **GET** /business-unarranged-account-overdraft | Obtém a lista de adiantamento de depositante de Pessoa Jurídica.
[**get_personal_unarranged_account_overdraft**](UnarrangedAccountOverdraftApi.md#get_personal_unarranged_account_overdraft) | **GET** /personal-unarranged-account-overdraft | Obtém a lista de adiantamento de depositante de Pessoa Natural.

# **get_business_unarranged_account_overdraft**
> ResponseBusinessUnarrangedAccountOverdraft get_business_unarranged_account_overdraft(page=page, page_size=page_size)

Obtém a lista de adiantamento de depositante de Pessoa Jurídica.

Obtém a lista de adiantamento de depositante de Pessoa Jurídica.

### Example
```python
from __future__ import print_function
import time
import opendata-unarranged_1_0_0-beta_1_yml
from opendata-unarranged_1_0_0-beta_1_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendata-unarranged_1_0_0-beta_1_yml.UnarrangedAccountOverdraftApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém a lista de adiantamento de depositante de Pessoa Jurídica.
    api_response = api_instance.get_business_unarranged_account_overdraft(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnarrangedAccountOverdraftApi->get_business_unarranged_account_overdraft: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponseBusinessUnarrangedAccountOverdraft**](ResponseBusinessUnarrangedAccountOverdraft.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_unarranged_account_overdraft**
> ResponsePersonalUnarrangedAccountOverdraft get_personal_unarranged_account_overdraft(page=page, page_size=page_size)

Obtém a lista de adiantamento de depositante de Pessoa Natural.

Obtém a lista de adiantamento de depositante de Pessoa Natural.

### Example
```python
from __future__ import print_function
import time
import opendata-unarranged_1_0_0-beta_1_yml
from opendata-unarranged_1_0_0-beta_1_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendata-unarranged_1_0_0-beta_1_yml.UnarrangedAccountOverdraftApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém a lista de adiantamento de depositante de Pessoa Natural.
    api_response = api_instance.get_personal_unarranged_account_overdraft(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnarrangedAccountOverdraftApi->get_personal_unarranged_account_overdraft: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponsePersonalUnarrangedAccountOverdraft**](ResponsePersonalUnarrangedAccountOverdraft.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

