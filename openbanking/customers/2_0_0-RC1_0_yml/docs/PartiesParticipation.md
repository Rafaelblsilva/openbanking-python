# PartiesParticipation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_type** | **str** | Indica se a pessoa da parte envolvida é uma pessoa natural ou juridica | 
**type** | **str** | Indica o perfil de atuação na empresa. Vide Enum O administrador é o responsável por desempenhar todas as funções administrativas da empresa. É ele quem conduz o dia a dia do negócio, assinando documentos, respondendo legalmente pela sociedade, realizando empréstimos e outras ações gerenciais. Apesar de estar na linha de frente da empresa, ele é denominado sócio por também possuir sua parcela de participação no Capital Social. Sócio não tem qualquer envolvimento nas atividades administrativas da sociedade.  | 
**civil_name** | **str** | Nome civil completo da pessoa natural (Direito fundamental da pessoa, o nome civil é aquele atribuído à pessoa natural desde o registro de seu nascimento, com o qual será identificada por toda a sua vida, bem como após a sua morte)  [Restrição] O campo civilName deve ser obrigatoriamente preenchido quando personType for PESSOA_NATURAL.  | [optional] 
**social_name** | **str** | Nome social da pessoa natural, se houver. (aquele pelo qual travestis e transexuais se reconhecem, bem como são identificados por sua comunidade e em seu meio social, conforme Decreto Local).     | [optional] 
**company_name** | **str** | Razão social da empresa consultada é o termo registrado sob o qual uma pessoa jurídica (PJ) se individualiza e exerce suas atividades. Também pode ser chamada por denominação social ou firma empresarial  [Restrição] o campo companyName deve ser obrigatoriamente preenchido quando personType for PESSOA_JURIDICA.  | [optional] 
**trade_name** | **str** | Nome fantasia da pessoa jurídica, se houver. (É o nome popular da empresa, utilizado para divulgação da empresa e melhor fixação com o público). De preenchimento obrigatório se houver | [optional] 
**start_date** | **datetime** | Data de início da participação, conforme especificação RFC-3339. | [optional] 
**shareholding** | **str** | Percentual de participação societária (informar com 6 casas decimais). O Sócio só deve ser informado se sua participação societária for igual ou superior a 25%. p.ex: 0.250000 (Este valor  representa 25%. O valor &#x27;1 &#x27;representa 100%).  [Restrição]: Campo obrigatório caso o type for igual a SOCIO e este tiver participação societária maior que 25%.  | [optional] 
**document_type** | [**EnumPartiesParticipationDocumentType**](EnumPartiesParticipationDocumentType.md) |  | 
**document_number** | **str** | Número do documento informado. Campo Texto Livre para preencher número e dígito do documento se houver | 
**document_additional_info** | **str** | Campo livre, de preenchimento obrigatório quando o documento informado tiver informações complementares relevantes para a sua identificação | [optional] 
**document_country** | **str** | País de emissão do documento. Código do pais de acordo com o código alpha3 do ISO-3166.  | [optional] 
**document_expiration_date** | **date** | Data de validade do documento informado, conforme especificação RFC-3339. | [optional] 
**document_issue_date** | **date** | Data de emissão do documento, conforme especificação RFC-3339. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

