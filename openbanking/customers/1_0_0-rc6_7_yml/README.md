# customers-1-0-0-rc6-7-yml
API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0-rc6.7
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
import customers_1_0_0-rc6_7_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import customers_1_0_0-rc6_7_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import customers_1_0_0-rc6_7_yml
from customers_1_0_0-rc6_7_yml.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = customers_1_0_0-rc6_7_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = customers_1_0_0-rc6_7_yml.CustomersApi(customers_1_0_0-rc6_7_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os registros de relacionamentos com a instituição financeira e de representantes da pessoa jurídica.
    api_response = api_instance.customers_get_business_financial_relations(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_get_business_financial_relations: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = customers_1_0_0-rc6_7_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = customers_1_0_0-rc6_7_yml.CustomersApi(customers_1_0_0-rc6_7_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os registros de identificação da pessoa jurídica.
    api_response = api_instance.customers_get_business_identifications(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_get_business_identifications: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = customers_1_0_0-rc6_7_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = customers_1_0_0-rc6_7_yml.CustomersApi(customers_1_0_0-rc6_7_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os registros de qualificação da pessoa jurídica.
    api_response = api_instance.customers_get_business_qualifications(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_get_business_qualifications: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = customers_1_0_0-rc6_7_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = customers_1_0_0-rc6_7_yml.CustomersApi(customers_1_0_0-rc6_7_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os registros de relacionamentos com a instituição financeira e de representantes da pessoa natural.
    api_response = api_instance.customers_get_personal_financial_relations(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_get_personal_financial_relations: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = customers_1_0_0-rc6_7_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = customers_1_0_0-rc6_7_yml.CustomersApi(customers_1_0_0-rc6_7_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os registros de identificação da pessoa natural.
    api_response = api_instance.customers_get_personal_identifications(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_get_personal_identifications: %s\n" % e)

# Configure OAuth2 access token for authorization: OAuth2Security
configuration = customers_1_0_0-rc6_7_yml.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = customers_1_0_0-rc6_7_yml.CustomersApi(customers_1_0_0-rc6_7_yml.ApiClient(configuration))
authorization = 'authorization_example' # str | Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado
x_fapi_auth_date = 'x_fapi_auth_date_example' # str | Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | O endereço IP do usuário se estiver atualmente logado com o receptor. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta. (optional)
x_customer_user_agent = 'x_customer_user_agent_example' # str | Indica o user-agent que o usuário utiliza. (optional)

try:
    # Obtém os registros de qualificação da pessoa natural.
    api_response = api_instance.customers_get_personal_qualifications(authorization, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_customer_user_agent=x_customer_user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_get_personal_qualifications: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.banco.com.br/open-banking/customers/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CustomersApi* | [**customers_get_business_financial_relations**](docs/CustomersApi.md#customers_get_business_financial_relations) | **GET** /business/financial-relations | Obtém os registros de relacionamentos com a instituição financeira e de representantes da pessoa jurídica.
*CustomersApi* | [**customers_get_business_identifications**](docs/CustomersApi.md#customers_get_business_identifications) | **GET** /business/identifications | Obtém os registros de identificação da pessoa jurídica.
*CustomersApi* | [**customers_get_business_qualifications**](docs/CustomersApi.md#customers_get_business_qualifications) | **GET** /business/qualifications | Obtém os registros de qualificação da pessoa jurídica.
*CustomersApi* | [**customers_get_personal_financial_relations**](docs/CustomersApi.md#customers_get_personal_financial_relations) | **GET** /personal/financial-relations | Obtém os registros de relacionamentos com a instituição financeira e de representantes da pessoa natural.
*CustomersApi* | [**customers_get_personal_identifications**](docs/CustomersApi.md#customers_get_personal_identifications) | **GET** /personal/identifications | Obtém os registros de identificação da pessoa natural.
*CustomersApi* | [**customers_get_personal_qualifications**](docs/CustomersApi.md#customers_get_personal_qualifications) | **GET** /personal/qualifications | Obtém os registros de qualificação da pessoa natural.

## Documentation For Models

 - [BusinessAccount](docs/BusinessAccount.md)
 - [BusinessContacts](docs/BusinessContacts.md)
 - [BusinessFinancialRelationData](docs/BusinessFinancialRelationData.md)
 - [BusinessIdentificationData](docs/BusinessIdentificationData.md)
 - [BusinessInformedPatrimony](docs/BusinessInformedPatrimony.md)
 - [BusinessOtherDocument](docs/BusinessOtherDocument.md)
 - [BusinessPostalAddress](docs/BusinessPostalAddress.md)
 - [BusinessProcurator](docs/BusinessProcurator.md)
 - [BusinessQualificationData](docs/BusinessQualificationData.md)
 - [BusinessQualificationDataInformedRevenue](docs/BusinessQualificationDataInformedRevenue.md)
 - [CustomerEmail](docs/CustomerEmail.md)
 - [CustomerPhone](docs/CustomerPhone.md)
 - [EconomicActivity](docs/EconomicActivity.md)
 - [EnumAreaCode](docs/EnumAreaCode.md)
 - [EnumCountrySubDivision](docs/EnumCountrySubDivision.md)
 - [EnumCustomerPhoneType](docs/EnumCustomerPhoneType.md)
 - [EnumFiliationType](docs/EnumFiliationType.md)
 - [EnumInformedIncomeFrequency](docs/EnumInformedIncomeFrequency.md)
 - [EnumInformedRevenueFrequency](docs/EnumInformedRevenueFrequency.md)
 - [EnumMaritalStatusCode](docs/EnumMaritalStatusCode.md)
 - [EnumOccupationMainCodeType](docs/EnumOccupationMainCodeType.md)
 - [EnumPartiesParticipationDocumentType](docs/EnumPartiesParticipationDocumentType.md)
 - [EnumPersonalOtherDocumentType](docs/EnumPersonalOtherDocumentType.md)
 - [EnumProcuratorsTypePersonal](docs/EnumProcuratorsTypePersonal.md)
 - [EnumProductServiceType](docs/EnumProductServiceType.md)
 - [EnumSex](docs/EnumSex.md)
 - [GeographicCoordinates](docs/GeographicCoordinates.md)
 - [Links](docs/Links.md)
 - [Meta](docs/Meta.md)
 - [Nationality](docs/Nationality.md)
 - [NationalityOtherDocument](docs/NationalityOtherDocument.md)
 - [PartiesParticipation](docs/PartiesParticipation.md)
 - [PersonalAccount](docs/PersonalAccount.md)
 - [PersonalContacts](docs/PersonalContacts.md)
 - [PersonalDocument](docs/PersonalDocument.md)
 - [PersonalFinancialRelationData](docs/PersonalFinancialRelationData.md)
 - [PersonalIdentificationData](docs/PersonalIdentificationData.md)
 - [PersonalIdentificationDataFiliation](docs/PersonalIdentificationDataFiliation.md)
 - [PersonalInformedPatrimony](docs/PersonalInformedPatrimony.md)
 - [PersonalOtherDocument](docs/PersonalOtherDocument.md)
 - [PersonalPostalAddress](docs/PersonalPostalAddress.md)
 - [PersonalProcurator](docs/PersonalProcurator.md)
 - [PersonalQualificationData](docs/PersonalQualificationData.md)
 - [PersonalQualificationDataInformedIncome](docs/PersonalQualificationDataInformedIncome.md)
 - [ResponseBusinessCustomersFinancialRelation](docs/ResponseBusinessCustomersFinancialRelation.md)
 - [ResponseBusinessCustomersIdentification](docs/ResponseBusinessCustomersIdentification.md)
 - [ResponseBusinessCustomersQualification](docs/ResponseBusinessCustomersQualification.md)
 - [ResponseError](docs/ResponseError.md)
 - [ResponseErrorErrors](docs/ResponseErrorErrors.md)
 - [ResponsePersonalCustomersFinancialRelation](docs/ResponsePersonalCustomersFinancialRelation.md)
 - [ResponsePersonalCustomersIdentification](docs/ResponsePersonalCustomersIdentification.md)
 - [ResponsePersonalCustomersQualification](docs/ResponsePersonalCustomersQualification.md)

## Documentation For Authorization


## OAuth2Security

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://authserver.example/authorization
- **Scopes**: 
 - **customers**: Escopo necessário para acesso à API Customers. O controle dos endpoints específicos é feito via permissions.

## OpenId



## Author

gt-interfaces@openbankingbr.org