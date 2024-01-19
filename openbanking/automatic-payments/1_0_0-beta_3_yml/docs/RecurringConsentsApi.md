# automatic-payments_1_0_0-beta_3_yml.RecurringConsentsApi

All URIs are relative to *https://api.banco.com.br/open-banking/automatic-payments/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**automatic_payments_get_recurring_consents_consent_id**](RecurringConsentsApi.md#automatic_payments_get_recurring_consents_consent_id) | **GET** /recurring-consents/{recurringConsentId} | Busca informações de um consentimento.
[**automatic_payments_patch_recurring_consents_consent_id**](RecurringConsentsApi.md#automatic_payments_patch_recurring_consents_consent_id) | **PATCH** /recurring-consents/{recurringConsentId} | Revoga ou edita um consentimento.
[**automatic_payments_post_recurring_consents**](RecurringConsentsApi.md#automatic_payments_post_recurring_consents) | **POST** /recurring-consents | Cria um consentimento para transações de pagamentos.

# **automatic_payments_get_recurring_consents_consent_id**
> ResponseRecurringConsent automatic_payments_get_recurring_consents_consent_id(authorization, x_fapi_interaction_id, recurring_consent_id, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)

Busca informações de um consentimento.

Método para buscar informações sobre um consentimento de longa duração.

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
api_instance = automatic-payments_1_0_0-beta_3_yml.RecurringConsentsApi(automatic-payments_1_0_0-beta_3_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
recurring_consent_id = 'recurring_consent_id_example' # str | O `recurringConsentId` é o identificador único do consentimento de longa duração e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independe da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para `recurringConsentId` temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora (bancoex). - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o iniciador. (optional)

try:
    # Busca informações de um consentimento.
    api_response = api_instance.automatic_payments_get_recurring_consents_consent_id(authorization, x_fapi_interaction_id, recurring_consent_id, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringConsentsApi->automatic_payments_get_recurring_consents_consent_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **recurring_consent_id** | **str**| O &#x60;recurringConsentId&#x60; é o identificador único do consentimento de longa duração e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independe da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para &#x60;recurringConsentId&#x60; temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora (bancoex). - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o iniciador. | [optional] 

### Return type

[**ResponseRecurringConsent**](ResponseRecurringConsent.md)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **automatic_payments_patch_recurring_consents_consent_id**
> ResponseRecurringConsent automatic_payments_patch_recurring_consents_consent_id(body, authorization, x_fapi_interaction_id, x_idempotency_key, recurring_consent_id, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)

Revoga ou edita um consentimento.

Método para rejeitar, revogar ou editar um consentimento de longa duração:   1 - Informações sobre a revogação: - Caso bem sucedido, o consentimento vai para o status “REVOKED”; - Apenas consentimentos com status “AUTHORISED” podem ser revogados; - Pagamentos automáticos associados ao consentimento e que estão agendados para ocorrer até as 23:59h do próximo dia (a partir do dia de  solicitação da revogação) deverão ser mantidos. Pagamentos agendados para ocorrer após esse período devem ser cancelados. - Demais orientações referentes a revogação podem ser encontrados no header da API, tópico “Validações”, item 3.  2 - Informações sobre a edição:  - Os campos que são passíveis de edição e suas regras podem ser encontrados através do [link](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/198410772); - A edição é possível apenas em casos de consentimento para Pix Automático (“automatic” escolhido no oneOf do objeto “recurringConfiguration”); - O envio do item \"/data/creditors/name\" atualizará o nome do recebedor em todos os elementos do array.  3 - Informações sobre a rejeição:   - Caso haja necessidade de cancelamento de um consentimento ainda não autorizado, o iniciador poderá chamar o endpoint para mover o consentimento para REJECTED. 

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
api_instance = automatic-payments_1_0_0-beta_3_yml.RecurringConsentsApi(automatic-payments_1_0_0-beta_3_yml.ApiClient(configuration))
body = automatic-payments_1_0_0-beta_3_yml.PatchRecurringConsent() # PatchRecurringConsent | Payload para criação do consentimento para iniciação do pagamento.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
recurring_consent_id = 'recurring_consent_id_example' # str | O `recurringConsentId` é o identificador único do consentimento de longa duração e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independe da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para `recurringConsentId` temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora (bancoex). - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o iniciador. (optional)

try:
    # Revoga ou edita um consentimento.
    api_response = api_instance.automatic_payments_patch_recurring_consents_consent_id(body, authorization, x_fapi_interaction_id, x_idempotency_key, recurring_consent_id, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringConsentsApi->automatic_payments_patch_recurring_consents_consent_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchRecurringConsent**](PatchRecurringConsent.md)| Payload para criação do consentimento para iniciação do pagamento. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **recurring_consent_id** | **str**| O &#x60;recurringConsentId&#x60; é o identificador único do consentimento de longa duração e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independe da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para &#x60;recurringConsentId&#x60; temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora (bancoex). - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o iniciador. | [optional] 

### Return type

[**ResponseRecurringConsent**](ResponseRecurringConsent.md)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **automatic_payments_post_recurring_consents**
> ResponsePostRecurringConsent automatic_payments_post_recurring_consents(body, authorization, x_fapi_interaction_id, x_idempotency_key, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)

Cria um consentimento para transações de pagamentos.

Método para criação de consentimento de longa duração. Retorna um `recurringConsentId` no status AWAITING_AUTHORISATION.

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
api_instance = automatic-payments_1_0_0-beta_3_yml.RecurringConsentsApi(automatic-payments_1_0_0-beta_3_yml.ApiClient(configuration))
body = automatic-payments_1_0_0-beta_3_yml.CreateRecurringConsent() # CreateRecurringConsent | Payload para criação do consentimento para iniciação do pagamento.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o iniciador. (optional)

try:
    # Cria um consentimento para transações de pagamentos.
    api_response = api_instance.automatic_payments_post_recurring_consents(body, authorization, x_fapi_interaction_id, x_idempotency_key, x_customer_user_agent=x_customer_user_agent, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringConsentsApi->automatic_payments_post_recurring_consents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRecurringConsent**](CreateRecurringConsent.md)| Payload para criação do consentimento para iniciação do pagamento. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o iniciador. | [optional] 

### Return type

[**ResponsePostRecurringConsent**](ResponsePostRecurringConsent.md)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

