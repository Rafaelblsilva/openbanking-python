# webhook_1_1_0_yml.NoRedirectEnrollmentIdNotificationApi

All URIs are relative to *https://api.banco.com.br/open-banking/webhook/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrollment_id_notification**](NoRedirectEnrollmentIdNotificationApi.md#enrollment_id_notification) | **POST** /enrollments/{versionApi}/enrollments/{enrollmentId} | Notificações de mudanças de estados do vínculo de conta da API - Pagamentos sem Redirecionamento.

# **enrollment_id_notification**
> enrollment_id_notification(body, x_webhook_interaction_id, enrollment_id, version_api)

Notificações de mudanças de estados do vínculo de conta da API - Pagamentos sem Redirecionamento.

Notificações de mudanças de estados do vínculo de conta da API - Pagamentos sem Redirecionamento.

### Example
```python
from __future__ import print_function
import time
import webhook_1_1_0_yml
from webhook_1_1_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = webhook_1_1_0_yml.NoRedirectEnrollmentIdNotificationApi()
body = webhook_1_1_0_yml.RequestBodyWebhook() # RequestBodyWebhook | Payload enviado para notificar a alteração no estado do vínculo.
x_webhook_interaction_id = 'x_webhook_interaction_id_example' # str | Identificador único para cada tentativa de notificação realizada. Caso haja retentativas de notificação para o mesmo evento, este identificador não poderá ser reaproveitado da notificação anterior. O identificador deverá seguir o padrão UUID [RFC4122](https://tools.ietf.org/html/rfc4122).
enrollment_id = 'enrollment_id_example' # str | Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na RFC8141 é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização.
version_api = 'version_api_example' # str | Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook

try:
    # Notificações de mudanças de estados do vínculo de conta da API - Pagamentos sem Redirecionamento.
    api_instance.enrollment_id_notification(body, x_webhook_interaction_id, enrollment_id, version_api)
except ApiException as e:
    print("Exception when calling NoRedirectEnrollmentIdNotificationApi->enrollment_id_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestBodyWebhook**](RequestBodyWebhook.md)| Payload enviado para notificar a alteração no estado do vínculo. | 
 **x_webhook_interaction_id** | **str**| Identificador único para cada tentativa de notificação realizada. Caso haja retentativas de notificação para o mesmo evento, este identificador não poderá ser reaproveitado da notificação anterior. O identificador deverá seguir o padrão UUID [RFC4122](https://tools.ietf.org/html/rfc4122). | 
 **enrollment_id** | **str**| Identificador único do vínculo de conta criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na RFC8141 é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. | 
 **version_api** | **str**| Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

