# common_2_0_0-beta_1_yml.DiscoveryApi

All URIs are relative to *http://api.banco.com.br/open-banking/discovery/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_outage**](DiscoveryApi.md#get_outage) | **GET** /outages | a descrição referente ao código de status retornado pelas APIs
[**get_status**](DiscoveryApi.md#get_status) | **GET** /status | a descrição referente ao código de status retornado pelas APIs

# **get_outage**
> ResponseDiscoveryOutageList get_outage(page=page, page_size=page_size)

a descrição referente ao código de status retornado pelas APIs

a descrição referente ao código de status retornado pelas APIs

### Example
```python
from __future__ import print_function
import time
import common_2_0_0-beta_1_yml
from common_2_0_0-beta_1_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = common_2_0_0-beta_1_yml.DiscoveryApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # a descrição referente ao código de status retornado pelas APIs
    api_response = api_instance.get_outage(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_outage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponseDiscoveryOutageList**](ResponseDiscoveryOutageList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> ResponseDiscoveryStatusList get_status(page=page, page_size=page_size)

a descrição referente ao código de status retornado pelas APIs

 descrição referente ao código de status retornado pelas APIs

### Example
```python
from __future__ import print_function
import time
import common_2_0_0-beta_1_yml
from common_2_0_0-beta_1_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = common_2_0_0-beta_1_yml.DiscoveryApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # a descrição referente ao código de status retornado pelas APIs
    api_response = api_instance.get_status(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponseDiscoveryStatusList**](ResponseDiscoveryStatusList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

