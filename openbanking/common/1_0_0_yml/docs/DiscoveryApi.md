# common_1_0_0_yml.DiscoveryApi

All URIs are relative to *http://api.banco.com.br/open-banking/discovery/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_outstage**](DiscoveryApi.md#get_outstage) | **GET** /outstage | a descrição referente ao código de status retornado pelas APIs
[**get_status**](DiscoveryApi.md#get_status) | **GET** /status | a descrição referente ao código de status retornado pelas APIs

# **get_outstage**
> ResponseDiscoveryOutstageList get_outstage()

a descrição referente ao código de status retornado pelas APIs

a descrição referente ao código de status retornado pelas APIs

### Example
```python
from __future__ import print_function
import time
import common_1_0_0_yml
from common_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = common_1_0_0_yml.DiscoveryApi()

try:
    # a descrição referente ao código de status retornado pelas APIs
    api_response = api_instance.get_outstage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_outstage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseDiscoveryOutstageList**](ResponseDiscoveryOutstageList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> ResponseDiscoveryStatusList get_status()

a descrição referente ao código de status retornado pelas APIs

 descrição referente ao código de status retornado pelas APIs

### Example
```python
from __future__ import print_function
import time
import common_1_0_0_yml
from common_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = common_1_0_0_yml.DiscoveryApi()

try:
    # a descrição referente ao código de status retornado pelas APIs
    api_response = api_instance.get_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseDiscoveryStatusList**](ResponseDiscoveryStatusList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

