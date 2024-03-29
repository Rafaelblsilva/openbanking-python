# variable-incomes-1-0-1-yml
API de informações de operações de Renda Variável Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Renda Variável mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente, movimentações financeiras e detalhes da nota de negociação.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  A granularidade de exposição de operações de renda variável se dá por cada ativo (ticker) da carteira do cliente.  Compartilhamento considera lote padrão e fracionário, entretanto, no Open Finance Brasil, as informações são consolidadas via ticker do lote padrão.  A defasagem em relação ao canal eletrônico da instituição deve ser o fechamento (pregão) do dia anterior (d-1).   Em relação ao aluguel de ações: neste momento não faz parte do escopo de compartilhamento a carteira/posição de aluguel do cliente (ativos alugados e movimentações relacionadas a esses ativos).  Apenas deve ser compartilhado as transações de pagamento ou recebimento de juros oriundos dos contratos de ações alugadas (ou doadas) pelos clientes.  Para o identificador do investimento (investmentId) deve ser adotado o seguinte comportamento:  - Após 12 meses sem movimentações e com quantidade de ativos zerada, o resourceId correspondente ao investmentId em questão deve passar ao status UNAVAILABLE (considerando consentimento válido);  - Nas situações em que o cliente compre novamente o ativo após um período de 12 meses sem movimentação e com quantidade de ativos zerada, o mesmo identificador (investmentId) deve ser utilizado. Especificamente para tais produtos, o status do recurso na resources deve passar de UNAVAILABLE para AVAILABLE.  Segue abaixo tabela com o escopo de produtos a ser considerado para compartilhamento:  ```    |----------------------|-------------------------------|----------------------|-----------------------------------|    | CLASSE DE ATIVOS     | PRODUTO                       | SUBPRODUTO           | DENOMINAÇÃO                       |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       |     -                | FIAGRO                            |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | Subscrição           | Bonus / Direito / Recibo          |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       | Fundo imobiliario    | FII                               |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | À vista              | ON / PN / UNIT                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF de Renda Variável             |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF Internacional                 |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF Renda Fixa       | ETF Renda Fixa                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    ``` 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.1
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
import variable-incomes_1_0_1_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import variable-incomes_1_0_1_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import variable-incomes_1_0_1_yml
from variable-incomes_1_0_1_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = variable-incomes_1_0_1_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = variable-incomes_1_0_1_yml.BalancesApi(variable-incomes_1_0_1_yml.ApiClient(configuration))
investment_id = 'investment_id_example' # str | Identifica de forma única o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta.
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC. (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém a posição da operação de Renda Variável identificada por investmentId.
    api_response = api_instance.variable_incomes_get_investments_investment_id_balances(investment_id, authorization, x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancesApi->variable_incomes_get_investments_investment_id_balances: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.banco.com.br/open-banking/variable-incomes/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BalancesApi* | [**variable_incomes_get_investments_investment_id_balances**](docs/BalancesApi.md#variable_incomes_get_investments_investment_id_balances) | **GET** /investments/{investmentId}/balances | Obtém a posição da operação de Renda Variável identificada por investmentId.
*BrokerNoteDetailsApi* | [**variable_incomes_get_investments_investment_id_broker_notes_broker_note_id**](docs/BrokerNoteDetailsApi.md#variable_incomes_get_investments_investment_id_broker_notes_broker_note_id) | **GET** /broker-notes/{brokerNoteId} | Obtém as informações da nota de negociação identificado nas movimentações de compra e venda de ativos em bolsa. O brokerNoteId é enviado nos movimentos de compra ou venda de ativos e deve ser passada como parâmetro de entrada no endpoint “Nota de Negociação”.Como conteúdo do campo brokerNoteId é esperado que a transmissora gere um identificar único, imutável, para cada número (natural) de nota de negociação. 
*ProductIdentificationApi* | [**variable_incomes_get_investments_investment_id**](docs/ProductIdentificationApi.md#variable_incomes_get_investments_investment_id) | **GET** /investments/{investmentId} | Obtém os dados da operação de Renda Variável identificada por investmentId.
*ProductListApi* | [**variable_incomes_get_investments**](docs/ProductListApi.md#variable_incomes_get_investments) | **GET** /investments | Obtém a lista de operações de Renda Variável mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.
*TransactionsApi* | [**variable_incomes_get_investments_investment_id_transactions**](docs/TransactionsApi.md#variable_incomes_get_investments_investment_id_transactions) | **GET** /investments/{investmentId}/transactions | Obtém as movimentações históricas (últimos 12 meses) da operação de Renda Variável identificada por investmentId.
*TransactionsCurrentApi* | [**variable_incomes_get_investments_investment_id_transactions_current**](docs/TransactionsCurrentApi.md#variable_incomes_get_investments_investment_id_transactions_current) | **GET** /investments/{investmentId}/transactions-current | Obtém as movimentações recentes da operação de Renda Variável identificada por investmentId. O período a ser considerado para apresentação de movimentações será de até 7 dias - 7 dias anteriores da consulta, incluindo o dia da consulta (D-6).

## Documentation For Models

 - [EnumVariableIncomesTransactionsCurrentTransactionType](docs/EnumVariableIncomesTransactionsCurrentTransactionType.md)
 - [EnumVariableIncomesTransactionsCurrentType](docs/EnumVariableIncomesTransactionsCurrentType.md)
 - [EnumVariableIncomesTransactionsTransactionType](docs/EnumVariableIncomesTransactionsTransactionType.md)
 - [EnumVariableIncomesTransactionsType](docs/EnumVariableIncomesTransactionsType.md)
 - [InlineResponse423](docs/InlineResponse423.md)
 - [InlineResponse4231](docs/InlineResponse4231.md)
 - [InlineResponse4231Meta](docs/InlineResponse4231Meta.md)
 - [InlineResponse423Meta](docs/InlineResponse423Meta.md)
 - [MetaOnlyRequestDateTime](docs/MetaOnlyRequestDateTime.md)
 - [MetaSingle](docs/MetaSingle.md)
 - [MetaWithAbleAdditionalProperties](docs/MetaWithAbleAdditionalProperties.md)
 - [ResponseErrorMetaSingle](docs/ResponseErrorMetaSingle.md)
 - [ResponseErrorMetaSingleErrors](docs/ResponseErrorMetaSingleErrors.md)
 - [ResponseErrorWithAbleAdditionalProperties](docs/ResponseErrorWithAbleAdditionalProperties.md)
 - [ResponseVariableIncomesBalanceData](docs/ResponseVariableIncomesBalanceData.md)
 - [ResponseVariableIncomesBalances](docs/ResponseVariableIncomesBalances.md)
 - [ResponseVariableIncomesBroker](docs/ResponseVariableIncomesBroker.md)
 - [ResponseVariableIncomesBrokerData](docs/ResponseVariableIncomesBrokerData.md)
 - [ResponseVariableIncomesBrokerDataBrokerageFee](docs/ResponseVariableIncomesBrokerDataBrokerageFee.md)
 - [ResponseVariableIncomesBrokerDataClearingCustodyFee](docs/ResponseVariableIncomesBrokerDataClearingCustodyFee.md)
 - [ResponseVariableIncomesBrokerDataClearingRegistrationFee](docs/ResponseVariableIncomesBrokerDataClearingRegistrationFee.md)
 - [ResponseVariableIncomesBrokerDataClearingSettlementFee](docs/ResponseVariableIncomesBrokerDataClearingSettlementFee.md)
 - [ResponseVariableIncomesBrokerDataGrossValue](docs/ResponseVariableIncomesBrokerDataGrossValue.md)
 - [ResponseVariableIncomesBrokerDataIncomeTax](docs/ResponseVariableIncomesBrokerDataIncomeTax.md)
 - [ResponseVariableIncomesBrokerDataNetValue](docs/ResponseVariableIncomesBrokerDataNetValue.md)
 - [ResponseVariableIncomesBrokerDataStockExchangeAssetTradeNoticeFee](docs/ResponseVariableIncomesBrokerDataStockExchangeAssetTradeNoticeFee.md)
 - [ResponseVariableIncomesBrokerDataStockExchangeFee](docs/ResponseVariableIncomesBrokerDataStockExchangeFee.md)
 - [ResponseVariableIncomesBrokerDataTaxes](docs/ResponseVariableIncomesBrokerDataTaxes.md)
 - [ResponseVariableIncomesProductIdentification](docs/ResponseVariableIncomesProductIdentification.md)
 - [ResponseVariableIncomesProductIdentificationData](docs/ResponseVariableIncomesProductIdentificationData.md)
 - [ResponseVariableIncomesProductList](docs/ResponseVariableIncomesProductList.md)
 - [ResponseVariableIncomesProductListData](docs/ResponseVariableIncomesProductListData.md)
 - [ResponseVariableIncomesTransactions](docs/ResponseVariableIncomesTransactions.md)
 - [ResponseVariableIncomesTransactionsCurrent](docs/ResponseVariableIncomesTransactionsCurrent.md)
 - [ResponseVariableIncomesTransactionsCurrentData](docs/ResponseVariableIncomesTransactionsCurrentData.md)
 - [ResponseVariableIncomesTransactionsData](docs/ResponseVariableIncomesTransactionsData.md)
 - [ResponseVariableIncomesTransactionsDataTransactionUnitPrice](docs/ResponseVariableIncomesTransactionsDataTransactionUnitPrice.md)
 - [ResponseVariableIncomesTransactionsDataTransactionValue](docs/ResponseVariableIncomesTransactionsDataTransactionValue.md)
 - [VariableIncomesBalancesBlockedBalance](docs/VariableIncomesBalancesBlockedBalance.md)
 - [VariableIncomesBalancesClosingPrice](docs/VariableIncomesBalancesClosingPrice.md)
 - [VariableIncomesBalancesGrossAmount](docs/VariableIncomesBalancesGrossAmount.md)
 - [VariableIncomesLinks](docs/VariableIncomesLinks.md)
 - [VariableIncomesMeta](docs/VariableIncomesMeta.md)
 - [VariableIncomesProductListLinks](docs/VariableIncomesProductListLinks.md)
 - [VariableIncomesTransactionsLinks](docs/VariableIncomesTransactionsLinks.md)

## Documentation For Authorization


## OAuth2AuthorizationCode

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://authserver.example/authorization
- **Scopes**: 
 - **variable-incomes**: Escopo necessário para acesso à API Variable Incomes. O controle dos endpoints específicos é feito via permissions.


## Author

gt-interfaces@openbankingbr.org
