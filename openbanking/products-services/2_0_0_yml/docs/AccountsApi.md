# products-services_2_0_0_yml.AccountsApi

All URIs are relative to *http://api.banco.com.br/open-banking/products-services/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_accounts**](AccountsApi.md#get_business_accounts) | **GET** /business-accounts | Obtém dados das contas pessoa jurídica
[**get_personal_accounts**](AccountsApi.md#get_personal_accounts) | **GET** /personal-accounts | Obtém dados das contas pessoa natural

# **get_business_accounts**
> ResponseBusinessAccounts get_business_accounts()

Obtém dados das contas pessoa jurídica

Obtém dados das contas pessoa jurídica

### Example
```python
from __future__ import print_function
import time
import products-services_2_0_0_yml
from products-services_2_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_2_0_0_yml.AccountsApi()

try:
    # Obtém dados das contas pessoa jurídica
    api_response = api_instance.get_business_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_business_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseBusinessAccounts**](ResponseBusinessAccounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_accounts**
> ResponsePersonalAccounts get_personal_accounts()

Obtém dados das contas pessoa natural

Obtém dados das contas

### Example
```python
from __future__ import print_function
import time
import products-services_2_0_0_yml
from products-services_2_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_2_0_0_yml.AccountsApi()

try:
    # Obtém dados das contas pessoa natural
    api_response = api_instance.get_personal_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_personal_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsePersonalAccounts**](ResponsePersonalAccounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

