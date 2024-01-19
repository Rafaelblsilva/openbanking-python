# invoice-financings-2-1-0-rc-2-yml
API de informações de operações de antecipação de recebíveis do Open Finance Brasil - Fase 2.  API que retorna informações de operações de crédito do tipo antecipação de recebíveis, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos (ao menos para os últimos 12 meses), amortizações, garantias, encargos e taxas de juros remuneratórios. \\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ### Observação:   - No endpoint `/contracts/{contratId}/payments` a paginação ocorrerá sob os dados contidos no campo `releases` do tipo lista.     ## Permissions necessárias para a API Invoice-financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **INVOICE_FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **INVOICE_FINANCINGS_PAYMENTS_READ** 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.1.0-rc.2
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
import invoice-financings_2_1_0-rc_2_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import invoice-financings_2_1_0-rc_2_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import invoice-financings_2_1_0-rc_2_yml
from invoice-financings_2_1_0-rc_2_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = invoice-financings_2_1_0-rc_2_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = invoice-financings_2_1_0-rc_2_yml.InvoiceFinancingsApi(invoice-financings_2_1_0-rc_2_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)
pagination_key = 'pagination_key_example' # str | Identificador de rechamada, utilizado para evitar a contagem de chamadas ao endpoint durante a paginação. (optional)

