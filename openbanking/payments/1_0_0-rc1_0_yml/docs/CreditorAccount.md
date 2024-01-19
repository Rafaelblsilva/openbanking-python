# CreditorAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ispb** | **str** | Deve ser preenchido com o ISPB (Identificador do Sistema de Pagamentos Brasileiros) do participante do SPI (Sistema de pagamentos instantâneos) somente com números.  | 
**branch_code** | **str** | Código da Agência detentora da conta sem dígito.   (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito,   no exercício de atividades da instituição, não podendo ser móvel ou transitória).   [Restrição] Preenchimento obrigatório para os seguintes tipos de conta: CACC (CONTA_DEPOSITO_A_VISTA), SVGS (CONTA_POUPANCA) e SLRY (CONTA_SALARIO).  | [optional] 
**number** | **str** | Número da conta sem o dígito. | 
**check_digit** | **str** | Dígito da conta. | 
**account_type** | [**EnumAccountPaymentsType**](EnumAccountPaymentsType.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

