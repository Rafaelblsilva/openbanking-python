# products-services_1_0_0-rc5_yml.FinancingsApi

All URIs are relative to *http://api.banco.com.br/open-banking/products-services/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_financings**](FinancingsApi.md#get_business_financings) | **GET** /business-financings | Obtém a lista de Financiamentos de Pessoa Jurídica.
[**get_personal_financings**](FinancingsApi.md#get_personal_financings) | **GET** /personal-financings | Obtém a lista de Financiamentos de Pessoa Natural.

# **get_business_financings**
> ResponseBusinessFinancings get_business_financings(page=page, page_size=page_size)

Obtém a lista de Financiamentos de Pessoa Jurídica.

Obtém a lista de Financiamentos de Pessoa Jurídica.

### Example
```python
from __future__ import print_function
import time
import products-services_1_0_0-rc5_yml
from products-services_1_0_0-rc5_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_1_0_0-rc5_yml.FinancingsApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém a lista de Financiamentos de Pessoa Jurídica.
    api_response = api_instance.get_business_financings(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancingsApi->get_business_financings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponseBusinessFinancings**](ResponseBusinessFinancings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_financings**
> ResponsePersonalFinancings get_personal_financings(page=page, page_size=page_size)

Obtém a lista de Financiamentos de Pessoa Natural.

Obtém a lista de Financiamentos de Pessoa Natural

### Example
```python
from __future__ import print_function
import time
import products-services_1_0_0-rc5_yml
from products-services_1_0_0-rc5_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_1_0_0-rc5_yml.FinancingsApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém a lista de Financiamentos de Pessoa Natural.
    api_response = api_instance.get_personal_financings(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancingsApi->get_personal_financings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponsePersonalFinancings**](ResponsePersonalFinancings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

