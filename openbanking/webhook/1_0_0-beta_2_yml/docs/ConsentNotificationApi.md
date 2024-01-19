# webhook_1_0_0-beta_2_yml.ConsentNotificationApi

All URIs are relative to *https://api.banco.com.br/open-banking/webhook/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consent_notification**](ConsentNotificationApi.md#consent_notification) | **POST** /payments/{versionApi}/consents/{consentId} | Notificações de mudanças de estados de consentimentos da API de Iniciação de Pagamentos.

# **consent_notification**
> consent_notification(body, x_webhook_interaction_id, consent_id, version_api)

Notificações de mudanças de estados de consentimentos da API de Iniciação de Pagamentos.

Notificações de mudanças de estados de consentimentos da API de Iniciação de Pagamentos.

### Example
```python
from __future__ import print_function
import time
import webhook_1_0_0-beta_2_yml
from webhook_1_0_0-beta_2_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = webhook_1_0_0-beta_2_yml.ConsentNotificationApi()
body = webhook_1_0_0-beta_2_yml.RequestBodyWebhook() # RequestBodyWebhook | Payload enviado para notificar a alteração no estado do consentimento.
x_webhook_interaction_id = 'x_webhook_interaction_id_example' # str | Identificador único para cada tentativa de notificação realizada. O identificador deverá seguir o padrão UID [RFC4122](https://tools.ietf.org/html/rfc4122).
consent_id = 'consent_id_example' # str | O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
version_api = 'version_api_example' # str | Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook

try:
    # Notificações de mudanças de estados de consentimentos da API de Iniciação de Pagamentos.
    api_instance.consent_notification(body, x_webhook_interaction_id, consent_id, version_api)
except ApiException as e:
    print("Exception when calling ConsentNotificationApi->consent_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestBodyWebhook**](RequestBodyWebhook.md)| Payload enviado para notificar a alteração no estado do consentimento. | 
 **x_webhook_interaction_id** | **str**| Identificador único para cada tentativa de notificação realizada. O identificador deverá seguir o padrão UID [RFC4122](https://tools.ietf.org/html/rfc4122). | 
 **consent_id** | **str**| O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \&quot;urn\&quot; e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  | 
 **version_api** | **str**| Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

