# channels_1_0_0_yml.ElectronicChannelsApi

All URIs are relative to *http://api.banco.com.br/open-banking/channels/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_banking_agents**](ElectronicChannelsApi.md#get_banking_agents) | **GET** /banking-agents | Obtém a lista de correspondentes bancários da instituição financeira.
[**get_branches**](ElectronicChannelsApi.md#get_branches) | **GET** /branches | Obtém a lista de dependências próprias da instituição financeira.
[**get_electronic_channels**](ElectronicChannelsApi.md#get_electronic_channels) | **GET** /electronic-channels | Obtém a lista de canais eletrônicos de atendimento da instituição financeira.
[**get_phone_channels**](ElectronicChannelsApi.md#get_phone_channels) | **GET** /phone-channels | Obtém a lista de canais telefônicos de atendimento da instituição financeira.

# **get_banking_agents**
> ResponseBankingAgentsList get_banking_agents()

Obtém a lista de correspondentes bancários da instituição financeira.

Método para obter a lista de correspondentes bancários da instituição financeira.

### Example
```python
from __future__ import print_function
import time
import channels_1_0_0_yml
from channels_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = channels_1_0_0_yml.ElectronicChannelsApi()

try:
    # Obtém a lista de correspondentes bancários da instituição financeira.
    api_response = api_instance.get_banking_agents()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectronicChannelsApi->get_banking_agents: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseBankingAgentsList**](ResponseBankingAgentsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branches**
> ResponseBranchesList get_branches()

Obtém a lista de dependências próprias da instituição financeira.

Método para obter a lista de dependências próprias da instituição financeira.

### Example
```python
from __future__ import print_function
import time
import channels_1_0_0_yml
from channels_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = channels_1_0_0_yml.ElectronicChannelsApi()

try:
    # Obtém a lista de dependências próprias da instituição financeira.
    api_response = api_instance.get_branches()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectronicChannelsApi->get_branches: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseBranchesList**](ResponseBranchesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_electronic_channels**
> ResponseElectronicChannelsList get_electronic_channels()

Obtém a lista de canais eletrônicos de atendimento da instituição financeira.

Método para obter a lista de canais eletrônicos de atendimento da instituição financeira.

### Example
```python
from __future__ import print_function
import time
import channels_1_0_0_yml
from channels_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = channels_1_0_0_yml.ElectronicChannelsApi()

try:
    # Obtém a lista de canais eletrônicos de atendimento da instituição financeira.
    api_response = api_instance.get_electronic_channels()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectronicChannelsApi->get_electronic_channels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseElectronicChannelsList**](ResponseElectronicChannelsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_channels**
> ResponsePhoneChannelsList get_phone_channels()

Obtém a lista de canais telefônicos de atendimento da instituição financeira.

Método para obter a lista de canais telefônicos de atendimento da instituição financeira.

### Example
```python
from __future__ import print_function
import time
import channels_1_0_0_yml
from channels_1_0_0_yml.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = channels_1_0_0_yml.ElectronicChannelsApi()

try:
    # Obtém a lista de canais telefônicos de atendimento da instituição financeira.
    api_response = api_instance.get_phone_channels()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElectronicChannelsApi->get_phone_channels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsePhoneChannelsList**](ResponsePhoneChannelsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

