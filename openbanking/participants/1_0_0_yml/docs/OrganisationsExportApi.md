# participants_1_0_0_yml.OrganisationsExportApi

All URIs are relative to *https://data.directory.openbankingbrasil.org.br*

Method | HTTP request | Description
------------- | ------------- | -------------
[**participants_get**](OrganisationsExportApi.md#participants_get) | **GET** /participants | Recupera informações técnicas sobre Participantes registrados no diretório, essas informações permitem identificar e consumir as APIs dos participantes

# **participants_get**
> OrganisationsExportOpenData participants_get()

Recupera informações técnicas sobre Participantes registrados no diretório, essas informações permitem identificar e consumir as APIs dos participantes

### Example
```python
from __future__ import print_function
import time
import participants_1_0_0_yml
from participants_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = participants_1_0_0_yml.OrganisationsExportApi()

try:
    # Recupera informações técnicas sobre Participantes registrados no diretório, essas informações permitem identificar e consumir as APIs dos participantes
    api_response = api_instance.participants_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationsExportApi->participants_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganisationsExportOpenData**](OrganisationsExportOpenData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

