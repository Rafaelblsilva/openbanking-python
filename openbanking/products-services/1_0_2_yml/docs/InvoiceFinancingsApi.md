# products-services_1_0_2_yml.InvoiceFinancingsApi

All URIs are relative to *http://api.banco.com.br/open-banking/products-services/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_invoice_financings**](InvoiceFinancingsApi.md#get_business_invoice_financings) | **GET** /business-invoice-financings | Obtém a lista de Adiantamento de Recebíveis de Pessoa Jurídica.
[**get_personal_invoice_financings**](InvoiceFinancingsApi.md#get_personal_invoice_financings) | **GET** /personal-invoice-financings | Obtém a lista de Adiantamento de Recebíveis de Pessoa Natural.

# **get_business_invoice_financings**
> ResponseBusinessInvoiceFinancings get_business_invoice_financings(page=page, page_size=page_size)

Obtém a lista de Adiantamento de Recebíveis de Pessoa Jurídica.

Obtém a lista de Adiantamento de Recebíveis de Pessoa Jurídica.

### Example
```python
from __future__ import print_function
import time
import products-services_1_0_2_yml
from products-services_1_0_2_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_1_0_2_yml.InvoiceFinancingsApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém a lista de Adiantamento de Recebíveis de Pessoa Jurídica.
    api_response = api_instance.get_business_invoice_financings(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceFinancingsApi->get_business_invoice_financings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponseBusinessInvoiceFinancings**](ResponseBusinessInvoiceFinancings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_invoice_financings**
> ResponsePersonalInvoiceFinancings get_personal_invoice_financings(page=page, page_size=page_size)

Obtém a lista de Adiantamento de Recebíveis de Pessoa Natural.

Obtém a lista de Adiantamento de Recebíveis de Pessoa Natural.

### Example
```python
from __future__ import print_function
import time
import products-services_1_0_2_yml
from products-services_1_0_2_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_1_0_2_yml.InvoiceFinancingsApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém a lista de Adiantamento de Recebíveis de Pessoa Natural.
    api_response = api_instance.get_personal_invoice_financings(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceFinancingsApi->get_personal_invoice_financings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponsePersonalInvoiceFinancings**](ResponsePersonalInvoiceFinancings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

