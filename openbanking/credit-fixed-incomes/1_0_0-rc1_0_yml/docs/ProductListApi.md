# credit-fixed-incomes_1_0_0-rc1_0_yml.ProductListApi

All URIs are relative to *https://api.banco.com.br/open-banking/credit-fixed-incomes/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_fixed_incomes_get_investments**](ProductListApi.md#credit_fixed_incomes_get_investments) | **GET** /investments | Obtém a lista de operações de Renda Fixa Crédito mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.

# **credit_fixed_incomes_get_investments**
> ResponseCreditFixedIncomesProductList credit_fixed_incomes_get_investments(authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, pagination_key=pagination_key)

Obtém a lista de operações de Renda Fixa Crédito mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.

Obtém a lista de operações de Renda Fixa Crédito mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.        -

### Example
```python
from __future__ import print_function
import time
import credit-fixed-incomes_1_0_0-rc1_0_yml
from credit-fixed-incomes_1_0_0-rc1_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = credit-fixed-incomes_1_0_0-rc1_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = credit-fixed-incomes_1_0_0-rc1_0_yml.ProductListApi(credit-fixed-incomes_1_0_0-rc1_0_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC. (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém a lista de operações de Renda Fixa Crédito mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.
    api_response = api_instance.credit_fixed_incomes_get_investments(authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductListApi->credit_fixed_incomes_get_investments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \&quot;espelhado\&quot; pela transmissora (server) no cabeçalho de resposta. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC. | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]
 **pagination_key** | **str**| Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. | [optional] 

### Return type

[**ResponseCreditFixedIncomesProductList**](ResponseCreditFixedIncomesProductList.md)

### Authorization

[OAuth2Security](../README.md#OAuth2Security), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

