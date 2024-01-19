# exchanges_1_0_0-rc_3_yml.EventsApi

All URIs are relative to *https://api.banco.com.br/open-banking/exchanges/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchanges_get_operations_operation_id_events**](EventsApi.md#exchanges_get_operations_operation_id_events) | **GET** /operations/{operationId}/events | Obtém os dados dos eventos da operação de Câmbio identificada por operationId.

# **exchanges_get_operations_operation_id_events**
> OKResponseEvents exchanges_get_operations_operation_id_events(operation_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, pagination_key=pagination_key)

Obtém os dados dos eventos da operação de Câmbio identificada por operationId.

Obtém os dados dos eventos da operação de Câmbio identificada por operationId.

### Example
```python
from __future__ import print_function
import time
import exchanges_1_0_0-rc_3_yml
from exchanges_1_0_0-rc_3_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = exchanges_1_0_0-rc_3_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = exchanges_1_0_0-rc_3_yml.EventsApi(exchanges_1_0_0-rc_3_yml.ApiClient(configuration))
operation_id = 'operation_id_example' # str | Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC. (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas.  A transmissora deve considerar entrada como 25, caso seja informado algum valor menor pela receptora.  Enquanto houver mais que 25 registros a enviar, a transmissora deve considerar o mínimo por página como 25.  Somente a última página retornada (ou primeira, no caso de página única) pode conter menos de 25 registros.  Mais informações, acesse Especificações de APIs > Padrões > Paginação.  (optional) (default to 25)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém os dados dos eventos da operação de Câmbio identificada por operationId.
    api_response = api_instance.exchanges_get_operations_operation_id_events(operation_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->exchanges_get_operations_operation_id_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **str**| Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \&quot;espelhado\&quot; pela transmissora (server) no cabeçalho de resposta. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC. | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas.  A transmissora deve considerar entrada como 25, caso seja informado algum valor menor pela receptora.  Enquanto houver mais que 25 registros a enviar, a transmissora deve considerar o mínimo por página como 25.  Somente a última página retornada (ou primeira, no caso de página única) pode conter menos de 25 registros.  Mais informações, acesse Especificações de APIs &gt; Padrões &gt; Paginação.  | [optional] [default to 25]
 **pagination_key** | **str**| Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. | [optional] 

### Return type

[**OKResponseEvents**](OKResponseEvents.md)

### Authorization

[OAuth2AuthorizationCode](../README.md#OAuth2AuthorizationCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

