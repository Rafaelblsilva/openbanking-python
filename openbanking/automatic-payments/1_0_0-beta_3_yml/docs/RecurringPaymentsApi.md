# automatic-payments_1_0_0-beta_3_yml.RecurringPaymentsApi

All URIs are relative to *https://api.banco.com.br/open-banking/automatic-payments/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**automatic_payments_get_pix_recurring_payments**](RecurringPaymentsApi.md#automatic_payments_get_pix_recurring_payments) | **GET** /pix/recurring-payments | Busca informações de transações de pagamentos associadas a um consentimento.
[**automatic_payments_get_pix_recurring_payments_payment_id**](RecurringPaymentsApi.md#automatic_payments_get_pix_recurring_payments_payment_id) | **GET** /pix/recurring-payments/{recurringPaymentId} | Busca informações de uma transação de pagamento.
[**automatic_payments_patch_pix_recurring_payments_payment_id**](RecurringPaymentsApi.md#automatic_payments_patch_pix_recurring_payments_payment_id) | **PATCH** /pix/recurring-payments/{recurringPaymentId} | Cancelamento de solicitação de pagamento automático.
[**automatic_payments_post_pix_recurring_payments**](RecurringPaymentsApi.md#automatic_payments_post_pix_recurring_payments) | **POST** /pix/recurring-payments | Cria uma transação de pagamento.

# **automatic_payments_get_pix_recurring_payments**
> ResponseRecurringPixPayment automatic_payments_get_pix_recurring_payments(authorization, x_fapi_interaction_id, recurring_consent_id, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, start_date=start_date, end_date=end_date)

Busca informações de transações de pagamentos associadas a um consentimento.

Método para buscar informações sobre um conjunto de pagamentos associados ao mesmo recurringConsentId.  Também é possível enviar uma data de início (startDate) e final (endDate), caso a busca seja por transações em uma determinada janela de tempo. 

### Example
```python
from __future__ import print_function
import time
import automatic-payments_1_0_0-beta_3_yml
from automatic-payments_1_0_0-beta_3_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2ClientCredentials
configuration = automatic-payments_1_0_0-beta_3_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = automatic-payments_1_0_0-beta_3_yml.RecurringPaymentsApi(automatic-payments_1_0_0-beta_3_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
recurring_consent_id = 'recurring_consent_id_example' # str | O `recurringConsentId` é o identificador único do consentimento de longa duração e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independe da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para `recurringConsentId` temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora (bancoex). - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o iniciador. (optional)
start_date = 'start_date_example' # str | Data inicial de corte da ocorrência do pagamento ligada ao consentimento de longa duração. (optional)
end_date = 'end_date_example' # str | Data final de corte para recuperação da ocorrência do pagamento ligada ao consentimento de longa duração. (optional)

try:
    # Busca informações de transações de pagamentos associadas a um consentimento.
    api_response = api_instance.automatic_payments_get_pix_recurring_payments(authorization, x_fapi_interaction_id, recurring_consent_id, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringPaymentsApi->automatic_payments_get_pix_recurring_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **recurring_consent_id** | **str**| O &#x60;recurringConsentId&#x60; é o identificador único do consentimento de longa duração e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independe da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para &#x60;recurringConsentId&#x60; temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora (bancoex). - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o iniciador. | [optional] 
 **start_date** | **str**| Data inicial de corte da ocorrência do pagamento ligada ao consentimento de longa duração. | [optional] 
 **end_date** | **str**| Data final de corte para recuperação da ocorrência do pagamento ligada ao consentimento de longa duração. | [optional] 

### Return type

[**ResponseRecurringPixPayment**](ResponseRecurringPixPayment.md)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **automatic_payments_get_pix_recurring_payments_payment_id**
> ResponseRecurringPaymentsIdRead automatic_payments_get_pix_recurring_payments_payment_id(authorization, x_fapi_interaction_id, recurring_payment_id, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)

Busca informações de uma transação de pagamento.

Método para buscar informações sobre um pagamento.

### Example
```python
from __future__ import print_function
import time
import automatic-payments_1_0_0-beta_3_yml
from automatic-payments_1_0_0-beta_3_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2ClientCredentials
configuration = automatic-payments_1_0_0-beta_3_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = automatic-payments_1_0_0-beta_3_yml.RecurringPaymentsApi(automatic-payments_1_0_0-beta_3_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
recurring_payment_id = 'recurring_payment_id_example' # str | Identificador da operação de pagamento.
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o iniciador. (optional)

try:
    # Busca informações de uma transação de pagamento.
    api_response = api_instance.automatic_payments_get_pix_recurring_payments_payment_id(authorization, x_fapi_interaction_id, recurring_payment_id, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringPaymentsApi->automatic_payments_get_pix_recurring_payments_payment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **recurring_payment_id** | **str**| Identificador da operação de pagamento. | 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o iniciador. | [optional] 

### Return type

[**ResponseRecurringPaymentsIdRead**](ResponseRecurringPaymentsIdRead.md)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **automatic_payments_patch_pix_recurring_payments_payment_id**
> ResponseRecurringPaymentsIdRead automatic_payments_patch_pix_recurring_payments_payment_id(body, authorization, x_fapi_interaction_id, x_idempotency_key, recurring_payment_id, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)

Cancelamento de solicitação de pagamento automático.

Esse endpoint deve ser usado para cancelar as transações que estejam em uma das seguintes situações:  Agendada com sucesso (SCHD), retida para análise (PDNG). Caso a requisição seja bem sucedida, a transação vai para a situação CANC.   Caso o status do pagamento seja diferente de SCHD/PDNG ou alguma outra regra de negócio impeça o cancelamento, a requisição PATCH retorna  HTTP Status 422 com o code PAGAMENTO_NAO_PERMITE_CANCELAMENTO.   Caso receba um 422, a iniciadora deve fazer uma requisição GET no pagamento para verificar a situação atual dele, bem como detalhes associados.   [Restrição] Para o Pix Automático (“recurringConfiguration” igual a “automatic”) tanto o recebedor quanto o pagador poderão realizar o  cancelamento, sendo permitido ao recebedor a solicitação de cancelamento até as 22:00 (Horário de Brasília) e ao pagador até as 23:59  (Horário de Brasília) do dia anterior à data de efetivação do pagamento. 

### Example
```python
from __future__ import print_function
import time
import automatic-payments_1_0_0-beta_3_yml
from automatic-payments_1_0_0-beta_3_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2ClientCredentials
configuration = automatic-payments_1_0_0-beta_3_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = automatic-payments_1_0_0-beta_3_yml.RecurringPaymentsApi(automatic-payments_1_0_0-beta_3_yml.ApiClient(configuration))
body = automatic-payments_1_0_0-beta_3_yml.PatchPixPayment() # PatchPixPayment | Atualização do Pagamento Recorrente.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
recurring_payment_id = 'recurring_payment_id_example' # str | Identificador da operação de pagamento.
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o iniciador. (optional)

try:
    # Cancelamento de solicitação de pagamento automático.
    api_response = api_instance.automatic_payments_patch_pix_recurring_payments_payment_id(body, authorization, x_fapi_interaction_id, x_idempotency_key, recurring_payment_id, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringPaymentsApi->automatic_payments_patch_pix_recurring_payments_payment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchPixPayment**](PatchPixPayment.md)| Atualização do Pagamento Recorrente. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **recurring_payment_id** | **str**| Identificador da operação de pagamento. | 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o iniciador. | [optional] 

### Return type

[**ResponseRecurringPaymentsIdRead**](ResponseRecurringPaymentsIdRead.md)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **automatic_payments_post_pix_recurring_payments**
> ResponseRecurringPaymentsIdPost automatic_payments_post_pix_recurring_payments(body, authorization, x_fapi_interaction_id, x_idempotency_key, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)

Cria uma transação de pagamento.

Método para criação de uma transação de pagamento. Retorna um recurringPaymentId.

### Example
```python
from __future__ import print_function
import time
import automatic-payments_1_0_0-beta_3_yml
from automatic-payments_1_0_0-beta_3_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: NonRedirectAuthorizationCode
configuration = automatic-payments_1_0_0-beta_3_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = automatic-payments_1_0_0-beta_3_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = automatic-payments_1_0_0-beta_3_yml.RecurringPaymentsApi(automatic-payments_1_0_0-beta_3_yml.ApiClient(configuration))
body = automatic-payments_1_0_0-beta_3_yml.CreateRecurringPixPayment() # CreateRecurringPixPayment | Payload para criação da iniciação do pagamento Pix.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o iniciador. (optional)

try:
    # Cria uma transação de pagamento.
    api_response = api_instance.automatic_payments_post_pix_recurring_payments(body, authorization, x_fapi_interaction_id, x_idempotency_key, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringPaymentsApi->automatic_payments_post_pix_recurring_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRecurringPixPayment**](CreateRecurringPixPayment.md)| Payload para criação da iniciação do pagamento Pix. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o iniciador. | [optional] 

### Return type

[**ResponseRecurringPaymentsIdPost**](ResponseRecurringPaymentsIdPost.md)

### Authorization

[NonRedirectAuthorizationCode](../README.md#NonRedirectAuthorizationCode), [OAuth2AuthorizationCode](../README.md#OAuth2AuthorizationCode)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

