# products-services_3_0_0_yml.LoansApi

All URIs are relative to *http://api.banco.com.br/open-banking/products-services/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_loans**](LoansApi.md#get_business_loans) | **GET** /business-loans | Obtém dados sobre empréstimos pessoa jurídica
[**get_personal_loans**](LoansApi.md#get_personal_loans) | **GET** /personal-loans | Obtém dados sobre empréstimos pessoa natural

# **get_business_loans**
> ResponseBusinessLoans get_business_loans()

Obtém dados sobre empréstimos pessoa jurídica

Obtém dados sobre empréstimos pessoa jurídica

### Example
```python
from __future__ import print_function
import time
import products-services_3_0_0_yml
from products-services_3_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_3_0_0_yml.LoansApi()

try:
    # Obtém dados sobre empréstimos pessoa jurídica
    api_response = api_instance.get_business_loans()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->get_business_loans: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseBusinessLoans**](ResponseBusinessLoans.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_loans**
> ResponsePersonalLoans get_personal_loans()

Obtém dados sobre empréstimos pessoa natural

Obtém dados sobre empréstimos pessoa natural

### Example
```python
from __future__ import print_function
import time
import products-services_3_0_0_yml
from products-services_3_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_3_0_0_yml.LoansApi()

try:
    # Obtém dados sobre empréstimos pessoa natural
    api_response = api_instance.get_personal_loans()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->get_personal_loans: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsePersonalLoans**](ResponsePersonalLoans.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

