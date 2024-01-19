# exchanges-1-0-0-rc-4-yml
API de informações de operações de Câmbio Open Finance Brasil – Fase 4.  API que retorna informações de operações de Câmbio realizadas nas instituições transmissoras por seus clientes, incluindo dados como informações da operação contratada, valor da operação em moeda nacional e moeda estrangeira, classificação da operação, forma de entrega, VET e, quando aplicável, valor a liquidar.  Também serão compartilhados os eventos de alteração da operação, caso existam, com as informações modificadas.  Não possui segregação entre pessoa natural e pessoa jurídica.  Requer consentimento do cliente para todos os endpoints.  __São escopo de compartilhamento as operações de compra e venda de moeda estrangeira de liquidação pronta ou futura, inclusive com adiantamento.  Operações de câmbio anuladas não são escopo de exposição, bem como eventos de vinculação de operações.  A exposição se dará por cada operação de câmbio contratada pelo cliente.__ 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0-rc.4
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
import exchanges_1_0_0-rc_4_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import exchanges_1_0_0-rc_4_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import exchanges_1_0_0-rc_4_yml
from exchanges_1_0_0-rc_4_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = exchanges_1_0_0-rc_4_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = exchanges_1_0_0-rc_4_yml.EventsApi(exchanges_1_0_0-rc_4_yml.ApiClient(configuration))
operation_id = 'operation_id_example' # str | Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser “espelhado” pela transmissora (server) no cabeçalho de resposta. Caso não seja recebido ou se for recebido um valor inválido, a transmissora deve gerar um x-fapi-interaction-id e retorná-lo na resposta com o HTTP Status Code 400. A receptora deve acatar o valor recebido da transmissora.
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

## Documentation for API Endpoints

All URIs are relative to *https://api.banco.com.br/open-banking/exchanges/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EventsApi* | [**exchanges_get_operations_operation_id_events**](docs/EventsApi.md#exchanges_get_operations_operation_id_events) | **GET** /operations/{operationId}/events | Obtém os dados dos eventos da operação de Câmbio identificada por operationId.
*OperationDetailsApi* | [**exchanges_get_operations_operation_id**](docs/OperationDetailsApi.md#exchanges_get_operations_operation_id) | **GET** /operations/{operationId} | Obtém os dados da operação de Câmbio identificada por operationId.
*ProductListApi* | [**exchanges_get_operations**](docs/ProductListApi.md#exchanges_get_operations) | **GET** /operations | Obtém a lista de operações de Câmbio mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.

## Documentation For Models

 - [EnumExchangesDeliveryForeignCurrency](docs/EnumExchangesDeliveryForeignCurrency.md)
 - [EnumExchangesEventType](docs/EnumExchangesEventType.md)
 - [EnumExchangesOperationType](docs/EnumExchangesOperationType.md)
 - [Events](docs/Events.md)
 - [EventsForeignPartie](docs/EventsForeignPartie.md)
 - [EventsLocalCurrencyOperationTax](docs/EventsLocalCurrencyOperationTax.md)
 - [EventsOperationOutstandingBalance](docs/EventsOperationOutstandingBalance.md)
 - [Links](docs/Links.md)
 - [LinksOperationId](docs/LinksOperationId.md)
 - [MetaWithAbleAdditionalProperties](docs/MetaWithAbleAdditionalProperties.md)
 - [OKResponseEvents](docs/OKResponseEvents.md)
 - [OKResponseOperationDetails](docs/OKResponseOperationDetails.md)
 - [OKResponseProductList](docs/OKResponseProductList.md)
 - [OpenDataMeta](docs/OpenDataMeta.md)
 - [OpenDataMetaOperationId](docs/OpenDataMetaOperationId.md)
 - [OperationDetails](docs/OperationDetails.md)
 - [OperationDetailsForeignOperationValue](docs/OperationDetailsForeignOperationValue.md)
 - [OperationDetailsLocalCurrencyOperationTax](docs/OperationDetailsLocalCurrencyOperationTax.md)
 - [OperationDetailsLocalCurrencyOperationValue](docs/OperationDetailsLocalCurrencyOperationValue.md)
 - [OperationDetailsOperationOutstandingBalance](docs/OperationDetailsOperationOutstandingBalance.md)
 - [OperationDetailsVetAmount](docs/OperationDetailsVetAmount.md)
 - [ProductList](docs/ProductList.md)
 - [ResponseErrorWithAbleAdditionalProperties](docs/ResponseErrorWithAbleAdditionalProperties.md)
 - [ResponseErrorWithAbleAdditionalPropertiesErrors](docs/ResponseErrorWithAbleAdditionalPropertiesErrors.md)

## Documentation For Authorization


## OAuth2AuthorizationCode

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://authserver.example/authorization
- **Scopes**: 
 - **exchanges**: Escopo necessário para acesso à API exchanges. O controle dos endpoints específicos é feito via permissions.


## Author

gt-interfaces@openbankingbr.org