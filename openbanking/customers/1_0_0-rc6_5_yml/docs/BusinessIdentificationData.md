# BusinessIdentificationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_date_time** | **datetime** | Data e hora da atualização do bloco, conforme especificação RFC-3339 | 
**business_id** | **str** | Um identificador único e imutável usado para identificar o recurso cliente pessoa jurídica. Este identificador não tem significado para o cliente que deu o consentimento | 
**brand_name** | **str** | Nome da Marca reportada pelo participante do Open Banking. O conceito a que se refere a &#x27;marca&#x27; é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes  | 
**company_name** | **str** | Razão social da empresa consultada é o termo registrado sob o qual uma pessoa jurídica (PJ) se individualiza e exerce suas atividades. Também pode ser chamada por denominação social ou firma empresarial | 
**trade_name** | **str** | Nome fantasia da pessoa jurídica, se houver. (É o nome popular da empresa, utilizado para divulgação da empresa e melhor fixação com o público). De preenchimento obrigatório se houver | 
**incorporation_date** | **datetime** | Data de constituição da empresa, conforme especificação RFC-3339. | 
**cnpj_number** | **str** | Número completo do CNPJ da Empresa consultada  - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara | 
**company_cnpj_number** | **list[str]** | Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica.  Deve-se ter apenas os números do CNPJ, sem máscara  | 
**other_documents** | [**list[BusinessOtherDocument]**](BusinessOtherDocument.md) | Relação dos demais documentos | [optional] 
**parties** | [**list[PartiesParticipation]**](PartiesParticipation.md) | Lista relativa às informações das partes envolvidas, como: sócio e /ou administrador  | 
**contacts** | [**BusinessContacts**](BusinessContacts.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

