# BankingAgentPostalAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Deverá trazer toda a informação referente ao endereço da dependência informada: Tipo de logradouro + Nome do logradouro + Número do Logradouro (se não existir usar &#x27; s/n&#x27;) + complemento (se houver), como, p.ex.: &#x27;R Diamatina, 59, bloco 35, fundos&#x27; &#x27;Praça da Boa Vontade s/n&#x27; | 
**additional_info** | **str** | Alguns logradouros ainda necessitam ser especificados por meio de complemento | [optional] 
**district_name** | **str** | Bairro é uma comunidade ou região localizada em uma cidade ou município de acordo com as suas subdivisões geográficas. p.ex: &#x27;Paraíso&#x27; | 
**town_name** | **str** | Localidade: O nome da localidade corresponde à designação da cidade ou município no qual o endereço está localizado. p.ex. &#x27;São Paulo&#x27; | 
**ibge_code** | **str** | Código IBGE do município | [optional] 
**country_sub_division** | **str** | Enumeração referente a cada sigla da unidade da federação que identifica o estado ou o distrito federal, no qual o endereço está localizado. p.ex. &#x27;AC&#x27;. São consideradas apenas as siglas para os estados brasileiros | 
**post_code** | **str** | Código de Endereçamento Postal | 
**country** | **str** | Nome do país | [optional] 
**country_code** | **str** | Código do país de acordo com a ISO 3166-1 alpha-3 | [optional] 
**geographic_coordinates** | [**GeographicCoordinates**](GeographicCoordinates.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

