# payments_1_0_0-rc5_5_yml.PagamentosApi

All URIs are relative to *https://api.banco.com.br/open-banking/payments/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_get_consents_consent_id**](PagamentosApi.md#payments_get_consents_consent_id) | **GET** /consents/{consentId} | Consultar consentimento para iniciação de pagamento.
[**payments_get_pix_payments_payment_id**](PagamentosApi.md#payments_get_pix_payments_payment_id) | **GET** /pix/payments/{paymentId} | Consultar iniciação de pagamento.
[**payments_post_consents**](PagamentosApi.md#payments_post_consents) | **POST** /consents | Criar consentimento para a iniciação de pagamento.
[**payments_post_pix_payments**](PagamentosApi.md#payments_post_pix_payments) | **POST** /pix/payments | Criar iniciação de pagamento.

# **payments_get_consents_consent_id**
> ResponsePaymentConsent payments_get_consents_consent_id(consent_id, authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)

Consultar consentimento para iniciação de pagamento.

Método para consulta do consentimento para a iniciação de pagamento.

### Example
```python
from __future__ import print_function
import time
import payments_1_0_0-rc5_5_yml
from payments_1_0_0-rc5_5_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2ClientCredentials
configuration = payments_1_0_0-rc5_5_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = payments_1_0_0-rc5_5_yml.PagamentosApi(payments_1_0_0-rc5_5_yml.ApiClient(configuration))
consent_id = 'consent_id_example' # str | O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Consultar consentimento para iniciação de pagamento.
    api_response = api_instance.payments_get_consents_consent_id(consent_id, authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PagamentosApi->payments_get_consents_consent_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponsePaymentConsent**](ResponsePaymentConsent.md)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_get_pix_payments_payment_id**
> ResponsePixPayment payments_get_pix_payments_payment_id(payment_id, authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)

Consultar iniciação de pagamento.

Método para consultar uma iniciação de pagamento.

### Example
```python
from __future__ import print_function
import time
import payments_1_0_0-rc5_5_yml
from payments_1_0_0-rc5_5_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = payments_1_0_0-rc5_5_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuth2ClientCredentials
configuration = payments_1_0_0-rc5_5_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = payments_1_0_0-rc5_5_yml.PagamentosApi(payments_1_0_0-rc5_5_yml.ApiClient(configuration))
payment_id = 'payment_id_example' # str | Identificador da operação de pagamento.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Consultar iniciação de pagamento.
    api_response = api_instance.payments_get_pix_payments_payment_id(payment_id, authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PagamentosApi->payments_get_pix_payments_payment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Identificador da operação de pagamento. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponsePixPayment**](ResponsePixPayment.md)

### Authorization

[OAuth2AuthorizationCode](../README.md#OAuth2AuthorizationCode), [OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_post_consents**
> ResponsePaymentConsent payments_post_consents(body, authorization, x_idempotency_key, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)

Criar consentimento para a iniciação de pagamento.

Método de criação do consentimento para a iniciação de pagamento.

### Example
```python
from __future__ import print_function
import time
import payments_1_0_0-rc5_5_yml
from payments_1_0_0-rc5_5_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2ClientCredentials
configuration = payments_1_0_0-rc5_5_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = payments_1_0_0-rc5_5_yml.PagamentosApi(payments_1_0_0-rc5_5_yml.ApiClient(configuration))
body = payments_1_0_0-rc5_5_yml.CreatePaymentConsent() # CreatePaymentConsent | Payload para criação do consentimento para iniciação do pagamento.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Criar consentimento para a iniciação de pagamento.
    api_response = api_instance.payments_post_consents(body, authorization, x_idempotency_key, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PagamentosApi->payments_post_consents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePaymentConsent**](CreatePaymentConsent.md)| Payload para criação do consentimento para iniciação do pagamento. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponsePaymentConsent**](ResponsePaymentConsent.md)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_post_pix_payments**
> ResponsePixPayment payments_post_pix_payments(body, authorization, x_idempotency_key, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)

Criar iniciação de pagamento.

Método para criar uma iniciação de pagamento.

### Example
```python
from __future__ import print_function
import time
import payments_1_0_0-rc5_5_yml
from payments_1_0_0-rc5_5_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = payments_1_0_0-rc5_5_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = payments_1_0_0-rc5_5_yml.PagamentosApi(payments_1_0_0-rc5_5_yml.ApiClient(configuration))
body = payments_1_0_0-rc5_5_yml.CreatePixPayment() # CreatePixPayment | Payload para criação da iniciação do pagamento Pix.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Criar iniciação de pagamento.
    api_response = api_instance.payments_post_pix_payments(body, authorization, x_idempotency_key, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PagamentosApi->payments_post_pix_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePixPayment**](CreatePixPayment.md)| Payload para criação da iniciação do pagamento Pix. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponsePixPayment**](ResponsePixPayment.md)

### Authorization

[OAuth2AuthorizationCode](../README.md#OAuth2AuthorizationCode)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

