# IdentifyProduct

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_institution_cnpj_number** | **str** | CNPJ da instituição emissora. | 
**isin_code** | **str** | Código ISIN da emissão, Código ISIN do produto, Código da emissora (campo opcional): código universal que identifica cada valor mobiliário ou instrumento financeiro, conforme Norma ISO 6166  | [optional] 
**investment_type** | [**EnumInvestmentType**](EnumInvestmentType.md) |  | 
**remuneration** | [**Remuneration**](Remuneration.md) |  | 
**issue_unit_price** | [**IdentifyProductIssueUnitPrice**](IdentifyProductIssueUnitPrice.md) |  | 
**due_date** | **date** | Data de vencimento do título. | 
**issue_date** | **date** | Data de emissão do título. | 
**clearing_code** | **str** | Código de registro do ativo na clearing. | [optional] 
**purchase_date** | **date** | Data de aquisição do cliente. | 
**grace_period_date** | **date** | Data até a qual o cliente não poderá resgatar antecipadamente seu investimento. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

