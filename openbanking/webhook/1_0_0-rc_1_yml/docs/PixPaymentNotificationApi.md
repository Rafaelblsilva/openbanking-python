# webhook_1_0_0-rc_1_yml.PixPaymentNotificationApi

All URIs are relative to *https://api.banco.com.br/open-banking/webhook/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pix_payment_notification**](PixPaymentNotificationApi.md#pix_payment_notification) | **POST** /payments/{versionApi}/pix/payments/{paymentId} | Notificações de mudanças de estados do pagamento: Arranjo Pix da API de Iniciação de Pagamentos.

# **pix_payment_notification**
> pix_payment_notification(body, x_webhook_interaction_id, payment_id, version_api)

Notificações de mudanças de estados do pagamento: Arranjo Pix da API de Iniciação de Pagamentos.

Notificações de mudanças de estados do pagamento: Arranjo Pix da API de Iniciação de Pagamentos.

### Example
```python
from __future__ import print_function
import time
import webhook_1_0_0-rc_1_yml
from webhook_1_0_0-rc_1_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = webhook_1_0_0-rc_1_yml.PixPaymentNotificationApi()
body = webhook_1_0_0-rc_1_yml.RequestBodyWebhook() # RequestBodyWebhook | Payload enviado para notificar a alteração no estado do pagamento.
x_webhook_interaction_id = 'x_webhook_interaction_id_example' # str | Identificador único para cada tentativa de notificação realizada. O identificador deverá seguir o padrão UID [RFC4122](https://tools.ietf.org/html/rfc4122).
payment_id = 'payment_id_example' # str | Identificador da operação de pagamento.
version_api = 'version_api_example' # str | Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook

try:
    # Notificações de mudanças de estados do pagamento: Arranjo Pix da API de Iniciação de Pagamentos.
    api_instance.pix_payment_notification(body, x_webhook_interaction_id, payment_id, version_api)
except ApiException as e:
    print("Exception when calling PixPaymentNotificationApi->pix_payment_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestBodyWebhook**](RequestBodyWebhook.md)| Payload enviado para notificar a alteração no estado do pagamento. | 
 **x_webhook_interaction_id** | **str**| Identificador único para cada tentativa de notificação realizada. O identificador deverá seguir o padrão UID [RFC4122](https://tools.ietf.org/html/rfc4122). | 
 **payment_id** | **str**| Identificador da operação de pagamento. | 
 **version_api** | **str**| Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

