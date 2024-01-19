# PersonalPostalAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_main** | **bool** | Indica se o endereço informado é o principal. | 
**address** | **str** | Corresponde ao endereço residencial do cliente. | 
**additional_info** | **str** | Alguns logradouros ainda necessitam ser especificados por meio de complemento. | [optional] 
**district_name** | **str** | Bairro é uma comunidade ou região localizada em uma cidade ou município de acordo com as suas subdivisões geográficas. | 
**town_name** | **str** | Localidade: O nome da localidade corresponde à designação da cidade ou município no qual o endereço está localizado.  | 
**ibge_town_code** | **str** | Código IBGE de Município. A Tabela de Códigos de Municípios do IBGE apresenta a lista dos municípios brasileiros associados a um código composto de 7 dígitos, sendo os dois primeiros referentes ao código da Unidade da Federação. | [optional] 
**country_sub_division** | [**EnumCountrySubDivision**](EnumCountrySubDivision.md) |  | 
**post_code** | **str** | Código de Endereçamento Postal: Composto por um conjunto numérico de oito dígitos, o objetivo principal do CEP é orientar e acelerar o encaminhamento, o tratamento e a entrega de objetos postados nos Correios, por meio da sua atribuição a localidades, logradouros, unidades dos Correios, serviços, órgãos públicos, empresas e edifícios. p.ex. &#x27;01311000&#x27;.  | 
**country** | **str** | Nome do país | 
**country_code** | **str** | Código do pais de acordo com o código “alpha3” do ISO-3166. | [optional] 
**geographic_coordinates** | [**GeographicCoordinates**](GeographicCoordinates.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

