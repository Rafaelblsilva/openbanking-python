# enrollments_1_1_0_yml.VnculoDeDispositivoApi

All URIs are relative to *https://mtls-api.banco.com.br/open-banking/enrollments/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_enrollment**](VnculoDeDispositivoApi.md#delete_enrollment) | **PATCH** /enrollments/{enrollmentId} | Revogar ou rejeitar vínculo de conta.
[**enrollment_create_fido_registration_options**](VnculoDeDispositivoApi.md#enrollment_create_fido_registration_options) | **POST** /enrollments/{enrollmentId}/fido-registration-options | Obter parâmetros para criação de credenciais FIDO2.
[**enrollment_create_fido_signing_options**](VnculoDeDispositivoApi.md#enrollment_create_fido_signing_options) | **POST** /enrollments/{enrollmentId}/fido-sign-options | Obter parâmetros para autenticação FIDO2.
[**enrollment_register_fido_credential**](VnculoDeDispositivoApi.md#enrollment_register_fido_credential) | **POST** /enrollments/{enrollmentId}/fido-registration | Associação da credencial FIDO2 ao vínculo de conta.
[**get_enrollment**](VnculoDeDispositivoApi.md#get_enrollment) | **GET** /enrollments/{enrollmentId} | Consultar vínculo de conta.
[**post_enrollments**](VnculoDeDispositivoApi.md#post_enrollments) | **POST** /enrollments | Criar vínculo de conta.
[**risk_signals**](VnculoDeDispositivoApi.md#risk_signals) | **POST** /enrollments/{enrollmentId}/risk-signals | Envio de sinais de risco para iniciação do vínculo de dispositivo

# **delete_enrollment**
> delete_enrollment(body, authorization, x_fapi_interaction_id, x_idempotency_key, enrollment_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)

Revogar ou rejeitar vínculo de conta.

Método para revogar ou rejeitar um vínculo de conta. Após a execução com sucesso deste método irreversível, o vínculo de conta não poderá mais ser utilizado para autenticação nem autorização de iniciação de pagamentos. Os conceitos de revogação e rejeição estão associados à máquina de estados do vínculo de conta\\:  • Revogação: Cancelamento de um vínculo de conta no status \"AUTHORISED\";  • Rejeição: Cancelamento do vínculo de conta nos status \"AWATING_RISK_SIGNALS\", \"AWATING_ENROLLMENT\" e \"AWAITING_ACCOUNT_HOLDER_VALIDATION\"  Cabe ao cliente desta API distinguir entre os dois cenários para determinar o motivo adequado. 

### Example
```python
from __future__ import print_function
import time
import enrollments_1_1_0_yml
from enrollments_1_1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2ClientCredentials
configuration = enrollments_1_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = enrollments_1_1_0_yml.VnculoDeDispositivoApi(enrollments_1_1_0_yml.ApiClient(configuration))
body = enrollments_1_1_0_yml.EnrollmentsEnrollmentIdBody() # EnrollmentsEnrollmentIdBody | Dados para regovação do vínculo de conta.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
enrollment_id = enrollments_1_1_0_yml.EnrollmentId() # EnrollmentId | Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com a iniciadora. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Revogar ou rejeitar vínculo de conta.
    api_instance.delete_enrollment(body, authorization, x_fapi_interaction_id, x_idempotency_key, enrollment_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
except ApiException as e:
    print("Exception when calling VnculoDeDispositivoApi->delete_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrollmentsEnrollmentIdBody**](EnrollmentsEnrollmentIdBody.md)| Dados para regovação do vínculo de conta. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **enrollment_id** | [**EnrollmentId**](.md)| Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com a iniciadora. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/json; charset=utf-8, application/jwt, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_create_fido_registration_options**
> EnrollmentFidoRegistrationOptions enrollment_create_fido_registration_options(body, authorization, x_fapi_interaction_id, x_idempotency_key, enrollment_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)

Obter parâmetros para criação de credenciais FIDO2.

Método para obter os parâmetros para criação de uma nova credencial FIDO2. Um novo challenge deve ser criado a cada chamada. Os parâmetros da resposta devem ser compatíveis com a definição [W3C](https://www.w3.org/TR/webauthn-2/#dictionary-makecredentialoptions) 

### Example
```python
from __future__ import print_function
import time
import enrollments_1_1_0_yml
from enrollments_1_1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = enrollments_1_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = enrollments_1_1_0_yml.VnculoDeDispositivoApi(enrollments_1_1_0_yml.ApiClient(configuration))
body = enrollments_1_1_0_yml.EnrollmentFidoOptionsInput() # EnrollmentFidoOptionsInput | Payload para criação de parâmetros de registro de nova credencial FIDO2.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
enrollment_id = enrollments_1_1_0_yml.EnrollmentId() # EnrollmentId | Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com a iniciadora. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obter parâmetros para criação de credenciais FIDO2.
    api_response = api_instance.enrollment_create_fido_registration_options(body, authorization, x_fapi_interaction_id, x_idempotency_key, enrollment_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnculoDeDispositivoApi->enrollment_create_fido_registration_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrollmentFidoOptionsInput**](EnrollmentFidoOptionsInput.md)| Payload para criação de parâmetros de registro de nova credencial FIDO2. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **enrollment_id** | [**EnrollmentId**](.md)| Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com a iniciadora. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**EnrollmentFidoRegistrationOptions**](EnrollmentFidoRegistrationOptions.md)

### Authorization

[OAuth2AuthorizationCode](../README.md#OAuth2AuthorizationCode)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_create_fido_signing_options**
> EnrollmentFidoSignOptions enrollment_create_fido_signing_options(body, authorization, x_fapi_interaction_id, x_idempotency_key, enrollment_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)

Obter parâmetros para autenticação FIDO2.

Método para obter os parâmetros para autenticação a partir de uma credencial FIDO2 previamente registrada. Um novo challenge deve ser criado a cada chamada. Os parâmetros da resposta devem ser compatíveis com a [definição W3C](https://www.w3.org/TR/webauthn-2/#dictionary-assertion-options) 

### Example
```python
from __future__ import print_function
import time
import enrollments_1_1_0_yml
from enrollments_1_1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2ClientCredentials
configuration = enrollments_1_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = enrollments_1_1_0_yml.VnculoDeDispositivoApi(enrollments_1_1_0_yml.ApiClient(configuration))
body = enrollments_1_1_0_yml.EnrollmentIdFidosignoptionsBody() # EnrollmentIdFidosignoptionsBody | Payload para autenticação a partir de uma credencial FIDO2 previamente registrada.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
enrollment_id = enrollments_1_1_0_yml.EnrollmentId() # EnrollmentId | Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com a iniciadora. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obter parâmetros para autenticação FIDO2.
    api_response = api_instance.enrollment_create_fido_signing_options(body, authorization, x_fapi_interaction_id, x_idempotency_key, enrollment_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnculoDeDispositivoApi->enrollment_create_fido_signing_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrollmentIdFidosignoptionsBody**](EnrollmentIdFidosignoptionsBody.md)| Payload para autenticação a partir de uma credencial FIDO2 previamente registrada. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **enrollment_id** | [**EnrollmentId**](.md)| Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com a iniciadora. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**EnrollmentFidoSignOptions**](EnrollmentFidoSignOptions.md)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_register_fido_credential**
> enrollment_register_fido_credential(body, authorization, x_fapi_interaction_id, x_idempotency_key, enrollment_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)

Associação da credencial FIDO2 ao vínculo de conta.

O vínculo de conta deve estar no status \"AWAITING_ENROLLMENT\".  Após o registro com sucesso, o vínculo de conta deve transitar ao status \"AUTHORISED\". A falha de verificação da credencial FIDO2 deve causar a rejeição do vínculo de conta por parte da detentora, uma vez que não é possível reusar um mesmo \"challenge\" para mais de um registro. 

### Example
```python
from __future__ import print_function
import time
import enrollments_1_1_0_yml
from enrollments_1_1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = enrollments_1_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = enrollments_1_1_0_yml.VnculoDeDispositivoApi(enrollments_1_1_0_yml.ApiClient(configuration))
body = enrollments_1_1_0_yml.EnrollmentFidoRegistration() # EnrollmentFidoRegistration | Payload para criação de parâmetros de registro de nova credencial FIDO2.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
enrollment_id = enrollments_1_1_0_yml.EnrollmentId() # EnrollmentId | Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com a iniciadora. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Associação da credencial FIDO2 ao vínculo de conta.
    api_instance.enrollment_register_fido_credential(body, authorization, x_fapi_interaction_id, x_idempotency_key, enrollment_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
except ApiException as e:
    print("Exception when calling VnculoDeDispositivoApi->enrollment_register_fido_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrollmentFidoRegistration**](EnrollmentFidoRegistration.md)| Payload para criação de parâmetros de registro de nova credencial FIDO2. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **enrollment_id** | [**EnrollmentId**](.md)| Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com a iniciadora. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2AuthorizationCode](../README.md#OAuth2AuthorizationCode)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/json; charset=utf-8, application/jwt, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrollment**
> ResponseEnrollment get_enrollment(enrollment_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)

Consultar vínculo de conta.

Método para consultar um vínculo de conta para iniciação de pagamento sem redirecionamento.

### Example
```python
from __future__ import print_function
import time
import enrollments_1_1_0_yml
from enrollments_1_1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2ClientCredentials
configuration = enrollments_1_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = enrollments_1_1_0_yml.VnculoDeDispositivoApi(enrollments_1_1_0_yml.ApiClient(configuration))
enrollment_id = enrollments_1_1_0_yml.EnrollmentId() # EnrollmentId | Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com a iniciadora. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Consultar vínculo de conta.
    api_response = api_instance.get_enrollment(enrollment_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnculoDeDispositivoApi->get_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_id** | [**EnrollmentId**](.md)| Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com a iniciadora. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponseEnrollment**](ResponseEnrollment.md)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_enrollments**
> ResponseCreateEnrollment post_enrollments(body, authorization, x_fapi_interaction_id, x_idempotency_key, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)

Criar vínculo de conta.

Método para criar um novo vínculo de conta. Retorna um enrollment em status AWAITING_RISK_SIGNALS.   

### Example
```python
from __future__ import print_function
import time
import enrollments_1_1_0_yml
from enrollments_1_1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2ClientCredentials
configuration = enrollments_1_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = enrollments_1_1_0_yml.VnculoDeDispositivoApi(enrollments_1_1_0_yml.ApiClient(configuration))
body = enrollments_1_1_0_yml.CreateEnrollment() # CreateEnrollment | Payload para criação de vínculo de conta.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com a iniciadora. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Criar vínculo de conta.
    api_response = api_instance.post_enrollments(body, authorization, x_fapi_interaction_id, x_idempotency_key, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnculoDeDispositivoApi->post_enrollments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEnrollment**](CreateEnrollment.md)| Payload para criação de vínculo de conta. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com a iniciadora. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponseCreateEnrollment**](ResponseCreateEnrollment.md)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/jwt, application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **risk_signals**
> risk_signals(body, authorization, x_fapi_interaction_id, x_idempotency_key, enrollment_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)

Envio de sinais de risco para iniciação do vínculo de dispositivo

Envio de sinais de risco para iniciação do vínculo de dispositivo, o status do enrollment deve estar em `AWAITING_RISK_SIGNALS`. Após recebimento com sucesso dos sinais, o status do enrollment deve transitar para `AWAITING_ACCOUNT_HOLDER_VALIDATION`. 

### Example
```python
from __future__ import print_function
import time
import enrollments_1_1_0_yml
from enrollments_1_1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2ClientCredentials
configuration = enrollments_1_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = enrollments_1_1_0_yml.VnculoDeDispositivoApi(enrollments_1_1_0_yml.ApiClient(configuration))
body = enrollments_1_1_0_yml.RiskSignals() # RiskSignals | Payload para criação de vínculo de conta.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora.
x_idempotency_key = 'x_idempotency_key_example' # str | Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência.
enrollment_id = enrollments_1_1_0_yml.EnrollmentId() # EnrollmentId | Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com a iniciadora. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Envio de sinais de risco para iniciação do vínculo de dispositivo
    api_instance.risk_signals(body, authorization, x_fapi_interaction_id, x_idempotency_key, enrollment_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
except ApiException as e:
    print("Exception when calling VnculoDeDispositivoApi->risk_signals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RiskSignals**](RiskSignals.md)| Payload para criação de vínculo de conta. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. | 
 **x_idempotency_key** | **str**| Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. | 
 **enrollment_id** | [**EnrollmentId**](.md)| Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para enrollmentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com a iniciadora. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2ClientCredentials](../README.md#OAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/json; charset=utf-8, application/jwt, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

