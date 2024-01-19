# ResponseFundsProductListData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_name** | **str** | Nome da Marca reportada pelo participante no Open Finance. Recomenda-se utilizar, sempre que possível, o mesmo nome de marca atribuído no campo do diretório Customer Friendly Server Name (Authorisation Server). | 
**company_cnpj** | **str** | Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara. | 
**anbima_category** | **str** | Conforme classificação ANBIMA, que segue a deliberação 77 da ANBIMA.  – Renda Fixa  – Ações  – Multimercado  – Cambial  https://www.anbima.com.br/data/files/5A/44/2C/B7/8411B510CD3B4DA568A80AC2/DeliberacaoN77-Diretriz-de-Classificacao-de-Fundos.pdf  | [optional] 
**anbima_class** | **str** | Campo necessário para aderência a Resolução CVM175. Aguardando definições de mercado. Deve se tratar de campo do tipo enum. | [optional] 
**anbima_subclass** | **str** | Campo necessário para aderência a Resolução CVM175. Aguardando definições de mercado. Deve se tratar de campo do tipo enum. | [optional] 
**investment_id** | **str** | Identifica de forma única  o relacionamento do cliente com o fundo, mantendo as regras de imutabilidade dentro da instituição transmissora. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

