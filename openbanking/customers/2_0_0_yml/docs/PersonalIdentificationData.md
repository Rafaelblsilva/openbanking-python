# PersonalIdentificationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_date_time** | **datetime** | Data e hora da atualização dos campos \\&lt;_endpoint_\\&gt;, conforme especificação RFC-3339, formato UTC. Quando não existente uma data vinculada especificamente ao bloco, assumir a data e hora de atualização do cadastro como um todo.  | 
**personal_id** | **str** | Um identificador único e imutável usado para identificar o recurso cliente pessoa natural. Este identificador não tem significado para o cliente que deu o consentimento | 
**brand_name** | **str** | Nome da Marca reportada pelo participante no Open Finance. Recomenda-se utilizar, sempre que possível, o mesmo nome de marca atribuído no campo do diretório Customer Friendly Server Name (Authorisation Server). | 
**civil_name** | **str** | Nome civil completo da pessoa natural (Direito fundamental da pessoa, o nome civil é aquele atribuído à pessoa natural desde o registro de seu nascimento, com o qual será identificada por toda a sua vida, bem como após a sua morte) | 
**social_name** | **str** | Nome social da pessoa natural, se houver. (aquele pelo qual travestis e transexuais se reconhecem, bem como são identificados por sua comunidade e em seu meio social, conforme Decreto Local) | [optional] 
**birth_date** | **date** | Data de nascimento, conforme especificação RFC-3339 | 
**marital_status_code** | [**EnumMaritalStatusCode**](EnumMaritalStatusCode.md) |  | [optional] 
**marital_status_additional_info** | **str** | Campo livre para complementar a informação relativa ao estado marital.  [Restrição] Preenchimento obrigatório quando selecionado o tipo &#x27;OUTRO&#x27;.  | [optional] 
**sex** | [**EnumSex**](EnumSex.md) |  | [optional] 
**companies_cnpj** | **list[str]** | Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica.  Deve-se ter apenas os números do CNPJ, sem máscara  | 
**documents** | [**PersonalDocument**](PersonalDocument.md) |  | 
**other_documents** | [**list[PersonalOtherDocument]**](PersonalOtherDocument.md) | Relação dos demais documentos | [optional] 
**has_brazilian_nationality** | **bool** | Informa se o Cliente tem nacionalidade brasileira. | 
**nationality** | [**list[Nationality]**](Nationality.md) |  | [optional] 
**filiation** | [**list[PersonalIdentificationDataFiliation]**](PersonalIdentificationDataFiliation.md) |  | [optional] 
**contacts** | [**PersonalContacts**](PersonalContacts.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

