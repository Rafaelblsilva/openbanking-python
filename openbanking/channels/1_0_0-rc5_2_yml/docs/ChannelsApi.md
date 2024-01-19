# channels_1_0_0-rc5_2_yml.ChannelsApi

All URIs are relative to *http://api.banco.com.br/open-banking/channels/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_banking_agents**](ChannelsApi.md#get_banking_agents) | **GET** /banking-agents | Obtém a lista de correspondentes bancários da instituição financeira.
[**get_branches**](ChannelsApi.md#get_branches) | **GET** /branches | Obtém a lista de dependências próprias da instituição financeira.
[**get_electronic_channels**](ChannelsApi.md#get_electronic_channels) | **GET** /electronic-channels | Obtém a lista de canais eletrônicos de atendimento da instituição financeira.
[**get_phone_channels**](ChannelsApi.md#get_phone_channels) | **GET** /phone-channels | Obtém a lista de canais telefônicos de atendimento da instituição financeira.
[**get_shared_automated_teller_machines**](ChannelsApi.md#get_shared_automated_teller_machines) | **GET** /shared-automated-teller-machines | Obtém a lista de terminais compartilhados de autoatendimento.

# **get_banking_agents**
> ResponseBankingAgentsList get_banking_agents(page=page, page_size=page_size)

Obtém a lista de correspondentes bancários da instituição financeira.

Método para obter a lista de correspondentes bancários da instituição financeira.

### Example
```python
from __future__ import print_function
import time
import channels_1_0_0-rc5_2_yml
from channels_1_0_0-rc5_2_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = channels_1_0_0-rc5_2_yml.ChannelsApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém a lista de correspondentes bancários da instituição financeira.
    api_response = api_instance.get_banking_agents(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_banking_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponseBankingAgentsList**](ResponseBankingAgentsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branches**
> ResponseBranchesList get_branches(page=page, page_size=page_size)

Obtém a lista de dependências próprias da instituição financeira.

Método para obter a lista de dependências próprias da instituição financeira.

### Example
```python
from __future__ import print_function
import time
import channels_1_0_0-rc5_2_yml
from channels_1_0_0-rc5_2_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = channels_1_0_0-rc5_2_yml.ChannelsApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém a lista de dependências próprias da instituição financeira.
    api_response = api_instance.get_branches(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponseBranchesList**](ResponseBranchesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_electronic_channels**
> ResponseElectronicChannelsList get_electronic_channels(page=page, page_size=page_size)

Obtém a lista de canais eletrônicos de atendimento da instituição financeira.

Método para obter a lista de canais eletrônicos de atendimento da instituição financeira.

### Example
```python
from __future__ import print_function
import time
import channels_1_0_0-rc5_2_yml
from channels_1_0_0-rc5_2_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = channels_1_0_0-rc5_2_yml.ChannelsApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém a lista de canais eletrônicos de atendimento da instituição financeira.
    api_response = api_instance.get_electronic_channels(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_electronic_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponseElectronicChannelsList**](ResponseElectronicChannelsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_channels**
> ResponsePhoneChannelsList get_phone_channels(page=page, page_size=page_size)

Obtém a lista de canais telefônicos de atendimento da instituição financeira.

Método para obter a lista de canais telefônicos de atendimento da instituição financeira.

### Example
```python
from __future__ import print_function
import time
import channels_1_0_0-rc5_2_yml
from channels_1_0_0-rc5_2_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = channels_1_0_0-rc5_2_yml.ChannelsApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém a lista de canais telefônicos de atendimento da instituição financeira.
    api_response = api_instance.get_phone_channels(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_phone_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponsePhoneChannelsList**](ResponsePhoneChannelsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_automated_teller_machines**
> ResponseSharedAutomatedTellerMachinesList get_shared_automated_teller_machines(page=page, page_size=page_size)

Obtém a lista de terminais compartilhados de autoatendimento.

Método para obter a lista de terminais compartilhados de autoatendimento da instituição financeira.

### Example
```python
from __future__ import print_function
import time
import channels_1_0_0-rc5_2_yml
from channels_1_0_0-rc5_2_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = channels_1_0_0-rc5_2_yml.ChannelsApi()
page = 1 # int | Número da página que está sendo requisitada (o valor da primeira página é 1). (optional) (default to 1)
page_size = 25 # int | Quantidade total de registros por páginas. (optional) (default to 25)

try:
    # Obtém a lista de terminais compartilhados de autoatendimento.
    api_response = api_instance.get_shared_automated_teller_machines(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_shared_automated_teller_machines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Número da página que está sendo requisitada (o valor da primeira página é 1). | [optional] [default to 1]
 **page_size** | **int**| Quantidade total de registros por páginas. | [optional] [default to 25]

### Return type

[**ResponseSharedAutomatedTellerMachinesList**](ResponseSharedAutomatedTellerMachinesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

