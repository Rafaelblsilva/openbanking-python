# common-1-0-1-yml
As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

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
import common_1_0_1_yml 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import common_1_0_1_yml
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import common_1_0_1_yml
from common_1_0_1_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = common_1_0_1_yml.DiscoveryApi(common_1_0_1_yml.ApiClient(configuration))
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # a descrição referente ao código de status retornado pelas APIs
    api_response = api_instance.get_outage(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_outage: %s\n" % e)

# create an instance of the API class
api_instance = common_1_0_1_yml.DiscoveryApi(common_1_0_1_yml.ApiClient(configuration))
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # a descrição referente ao código de status retornado pelas APIs
    api_response = api_instance.get_status(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_status: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://api.banco.com.br/open-banking/discovery/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DiscoveryApi* | [**get_outage**](docs/DiscoveryApi.md#get_outage) | **GET** /outages | a descrição referente ao código de status retornado pelas APIs
*DiscoveryApi* | [**get_status**](docs/DiscoveryApi.md#get_status) | **GET** /status | a descrição referente ao código de status retornado pelas APIs

## Documentation For Models

 - [Links](docs/Links.md)
 - [Meta](docs/Meta.md)
 - [ResponseDiscoveryOutageList](docs/ResponseDiscoveryOutageList.md)
 - [ResponseDiscoveryOutageListData](docs/ResponseDiscoveryOutageListData.md)
 - [ResponseDiscoveryStatusList](docs/ResponseDiscoveryStatusList.md)
 - [ResponseDiscoveryStatusListData](docs/ResponseDiscoveryStatusListData.md)
 - [Status](docs/Status.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

apiteam@swagger.io
