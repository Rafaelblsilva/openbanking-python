# insurances-1-0-0-yml
As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
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
import insurances_1_0_0_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import insurances_1_0_0_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import insurances_1_0_0_yml
from insurances_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = insurances_1_0_0_yml.SegurosApi(insurances_1_0_0_yml.ApiClient(configuration))
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Conjunto de informações referentes a seguros pessoais de uma instituição
    api_response = api_instance.get_personal_insurance(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegurosApi->get_personal_insurance: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.banco.com.br/open-banking/opendata-insurance/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SegurosApi* | [**get_personal_insurance**](docs/SegurosApi.md#get_personal_insurance) | **GET** /personals | Conjunto de informações referentes a seguros pessoais de uma instituição

## Documentation For Models

 - [AgeAdjustment](docs/AgeAdjustment.md)
 - [BenefitRecalculation](docs/BenefitRecalculation.md)
 - [CnpjNumber](docs/CnpjNumber.md)
 - [CurrencyCode](docs/CurrencyCode.md)
 - [EnumContractTypePersonal](docs/EnumContractTypePersonal.md)
 - [EnumExcludedRisks](docs/EnumExcludedRisks.md)
 - [EnumGracePeriodUnit](docs/EnumGracePeriodUnit.md)
 - [EnumInsurancePersonalBenefitRecalculationUpdateIndex](docs/EnumInsurancePersonalBenefitRecalculationUpdateIndex.md)
 - [EnumInsurancePersonalCoverageTypePersonal](docs/EnumInsurancePersonalCoverageTypePersonal.md)
 - [EnumPersonalIndemnityPaymentFrequencyType](docs/EnumPersonalIndemnityPaymentFrequencyType.md)
 - [EnumPersonalInsuranceIndemnityPaymentIncome](docs/EnumPersonalInsuranceIndemnityPaymentIncome.md)
 - [EnumPersonalInsuranceIndemnityPaymentMethod](docs/EnumPersonalInsuranceIndemnityPaymentMethod.md)
 - [EnumPersonalInsuranceOtherGuaranteedValues](docs/EnumPersonalInsuranceOtherGuaranteedValues.md)
 - [EnumPersonalInsurancePremiumPaymentFrequency](docs/EnumPersonalInsurancePremiumPaymentFrequency.md)
 - [EnumPersonalUpdateIndex](docs/EnumPersonalUpdateIndex.md)
 - [EnumPremiumPaymentMethodTypePersonal](docs/EnumPremiumPaymentMethodTypePersonal.md)
 - [EnumProductModality](docs/EnumProductModality.md)
 - [GracePeriod](docs/GracePeriod.md)
 - [InlineResponse529](docs/InlineResponse529.md)
 - [InlineResponse529Errors](docs/InlineResponse529Errors.md)
 - [InlineResponse529Meta](docs/InlineResponse529Meta.md)
 - [InsurancePensionEnumFinancialRegime](docs/InsurancePensionEnumFinancialRegime.md)
 - [InsurancePensionEnumPmbacRemuneration](docs/InsurancePensionEnumPmbacRemuneration.md)
 - [InsurancePensionMaxValue](docs/InsurancePensionMaxValue.md)
 - [InsurancePensionMinValue](docs/InsurancePensionMinValue.md)
 - [Links](docs/Links.md)
 - [Meta](docs/Meta.md)
 - [OKResponsePersonalInsuranceList](docs/OKResponsePersonalInsuranceList.md)
 - [OpenDataMeta](docs/OpenDataMeta.md)
 - [Participant](docs/Participant.md)
 - [PersonalCoverageItem](docs/PersonalCoverageItem.md)
 - [PersonalCoverageItemAttributes](docs/PersonalCoverageItemAttributes.md)
 - [PersonalCoverageItemAttributesDeductible](docs/PersonalCoverageItemAttributesDeductible.md)
 - [PersonalCoverageItemAttributesDifferentiatedDeductible](docs/PersonalCoverageItemAttributesDifferentiatedDeductible.md)
 - [PersonalInsuranceData](docs/PersonalInsuranceData.md)
 - [PersonalInsuranceGracePeriod](docs/PersonalInsuranceGracePeriod.md)
 - [PersonalInsuranceMinimumRequirement](docs/PersonalInsuranceMinimumRequirement.md)
 - [PersonalInsurancePortabilityGraceTime](docs/PersonalInsurancePortabilityGraceTime.md)
 - [PersonalInsurancePremiumPayment](docs/PersonalInsurancePremiumPayment.md)
 - [PersonalInsuranceReclaim](docs/PersonalInsuranceReclaim.md)
 - [PersonalInsuranceReclaimTableItem](docs/PersonalInsuranceReclaimTableItem.md)
 - [PersonalInsuranceSociety](docs/PersonalInsuranceSociety.md)
 - [ResponseError](docs/ResponseError.md)
 - [ResponseErrorErrors](docs/ResponseErrorErrors.md)
 - [TermsAndConditionsItem](docs/TermsAndConditionsItem.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

gt-interfaces@openbankingbr.org
