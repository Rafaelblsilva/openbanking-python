# ConsentsDebtorAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ispb** | **str** | Deve ser preenchido com o ISPB (Identificador do Sistema de Pagamentos Brasileiros) do participante do SPI (Sistema de pagamentos instantâneos) somente com números.  | 
**issuer** | **str** | Código da Agência emissora da conta sem dígito.  (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito,  no exercício de atividades da instituição, não podendo ser móvel ou transitória).  [Restrição] Preenchimento obrigatório para os seguintes tipos de conta: CACC (CONTA_DEPOSITO_A_VISTA) e SVGS (CONTA_POUPANCA).  | 
**number** | **str** | Deve ser preenchido com o número da conta transacional do usuário pagador, com dígito verificador (se este existir), se houver valor alfanumérico, este deve ser convertido para 0.  | 
**account_type** | [**EnumAccountTypeConsents**](EnumAccountTypeConsents.md) |  | 
**ibge_town_code** | **str** | Campo utilizado pela iniciadora para cálculo do dia útil de liquidação do pagamento (vide especificação do endToEndId) baseado no município de cadastro do usuário pagador no detentor.  [Restrições] - Campo obrigatório que deverá ser retornado quando o consentimento estiver ou passar pelo status AUTHORISED; - Campo obrigatório quando o oneOf utilizado do recurringConfiguration for “automatic”.   | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

