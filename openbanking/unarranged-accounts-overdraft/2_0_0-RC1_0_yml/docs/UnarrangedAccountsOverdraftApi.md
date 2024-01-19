# unarranged-accounts-overdraft_2_0_0-RC1_0_yml.UnarrangedAccountsOverdraftApi

All URIs are relative to *https://api.banco.com.br/open-banking/unarranged-accounts-overdraft/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**unarranged_accounts_overdraft_get_contracts**](UnarrangedAccountsOverdraftApi.md#unarranged_accounts_overdraft_get_contracts) | **GET** /contracts | Obtém a lista de contratos de adiantamento a depositantes consentidos pelo cliente.
[**unarranged_accounts_overdraft_get_contracts_contract_id**](UnarrangedAccountsOverdraftApi.md#unarranged_accounts_overdraft_get_contracts_contract_id) | **GET** /contracts/{contractId} | Obtém os dados do contrato de adiantamento a depositantes identificado por contractId
[**unarranged_accounts_overdraft_get_contracts_contract_id_payments**](UnarrangedAccountsOverdraftApi.md#unarranged_accounts_overdraft_get_contracts_contract_id_payments) | **GET** /contracts/{contractId}/payments | Obtém os dados de pagamentos do contrato de adiantamento a depositantes identificado por contractId
[**unarranged_accounts_overdraft_get_contracts_contract_id_scheduled_instalments**](UnarrangedAccountsOverdraftApi.md#unarranged_accounts_overdraft_get_contracts_contract_id_scheduled_instalments) | **GET** /contracts/{contractId}/scheduled-instalments | Obtém os dados do cronograma de parcelas do contrato de adiantamento a depositantes identificado por contractId
[**unarranged_accounts_overdraft_get_contracts_contract_id_warranties**](UnarrangedAccountsOverdraftApi.md#unarranged_accounts_overdraft_get_contracts_contract_id_warranties) | **GET** /contracts/{contractId}/warranties | Obtém a lista de garantias vinculadas ao contrato de adiantamento a depositantes identificado por contractId

# **unarranged_accounts_overdraft_get_contracts**
> ResponseUnarrangedAccountOverdraftContractList unarranged_accounts_overdraft_get_contracts(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, pagination_key=pagination_key)

Obtém a lista de contratos de adiantamento a depositantes consentidos pelo cliente.

Método para obter a lista de contratos de adiantamento a depositantes mantidos pelo cliente na instituição transmissora e para os quais ele tenha fornecido consentimento.

### Example
```python
from __future__ import print_function
import time
import unarranged-accounts-overdraft_2_0_0-RC1_0_yml
from unarranged-accounts-overdraft_2_0_0-RC1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = unarranged-accounts-overdraft_2_0_0-RC1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = unarranged-accounts-overdraft_2_0_0-RC1_0_yml.UnarrangedAccountsOverdraftApi(unarranged-accounts-overdraft_2_0_0-RC1_0_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém a lista de contratos de adiantamento a depositantes consentidos pelo cliente.
    api_response = api_instance.unarranged_accounts_overdraft_get_contracts(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnarrangedAccountsOverdraftApi->unarranged_accounts_overdraft_get_contracts: %s\n" % e)
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
 **pagination_key** | **str**| Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. | [optional] 

### Return type

[**ResponseUnarrangedAccountOverdraftContractList**](ResponseUnarrangedAccountOverdraftContractList.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarranged_accounts_overdraft_get_contracts_contract_id**
> ResponseUnarrangedAccountOverdraftContract unarranged_accounts_overdraft_get_contracts_contract_id(contract_id, authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)

Obtém os dados do contrato de adiantamento a depositantes identificado por contractId

Método para obter os dados do contrato de adiantamento a depositantes identificado por contractId mantido pelo cliente na instituição transmissora

### Example
```python
from __future__ import print_function
import time
import unarranged-accounts-overdraft_2_0_0-RC1_0_yml
from unarranged-accounts-overdraft_2_0_0-RC1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = unarranged-accounts-overdraft_2_0_0-RC1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = unarranged-accounts-overdraft_2_0_0-RC1_0_yml.UnarrangedAccountsOverdraftApi(unarranged-accounts-overdraft_2_0_0-RC1_0_yml.ApiClient(configuration))
contract_id = 'contract_id_example' # str | Identificador do contrato para todos os tipos de operação de crédito.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os dados do contrato de adiantamento a depositantes identificado por contractId
    api_response = api_instance.unarranged_accounts_overdraft_get_contracts_contract_id(contract_id, authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnarrangedAccountsOverdraftApi->unarranged_accounts_overdraft_get_contracts_contract_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Identificador do contrato para todos os tipos de operação de crédito. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponseUnarrangedAccountOverdraftContract**](ResponseUnarrangedAccountOverdraftContract.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarranged_accounts_overdraft_get_contracts_contract_id_payments**
> ResponseUnarrangedAccountOverdraftPayments unarranged_accounts_overdraft_get_contracts_contract_id_payments(contract_id, authorization, page=page, page_size=page_size, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, pagination_key=pagination_key)

Obtém os dados de pagamentos do contrato de adiantamento a depositantes identificado por contractId

Método para obter os dados de pagamentos do contrato de adiantamento a depositantes identificado por contractId mantido pelo cliente na instituição transmissora

### Example
```python
from __future__ import print_function
import time
import unarranged-accounts-overdraft_2_0_0-RC1_0_yml
from unarranged-accounts-overdraft_2_0_0-RC1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = unarranged-accounts-overdraft_2_0_0-RC1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = unarranged-accounts-overdraft_2_0_0-RC1_0_yml.UnarrangedAccountsOverdraftApi(unarranged-accounts-overdraft_2_0_0-RC1_0_yml.ApiClient(configuration))
contract_id = 'contract_id_example' # str | Identificador do contrato para todos os tipos de operação de crédito.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém os dados de pagamentos do contrato de adiantamento a depositantes identificado por contractId
    api_response = api_instance.unarranged_accounts_overdraft_get_contracts_contract_id_payments(contract_id, authorization, page=page, page_size=page_size, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnarrangedAccountsOverdraftApi->unarranged_accounts_overdraft_get_contracts_contract_id_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Identificador do contrato para todos os tipos de operação de crédito. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **pagination_key** | **str**| Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. | [optional] 

### Return type

[**ResponseUnarrangedAccountOverdraftPayments**](ResponseUnarrangedAccountOverdraftPayments.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarranged_accounts_overdraft_get_contracts_contract_id_scheduled_instalments**
> ResponseUnarrangedAccountOverdraftInstalments unarranged_accounts_overdraft_get_contracts_contract_id_scheduled_instalments(contract_id, authorization, page=page, page_size=page_size, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, pagination_key=pagination_key)

Obtém os dados do cronograma de parcelas do contrato de adiantamento a depositantes identificado por contractId

Método para obter os dados do cronograma de parcelas do contrato de adiantamento a depositantes identificado por contractId mantido pelo cliente na instituição transmissora

### Example
```python
from __future__ import print_function
import time
import unarranged-accounts-overdraft_2_0_0-RC1_0_yml
from unarranged-accounts-overdraft_2_0_0-RC1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = unarranged-accounts-overdraft_2_0_0-RC1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = unarranged-accounts-overdraft_2_0_0-RC1_0_yml.UnarrangedAccountsOverdraftApi(unarranged-accounts-overdraft_2_0_0-RC1_0_yml.ApiClient(configuration))
contract_id = 'contract_id_example' # str | Identificador do contrato para todos os tipos de operação de crédito.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém os dados do cronograma de parcelas do contrato de adiantamento a depositantes identificado por contractId
    api_response = api_instance.unarranged_accounts_overdraft_get_contracts_contract_id_scheduled_instalments(contract_id, authorization, page=page, page_size=page_size, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnarrangedAccountsOverdraftApi->unarranged_accounts_overdraft_get_contracts_contract_id_scheduled_instalments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Identificador do contrato para todos os tipos de operação de crédito. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **pagination_key** | **str**| Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. | [optional] 

### Return type

[**ResponseUnarrangedAccountOverdraftInstalments**](ResponseUnarrangedAccountOverdraftInstalments.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarranged_accounts_overdraft_get_contracts_contract_id_warranties**
> ResponseUnarrangedAccountOverdraftWarranties unarranged_accounts_overdraft_get_contracts_contract_id_warranties(contract_id, authorization, page=page, page_size=page_size, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, pagination_key=pagination_key)

Obtém a lista de garantias vinculadas ao contrato de adiantamento a depositantes identificado por contractId

Método para obter a lista de garantias vinculadas ao contrato de adiantamento a depositantes identificado por contractId mantido pelo cliente na instituição transmissora

### Example
```python
from __future__ import print_function
import time
import unarranged-accounts-overdraft_2_0_0-RC1_0_yml
from unarranged-accounts-overdraft_2_0_0-RC1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = unarranged-accounts-overdraft_2_0_0-RC1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = unarranged-accounts-overdraft_2_0_0-RC1_0_yml.UnarrangedAccountsOverdraftApi(unarranged-accounts-overdraft_2_0_0-RC1_0_yml.ApiClient(configuration))
contract_id = 'contract_id_example' # str | Identificador do contrato para todos os tipos de operação de crédito.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém a lista de garantias vinculadas ao contrato de adiantamento a depositantes identificado por contractId
    api_response = api_instance.unarranged_accounts_overdraft_get_contracts_contract_id_warranties(contract_id, authorization, page=page, page_size=page_size, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnarrangedAccountsOverdraftApi->unarranged_accounts_overdraft_get_contracts_contract_id_warranties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Identificador do contrato para todos os tipos de operação de crédito. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_fapi_interaction_id** | **str**| Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \&quot;reproduzir\&quot; esse valor no cabeçalho de resposta. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **pagination_key** | **str**| Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. | [optional] 

### Return type

[**ResponseUnarrangedAccountOverdraftWarranties**](ResponseUnarrangedAccountOverdraftWarranties.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

