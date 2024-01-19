# accounts-2-1-0-yml
API de contas de depósito à vista, contas de poupança e contas pré-pagas do Open Finance Brasil – Fase 2. API que retorna informações de contas de depósito à vista, contas de poupança e contas de pagamento pré-pagas mantidas nas instituições transmissoras por seus clientes, incluindo dados de identificação da conta, saldos, limites e transações.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}/balances`   - permissions:     - GET: **ACCOUNTS_BALANCES_READ** ### `/accounts/{accountId}/transactions`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/transactions-current`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/overdraft-limits`   - permissions:     - GET: **ACCOUNTS_OVERDRAFT_LIMITS_READ**  ## Data de imutabilidade por tipo de transação​ O identificador de transações de contas é de envio obrigatório no Open Finance Brasil. De acordo com o tipo da transação deve haver o envio de um identificador único, estável e imutável em D0 ou D+1, conforme tabela abaixo ``` |---------------------------------------|-------------------------|-----------------------| | Tipo de Transação                     | Data da Obrigatoriedade | Data da Imutabilidade | |---------------------------------------|-------------------------|-----------------------| | TED                                   | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | PIX                                   | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | TRANSFERENCIA MESMA INSTITUIÇÃO (TEF) | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | TARIFA SERVIÇOS AVULSOS               | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | FOLHA DE PAGAMENTO                    | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | DOC                                   | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | BOLETO                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | CONVÊNIO ARRECADAÇÃO                  | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | PACOTE TARIFA SERVIÇOS                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | DEPÓSITO                              | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | SAQUE                                 | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | CARTÃO                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | ENCARGOS JUROS CHEQUE ESPECIAL        | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | RENDIMENTO APLICAÇÃO FINANCEIRA       | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | PORTABILIDADE SALÁRIO                 | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | RESGATE APLICAÇÃO FINANCEIRA          | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | OPERAÇÃO DE CRÉDITO                   | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | OUTROS                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| ``` 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.1.0
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
import accounts_2_1_0_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import accounts_2_1_0_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import accounts_2_1_0_yml
from accounts_2_1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_1_0_yml.AccountsApi(accounts_2_1_0_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
account_type = accounts_2_1_0_yml.EnumAccountType() # EnumAccountType | Tipos de contas. Modalidades tradicionais previstas pela Resolução 4.753, não contemplando contas vinculadas, conta de domiciliados no exterior, contas em moedas estrangeiras e conta correspondente moeda eletrônica. Vide Enum. (optional)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém a lista de contas consentidas pelo cliente.
    api_response = api_instance.accounts_get_accounts(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, account_type=account_type, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_accounts: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_1_0_yml.AccountsApi(accounts_2_1_0_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
account_id = 'account_id_example' # str | Identificador da conta de depósito à vista, de poupança ou de pagamento pré-paga.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os dados de identificação da conta identificada por accountId.
    api_response = api_instance.accounts_get_accounts_account_id(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_accounts_account_id: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_1_0_yml.AccountsApi(accounts_2_1_0_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
account_id = 'account_id_example' # str | Identificador da conta de depósito à vista, de poupança ou de pagamento pré-paga.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os saldos da conta identificada por accountId.
    api_response = api_instance.accounts_get_accounts_account_id_balances(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_accounts_account_id_balances: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_1_0_yml.AccountsApi(accounts_2_1_0_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
account_id = 'account_id_example' # str | Identificador da conta de depósito à vista, de poupança ou de pagamento pré-paga.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os limites da conta identificada por accountId.
    api_response = api_instance.accounts_get_accounts_account_id_overdraft_limits(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_accounts_account_id_overdraft_limits: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_1_0_yml.AccountsApi(accounts_2_1_0_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
account_id = 'account_id_example' # str | Identificador da conta de depósito à vista, de poupança ou de pagamento pré-paga.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
from_booking_date = '2013-10-20' # date | Data inicial de filtragem. [Restrição] Deve obrigatoriamente ser enviado caso o campo toBookingDate seja informado. Caso não seja informado, deve ser assumido o dia atual. (optional)
to_booking_date = '2013-10-20' # date | Data final de filtragem. [Restrição] Deve obrigatoriamente ser enviado caso o campo fromBookingDate seja informado. Caso não seja informado, deve ser assumido o dia atual. (optional)
credit_debit_indicator = accounts_2_1_0_yml.EnumCreditDebitIndicator() # EnumCreditDebitIndicator | Indicador do tipo de lançamento (optional)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém a lista de transações da conta identificada por accountId.
    api_response = api_instance.accounts_get_accounts_account_id_transactions(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_booking_date=from_booking_date, to_booking_date=to_booking_date, credit_debit_indicator=credit_debit_indicator, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_accounts_account_id_transactions: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_1_0_yml.AccountsApi(accounts_2_1_0_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
account_id = 'account_id_example' # str | Identificador da conta de depósito à vista, de poupança ou de pagamento pré-paga.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
from_booking_date = '2013-10-20' # date | Data inicial de filtragem. O período máximo utilizado no filtro é de 7 dias inclusive (D-6).    [Restrição] Deve obrigatoriamente ser enviado caso o campo toBookingDate seja informado.  Caso não seja informado, deve ser assumido o dia atual.  (optional)
to_booking_date = '2013-10-20' # date | Data final de filtragem. O período máximo utilizado no filtro é de 7 dias inclusive (D-6).    [Restrição] Deve obrigatoriamente ser enviado caso o campo fromBookingDate seja informado.  Caso não seja informado, deve ser assumido o dia atual.  (optional)
credit_debit_indicator = accounts_2_1_0_yml.EnumCreditDebitIndicator() # EnumCreditDebitIndicator | Indicador do tipo de lançamento (optional)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém a lista de transações recentes (últimos 7 dias) da conta identificada por accountId.
    api_response = api_instance.accounts_get_accounts_account_id_transactions_current(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_booking_date=from_booking_date, to_booking_date=to_booking_date, credit_debit_indicator=credit_debit_indicator, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_accounts_account_id_transactions_current: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.banco.com.br/open-banking/accounts/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**accounts_get_accounts**](docs/AccountsApi.md#accounts_get_accounts) | **GET** /accounts | Obtém a lista de contas consentidas pelo cliente.
*AccountsApi* | [**accounts_get_accounts_account_id**](docs/AccountsApi.md#accounts_get_accounts_account_id) | **GET** /accounts/{accountId} | Obtém os dados de identificação da conta identificada por accountId.
*AccountsApi* | [**accounts_get_accounts_account_id_balances**](docs/AccountsApi.md#accounts_get_accounts_account_id_balances) | **GET** /accounts/{accountId}/balances | Obtém os saldos da conta identificada por accountId.
*AccountsApi* | [**accounts_get_accounts_account_id_overdraft_limits**](docs/AccountsApi.md#accounts_get_accounts_account_id_overdraft_limits) | **GET** /accounts/{accountId}/overdraft-limits | Obtém os limites da conta identificada por accountId.
*AccountsApi* | [**accounts_get_accounts_account_id_transactions**](docs/AccountsApi.md#accounts_get_accounts_account_id_transactions) | **GET** /accounts/{accountId}/transactions | Obtém a lista de transações da conta identificada por accountId.
*AccountsApi* | [**accounts_get_accounts_account_id_transactions_current**](docs/AccountsApi.md#accounts_get_accounts_account_id_transactions_current) | **GET** /accounts/{accountId}/transactions-current | Obtém a lista de transações recentes (últimos 7 dias) da conta identificada por accountId.

## Documentation For Models

 - [AccountBalancesData](docs/AccountBalancesData.md)
 - [AccountBalancesDataAutomaticallyInvestedAmount](docs/AccountBalancesDataAutomaticallyInvestedAmount.md)
 - [AccountBalancesDataAvailableAmount](docs/AccountBalancesDataAvailableAmount.md)
 - [AccountBalancesDataBlockedAmount](docs/AccountBalancesDataBlockedAmount.md)
 - [AccountData](docs/AccountData.md)
 - [AccountIdentificationData](docs/AccountIdentificationData.md)
 - [AccountOverdraftLimitsData](docs/AccountOverdraftLimitsData.md)
 - [AccountOverdraftLimitsDataOverdraftContractedLimit](docs/AccountOverdraftLimitsDataOverdraftContractedLimit.md)
 - [AccountOverdraftLimitsDataOverdraftUsedLimit](docs/AccountOverdraftLimitsDataOverdraftUsedLimit.md)
 - [AccountOverdraftLimitsDataUnarrangedOverdraftAmount](docs/AccountOverdraftLimitsDataUnarrangedOverdraftAmount.md)
 - [AccountTransactionsData](docs/AccountTransactionsData.md)
 - [AccountTransactionsDataAmount](docs/AccountTransactionsDataAmount.md)
 - [EnumAccountSubType](docs/EnumAccountSubType.md)
 - [EnumAccountType](docs/EnumAccountType.md)
 - [EnumCompletedAuthorisedPaymentIndicator](docs/EnumCompletedAuthorisedPaymentIndicator.md)
 - [EnumCreditDebitIndicator](docs/EnumCreditDebitIndicator.md)
 - [EnumPartiePersonType](docs/EnumPartiePersonType.md)
 - [EnumTransactionTypes](docs/EnumTransactionTypes.md)
 - [Links](docs/Links.md)
 - [Meta](docs/Meta.md)
 - [MetaOnlyRequestDateTime](docs/MetaOnlyRequestDateTime.md)
 - [ResponseAccountBalances](docs/ResponseAccountBalances.md)
 - [ResponseAccountIdentification](docs/ResponseAccountIdentification.md)
 - [ResponseAccountList](docs/ResponseAccountList.md)
 - [ResponseAccountOverdraftLimits](docs/ResponseAccountOverdraftLimits.md)
 - [ResponseAccountTransactions](docs/ResponseAccountTransactions.md)
 - [ResponseError](docs/ResponseError.md)
 - [ResponseErrorMetaSingle](docs/ResponseErrorMetaSingle.md)
 - [ResponseErrorMetaSingleErrors](docs/ResponseErrorMetaSingleErrors.md)
 - [TransactionsLinks](docs/TransactionsLinks.md)
 - [XFapiInteractionId](docs/XFapiInteractionId.md)

## Documentation For Authorization


## OAuth2Security

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://authserver.example/authorization
- **Scopes**: 
 - **accounts**: Escopo necessário para acesso à API Accounts. O controle dos endpoints específicos é feito via permissions.

## OpenId



## Author

gt-interfaces@openbankingbr.org
