# ClientCreationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_type** | **str** | OIDC application type response | [optional] [default to 'web']
**tls_client_auth_subject_dn** | **str** | the subject dn used to authenticate this client | [optional] 
**grant_types** | **list[str]** | grant_types | [optional] 
**id_token_signed_response_alg** | **str** |  | [optional] 
**require_auth_time** | **bool** |  | [optional] 
**subject_type** | **str** |  | [optional] 
**response_types** | **list[str]** | response_types | [optional] 
**post_logout_redirect_uris** | **list[str]** | post_logout_redirect_uris | [optional] 
**token_endpoint_auth_method** | **str** |  | [optional] 
**introspection_endpoint_auth_method** | **str** |  | [optional] 
**revocation_endpoint_auth_method** | **str** |  | [optional] 
**client_id_issued_at** | **float** |  | [optional] 
**client_id** | **str** |  | [optional] 
**jwks_uri** | **str** |  | [optional] 
**registration_client_uri** | **str** | management uri location to manage client post creation | [optional] 
**registration_access_token** | **str** | token used to manage client post creation | [optional] 
**redirect_uris** | **list[str]** | redirect_uris | [optional] 
**request_uris** | **list[str]** | request_uris | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

