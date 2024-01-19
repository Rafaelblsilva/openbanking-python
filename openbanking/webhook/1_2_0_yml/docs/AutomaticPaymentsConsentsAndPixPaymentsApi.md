# webhook_1_2_0_yml.AutomaticPaymentsConsentsAndPixPaymentsApi

All URIs are relative to *https://api.banco.com.br/open-banking/webhook/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recurring_consent_id_notification**](AutomaticPaymentsConsentsAndPixPaymentsApi.md#recurring_consent_id_notification) | **POST** /automatic-payments/{versionApi}/recurring-consents/{recurringConsentId} | Notificações de mudanças da entidade de consentimentos da API de Pagamentos automáticos.
[**recurring_payment_id_notification**](AutomaticPaymentsConsentsAndPixPaymentsApi.md#recurring_payment_id_notification) | **POST** /automatic-payments/{versionApi}/pix/recurring-payments/{recurringPaymentId} | Notificações de mudanças da entidade de pagamentos da API de Pagamentos automáticos.

# **recurring_consent_id_notification**
> recurring_consent_id_notification(body, x_webhook_interaction_id, recurring_consent_id, version_api)

Notificações de mudanças da entidade de consentimentos da API de Pagamentos automáticos.

Notificações de mudanças da entidade de consentimentos da API de Pagamentos automáticos.

### Example
```python
from __future__ import print_function
import time
import webhook_1_2_0_yml
from webhook_1_2_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = webhook_1_2_0_yml.AutomaticPaymentsConsentsAndPixPaymentsApi()
body = webhook_1_2_0_yml.RequestBodyWebhook() # RequestBodyWebhook | Payload enviado para notificar a alteração na entidade do consentimento de longa duração.
x_webhook_interaction_id = 'x_webhook_interaction_id_example' # str | Identificador único para cada tentativa de notificação realizada. O identificador deverá seguir o padrão UID [RFC4122](https://tools.ietf.org/html/rfc4122).
recurring_consent_id = 'recurring_consent_id_example' # str | O recurringConsentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://datatracker.ietf.org/doc/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para recurringConsentId temos:  - o namespace(urn).  - o identificador associado ao namespace da instituição transnmissora (bancoex).  - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://datatracker.ietf.org/doc/html/rfc8141). 
version_api = 'version_api_example' # str | Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook

try:
    # Notificações de mudanças da entidade de consentimentos da API de Pagamentos automáticos.
    api_instance.recurring_consent_id_notification(body, x_webhook_interaction_id, recurring_consent_id, version_api)
except ApiException as e:
    print("Exception when calling AutomaticPaymentsConsentsAndPixPaymentsApi->recurring_consent_id_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestBodyWebhook**](RequestBodyWebhook.md)| Payload enviado para notificar a alteração na entidade do consentimento de longa duração. | 
 **x_webhook_interaction_id** | **str**| Identificador único para cada tentativa de notificação realizada. O identificador deverá seguir o padrão UID [RFC4122](https://tools.ietf.org/html/rfc4122). | 
 **recurring_consent_id** | **str**| O recurringConsentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://datatracker.ietf.org/doc/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para recurringConsentId temos:  - o namespace(urn).  - o identificador associado ao namespace da instituição transnmissora (bancoex).  - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://datatracker.ietf.org/doc/html/rfc8141).  | 
 **version_api** | **str**| Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recurring_payment_id_notification**
> recurring_payment_id_notification(body, x_webhook_interaction_id, recurring_payment_id, version_api)

Notificações de mudanças da entidade de pagamentos da API de Pagamentos automáticos.

Notificações de mudanças da entidade de pagamentos da API de Pagamentos automáticos.

### Example
```python
from __future__ import print_function
import time
import webhook_1_2_0_yml
from webhook_1_2_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = webhook_1_2_0_yml.AutomaticPaymentsConsentsAndPixPaymentsApi()
body = webhook_1_2_0_yml.RequestBodyWebhook() # RequestBodyWebhook | Payload enviado para notificar a alteração na entidade do pagamento automático.
x_webhook_interaction_id = 'x_webhook_interaction_id_example' # str | Identificador único para cada tentativa de notificação realizada. O identificador deverá seguir o padrão UID [RFC4122](https://tools.ietf.org/html/rfc4122).
recurring_payment_id = 'recurring_payment_id_example' # str | Identificador da operação de pagamento.
version_api = 'version_api_example' # str | Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook

try:
    # Notificações de mudanças da entidade de pagamentos da API de Pagamentos automáticos.
    api_instance.recurring_payment_id_notification(body, x_webhook_interaction_id, recurring_payment_id, version_api)
except ApiException as e:
    print("Exception when calling AutomaticPaymentsConsentsAndPixPaymentsApi->recurring_payment_id_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestBodyWebhook**](RequestBodyWebhook.md)| Payload enviado para notificar a alteração na entidade do pagamento automático. | 
 **x_webhook_interaction_id** | **str**| Identificador único para cada tentativa de notificação realizada. O identificador deverá seguir o padrão UID [RFC4122](https://tools.ietf.org/html/rfc4122). | 
 **recurring_payment_id** | **str**| Identificador da operação de pagamento. | 
 **version_api** | **str**| Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

