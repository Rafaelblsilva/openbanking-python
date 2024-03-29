# opendata-accounts-1-0-0-beta-1-yml
A API descrita neste documento é referente as API Accounts da fase OpenData do Open Finance Brasil.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0-beta.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://servicedesk.openbankingbrasil.org.br/Login.jsp?navLanguage=pt-BR](https://servicedesk.openbankingbrasil.org.br/Login.jsp?navLanguage=pt-BR)

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
import opendata-accounts_1_0_0-beta_1_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import opendata-accounts_1_0_0-beta_1_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import opendata-accounts_1_0_0-beta_1_yml
from opendata-accounts_1_0_0-beta_1_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = opendata-accounts_1_0_0-beta_1_yml.AccountsApi(opendata-accounts_1_0_0-beta_1_yml.ApiClient(configuration))
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém dados das contas pessoa jurídica
    api_response = api_instance.get_business_accounts(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_business_accounts: %s\n" % e)

# create an instance of the API class
api_instance = opendata-accounts_1_0_0-beta_1_yml.AccountsApi(opendata-accounts_1_0_0-beta_1_yml.ApiClient(configuration))
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém dados das contas pessoa natural
    api_response = api_instance.get_personal_accounts(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_personal_accounts: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://api.banco.com.br/open-banking/opendata-accounts/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**get_business_accounts**](docs/AccountsApi.md#get_business_accounts) | **GET** /business-accounts | Obtém dados das contas pessoa jurídica
*AccountsApi* | [**get_personal_accounts**](docs/AccountsApi.md#get_personal_accounts) | **GET** /personal-accounts | Obtém dados das contas pessoa natural

## Documentation For Models

 - [AccountFee](docs/AccountFee.md)
 - [AccountOtherService](docs/AccountOtherService.md)
 - [AccountPriorityService](docs/AccountPriorityService.md)
 - [AccountPriorityServiceCode](docs/AccountPriorityServiceCode.md)
 - [AccountType](docs/AccountType.md)
 - [AccountsIncomeRate](docs/AccountsIncomeRate.md)
 - [AccountsTermsConditions](docs/AccountsTermsConditions.md)
 - [BusinessAccountsService](docs/BusinessAccountsService.md)
 - [BusinessData](docs/BusinessData.md)
 - [BusinessDataFees](docs/BusinessDataFees.md)
 - [Currency](docs/Currency.md)
 - [Customer](docs/Customer.md)
 - [Links](docs/Links.md)
 - [MaximumPrice](docs/MaximumPrice.md)
 - [Meta](docs/Meta.md)
 - [MinimumBalance](docs/MinimumBalance.md)
 - [MinimumPrice](docs/MinimumPrice.md)
 - [MonthlyPrice](docs/MonthlyPrice.md)
 - [OpeningClosingChannels](docs/OpeningClosingChannels.md)
 - [PersonalAccountPrice](docs/PersonalAccountPrice.md)
 - [PersonalAccountPriceIntervals](docs/PersonalAccountPriceIntervals.md)
 - [PersonalAccountPriorityServicePrice](docs/PersonalAccountPriorityServicePrice.md)
 - [PersonalAccountServiceBundle](docs/PersonalAccountServiceBundle.md)
 - [PersonalData](docs/PersonalData.md)
 - [PersonalDataParticipant](docs/PersonalDataParticipant.md)
 - [Price](docs/Price.md)
 - [PriceIntervals](docs/PriceIntervals.md)
 - [PriorityServiceMaximumPrice](docs/PriorityServiceMaximumPrice.md)
 - [PriorityServiceMinimumPrice](docs/PriorityServiceMinimumPrice.md)
 - [PriorityServiceName](docs/PriorityServiceName.md)
 - [ResponseBusinessAccounts](docs/ResponseBusinessAccounts.md)
 - [ResponseError](docs/ResponseError.md)
 - [ResponseErrorMeta](docs/ResponseErrorMeta.md)
 - [ResponseErrorMetaSingle](docs/ResponseErrorMetaSingle.md)
 - [ResponseErrorMetaSingleErrors](docs/ResponseErrorMetaSingleErrors.md)
 - [ResponseErrorMetaSingleMeta](docs/ResponseErrorMetaSingleMeta.md)
 - [ResponsePersonalAccounts](docs/ResponsePersonalAccounts.md)
 - [ServiceBundle](docs/ServiceBundle.md)
 - [ServiceBundleServiceDetail](docs/ServiceBundleServiceDetail.md)
 - [TransactionMethods](docs/TransactionMethods.md)

## Documentation For Authorization


## APIKey1

- **Type**: API key
- **API key parameter name**: API Key
- **Location**: URL query string

## APIKey2

- **Type**: API key
- **API key parameter name**: API Key
- **Location**: URL query string


## Author


