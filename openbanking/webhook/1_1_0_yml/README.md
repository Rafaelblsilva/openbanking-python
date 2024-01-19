# webhook-1-1-0-yml
API de Webhook é responsável por notificar eventos definidos em cada uma das APIs que possuem a funcionalidade no Open Finance Brasil.    Informações sobre endpoints suportados e funcionamento podem ser encontrados na página <a href=\"https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/105021661/Conven+o+de+Webhook\">Convenção de Webhook</a>, disponível no portal do desenvolvedor do Open Finance Brasil. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://openbanking-brasil.github.io/areadesenvolvedor/](https://openbanking-brasil.github.io/areadesenvolvedor/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import webhook_1_1_0_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import webhook_1_1_0_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import webhook_1_1_0_yml
from webhook_1_1_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = webhook_1_1_0_yml.NoRedirectEnrollmentIdNotificationApi(webhook_1_1_0_yml.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *https://api.banco.com.br/open-banking/webhook/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*NoRedirectEnrollmentIdNotificationApi* | [**enrollment_id_notification**](docs/NoRedirectEnrollmentIdNotificationApi.md#enrollment_id_notification) | **POST** /enrollments/{versionApi}/enrollments/{enrollmentId} | Notificações de mudanças de estados do vínculo de conta da API - Pagamentos sem Redirecionamento.
*PaymentsConsentsAndPIXPaymentsApi* | [**consent_notification**](docs/PaymentsConsentsAndPIXPaymentsApi.md#consent_notification) | **POST** /payments/{versionApi}/consents/{consentId} | Notificações de mudanças de estados de consentimentos da API de Iniciação de Pagamentos.
*PaymentsConsentsAndPIXPaymentsApi* | [**pix_payment_notification**](docs/PaymentsConsentsAndPIXPaymentsApi.md#pix_payment_notification) | **POST** /payments/{versionApi}/pix/payments/{paymentId} | Notificações de mudanças de estados do pagamento: Arranjo Pix da API de Iniciação de Pagamentos.

## Documentation For Models

 - [RequestBodyWebhook](docs/RequestBodyWebhook.md)
 - [RequestBodyWebhookData](docs/RequestBodyWebhookData.md)
 - [XWebhookInteractionId](docs/XWebhookInteractionId.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

gt-interfaces@openbankingbr.org