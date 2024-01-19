# accounts_2_0_0_yml.AccountsApi

All URIs are relative to *https://api.banco.com.br/open-banking/accounts/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_get_accounts**](AccountsApi.md#accounts_get_accounts) | **GET** /accounts | Obtém a lista de contas consentidas pelo cliente.
[**accounts_get_accounts_account_id**](AccountsApi.md#accounts_get_accounts_account_id) | **GET** /accounts/{accountId} | Obtém os dados de identificação da conta identificada por accountId.
[**accounts_get_accounts_account_id_balances**](AccountsApi.md#accounts_get_accounts_account_id_balances) | **GET** /accounts/{accountId}/balances | Obtém os saldos da conta identificada por accountId.
[**accounts_get_accounts_account_id_overdraft_limits**](AccountsApi.md#accounts_get_accounts_account_id_overdraft_limits) | **GET** /accounts/{accountId}/overdraft-limits | Obtém os limites da conta identificada por accountId.
[**accounts_get_accounts_account_id_transactions**](AccountsApi.md#accounts_get_accounts_account_id_transactions) | **GET** /accounts/{accountId}/transactions | Obtém a lista de transações da conta identificada por accountId.
[**accounts_get_accounts_account_id_transactions_current**](AccountsApi.md#accounts_get_accounts_account_id_transactions_current) | **GET** /accounts/{accountId}/transactions-current | Obtém a lista de transações recentes (últimos 7 dias) da conta identificada por accountId.

# **accounts_get_accounts**
> ResponseAccountList accounts_get_accounts(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, account_type=account_type, pagination_key=pagination_key)

Obtém a lista de contas consentidas pelo cliente.

Método para obter a lista de contas depósito à vista, poupança e pagamento pré-pagas mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.

### Example
```python
from __future__ import print_function
import time
import accounts_2_0_0_yml
from accounts_2_0_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_0_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_0_0_yml.AccountsApi(accounts_2_0_0_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
account_type = accounts_2_0_0_yml.EnumAccountType() # EnumAccountType | Tipos de contas. Modalidades tradicionais previstas pela Resolução 4.753, não contemplando contas vinculadas, conta de domiciliados no exterior, contas em moedas estrangeiras e conta correspondente moeda eletrônica. Vide Enum. (optional)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém a lista de contas consentidas pelo cliente.
    api_response = api_instance.accounts_get_accounts(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, account_type=account_type, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]
 **account_type** | [**EnumAccountType**](.md)| Tipos de contas. Modalidades tradicionais previstas pela Resolução 4.753, não contemplando contas vinculadas, conta de domiciliados no exterior, contas em moedas estrangeiras e conta correspondente moeda eletrônica. Vide Enum. | [optional] 
 **pagination_key** | **str**| Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. | [optional] 

### Return type

[**ResponseAccountList**](ResponseAccountList.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_accounts_account_id**
> ResponseAccountIdentification accounts_get_accounts_account_id(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)

Obtém os dados de identificação da conta identificada por accountId.

Método para obter os dados de identificação da conta de depósito à vista, poupança ou pagamento pré-paga identificada por accountId mantida pelo cliente na instituição transmissora.

### Example
```python
from __future__ import print_function
import time
import accounts_2_0_0_yml
from accounts_2_0_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_0_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_0_0_yml.AccountsApi(accounts_2_0_0_yml.ApiClient(configuration))
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **account_id** | **str**| Identificador da conta de depósito à vista, de poupança ou de pagamento pré-paga. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponseAccountIdentification**](ResponseAccountIdentification.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_accounts_account_id_balances**
> ResponseAccountBalances accounts_get_accounts_account_id_balances(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)

Obtém os saldos da conta identificada por accountId.

Método para obter os saldos da conta de depósito à vista, poupança ou pagamento pré-paga identificada por accountId mantida pelo cliente na instituição transmissora.

### Example
```python
from __future__ import print_function
import time
import accounts_2_0_0_yml
from accounts_2_0_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_0_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_0_0_yml.AccountsApi(accounts_2_0_0_yml.ApiClient(configuration))
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **account_id** | **str**| Identificador da conta de depósito à vista, de poupança ou de pagamento pré-paga. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponseAccountBalances**](ResponseAccountBalances.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_accounts_account_id_overdraft_limits**
> ResponseAccountOverdraftLimits accounts_get_accounts_account_id_overdraft_limits(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)

Obtém os limites da conta identificada por accountId.

Método para obter os limites da conta de depósito à vista, poupança ou pagamento pré-paga identificada por accountId mantida pelo cliente na instituição transmissora.

### Example
```python
from __future__ import print_function
import time
import accounts_2_0_0_yml
from accounts_2_0_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_0_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_0_0_yml.AccountsApi(accounts_2_0_0_yml.ApiClient(configuration))
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **account_id** | **str**| Identificador da conta de depósito à vista, de poupança ou de pagamento pré-paga. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponseAccountOverdraftLimits**](ResponseAccountOverdraftLimits.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_accounts_account_id_transactions**
> ResponseAccountTransactions accounts_get_accounts_account_id_transactions(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_booking_date=from_booking_date, to_booking_date=to_booking_date, credit_debit_indicator=credit_debit_indicator, pagination_key=pagination_key)

Obtém a lista de transações da conta identificada por accountId.

Método para obter a lista de transações da conta de depósito à vista, poupança ou pagamento pré-paga identificada por accountId mantida pelo cliente na instituição transmissora.

### Example
```python
from __future__ import print_function
import time
import accounts_2_0_0_yml
from accounts_2_0_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_0_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_0_0_yml.AccountsApi(accounts_2_0_0_yml.ApiClient(configuration))
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
credit_debit_indicator = accounts_2_0_0_yml.EnumCreditDebitIndicator() # EnumCreditDebitIndicator | Indicador do tipo de lançamento (optional)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém a lista de transações da conta identificada por accountId.
    api_response = api_instance.accounts_get_accounts_account_id_transactions(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_booking_date=from_booking_date, to_booking_date=to_booking_date, credit_debit_indicator=credit_debit_indicator, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_accounts_account_id_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **account_id** | **str**| Identificador da conta de depósito à vista, de poupança ou de pagamento pré-paga. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]
 **from_booking_date** | **date**| Data inicial de filtragem. [Restrição] Deve obrigatoriamente ser enviado caso o campo toBookingDate seja informado. Caso não seja informado, deve ser assumido o dia atual. | [optional] 
 **to_booking_date** | **date**| Data final de filtragem. [Restrição] Deve obrigatoriamente ser enviado caso o campo fromBookingDate seja informado. Caso não seja informado, deve ser assumido o dia atual. | [optional] 
 **credit_debit_indicator** | [**EnumCreditDebitIndicator**](.md)| Indicador do tipo de lançamento | [optional] 
 **pagination_key** | **str**| Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. | [optional] 

### Return type

[**ResponseAccountTransactions**](ResponseAccountTransactions.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_accounts_account_id_transactions_current**
> ResponseAccountTransactions accounts_get_accounts_account_id_transactions_current(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_booking_date=from_booking_date, to_booking_date=to_booking_date, credit_debit_indicator=credit_debit_indicator, pagination_key=pagination_key)

Obtém a lista de transações recentes (últimos 7 dias) da conta identificada por accountId.

Método para obter a lista de transações recentes (últimos 7 dias) da conta de depósito à vista, poupança ou pagamento pré-paga identificada por accountId mantida pelo cliente na instituição transmissora.

### Example
```python
from __future__ import print_function
import time
import accounts_2_0_0_yml
from accounts_2_0_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = accounts_2_0_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = accounts_2_0_0_yml.AccountsApi(accounts_2_0_0_yml.ApiClient(configuration))
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
credit_debit_indicator = accounts_2_0_0_yml.EnumCreditDebitIndicator() # EnumCreditDebitIndicator | Indicador do tipo de lançamento (optional)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém a lista de transações recentes (últimos 7 dias) da conta identificada por accountId.
    api_response = api_instance.accounts_get_accounts_account_id_transactions_current(authorization, account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_booking_date=from_booking_date, to_booking_date=to_booking_date, credit_debit_indicator=credit_debit_indicator, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_accounts_account_id_transactions_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **account_id** | **str**| Identificador da conta de depósito à vista, de poupança ou de pagamento pré-paga. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]
 **from_booking_date** | **date**| Data inicial de filtragem. O período máximo utilizado no filtro é de 7 dias inclusive (D-6).    [Restrição] Deve obrigatoriamente ser enviado caso o campo toBookingDate seja informado.  Caso não seja informado, deve ser assumido o dia atual.  | [optional] 
 **to_booking_date** | **date**| Data final de filtragem. O período máximo utilizado no filtro é de 7 dias inclusive (D-6).    [Restrição] Deve obrigatoriamente ser enviado caso o campo fromBookingDate seja informado.  Caso não seja informado, deve ser assumido o dia atual.  | [optional] 
 **credit_debit_indicator** | [**EnumCreditDebitIndicator**](.md)| Indicador do tipo de lançamento | [optional] 
 **pagination_key** | **str**| Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. | [optional] 

### Return type

[**ResponseAccountTransactions**](ResponseAccountTransactions.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

