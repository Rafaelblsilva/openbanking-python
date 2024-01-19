# products-services_1_0_0_yml.FinancingsApi

All URIs are relative to *http://api.banco.com.br/open-banking/products-services/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_financings**](FinancingsApi.md#get_business_financings) | **GET** /business-financings | Obtém a lista de Financiamentos de Pessoa Física.
[**get_personal_financings**](FinancingsApi.md#get_personal_financings) | **GET** /personal-financings | Obtém a lista de Financiamentos de Pessoa Física.

# **get_business_financings**
> ResponseBusinessFinancingsList get_business_financings()

Obtém a lista de Financiamentos de Pessoa Física.

Obtém a lista de Financiamentos de Pessoa Física.

### Example
```python
from __future__ import print_function
import time
import products-services_1_0_0_yml
from products-services_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_1_0_0_yml.FinancingsApi()

try:
    # Obtém a lista de Financiamentos de Pessoa Física.
    api_response = api_instance.get_business_financings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancingsApi->get_business_financings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseBusinessFinancingsList**](ResponseBusinessFinancingsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_financings**
> ResponsePersonalFinancingsList get_personal_financings()

Obtém a lista de Financiamentos de Pessoa Física.

Obtém a lista de Financiamentos de Pessoa Física

### Example
```python
from __future__ import print_function
import time
import products-services_1_0_0_yml
from products-services_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_1_0_0_yml.FinancingsApi()

try:
    # Obtém a lista de Financiamentos de Pessoa Física.
    api_response = api_instance.get_personal_financings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancingsApi->get_personal_financings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsePersonalFinancingsList**](ResponsePersonalFinancingsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

