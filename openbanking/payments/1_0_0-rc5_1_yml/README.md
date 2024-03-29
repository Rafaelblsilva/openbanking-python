# payments-1-0-0-rc5-1-yml
API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora  de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:   - Certificados exigidos para assinatura de mensagens:   [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Algoritmos usados para assinatura de mensagens `JWS`:   [Perfil de segurança FAPI - Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-financial-api-1_ID1.md#algorithm-considerations)  - Mensagens assinadas, `JWS` e `JWKS`:   [Guia de usuário (Receptoras e iniciadoras de pagamento)](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/tpp-user-guide.md#143-what-is-a-jwt-jwe-jws-and-jwk) 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0-rc5.1
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
import payments_1_0_0-rc5_1_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import payments_1_0_0-rc5_1_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import payments_1_0_0-rc5_1_yml
from payments_1_0_0-rc5_1_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = payments_1_0_0-rc5_1_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = payments_1_0_0-rc5_1_yml.PagamentosApi(payments_1_0_0-rc5_1_yml.ApiClient(configuration))
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

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = payments_1_0_0-rc5_1_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = payments_1_0_0-rc5_1_yml.PagamentosApi(payments_1_0_0-rc5_1_yml.ApiClient(configuration))
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

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = payments_1_0_0-rc5_1_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = payments_1_0_0-rc5_1_yml.PagamentosApi(payments_1_0_0-rc5_1_yml.ApiClient(configuration))
body = payments_1_0_0-rc5_1_yml.CreatePaymentConsent() # CreatePaymentConsent | Payload para criação do consentimento para iniciação do pagamento.
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

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = payments_1_0_0-rc5_1_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = payments_1_0_0-rc5_1_yml.PagamentosApi(payments_1_0_0-rc5_1_yml.ApiClient(configuration))
body = payments_1_0_0-rc5_1_yml.CreatePixPayment() # CreatePixPayment | Payload para criação da iniciação do pagamento Pix.
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

## Documentation for API Endpoints

All URIs are relative to *https://api.banco.com.br/open-banking/payments/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PagamentosApi* | [**payments_get_consents_consent_id**](docs/PagamentosApi.md#payments_get_consents_consent_id) | **GET** /consents/{consentId} | Consultar consentimento para iniciação de pagamento.
*PagamentosApi* | [**payments_get_pix_payments_payment_id**](docs/PagamentosApi.md#payments_get_pix_payments_payment_id) | **GET** /pix/payments/{paymentId} | Consultar iniciação de pagamento.
*PagamentosApi* | [**payments_post_consents**](docs/PagamentosApi.md#payments_post_consents) | **POST** /consents | Criar consentimento para a iniciação de pagamento.
*PagamentosApi* | [**payments_post_pix_payments**](docs/PagamentosApi.md#payments_post_pix_payments) | **POST** /pix/payments | Criar iniciação de pagamento.

## Documentation For Models

 - [BusinessEntity](docs/BusinessEntity.md)
 - [BusinessEntityDocument](docs/BusinessEntityDocument.md)
 - [CreatePaymentConsent](docs/CreatePaymentConsent.md)
 - [CreatePaymentConsentData](docs/CreatePaymentConsentData.md)
 - [CreatePixPayment](docs/CreatePixPayment.md)
 - [CreatePixPaymentData](docs/CreatePixPaymentData.md)
 - [CreditorAccount](docs/CreditorAccount.md)
 - [DebtorAccount](docs/DebtorAccount.md)
 - [EndToEndId](docs/EndToEndId.md)
 - [EnumAccountPaymentsType](docs/EnumAccountPaymentsType.md)
 - [EnumLocalInstrument](docs/EnumLocalInstrument.md)
 - [Identification](docs/Identification.md)
 - [InlineResponse422](docs/InlineResponse422.md)
 - [InlineResponse4221](docs/InlineResponse4221.md)
 - [InlineResponse4221Errors](docs/InlineResponse4221Errors.md)
 - [InlineResponse422Errors](docs/InlineResponse422Errors.md)
 - [Links](docs/Links.md)
 - [LoggedUser](docs/LoggedUser.md)
 - [LoggedUserDocument](docs/LoggedUserDocument.md)
 - [Meta](docs/Meta.md)
 - [PaymentConsent](docs/PaymentConsent.md)
 - [PaymentPix](docs/PaymentPix.md)
 - [ResponseError](docs/ResponseError.md)
 - [ResponseErrorErrors](docs/ResponseErrorErrors.md)
 - [ResponsePaymentConsent](docs/ResponsePaymentConsent.md)
 - [ResponsePaymentConsentData](docs/ResponsePaymentConsentData.md)
 - [ResponsePixPayment](docs/ResponsePixPayment.md)
 - [ResponsePixPaymentData](docs/ResponsePixPaymentData.md)
 - [XFapiInteractionId](docs/XFapiInteractionId.md)

## Documentation For Authorization


## OAuth2Security

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://authserver.example/authorization
- **Scopes**: 
 - **payments**: Escopo necessário para acesso à API Payment Initiation.

## OpenId



## Author

gt-interfaces@openbankingbr.org