try:
    # Obtém a lista de contratos de antecipação de recebíveis consentidos pelo cliente.
    api_response = api_instance.invoice_financings_get_contracts(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, page=page, page_size=page_size, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceFinancingsApi->invoice_financings_get_contracts: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = invoice-financings_2_1_0-rc_2_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = invoice-financings_2_1_0-rc_2_yml.InvoiceFinancingsApi(invoice-financings_2_1_0-rc_2_yml.ApiClient(configuration))
contract_id = 'contract_id_example' # str | Identificador do contrato para todos os tipos de operação de crédito.
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os dados do contrato de antecipação de recebíveis identificado por contractId
    api_response = api_instance.invoice_financings_get_contracts_contract_id(contract_id, authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceFinancingsApi->invoice_financings_get_contracts_contract_id: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = invoice-financings_2_1_0-rc_2_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = invoice-financings_2_1_0-rc_2_yml.InvoiceFinancingsApi(invoice-financings_2_1_0-rc_2_yml.ApiClient(configuration))
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
    # Obtém os dados de pagamentos do contrato de antecipação de recebíveis identificado por contractId
    api_response = api_instance.invoice_financings_get_contracts_contract_id_payments(contract_id, authorization, page=page, page_size=page_size, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceFinancingsApi->invoice_financings_get_contracts_contract_id_payments: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = invoice-financings_2_1_0-rc_2_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = invoice-financings_2_1_0-rc_2_yml.InvoiceFinancingsApi(invoice-financings_2_1_0-rc_2_yml.ApiClient(configuration))
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
    # Obtém os dados do cronograma de parcelas do contrato de antecipação de recebíveis identificado por contractId
    api_response = api_instance.invoice_financings_get_contracts_contract_id_scheduled_instalments(contract_id, authorization, page=page, page_size=page_size, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceFinancingsApi->invoice_financings_get_contracts_contract_id_scheduled_instalments: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = invoice-financings_2_1_0-rc_2_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = invoice-financings_2_1_0-rc_2_yml.InvoiceFinancingsApi(invoice-financings_2_1_0-rc_2_yml.ApiClient(configuration))
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
    # Obtém a lista de garantias vinculadas ao contrato de antecipação de recebíveis identificado por contractId
    api_response = api_instance.invoice_financings_get_contracts_contract_id_warranties(contract_id, authorization, page=page, page_size=page_size, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceFinancingsApi->invoice_financings_get_contracts_contract_id_warranties: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.banco.com.br/open-banking/invoice-financings/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InvoiceFinancingsApi* | [**invoice_financings_get_contracts**](docs/InvoiceFinancingsApi.md#invoice_financings_get_contracts) | **GET** /contracts | Obtém a lista de contratos de antecipação de recebíveis consentidos pelo cliente.
*InvoiceFinancingsApi* | [**invoice_financings_get_contracts_contract_id**](docs/InvoiceFinancingsApi.md#invoice_financings_get_contracts_contract_id) | **GET** /contracts/{contractId} | Obtém os dados do contrato de antecipação de recebíveis identificado por contractId
*InvoiceFinancingsApi* | [**invoice_financings_get_contracts_contract_id_payments**](docs/InvoiceFinancingsApi.md#invoice_financings_get_contracts_contract_id_payments) | **GET** /contracts/{contractId}/payments | Obtém os dados de pagamentos do contrato de antecipação de recebíveis identificado por contractId
*InvoiceFinancingsApi* | [**invoice_financings_get_contracts_contract_id_scheduled_instalments**](docs/InvoiceFinancingsApi.md#invoice_financings_get_contracts_contract_id_scheduled_instalments) | **GET** /contracts/{contractId}/scheduled-instalments | Obtém os dados do cronograma de parcelas do contrato de antecipação de recebíveis identificado por contractId
*InvoiceFinancingsApi* | [**invoice_financings_get_contracts_contract_id_warranties**](docs/InvoiceFinancingsApi.md#invoice_financings_get_contracts_contract_id_warranties) | **GET** /contracts/{contractId}/warranties | Obtém a lista de garantias vinculadas ao contrato de antecipação de recebíveis identificado por contractId

## Documentation For Models

 - [EnumContractAmortizationScheduled](docs/EnumContractAmortizationScheduled.md)
 - [EnumContractCalculation](docs/EnumContractCalculation.md)
 - [EnumContractFeeCharge](docs/EnumContractFeeCharge.md)
 - [EnumContractFeeChargeType](docs/EnumContractFeeChargeType.md)
 - [EnumContractFinanceChargeType](docs/EnumContractFinanceChargeType.md)
 - [EnumContractInstalmentPeriodicity](docs/EnumContractInstalmentPeriodicity.md)
 - [EnumContractInterestRateType](docs/EnumContractInterestRateType.md)
 - [EnumContractProductSubTypeInvoiceFinancings](docs/EnumContractProductSubTypeInvoiceFinancings.md)
 - [EnumContractProductTypeInvoiceFinancings](docs/EnumContractProductTypeInvoiceFinancings.md)
 - [EnumContractReferentialRateIndexerSubType](docs/EnumContractReferentialRateIndexerSubType.md)
 - [EnumContractReferentialRateIndexerType](docs/EnumContractReferentialRateIndexerType.md)
 - [EnumContractTaxPeriodicity](docs/EnumContractTaxPeriodicity.md)
 - [EnumWarrantySubType](docs/EnumWarrantySubType.md)
 - [EnumWarrantyType](docs/EnumWarrantyType.md)
 - [InvoiceFinancingsBallonPaymentAmount](docs/InvoiceFinancingsBallonPaymentAmount.md)
 - [InvoiceFinancingsBalloonPayment](docs/InvoiceFinancingsBalloonPayment.md)
 - [InvoiceFinancingsChargeOverParcel](docs/InvoiceFinancingsChargeOverParcel.md)
 - [InvoiceFinancingsContract](docs/InvoiceFinancingsContract.md)
 - [InvoiceFinancingsContractData](docs/InvoiceFinancingsContractData.md)
 - [InvoiceFinancingsContractInterestRate](docs/InvoiceFinancingsContractInterestRate.md)
 - [InvoiceFinancingsContractedFee](docs/InvoiceFinancingsContractedFee.md)
 - [InvoiceFinancingsContractedWarranty](docs/InvoiceFinancingsContractedWarranty.md)
 - [InvoiceFinancingsFeeOverParcel](docs/InvoiceFinancingsFeeOverParcel.md)
 - [InvoiceFinancingsFinanceCharge](docs/InvoiceFinancingsFinanceCharge.md)
 - [InvoiceFinancingsInstalments](docs/InvoiceFinancingsInstalments.md)
 - [InvoiceFinancingsPayments](docs/InvoiceFinancingsPayments.md)
 - [InvoiceFinancingsReleases](docs/InvoiceFinancingsReleases.md)
 - [InvoiceFinancingsReleasesOverParcel](docs/InvoiceFinancingsReleasesOverParcel.md)
 - [Links](docs/Links.md)
 - [Meta](docs/Meta.md)
 - [MetaSingle](docs/MetaSingle.md)
 - [ResponseError](docs/ResponseError.md)
 - [ResponseErrorMetaSingle](docs/ResponseErrorMetaSingle.md)
 - [ResponseErrorMetaSingleErrors](docs/ResponseErrorMetaSingleErrors.md)
 - [ResponseInvoiceFinancingsContract](docs/ResponseInvoiceFinancingsContract.md)
 - [ResponseInvoiceFinancingsContractList](docs/ResponseInvoiceFinancingsContractList.md)
 - [ResponseInvoiceFinancingsInstalments](docs/ResponseInvoiceFinancingsInstalments.md)
 - [ResponseInvoiceFinancingsPayments](docs/ResponseInvoiceFinancingsPayments.md)
 - [ResponseInvoiceFinancingsWarranties](docs/ResponseInvoiceFinancingsWarranties.md)
 - [XFapiInteractionId](docs/XFapiInteractionId.md)

## Documentation For Authorization


## OAuth2Security

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://authserver.example/authorization
- **Scopes**: 
 - **invoice-financings**: Escopo necessário para acesso à API Invoice-financings. O controle dos endpoints específicos é feito via permissions.

## OpenId



## Author

gt-interfaces@openbankingbr.org