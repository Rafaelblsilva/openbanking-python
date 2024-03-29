# bank-fixed-incomes-1-0-1-yml
API de informações de operações de Renda Fixa Bancária Open Finance Brasil (Fase 4). API que retorna informações de operações de investimento do tipo Renda Fixa Bancária (CDB/RDB, LCI e LCA) mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação do produto, rentabilidade, quantidade, prazos, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A exposição se dará por cada operação de renda fixa contratada pelo cliente. 

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
import bank-fixed-incomes_1_0_1_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import bank-fixed-incomes_1_0_1_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import bank-fixed-incomes_1_0_1_yml
from bank-fixed-incomes_1_0_1_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthorizationCode
configuration = bank-fixed-incomes_1_0_1_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bank-fixed-incomes_1_0_1_yml.BalancesApi(bank-fixed-incomes_1_0_1_yml.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *https://api.banco.com.br/open-banking/bank-fixed-incomes/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BalancesApi* | [**bankt_fixed_incomes_get_investments_investment_id_balances**](docs/BalancesApi.md#bankt_fixed_incomes_get_investments_investment_id_balances) | **GET** /investments/{investmentId}/balances | Obtém a posição da operação de Renda Fixa Bancária identificada por investmentId.
*ProductIdentificationApi* | [**bankt_fixed_incomes_get_investments_investment_id**](docs/ProductIdentificationApi.md#bankt_fixed_incomes_get_investments_investment_id) | **GET** /investments/{investmentId} | Obtém os dados da operação de Renda Fixa Bancária identificada por investmentId.
*ProductListApi* | [**bankt_fixed_incomes_get_investments**](docs/ProductListApi.md#bankt_fixed_incomes_get_investments) | **GET** /investments | Obtém a lista de operações de Renda Fixa Bancária mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.
*TransactionsApi* | [**bankt_fixed_incomes_get_investments_investment_id_transactions**](docs/TransactionsApi.md#bankt_fixed_incomes_get_investments_investment_id_transactions) | **GET** /investments/{investmentId}/transactions | Obtém as movimentações históricas (últimos 12 meses) da operação de Renda Fixa Bancária identificada por investmentId.
*TransactionsCurrentApi* | [**bankt_fixed_incomes_get_investments_investment_id_transactions_current**](docs/TransactionsCurrentApi.md#bankt_fixed_incomes_get_investments_investment_id_transactions_current) | **GET** /investments/{investmentId}/transactions-current | Obtém as movimentações recentes da operação de Renda Fixa Bancária identificada por investmentId. O período a ser considerado para apresentação de movimentações será de até 7 dias - 7 dias anteriores da consulta, incluindo o dia da consulta (D-6).

## Documentation For Models

 - [BalanceAmount](docs/BalanceAmount.md)
 - [BalanceCurrency](docs/BalanceCurrency.md)
 - [BankFixedIncomeLinks](docs/BankFixedIncomeLinks.md)
 - [BankFixedIncomeProductListLinks](docs/BankFixedIncomeProductListLinks.md)
 - [BankFixedIncomeTransactionsLinks](docs/BankFixedIncomeTransactionsLinks.md)
 - [BankFixedIncomesMeta](docs/BankFixedIncomesMeta.md)
 - [BankFixedIncomesProductMovement](docs/BankFixedIncomesProductMovement.md)
 - [BankFixedIncomesProductMovementFinancialTransactionTax](docs/BankFixedIncomesProductMovementFinancialTransactionTax.md)
 - [BankFixedIncomesProductMovementIncomeTax](docs/BankFixedIncomesProductMovementIncomeTax.md)
 - [BankFixedIncomesProductMovementTransactionGrossValue](docs/BankFixedIncomesProductMovementTransactionGrossValue.md)
 - [BankFixedIncomesProductMovementTransactionNetValue](docs/BankFixedIncomesProductMovementTransactionNetValue.md)
 - [BankFixedIncomesProductMovementTransactionUnitPrice](docs/BankFixedIncomesProductMovementTransactionUnitPrice.md)
 - [BankFixedIncomesTransactionsMeta](docs/BankFixedIncomesTransactionsMeta.md)
 - [CurrencyCode](docs/CurrencyCode.md)
 - [EnumBankFixedIncomeIndexer](docs/EnumBankFixedIncomeIndexer.md)
 - [EnumBankFixedIncomeMovementType](docs/EnumBankFixedIncomeMovementType.md)
 - [EnumBankFixedIncomeTransactionType](docs/EnumBankFixedIncomeTransactionType.md)
 - [EnumCalculation](docs/EnumCalculation.md)
 - [EnumInvestmentType](docs/EnumInvestmentType.md)
 - [EnumRatePeriodicity](docs/EnumRatePeriodicity.md)
 - [EnumRateType](docs/EnumRateType.md)
 - [IdentifyProduct](docs/IdentifyProduct.md)
 - [IdentifyProductIssueUnitPrice](docs/IdentifyProductIssueUnitPrice.md)
 - [Remuneration](docs/Remuneration.md)
 - [ResponseBankFixedIncomesBalances](docs/ResponseBankFixedIncomesBalances.md)
 - [ResponseBankFixedIncomesBalancesData](docs/ResponseBankFixedIncomesBalancesData.md)
 - [ResponseBankFixedIncomesBalancesDataBlockedBalance](docs/ResponseBankFixedIncomesBalancesDataBlockedBalance.md)
 - [ResponseBankFixedIncomesBalancesDataFinancialTransactionTax](docs/ResponseBankFixedIncomesBalancesDataFinancialTransactionTax.md)
 - [ResponseBankFixedIncomesBalancesDataGrossAmount](docs/ResponseBankFixedIncomesBalancesDataGrossAmount.md)
 - [ResponseBankFixedIncomesBalancesDataIncomeTax](docs/ResponseBankFixedIncomesBalancesDataIncomeTax.md)
 - [ResponseBankFixedIncomesBalancesDataNetAmount](docs/ResponseBankFixedIncomesBalancesDataNetAmount.md)
 - [ResponseBankFixedIncomesBalancesDataPurchaseUnitPrice](docs/ResponseBankFixedIncomesBalancesDataPurchaseUnitPrice.md)
 - [ResponseBankFixedIncomesBalancesDataUpdatedUnitPrice](docs/ResponseBankFixedIncomesBalancesDataUpdatedUnitPrice.md)
 - [ResponseBankFixedIncomesProductIdentification](docs/ResponseBankFixedIncomesProductIdentification.md)
 - [ResponseBankFixedIncomesProductList](docs/ResponseBankFixedIncomesProductList.md)
 - [ResponseBankFixedIncomesProductListData](docs/ResponseBankFixedIncomesProductListData.md)
 - [ResponseBankFixedIncomesTransactions](docs/ResponseBankFixedIncomesTransactions.md)
 - [ResponseError](docs/ResponseError.md)
 - [ResponseErrorErrors](docs/ResponseErrorErrors.md)
 - [ResponseErrorMeta](docs/ResponseErrorMeta.md)
 - [ResponseErrorMetaSingle](docs/ResponseErrorMetaSingle.md)
 - [ResponseErrorMetaSingleErrors](docs/ResponseErrorMetaSingleErrors.md)
 - [ResponseErrorMetaSingleMeta](docs/ResponseErrorMetaSingleMeta.md)

## Documentation For Authorization


## OAuth2AuthorizationCode

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://authserver.example/authorization
- **Scopes**: 
 - **bank-fixed-incomes**: Escopo necessário para acesso à API Bank Fixed Incomes. O controle dos endpoints específicos é feito via permissions.


## Author

gt-interfaces@openbankingbr.org
