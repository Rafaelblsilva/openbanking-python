# CreditCardAccountsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_card_account_id** | **str** | Identifica de forma única a conta pagamento pós-paga do cliente, mantendo as regras de imutabilidade dentro da instituição transmissora. | 
**brand_name** | **str** | Nome da Marca reportada pelo participante do Open Banking. O conceito a que se refere a &#x27;marca&#x27; é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes | 
**company_cnpj** | **str** | Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara | 
**name** | **str** | Denominação/Identificação do nome da conta de pagamento pós-paga (cartão). Conforme CIRCULAR Nº 3.680,BCB, 2013: &#x27;conta de pagamento pós-paga: destinada à execução de transações de pagamento que independem do aporte prévio de recursos | 
**product_type** | [**EnumCreditCardAccountsProductType**](EnumCreditCardAccountsProductType.md) |  | 
**product_additional_info** | **str** | Informações complementares se tipo de Cartão &#x27;OUTROS&#x27; | [optional] 
**credit_card_network** | [**EnumCreditCardAccountNetwork**](EnumCreditCardAccountNetwork.md) |  | 
**network_additional_info** | **str** | Texto livre para especificar categoria de bandeira marcada como &#x27;OUTRAS&#x27; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

