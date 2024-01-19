# variable-incomes_1_0_0_yml.BrokerNoteDetailsApi

All URIs are relative to *https://api.banco.com.br/open-banking/variable-incomes/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variable_incomes_get_investments_investment_id_broker_notes_broker_note_id**](BrokerNoteDetailsApi.md#variable_incomes_get_investments_investment_id_broker_notes_broker_note_id) | **GET** /broker-notes/{brokerNoteId} | Obtém as informações da nota de negociação identificado nas movimentações de compra e venda de ativos em bolsa. O brokerNoteId é enviado nos movimentos de compra ou venda de ativos e deve ser passada como parâmetro de entrada no endpoint “Nota de Negociação”.Como conteúdo do campo brokerNoteId é esperado que a transmissora gere um identificar único, imutável, para cada número (natural) de nota de negociação. 

# **variable_incomes_get_investments_investment_id_broker_notes_broker_note_id**
> ResponseVariableIncomesBroker variable_incomes_get_investments_investment_id_broker_notes_broker_note_id(broker_note_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)

Obtém as informações da nota de negociação identificado nas movimentações de compra e venda de ativos em bolsa. O brokerNoteId é enviado nos movimentos de compra ou venda de ativos e deve ser passada como parâmetro de entrada no endpoint “Nota de Negociação”.Como conteúdo do campo brokerNoteId é esperado que a transmissora gere um identificar único, imutável, para cada número (natural) de nota de negociação. 

Obtém as informações da nota de negociação identificado nas movimentações de compra e venda de ativos em bolsa. O brokerNoteId é enviado nos movimentos de compra ou venda de ativos e deve ser passada como parâmetro de entrada no endpoint “Nota de Negociação”.Como conteúdo do campo brokerNoteId é esperado que a transmissora gere um identificar único, imutável, para cada número (natural) de nota de negociação. 

### Example
```python
from __future__ import print_function
import time
import variable-incomes_1_0_0_yml
from variable-incomes_1_0_0_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = variable-incomes_1_0_0_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = variable-incomes_1_0_0_yml.BrokerNoteDetailsApi(variable-incomes_1_0_0_yml.ApiClient(configuration))
broker_note_id = 'broker_note_id_example' # str | Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC. (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém as informações da nota de negociação identificado nas movimentações de compra e venda de ativos em bolsa. O brokerNoteId é enviado nos movimentos de compra ou venda de ativos e deve ser passada como parâmetro de entrada no endpoint “Nota de Negociação”.Como conteúdo do campo brokerNoteId é esperado que a transmissora gere um identificar único, imutável, para cada número (natural) de nota de negociação. 
    api_response = api_instance.variable_incomes_get_investments_investment_id_broker_notes_broker_note_id(broker_note_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BrokerNoteDetailsApi->variable_incomes_get_investments_investment_id_broker_notes_broker_note_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_note_id** | **str**| Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \&quot;espelhado\&quot; pela transmissora (server) no cabeçalho de resposta. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC. | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponseVariableIncomesBroker**](ResponseVariableIncomesBroker.md)

### Authorization

[OAuth2AuthorizationCode](../README.md#OAuth2AuthorizationCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

