# bank-fixed-incomes_1_0_2_yml.BalancesApi

All URIs are relative to *https://api.banco.com.br/open-banking/bank-fixed-incomes/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bankt_fixed_incomes_get_investments_investment_id_balances**](BalancesApi.md#bankt_fixed_incomes_get_investments_investment_id_balances) | **GET** /investments/{investmentId}/balances | Obtém a posição da operação de Renda Fixa Bancária identificada por investmentId.

# **bankt_fixed_incomes_get_investments_investment_id_balances**
> ResponseBankFixedIncomesBalances bankt_fixed_incomes_get_investments_investment_id_balances(investment_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)

Obtém a posição da operação de Renda Fixa Bancária identificada por investmentId.

Obtém a posição da operação de Renda Fixa Bancária identificada por investmentId.  Nos casos em que não houver posição para o investimento, ou seja, quantidade de ativos e valores monetários zerados, mas o mesmo ainda estiver no prazo de exposição (até 12 meses após a última movimentação), deve se retornar status code 200 e para o payload de retorno considerar os valores abaixo. Campos não obrigatórios não devem ser retornados:   - Valores monetários: 0.00 - Quantidade de ativos: 0.00 - Data e hora da última posição: mesmo conteúdo do campo requestDateTime 

### Example
```python
from __future__ import print_function
import time
import bank-fixed-incomes_1_0_2_yml
from bank-fixed-incomes_1_0_2_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = bank-fixed-incomes_1_0_2_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bank-fixed-incomes_1_0_2_yml.BalancesApi(bank-fixed-incomes_1_0_2_yml.ApiClient(configuration))
investment_id = 'investment_id_example' # str | Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém a posição da operação de Renda Fixa Bancária identificada por investmentId.
    api_response = api_instance.bankt_fixed_incomes_get_investments_investment_id_balances(investment_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancesApi->bankt_fixed_incomes_get_investments_investment_id_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investment_id** | **str**| Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora. | 
 **authorization** | **str**| Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado | 
 **x_fapi_interaction_id** | **str**| Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \&quot;espelhado\&quot; pela transmissora (server) no cabeçalho de resposta. | 
 **x_fapi_auth_date** | **str**| Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| O endereço IP do usuário se estiver atualmente logado com o receptor. | [optional] 
 **x_customer_user_agent** | **str**| Indica o user-agent que o usuário utiliza. | [optional] 

### Return type

[**ResponseBankFixedIncomesBalances**](ResponseBankFixedIncomesBalances.md)

### Authorization

[OAuth2AuthorizationCode](../README.md#OAuth2AuthorizationCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

