# InvoiceFinancingsContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_number** | **str** | Número do contrato dado pela instituição contratante. | 
**ipoc_code** | **str** | Número padronizado do contrato - IPOC (Identificação Padronizada da Operação de Crédito). Segundo DOC 3040, composta por: - **CNPJ da instituição:** 8 (oito) posições iniciais; - **Modalidade da operação:** 4 (quatro) posições; - **Tipo do cliente:** 1 (uma) posição( 1 &#x3D; pessoa natural - CPF, 2&#x3D; pessoa jurídica – CNPJ, 3 &#x3D; pessoa física no exterior, 4 &#x3D; pessoa jurídica no exterior, 5 &#x3D; pessoa natural sem CPF e 6 &#x3D; pessoa jurídica sem CNPJ); - **Código do cliente:** O número de posições varia conforme o tipo do cliente:   1. Para clientes pessoa física com CPF (tipo de cliente &#x3D; 1), informar as 11 (onze) posições do CPF;   2. Para clientes pessoa jurídica com CNPJ (tipo de cliente &#x3D; 2), informar as 8 (oito) posições iniciais do CNPJ;   3. Para os demais clientes (tipos de cliente 3, 4, 5 e 6), informar 14 (catorze) posições com complemento de zeros à esquerda se a identificação tiver tamanho inferior; - **Código do contrato:** 1 (uma) até 40 (quarenta) posições, sem complemento de caracteres.  | 
**product_name** | **str** | Denominação/Identificação do nome da Modalidade da Operação de Crédito divulgado ao cliente  | 
**product_type** | [**EnumContractProductTypeInvoiceFinancings**](EnumContractProductTypeInvoiceFinancings.md) |  | 
**product_sub_type** | [**EnumContractProductSubTypeInvoiceFinancings**](EnumContractProductSubTypeInvoiceFinancings.md) |  | 
**contract_date** | **date** | Data de contratação da operação de crédito. Especificação RFC-3339 | 
**disbursement_dates** | **list[date]** | Lista que traz as Datas de Desembolso do valor contratado.  | [optional] 
**settlement_date** | **date** | Data de liquidação da operação.  | [optional] 
**contract_amount** | **str** | Valor contratado da operação. Expresso em valor monetário com no mínimo 2 casas e no máximo 4 casas decimais. | [optional] 
**currency** | **str** | Moeda referente ao valor da garantia, segundo modelo ISO-4217. p.ex. &#x27;BRL&#x27; Todos os valores monetários informados estão representados com a moeda vigente do Brasil  | [optional] 
**due_date** | **date** | Data de vencimento Final da operação. Especificação RFC-3339 | [optional] 
**instalment_periodicity** | [**EnumContractInstalmentPeriodicity**](EnumContractInstalmentPeriodicity.md) |  | 
**instalment_periodicity_additional_info** | **str** | Campo obrigatório para complementar a informação relativa à periodicidade de pagamento regular quando tiver a opção OUTROS.   | [optional] 
**first_instalment_due_date** | **date** | Data de vencimento primeira parcela do principal.  | [optional] 
**cet** | **str** | CET – Custo Efetivo Total deve ser expresso na forma de taxa percentual anual e incorpora todos os encargos e despesas incidentes nas operações de crédito (taxa de juro, mas também tarifas, tributos, seguros e outras despesas cobradas).  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros  (representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%).  | [optional] 
**amortization_scheduled** | [**EnumContractAmortizationScheduled**](EnumContractAmortizationScheduled.md) |  | 
**amortization_scheduled_additional_info** | **str** | Campo obrigatório para complementar a informação relativa à amortização quando selecionada a opção OUTROS.  | [optional] 
**interest_rates** | [**list[InvoiceFinancingsContractInterestRate]**](InvoiceFinancingsContractInterestRate.md) | Objeto que traz o conjunto de informações necessárias para demonstrar a composição das taxas de juros remuneratórios da Modalidade de crédito.   Caso o contrato não possua taxas de juros, deve ser compartilhada uma lista vazia. Caso o contrato possua uma taxa de juros com valor 0, deve ser compartilhado um objeto com o valor 0 de forma explícita.  | 
**contracted_fees** | [**list[InvoiceFinancingsContractedFee]**](InvoiceFinancingsContractedFee.md) | Lista que traz as informações das tarifas pactuadas no contrato. | 
**contracted_finance_charges** | [**list[InvoiceFinancingsFinanceCharge]**](InvoiceFinancingsFinanceCharge.md) | Lista que traz os encargos pactuados no contrato | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

