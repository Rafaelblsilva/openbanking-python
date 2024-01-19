# funds_1_0_0_yml.ProductIdentificationApi

All URIs are relative to *https://api.banco.com.br/open-banking/funds/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**funds_get_investments_investment_id**](ProductIdentificationApi.md#funds_get_investments_investment_id) | **GET** /investments/{investmentId} | Obtém os dados da operação de Fundos de Investimento identificada por investmentId.

# **funds_get_investments_investment_id**
> ResponseFundsProductIdentification funds_get_investments_investment_id(investment_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)

Obtém os dados da operação de Fundos de Investimento identificada por investmentId.

Obtém os dados da operação de Fundos de Investimento identificada por investmentId.

### Example
```python
from __future__ import print_function
import time
import funds_1_0_0_yml
from funds_1_0_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = funds_1_0_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = funds_1_0_0_yml.ProductIdentificationApi(funds_1_0_0_yml.ApiClient(configuration))
investment_id = 'investment_id_example' # str | Identifica de forma única o relacionamento do cliente com o fundo, mantendo as regras de imutabilidade dentro da instituição transmissora.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC. (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os dados da operação de Fundos de Investimento identificada por investmentId.
    api_response = api_instance.funds_get_investments_investment_id(investment_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductIdentificationApi->funds_get_investments_investment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investment_id** | **str**| Identifica de forma única o relacionamento do cliente com o fundo, mantendo as regras de imutabilidade dentro da instituição transmissora. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \&quot;espelhado\&quot; pela transmissora (server) no cabeçalho de resposta. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC. | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponseFundsProductIdentification**](ResponseFundsProductIdentification.md)

### Authorization

[OAuth2AuthorizationCode](../README.md#OAuth2AuthorizationCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

