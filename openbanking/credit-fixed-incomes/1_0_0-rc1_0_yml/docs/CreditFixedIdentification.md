# CreditFixedIdentification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_institution_cnpj_number** | **str** | CNPJ da instituição emissora | 
**isin_code** | **str** | Código ISIN da emissão, Código ISIN do produto, Código da emissora (campo opcional): código universal que identifica cada valor mobiliário ou instrumento financeiro, conforme Norma ISO 6166.  | [optional] 
**investment_type** | [**EnumInvestimentType**](EnumInvestimentType.md) |  | 
**debtor_cnpj_number** | **str** | CNPJ do devedor (condicional para CRI e CRA)   [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;investmentType&#x27; for igual a \&quot;CRI\&quot; ou \&quot;CRA\&quot;.  | [optional] 
**debtor_name** | **str** | Nome do devedor (condicional para CRI e CRA)   [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo &#x27;investmentType&#x27; for igual a \&quot;CRI\&quot; ou \&quot;CRA\&quot;.  | [optional] 
**tax_exempt_product** | [**EnumTaxExemptProduct**](EnumTaxExemptProduct.md) |  | 
**remuneration** | [**Remuneration**](Remuneration.md) |  | 
**issue_unit_price** | [**IssueUnitPrice**](IssueUnitPrice.md) |  | 
**issue_date** | **date** | Data de emissão do título | 
**due_date** | **date** | Data de vencimento do título | 
**voucher_payment_indicator** | [**VoucherPaymentIndicator**](VoucherPaymentIndicator.md) |  | 
**voucher_payment_periodicity** | [**VoucherPaymentPeriodicity**](VoucherPaymentPeriodicity.md) |  | [optional] 
**voucher_payment_periodicity_additional_info** | **str** | Informações adicionais da periodicidade de pagamento de cupom   [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver &#x27;Outros&#x27; no campo &#x27;voucherPaymentPeriodicity&#x27;.  | [optional] 
**clearing_code** | **str** | Código de registro do ativo na clearing | [optional] 
**purchase_date** | **date** | Data de aquisição do cliente | 
**grace_period_date** | **date** | Data até a qual o cliente não poderá resgatar antecipadamente seu investimento | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

