# credit-cards_1_0_0-rc6_5_yml.CreditCardApi

All URIs are relative to *https://api.banco.com.br/open-banking/credit-cards-accounts/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_cards_get_accounts**](CreditCardApi.md#credit_cards_get_accounts) | **GET** /accounts | Conjunto de informações das Contas de pagamento pós paga
[**credit_cards_get_accounts_credit_card_account_id**](CreditCardApi.md#credit_cards_get_accounts_credit_card_account_id) | **GET** /accounts/{creditCardAccountId} | Obtém os dados de identificação da conta identificada por creditCardAccountId.
[**credit_cards_get_accounts_credit_card_account_id_bills**](CreditCardApi.md#credit_cards_get_accounts_credit_card_account_id_bills) | **GET** /accounts/{creditCardAccountId}/bills | Obtém a lista de faturas da conta identificada por creditCardAccountId.
[**credit_cards_get_accounts_credit_card_account_id_bills_bill_id_transactions**](CreditCardApi.md#credit_cards_get_accounts_credit_card_account_id_bills_bill_id_transactions) | **GET** /accounts/{creditCardAccountId}/bills/{billId}/transactions | Obtém a lista de transações da conta identificada por creditCardAccountId e billId.
[**credit_cards_get_accounts_credit_card_account_id_limits**](CreditCardApi.md#credit_cards_get_accounts_credit_card_account_id_limits) | **GET** /accounts/{creditCardAccountId}/limits | Obtém os limites da conta identificada por creditCardAccountId. 
[**credit_cards_get_accounts_credit_card_account_id_transactions**](CreditCardApi.md#credit_cards_get_accounts_credit_card_account_id_transactions) | **GET** /accounts/{creditCardAccountId}/transactions | Obtém a lista de transações da conta identificada por creditCardAccountId.

# **credit_cards_get_accounts**
> ResponseCreditCardAccountsList credit_cards_get_accounts(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size)

Conjunto de informações das Contas de pagamento pós paga

Método para obter a lista de contas de pagamento pós-paga mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento

### Example
```python
from __future__ import print_function
import time
import credit-cards_1_0_0-rc6_5_yml
from credit-cards_1_0_0-rc6_5_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = credit-cards_1_0_0-rc6_5_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = credit-cards_1_0_0-rc6_5_yml.CreditCardApi(credit-cards_1_0_0-rc6_5_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Conjunto de informações das Contas de pagamento pós paga
    api_response = api_instance.credit_cards_get_accounts(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardApi->credit_cards_get_accounts: %s\n" % e)
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

### Return type

[**ResponseCreditCardAccountsList**](ResponseCreditCardAccountsList.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_cards_get_accounts_credit_card_account_id**
> ResponseCreditCardAccountsIdentification credit_cards_get_accounts_credit_card_account_id(authorization, credit_card_account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)

Obtém os dados de identificação da conta identificada por creditCardAccountId.

Método para obter os dados de identificação da conta de pagamento pós-paga identificada por creditCardAccountId mantida pelo cliente na instituição transmissora.

### Example
```python
from __future__ import print_function
import time
import credit-cards_1_0_0-rc6_5_yml
from credit-cards_1_0_0-rc6_5_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = credit-cards_1_0_0-rc6_5_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = credit-cards_1_0_0-rc6_5_yml.CreditCardApi(credit-cards_1_0_0-rc6_5_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
credit_card_account_id = 'credit_card_account_id_example' # str | Identifica de forma única a conta pagamento pós-paga do cliente, mantendo as regras de imutabilidade detro da instituição transmissora
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os dados de identificação da conta identificada por creditCardAccountId.
    api_response = api_instance.credit_cards_get_accounts_credit_card_account_id(authorization, credit_card_account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardApi->credit_cards_get_accounts_credit_card_account_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **credit_card_account_id** | **str**| Identifica de forma única a conta pagamento pós-paga do cliente, mantendo as regras de imutabilidade detro da instituição transmissora | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponseCreditCardAccountsIdentification**](ResponseCreditCardAccountsIdentification.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_cards_get_accounts_credit_card_account_id_bills**
> ResponseCreditCardAccountsBills credit_cards_get_accounts_credit_card_account_id_bills(authorization, credit_card_account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_due_date=from_due_date, to_due_date=to_due_date)

Obtém a lista de faturas da conta identificada por creditCardAccountId.

Método para obter a lista de faturas da conta de pagamento pós-paga identificada por creditCardAccountId mantida pelo cliente na instituição transmissora.

### Example
```python
from __future__ import print_function
import time
import credit-cards_1_0_0-rc6_5_yml
from credit-cards_1_0_0-rc6_5_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = credit-cards_1_0_0-rc6_5_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = credit-cards_1_0_0-rc6_5_yml.CreditCardApi(credit-cards_1_0_0-rc6_5_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
credit_card_account_id = 'credit_card_account_id_example' # str | Identifica de forma única a conta pagamento pós-paga do cliente, mantendo as regras de imutabilidade detro da instituição transmissora
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
from_due_date = '2013-10-20' # date | Data inicial de filtragem. (optional)
to_due_date = '2013-10-20' # date | Data final de filtragem. (optional)

try:
    # Obtém a lista de faturas da conta identificada por creditCardAccountId.
    api_response = api_instance.credit_cards_get_accounts_credit_card_account_id_bills(authorization, credit_card_account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_due_date=from_due_date, to_due_date=to_due_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardApi->credit_cards_get_accounts_credit_card_account_id_bills: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **credit_card_account_id** | **str**| Identifica de forma única a conta pagamento pós-paga do cliente, mantendo as regras de imutabilidade detro da instituição transmissora | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]
 **from_due_date** | **date**| Data inicial de filtragem. | [optional] 
 **to_due_date** | **date**| Data final de filtragem. | [optional] 

### Return type

[**ResponseCreditCardAccountsBills**](ResponseCreditCardAccountsBills.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_cards_get_accounts_credit_card_account_id_bills_bill_id_transactions**
> ResponseCreditCardAccountsTransactions credit_cards_get_accounts_credit_card_account_id_bills_bill_id_transactions(authorization, credit_card_account_id, bill_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, transaction_type=transaction_type, payee_mcc=payee_mcc)

Obtém a lista de transações da conta identificada por creditCardAccountId e billId.

Método para obter a lista de transações da conta de pagamento pós-paga identificada por creditCardAccountId e billId mantida pelo cliente na instituição transmissora.

### Example
```python
from __future__ import print_function
import time
import credit-cards_1_0_0-rc6_5_yml
from credit-cards_1_0_0-rc6_5_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = credit-cards_1_0_0-rc6_5_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = credit-cards_1_0_0-rc6_5_yml.CreditCardApi(credit-cards_1_0_0-rc6_5_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
credit_card_account_id = 'credit_card_account_id_example' # str | Identifica de forma única a conta pagamento pós-paga do cliente, mantendo as regras de imutabilidade detro da instituição transmissora
bill_id = 'bill_id_example' # str | Identificador da fatura.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
from_transaction_date = '2013-10-20' # date | Data inicial de filtragem. (optional)
to_transaction_date = '2013-10-20' # date | Data final de filtragem. (optional)
transaction_type = credit-cards_1_0_0-rc6_5_yml.EnumCreditCardTransactionType() # EnumCreditCardTransactionType | Traz os tipos de Transação (optional)
payee_mcc = 1.2 # float | MCC é o Merchant Category Code, ou o código da categoria do estabelecimento comercial. Os MCCs são agrupados segundo suas similaridades (optional)

try:
    # Obtém a lista de transações da conta identificada por creditCardAccountId e billId.
    api_response = api_instance.credit_cards_get_accounts_credit_card_account_id_bills_bill_id_transactions(authorization, credit_card_account_id, bill_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, transaction_type=transaction_type, payee_mcc=payee_mcc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardApi->credit_cards_get_accounts_credit_card_account_id_bills_bill_id_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **credit_card_account_id** | **str**| Identifica de forma única a conta pagamento pós-paga do cliente, mantendo as regras de imutabilidade detro da instituição transmissora | 
 **bill_id** | **str**| Identificador da fatura. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]
 **from_transaction_date** | **date**| Data inicial de filtragem. | [optional] 
 **to_transaction_date** | **date**| Data final de filtragem. | [optional] 
 **transaction_type** | [**EnumCreditCardTransactionType**](.md)| Traz os tipos de Transação | [optional] 
 **payee_mcc** | **float**| MCC é o Merchant Category Code, ou o código da categoria do estabelecimento comercial. Os MCCs são agrupados segundo suas similaridades | [optional] 

### Return type

[**ResponseCreditCardAccountsTransactions**](ResponseCreditCardAccountsTransactions.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_cards_get_accounts_credit_card_account_id_limits**
> ResponseCreditCardAccountsLimits credit_cards_get_accounts_credit_card_account_id_limits(authorization, credit_card_account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)

Obtém os limites da conta identificada por creditCardAccountId. 

Método para obter os limites da conta de pagamento pós-paga identificada por creditCardAccountId mantida pelo cliente na instituição transmissora. 

### Example
```python
from __future__ import print_function
import time
import credit-cards_1_0_0-rc6_5_yml
from credit-cards_1_0_0-rc6_5_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = credit-cards_1_0_0-rc6_5_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = credit-cards_1_0_0-rc6_5_yml.CreditCardApi(credit-cards_1_0_0-rc6_5_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
credit_card_account_id = 'credit_card_account_id_example' # str | Identifica de forma única a conta pagamento pós-paga do cliente, mantendo as regras de imutabilidade detro da instituição transmissora
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os limites da conta identificada por creditCardAccountId. 
    api_response = api_instance.credit_cards_get_accounts_credit_card_account_id_limits(authorization, credit_card_account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardApi->credit_cards_get_accounts_credit_card_account_id_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **credit_card_account_id** | **str**| Identifica de forma única a conta pagamento pós-paga do cliente, mantendo as regras de imutabilidade detro da instituição transmissora | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponseCreditCardAccountsLimits**](ResponseCreditCardAccountsLimits.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_cards_get_accounts_credit_card_account_id_transactions**
> ResponseCreditCardAccountsTransactions credit_cards_get_accounts_credit_card_account_id_transactions(authorization, credit_card_account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, transaction_type=transaction_type, payee_mcc=payee_mcc)

Obtém a lista de transações da conta identificada por creditCardAccountId.

Método para obter a lista de transações da conta de pagamento pós-paga identificada por creditCardAccountId mantida pelo cliente na instituição transmissora.

### Example
```python
from __future__ import print_function
import time
import credit-cards_1_0_0-rc6_5_yml
from credit-cards_1_0_0-rc6_5_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = credit-cards_1_0_0-rc6_5_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = credit-cards_1_0_0-rc6_5_yml.CreditCardApi(credit-cards_1_0_0-rc6_5_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
credit_card_account_id = 'credit_card_account_id_example' # str | Identifica de forma única a conta pagamento pós-paga do cliente, mantendo as regras de imutabilidade detro da instituição transmissora
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
from_transaction_date = '2013-10-20' # date | Data inicial de filtragem. (optional)
to_transaction_date = '2013-10-20' # date | Data final de filtragem. (optional)
transaction_type = credit-cards_1_0_0-rc6_5_yml.EnumCreditCardTransactionType() # EnumCreditCardTransactionType | Traz os tipos de Transação (optional)
payee_mcc = 1.2 # float | MCC é o Merchant Category Code, ou o código da categoria do estabelecimento comercial. Os MCCs são agrupados segundo suas similaridades (optional)

try:
    # Obtém a lista de transações da conta identificada por creditCardAccountId.
    api_response = api_instance.credit_cards_get_accounts_credit_card_account_id_transactions(authorization, credit_card_account_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, transaction_type=transaction_type, payee_mcc=payee_mcc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardApi->credit_cards_get_accounts_credit_card_account_id_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **credit_card_account_id** | **str**| Identifica de forma única a conta pagamento pós-paga do cliente, mantendo as regras de imutabilidade detro da instituição transmissora | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]
 **from_transaction_date** | **date**| Data inicial de filtragem. | [optional] 
 **to_transaction_date** | **date**| Data final de filtragem. | [optional] 
 **transaction_type** | [**EnumCreditCardTransactionType**](.md)| Traz os tipos de Transação | [optional] 
 **payee_mcc** | **float**| MCC é o Merchant Category Code, ou o código da categoria do estabelecimento comercial. Os MCCs são agrupados segundo suas similaridades | [optional] 

### Return type

[**ResponseCreditCardAccountsTransactions**](ResponseCreditCardAccountsTransactions.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

