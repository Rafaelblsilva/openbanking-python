# UnarrangedAccountOverdraftContractData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_number** | **str** | Número do contrato dado pela instituição contratante. | 
**ipoc_code** | **str** | \&quot;Número padronizado do contrato - IPOC (Identificação Padronizada da Operação de Crédito). Segundo DOC 3040, composta por: - **CNPJ da instituição:** 8 (oito) posições iniciais; - **Modalidade da operação:** 4 (quatro) posições; - **Tipo do cliente:** 1 (uma) posição( 1 &#x3D; pessoa natural - CPF, 2&#x3D; pessoa jurídica – CNPJ, 3 &#x3D; pessoa física no exterior, 4 &#x3D; pessoa jurídica no exterior, 5 &#x3D; pessoa natural sem CPF e 6 &#x3D; pessoa jurídica sem CNPJ); - **Código do cliente:** O número de posições varia conforme o tipo do cliente:   1. Para clientes pessoa física com CPF (tipo de cliente &#x3D; 1), informar as 11 (onze) posições do CPF;   2. Para clientes pessoa jurídica com CNPJ (tipo de cliente &#x3D; 2), informar as 8 (oito) posições iniciais do CNPJ;   3. Para os demais clientes (tipos de cliente 3, 4, 5 e 6), informar 14 (catorze) posições com complemento de zeros à esquerda se a identificação tiver tamanho inferior; - **Código do contrato:** 1 (uma) até 40 (quarenta) posições, sem complemento de caracteres.\&quot;  | 
**product_name** | **str** | \&quot;Denominação/Identificação do nome da Modalidade da Operação de Crédito divulgado ao cliente\&quot;  | 
**product_type** | [**ProductType**](ProductType.md) |  | 
**product_sub_type** | [**ProductSubType**](ProductSubType.md) |  | 
**contract_date** | **date** | Data de contratação da operação de crédito. Especificação RFC-3339 | 
**disbursement_date** | **date** | Data do Desembolso do valor contratado. Especificação RFC-3339 | [optional] 
**settlement_date** | **date** | Data de liquidação da operação. [Restrição] Deve aceitar NA caso não seja retornado pela instituição.  | 
**contract_amount** | **float** | Valor contratado da operação. Expresso em valor monetário com até 4 casas decimais | 
**currency** | **str** | \&quot;Moeda referente ao valor da garantia, segundo modelo ISO-4217. p.ex. &#x27;BRL&#x27; Todos os valores monetários informados estão representados com a moeda vigente do Brasil\&quot;  | 
**due_date** | **date** | Data de vencimento Final da operação. Especificação RFC-3339 | 
**instalment_periodicity** | [**EnumContractInstalmentPeriodicity**](EnumContractInstalmentPeriodicity.md) |  | 
**instalment_periodicity_additional_info** | **str** | Campo obrigatório para complementar a informação relativa à periodicidade de pagamento regular quando tiver a opção OUTROS. [Restrição] Obrigatório para complementar a informação relativa da periodicidade de pagamento regular, quando selecionada o tipo ou subtipo OUTRO.   | 
**first_instalment_due_date** | **date** | Data de vencimento primeira parcela do principal | 
**cet** | **float** | \&quot;CET – Custo Efetivo Total deve ser expresso na forma de taxa percentual anual e   incorpora todos os encargos e despesas incidentes nas operações de crédito (taxa de juro, mas também tarifas, tributos, seguros e outras despesas cobradas). O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)\&quot;  | 
**amortization_scheduled** | **str** | Sistema de amortização (Vide Enum): - SAC (Sistema de Amortização Constante) - É aquele em que o valor da amortização permanece igual até o final. Os juros cobrados sobre o parcelamento não entram nesta conta. - PRICE (Sistema Francês de Amortização) - As parcelas são fixas do início ao fim do contrato. Ou seja, todas as parcelas terão o mesmo valor, desde a primeira até a última. Nos primeiros pagamentos, a maior parte do valor da prestação corresponde aos juros. Ao longo do tempo, a taxa de juros vai decrescendo. Como o valor da prestação é fixo, com o passar das parcelas, o valor de amortização vai aumentando. - SAM (Sistema de Amortização Misto) - Cada prestação (pagamento) é a média aritmética das prestações respectivas no Sistemas Price e no Sistema de Amortização Constante (SAC). - SEM SISTEMA DE AMORTIZAÇÃO  | 
**amortization_scheduled_additional_info** | **str** | Campo obrigatório para complementar a informação relativa à amortização quando selecionada a opção OUTROS. [Restrição] Obrigatório para complementar a informação relativa à amortização quando selecionada a opção OUTROS, para os demais casos informar \&quot;NA\&quot;.       | 
**interest_rates** | [**list[UnarrangedAccountOverdraftContractInterestRate]**](UnarrangedAccountOverdraftContractInterestRate.md) |  | 
**contracted_fees** | [**list[UnarrangedAccountOverdraftContractedFee]**](UnarrangedAccountOverdraftContractedFee.md) | Lista que traz a relação de tarifas pactuadas no contrato | 
**contracted_finance_charges** | [**list[UnarrangedAccountOverdraftFinanceCharge]**](UnarrangedAccountOverdraftFinanceCharge.md) | Lista que traz os encargos pactuados no contrato | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

