# PersonalIdentificationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_date_time** | **datetime** |  | 
**personal_id** | **str** | Um identificador único e imutável usado para identificar o recurso cliente pessoa natural. Este identificador não tem significado para o cliente que deu o consentimento | 
**brand_name** | **str** | Nome da Marca reportada pelo participante do Open Banking. O conceito a que se refere a &#x27;marca&#x27; é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes | 
**civil_name** | **str** | Nome civil completo da pessoa natural (Direito fundamental da pessoa, o nome civil é aquele atribuído à pessoa natural desde o registro de seu nascimento, com o qual será identificada por toda a sua vida, bem como após a sua morte) | 
**social_name** | **str** | Nome social da pessoa natural, se houver. (aquele pelo qual travestis e transexuais se reconhecem, bem como são identificados por sua comunidade e em seu meio social, conforme Decreto Local) | 
**birth_date** | **date** | Data de nascimento, conforme especificação RFC-3339 | 
**marital_status_code** | [**EnumMaritalStatusCode**](EnumMaritalStatusCode.md) |  | 
**marital_status_additional_info** | **str** | Campo livre para complementar a informação relativa ao estado marital, quando selecionada a opção &#x27;OUTROS&#x27; | [optional] 
**sex** | [**EnumSex**](EnumSex.md) |  | 
**company_cnpj** | **list[str]** | Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica.  Deve-se ter apenas os números do CNPJ, sem máscara  | 
**documents** | [**PersonalDocument**](PersonalDocument.md) |  | 
**other_documents** | [**list[PersonalOtherDocument]**](PersonalOtherDocument.md) | Relação dos demais documentos | 
**has_brazilian_nationality** | **bool** | Informa se o Cliente tem nacionalidade brasileira. | 
**nationality** | [**list[Nationality]**](Nationality.md) |  | 
**filiation** | [**list[PersonalIdentificationDataFiliation]**](PersonalIdentificationDataFiliation.md) |  | 
**contacts** | [**PersonalContacts**](PersonalContacts.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

