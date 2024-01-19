# EnrollmentFidoRegistrationOptionsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_id** | [**EnrollmentId**](EnrollmentId.md) |  | 
**rp** | [**FidoRelyingParty**](FidoRelyingParty.md) |  | 
**user** | [**FidoUser**](FidoUser.md) |  | 
**challenge** | **str** | Sequência de bytes aleatórios gerados pelo servidor FIDO2, codificados em base64. | 
**pub_key_cred_params** | [**list[FidoPublicKeyCredentialCreationOptions]**](FidoPublicKeyCredentialCreationOptions.md) |  | 
**timeout** | **int** | Timeout, em milissegundos, para registro da credencial FIDO2. | [optional] 
**exclude_credentials** | [**list[FidoPublicKeyCredentialDescriptor]**](FidoPublicKeyCredentialDescriptor.md) |  | [optional] 
**authenticator_selection** | [**FidoAuthenticatorSelectionCriteria**](FidoAuthenticatorSelectionCriteria.md) |  | [optional] 
**attestation** | **str** | Indica o tipo de attestation que o autenticador pode utilizar. | [optional] 
**attestation_formats** | **list[str]** | Indica as preferências de formato sobre o campo attestation. | [optional] 
**extensions** | **dict(str, str)** | Campo de extensão com opções que variam por plataforma. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

