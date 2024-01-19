# ConsentRevocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Estado atual do consentimento de longa duração  | [optional] 
**revocation** | [**ConsentRevocationRevocation**](ConsentRevocationRevocation.md) |  | [optional] 
**risk_signals** | [**RiskSignalsConsents**](RiskSignalsConsents.md) |  | [optional] 
**creditors** | [**list[ConsentRejectionCreditors]**](ConsentRejectionCreditors.md) |  | [optional] 
**start_date_time** | **datetime** | Data e hora em que o consentimento deve passar a ser válido. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format). | [optional] 
**expiration_date_time** | **datetime** | Data e hora em que o consentimento deve deixar de ser válido. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format). | [optional] 
**automatic** | [**ConsentRejectionAutomatic**](ConsentRejectionAutomatic.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

