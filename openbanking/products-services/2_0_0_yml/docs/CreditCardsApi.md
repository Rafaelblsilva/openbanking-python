# products-services_2_0_0_yml.CreditCardsApi

All URIs are relative to *http://api.banco.com.br/open-banking/products-services/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_credit_cards**](CreditCardsApi.md#get_business_credit_cards) | **GET** /business-credit-cards | Obtém dados sobre cartões de crédito pessoa jurídica
[**get_personal_credit_cards**](CreditCardsApi.md#get_personal_credit_cards) | **GET** /personal-credit-cards | Obtém dados sobre cartões de crédito pessoa natural

# **get_business_credit_cards**
> BusinessCreditCardResponse get_business_credit_cards()

Obtém dados sobre cartões de crédito pessoa jurídica

Obtém dados sobre cartões de crédito pessoa jurídica

### Example
```python
from __future__ import print_function
import time
import products-services_2_0_0_yml
from products-services_2_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_2_0_0_yml.CreditCardsApi()

try:
    # Obtém dados sobre cartões de crédito pessoa jurídica
    api_response = api_instance.get_business_credit_cards()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardsApi->get_business_credit_cards: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BusinessCreditCardResponse**](BusinessCreditCardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_credit_cards**
> PersonalCreditCardResponse get_personal_credit_cards()

Obtém dados sobre cartões de crédito pessoa natural

Obtém dados sobre cartões de crédito pessoa natural

### Example
```python
from __future__ import print_function
import time
import products-services_2_0_0_yml
from products-services_2_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = products-services_2_0_0_yml.CreditCardsApi()

try:
    # Obtém dados sobre cartões de crédito pessoa natural
    api_response = api_instance.get_personal_credit_cards()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardsApi->get_personal_credit_cards: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PersonalCreditCardResponse**](PersonalCreditCardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

