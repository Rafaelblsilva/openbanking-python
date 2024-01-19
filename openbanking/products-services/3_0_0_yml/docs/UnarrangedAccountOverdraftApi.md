# products-services_3_0_0_yml.UnarrangedAccountOverdraftApi

All URIs are relative to *http://api.banco.com.br/open-banking/products-services/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_unarranged_account_overdraft**](UnarrangedAccountOverdraftApi.md#get_business_unarranged_account_overdraft) | **GET** /business-unarranged-account-overdraft | Obtém a lista de adiantamento de depositante de Pessoa Jurídica.
[**get_personal_unarranged_account_overdraft**](UnarrangedAccountOverdraftApi.md#get_personal_unarranged_account_overdraft) | **GET** /personal-unarranged-account-overdraft | Obtém a lista de adiantamento de depositante de Pessoa Natural.

# **get_business_unarranged_account_overdraft**
> ResponseBusinessUnarrangedAccountOverdraft get_business_unarranged_account_overdraft()

Obtém a lista de adiantamento de depositante de Pessoa Jurídica.

Obtém a lista de adiantamento de depositante de Pessoa Jurídica.

### Example
```python
from __future__ import print_function
import time
import products-services_3_0_0_yml
from products-services_3_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_3_0_0_yml.UnarrangedAccountOverdraftApi()

try:
    # Obtém a lista de adiantamento de depositante de Pessoa Jurídica.
    api_response = api_instance.get_business_unarranged_account_overdraft()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnarrangedAccountOverdraftApi->get_business_unarranged_account_overdraft: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseBusinessUnarrangedAccountOverdraft**](ResponseBusinessUnarrangedAccountOverdraft.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_unarranged_account_overdraft**
> ResponsePersonalUnarrangedAccountOverdraft get_personal_unarranged_account_overdraft()

Obtém a lista de adiantamento de depositante de Pessoa Natural.

Obtém a lista de adiantamento de depositante de Pessoa Natural.

### Example
```python
from __future__ import print_function
import time
import products-services_3_0_0_yml
from products-services_3_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_3_0_0_yml.UnarrangedAccountOverdraftApi()

try:
    # Obtém a lista de adiantamento de depositante de Pessoa Natural.
    api_response = api_instance.get_personal_unarranged_account_overdraft()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnarrangedAccountOverdraftApi->get_personal_unarranged_account_overdraft: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsePersonalUnarrangedAccountOverdraft**](ResponsePersonalUnarrangedAccountOverdraft.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

