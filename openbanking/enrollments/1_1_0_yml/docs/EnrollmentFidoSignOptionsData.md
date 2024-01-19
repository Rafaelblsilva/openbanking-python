# EnrollmentFidoSignOptionsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge** | **str** | Sequência de bytes aleatórios gerados pelo servidor FIDO2, codificados em base64. | 
**timeout** | **int** | Expiração, em milissegundos, do challenge. | [optional] 
**rp_id** | **str** | Identificador da Relying Party. | [optional] 
**allow_credentials** | [**list[FidoPublicKeyCredentialDescriptor]**](FidoPublicKeyCredentialDescriptor.md) |  | [optional] 
**user_verification** | **str** |  | [optional] 
**extensions** | **dict(str, str)** | Campo de extensão com opções que variam por plataforma. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

