# consents-2-2-0-rc-1-yml
API que trata da criação, consulta e revogação de consentimentos para o Open Finance Brasil Dados cadastrais e transacionais - customer-data.   Não possui segregação entre pessoa natural e pessoa jurídica.      # Orientações importantes A API Consents trata dos consentimentos exclusivamente para a Dados cadastrais e transacionais do Open Finance Brasil. - As informações da instituição receptora não trafegam na API Consents – a autenticação da receptora se dá através do [DCR](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378307/Dynamic+Client+Registration).    - Na chamada para a criação do consentimento deve-se utilizar um token gerado via `client_credentials`. - Após o `POST` de criação do consentimento, o `STATUS` devolvido na resposta deverá ser `AWAITING_AUTHORISATION`. - O `STATUS` será alterado para `AUTHORISED` somente após autenticação e confirmação por parte do usuário na instituição transmissora dos dados. - Alteração obrigatória do status `AWAITING_AUTHORISATION` para `REVOKED` após 60 minutos. - Todas as datas trafegadas nesta API seguem o padrão da [RFC3339](https://tools.ietf.org/html/rfc3339) e formato \"zulu\". - A descrição do fluxo de consentimento encontra-se disponível no [Portal do desenvolvedor](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17369300/Dados+Cadastrais+e+Transacionais#Fluxo-b%C3%A1sico-de-consentimento). - O arquivo com o mapeamento completo entre `Roles`, `scopes` e `permissions` está disponibilizado no Portal do desenvolvedor, no mesmo item acima - descrição do fluxo de consentimento. - A receptora deve enviar obrigatoriamente, no pedido de criação de consentimento, todas as permissions dos agrupamentos de dados as quais ela deseja consentimento, conforme tabela abaixo:      ```   |----------------------|-------------------------------|----------------------------------------------------------|   | CATEGORIA DE DADOS   | AGRUPAMENTO                   | PERMISSIONS                                              |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Dados Cadastrais PF           | CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Informações complementares PF | CUSTOMERS_PERSONAL_ADITTIONALINFO_READ                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Dados Cadastrais PJ           | CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Informações complementares PJ | CUSTOMERS_BUSINESS_ADITTIONALINFO_READ                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Saldos                        | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_BALANCES_READ                                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Limites                       | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_OVERDRAFT_LIMITS_READ                           |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Extratos                      | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_TRANSACTIONS_READ                               |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Limites                       | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_LIMITS_READ                        |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Transações                    | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Faturas                       | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_READ                         |   |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ            |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Operações de Crédito | Dados do Contrato             | LOANS_READ                                               |   |                      |                               | LOANS_WARRANTIES_READ                                    |   |                      |                               | LOANS_SCHEDULED_INSTALMENTS_READ                         |   |                      |                               | LOANS_PAYMENTS_READ                                      |   |                      |                               | FINANCINGS_READ                                          |   |                      |                               | FINANCINGS_WARRANTIES_READ                               |   |                      |                               | FINANCINGS_SCHEDULED_INSTALMENTS_READ                    |   |                      |                               | FINANCINGS_PAYMENTS_READ                                 |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_READ                       |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_WARRANTIES_READ            |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_SCHEDULED_INSTALMENTS_READ |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_PAYMENTS_READ              |   |                      |                               | INVOICE_FINANCINGS_READ                                  |   |                      |                               | INVOICE_FINANCINGS_WARRANTIES_READ                       |   |                      |                               | INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ            |   |                      |                               | INVOICE_FINANCINGS_PAYMENTS_READ                         |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Investimento         | Dados da Operação             | BANK_FIXED_INCOMES_READ                                  |   |                      |                               | CREDIT_FIXED_INCOMES_READ                                |   |                      |                               | FUNDS_READ                                               |   |                      |                               | VARIABLE_INCOMES_READ                                    |   |                      |                               | TREASURE_TITLES_READ                                     |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   ``` - A instituição transmissora deve validar o preenchimento correto desses agrupamentos no momento da geração do consentimento. - Caso a instiuição receptora envie permissões divergentes ao agrupamento especificado na tabela, a transmissora deve rejeitar o pedido da receptora dando retorno HTTP Status Code 400. - A transmissora deve retornar, da lista de permissions requisitadas, apenas o subconjunto de permissions por ela suportada, removendo da lista as permissions de produtos não suportados e retornando HTTP Status Code 201. Caso não restem permissões funcionais, a instituição transmissora deve retornar o erro HTTP Code \"422 Unprocessable Entity\". - O endpoint `POST /consents/{consentId}/extends` é utilizado para renovação de consentimento ativo do cliente.  Ou seja, quando a receptora recebe pedido de renovação de consentimento com status ainda ativo para a transmissora, ela deve requisitar este endpoint. - Apenas consentimentos autorizados (status AUTHORISED) podem ser renovados pelo uso do endpoint `POST /consents/{consentId}/extends`. Essa renovação é feita exclusivamente via backende resulta em:   - Alteração do `expirationDateTime` do consentimento vigente;   - Persistência de informações para listar histórico de alterações que podem ser acessadas via endpoint `GET /consents/{consentId}/extends`. - A data de expiração `2300-01-01T00:00:00Z` (`expirationDateTime= 2300-01-01T00:00:00Z`) é a representação técnica de um consentimento com prazo de expiração indeterminado.  Ou seja, sempre que o cliente escolher prazo indeterminado para expiração de consentimento, a instituição receptora deve preencher `expirationDateTime= 2300-01-01T00:00:00Z` e assim informá-la para à instituição transmissora.  De igual forma, a instituição transmissora deve entender e representar consentimento com `expirationDateTime= 2300-01-01T00:00:00Z` como um consentimento com prazo de expiração indeterminado. - Os consentimentos em estado expirado ou cancelado não podem ser renovados sem redirecionamento.  Ou seja, não é possível utilizar o endpoint `POST /consents/{consentId}/extends` para consentimentos nesses estados (status REJECTED).  A transmissora deve retornar status de erro 422 (`ESTADO_CONSENTIMENTO_INVALIDO`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ser possível por apenas um cliente logado.  Não deve ser possível quando o consentimento foi criado demandando aprovações por múltiplas alçadas.  A transmissora deve retornar status de erro 422 (`DEPENDE_MULTIPLA_ALCADA`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ser possível para consentimento para o qual foi emitido um refresh token opaco.  Não deve ser possível quando o consentimento está vinculado a um refresh token do tipo JWT (com prazo não prorrogável).  A transmissora deve retornar status de erro 422 (`REFRESH_TOKEN_JWT`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ocorrer apenas até o período de 12 meses após a data de requisição (`current_datetime<= expirationDateTime<= current_datetime+12meses`), ou com prazo de expiração indeterminado (`expirationDateTime=2300-01-01T00:00:00Z`).  A transmissora deve retornar status de erro 422 (`DATA_EXPIRACAO_INVALIDA`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) sempre aumenta a data de expiração final do consentimento em relação à data de expiração vigente.  Ou seja, um consentimento com prazo de expiração para 6 meses no futuro não pode ter sua data de expiração alterada para apenas 3 meses no futuro.  A transmissora deve retornar status de erro 422 (`DATA_EXPIRACAO_INVALIDA`) para requisições que não seguem essa definição. - A renovação de consentimento ativo do cliente somente poderá ser aceita pela transmissora para um usuário logado na receptora, identificado por seu documento (`loggedUser`; `businessEntity` quando aplicável) e permitido a partir de token de acesso (informado no cabeçalho `Authorization`) conseguido anteriormente durante a criação e confirmação do consentimento vigente.  A transmissora deve validar documento fornecido (`loggedUser`; `businessEntity` quando aplicável) e token de acesso para executar a renovação de consentimento. Caso a transmissora detecte que trata-se de acesso inválido por questões de segurança, é esperado status de erro 401 ou 403. - Após a renovação de consentimento (`POST /consents/{consentId}/extends`) a transmissora deve garantir que a data de expiração do refresh token opaco, ao qual o consentimento está associado, seja:   - sem expiração: refresh token permanece ativo, desde que o consentimento associado permaneça ativo (status AUTHORIZED);   - com expiração: desde que, no mínimo, a nova data de expiração do refreshtoken seja igual à nova data do consentimento. - A lista do payload de resposta do endpoint de histórico de renovações feitas (`GET /consents/{consentId}/extends`) deve ser entregue em ordem decrescente pela data de requisição (`data[].requestDateTime`).  Dessa forma, o primeiro item da lista apresentará a mesma data de expiração do consentimento vigente, pois foi a última renovação feita. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.2.0-rc.1
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
import consents_2_2_0-rc_1_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import consents_2_2_0-rc_1_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import consents_2_2_0-rc_1_yml
from consents_2_2_0-rc_1_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = consents_2_2_0-rc_1_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = consents_2_2_0-rc_1_yml.ConsentsApi(consents_2_2_0-rc_1_yml.ApiClient(configuration))
consent_id = 'consent_id_example' # str | O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos:  - namespace(urn) - identificador associado ao namespace da instituição transnmissora (bancoex) - identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Deletar / Revogar o consentimento identificado por consentId.
    api_instance.consents_delete_consents_consent_id(consent_id, authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
except ApiException as e:
    print("Exception when calling ConsentsApi->consents_delete_consents_consent_id: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = consents_2_2_0-rc_1_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = consents_2_2_0-rc_1_yml.ConsentsApi(consents_2_2_0-rc_1_yml.ApiClient(configuration))
consent_id = 'consent_id_example' # str | O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos:  - namespace(urn) - identificador associado ao namespace da instituição transnmissora (bancoex) - identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obter detalhes do consentimento identificado por consentId.
    api_response = api_instance.consents_get_consents_consent_id(consent_id, authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->consents_get_consents_consent_id: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = consents_2_2_0-rc_1_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = consents_2_2_0-rc_1_yml.ConsentsApi(consents_2_2_0-rc_1_yml.ApiClient(configuration))
consent_id = 'consent_id_example' # str | O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos:  - namespace(urn) - identificador associado ao namespace da instituição transnmissora (bancoex) - identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obter detalhes de extensões feitas no consentimento identificado por consentId.
    api_response = api_instance.consents_get_consents_consent_id_extends(consent_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->consents_get_consents_consent_id_extends: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = consents_2_2_0-rc_1_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = consents_2_2_0-rc_1_yml.ConsentsApi(consents_2_2_0-rc_1_yml.ApiClient(configuration))
body = consents_2_2_0-rc_1_yml.CreateConsent() # CreateConsent | Payload para criação do consentimento.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Criar novo pedido de consentimento.
    api_response = api_instance.consents_post_consents(body, authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->consents_post_consents: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = consents_2_2_0-rc_1_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = consents_2_2_0-rc_1_yml.ConsentsApi(consents_2_2_0-rc_1_yml.ApiClient(configuration))
body = consents_2_2_0-rc_1_yml.CreateConsentExtends() # CreateConsentExtends | Payload para criação do consentimento.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor.
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta.
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza.
consent_id = 'consent_id_example' # str | O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos:  - namespace(urn) - identificador associado ao namespace da instituição transnmissora (bancoex) - identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141). 
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)

try:
    # Renovar consentimento identificado por consentId.
    api_response = api_instance.consents_post_consents_consent_id_extends(body, authorization, x_fapi_customer_ip_address, x_fapi_interaction_id, x_customer_user_agent, consent_id, x_fapi_auth_date=x_fapi_auth_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->consents_post_consents_consent_id_extends: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.banco.com.br/open-banking/consents/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConsentsApi* | [**consents_delete_consents_consent_id**](docs/ConsentsApi.md#consents_delete_consents_consent_id) | **DELETE** /consents/{consentId} | Deletar / Revogar o consentimento identificado por consentId.
*ConsentsApi* | [**consents_get_consents_consent_id**](docs/ConsentsApi.md#consents_get_consents_consent_id) | **GET** /consents/{consentId} | Obter detalhes do consentimento identificado por consentId.
*ConsentsApi* | [**consents_get_consents_consent_id_extends**](docs/ConsentsApi.md#consents_get_consents_consent_id_extends) | **GET** /consents/{consentId}/extends | Obter detalhes de extensões feitas no consentimento identificado por consentId.
*ConsentsApi* | [**consents_post_consents**](docs/ConsentsApi.md#consents_post_consents) | **POST** /consents | Criar novo pedido de consentimento.
*ConsentsApi* | [**consents_post_consents_consent_id_extends**](docs/ConsentsApi.md#consents_post_consents_consent_id_extends) | **POST** /consents/{consentId}/extends | Renovar consentimento identificado por consentId.

## Documentation For Models

 - [BusinessEntity](docs/BusinessEntity.md)
 - [BusinessEntityDocument](docs/BusinessEntityDocument.md)
 - [BusinessEntityExtends](docs/BusinessEntityExtends.md)
 - [CreateConsent](docs/CreateConsent.md)
 - [CreateConsentData](docs/CreateConsentData.md)
 - [CreateConsentExtends](docs/CreateConsentExtends.md)
 - [CreateConsentExtendsData](docs/CreateConsentExtendsData.md)
 - [EnumReasonCode](docs/EnumReasonCode.md)
 - [EnumRejectedBy](docs/EnumRejectedBy.md)
 - [InlineResponse529](docs/InlineResponse529.md)
 - [InlineResponse529Errors](docs/InlineResponse529Errors.md)
 - [InlineResponse529Meta](docs/InlineResponse529Meta.md)
 - [Links](docs/Links.md)
 - [LoggedUser](docs/LoggedUser.md)
 - [LoggedUserDocument](docs/LoggedUserDocument.md)
 - [LoggedUserExtends](docs/LoggedUserExtends.md)
 - [Meta](docs/Meta.md)
 - [Model422ResponseErrorCreateConsent](docs/Model422ResponseErrorCreateConsent.md)
 - [Model422ResponseErrorCreateConsentErrors](docs/Model422ResponseErrorCreateConsentErrors.md)
 - [RejectedReason](docs/RejectedReason.md)
 - [ResponseConsent](docs/ResponseConsent.md)
 - [ResponseConsentData](docs/ResponseConsentData.md)
 - [ResponseConsentExtends](docs/ResponseConsentExtends.md)
 - [ResponseConsentExtendsData](docs/ResponseConsentExtendsData.md)
 - [ResponseConsentRead](docs/ResponseConsentRead.md)
 - [ResponseConsentReadData](docs/ResponseConsentReadData.md)
 - [ResponseConsentReadDataRejection](docs/ResponseConsentReadDataRejection.md)
 - [ResponseConsentReadExtends](docs/ResponseConsentReadExtends.md)
 - [ResponseConsentReadExtendsData](docs/ResponseConsentReadExtendsData.md)
 - [ResponseError](docs/ResponseError.md)
 - [ResponseErrorErrors](docs/ResponseErrorErrors.md)

## Documentation For Authorization


## OAuth2AuthorizationCode

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://authserver.example/code
- **Scopes**: 
 - **openid**: Indica que a autorização está sendo realizada utilizando o protocolo definido pela openid.
 - **consent:consentId**: Escopo contendo o identificador único do consentimento criado para compartilhamento de dados solicitada.

## OAuth2Security

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **consents**: Criação do consentimento.


## Author

gt-interfaces@openbankingbr.org
