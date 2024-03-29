# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BusinessPostalAddress(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_main': 'bool',
        'address': 'str',
        'additional_info': 'str',
        'district_name': 'str',
        'town_name': 'str',
        'ibge_town_code': 'str',
        'country_sub_division': 'EnumCountrySubDivision',
        'post_code': 'str',
        'country': 'str',
        'country_code': 'str',
        'geographic_coordinates': 'GeographicCoordinates'
    }

    attribute_map = {
        'is_main': 'isMain',
        'address': 'address',
        'additional_info': 'additionalInfo',
        'district_name': 'districtName',
        'town_name': 'townName',
        'ibge_town_code': 'ibgeTownCode',
        'country_sub_division': 'countrySubDivision',
        'post_code': 'postCode',
        'country': 'country',
        'country_code': 'countryCode',
        'geographic_coordinates': 'geographicCoordinates'
    }

    def __init__(self, is_main=None, address=None, additional_info=None, district_name=None, town_name=None, ibge_town_code=None, country_sub_division=None, post_code=None, country=None, country_code=None, geographic_coordinates=None):  # noqa: E501
        """BusinessPostalAddress - a model defined in Swagger"""  # noqa: E501
        self._is_main = None
        self._address = None
        self._additional_info = None
        self._district_name = None
        self._town_name = None
        self._ibge_town_code = None
        self._country_sub_division = None
        self._post_code = None
        self._country = None
        self._country_code = None
        self._geographic_coordinates = None
        self.discriminator = None
        self.is_main = is_main
        self.address = address
        if additional_info is not None:
            self.additional_info = additional_info
        self.district_name = district_name
        self.town_name = town_name
        if ibge_town_code is not None:
            self.ibge_town_code = ibge_town_code
        self.country_sub_division = country_sub_division
        self.post_code = post_code
        self.country = country
        if country_code is not None:
            self.country_code = country_code
        if geographic_coordinates is not None:
            self.geographic_coordinates = geographic_coordinates

    @property
    def is_main(self):
        """Gets the is_main of this BusinessPostalAddress.  # noqa: E501

        Indica se o endereço informado é o principal  # noqa: E501

        :return: The is_main of this BusinessPostalAddress.  # noqa: E501
        :rtype: bool
        """
        return self._is_main

    @is_main.setter
    def is_main(self, is_main):
        """Sets the is_main of this BusinessPostalAddress.

        Indica se o endereço informado é o principal  # noqa: E501

        :param is_main: The is_main of this BusinessPostalAddress.  # noqa: E501
        :type: bool
        """
        if is_main is None:
            raise ValueError("Invalid value for `is_main`, must not be `None`")  # noqa: E501

        self._is_main = is_main

    @property
    def address(self):
        """Gets the address of this BusinessPostalAddress.  # noqa: E501

        Corresponde ao endereço comercial do cliente  # noqa: E501

        :return: The address of this BusinessPostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BusinessPostalAddress.

        Corresponde ao endereço comercial do cliente  # noqa: E501

        :param address: The address of this BusinessPostalAddress.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def additional_info(self):
        """Gets the additional_info of this BusinessPostalAddress.  # noqa: E501

        Alguns logradouros ainda necessitam ser especificados por meio de complemento  # noqa: E501

        :return: The additional_info of this BusinessPostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this BusinessPostalAddress.

        Alguns logradouros ainda necessitam ser especificados por meio de complemento  # noqa: E501

        :param additional_info: The additional_info of this BusinessPostalAddress.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def district_name(self):
        """Gets the district_name of this BusinessPostalAddress.  # noqa: E501

        Bairro é uma comunidade ou região localizada em uma cidade ou município de acordo com as suas subdivisões geográficas.  # noqa: E501

        :return: The district_name of this BusinessPostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._district_name

    @district_name.setter
    def district_name(self, district_name):
        """Sets the district_name of this BusinessPostalAddress.

        Bairro é uma comunidade ou região localizada em uma cidade ou município de acordo com as suas subdivisões geográficas.  # noqa: E501

        :param district_name: The district_name of this BusinessPostalAddress.  # noqa: E501
        :type: str
        """
        if district_name is None:
            raise ValueError("Invalid value for `district_name`, must not be `None`")  # noqa: E501

        self._district_name = district_name

    @property
    def town_name(self):
        """Gets the town_name of this BusinessPostalAddress.  # noqa: E501

        Localidade: O nome da localidade corresponde à designação da cidade ou município no qual o endereço está localizado.   # noqa: E501

        :return: The town_name of this BusinessPostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._town_name

    @town_name.setter
    def town_name(self, town_name):
        """Sets the town_name of this BusinessPostalAddress.

        Localidade: O nome da localidade corresponde à designação da cidade ou município no qual o endereço está localizado.   # noqa: E501

        :param town_name: The town_name of this BusinessPostalAddress.  # noqa: E501
        :type: str
        """
        if town_name is None:
            raise ValueError("Invalid value for `town_name`, must not be `None`")  # noqa: E501

        self._town_name = town_name

    @property
    def ibge_town_code(self):
        """Gets the ibge_town_code of this BusinessPostalAddress.  # noqa: E501

        Código IBGE de Município. A Tabela de Códigos de Municípios do IBGE apresenta a lista dos municípios brasileiros associados a um código composto de 7 dígitos, sendo os dois primeiros referentes ao código da Unidade da Federação.  # noqa: E501

        :return: The ibge_town_code of this BusinessPostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._ibge_town_code

    @ibge_town_code.setter
    def ibge_town_code(self, ibge_town_code):
        """Sets the ibge_town_code of this BusinessPostalAddress.

        Código IBGE de Município. A Tabela de Códigos de Municípios do IBGE apresenta a lista dos municípios brasileiros associados a um código composto de 7 dígitos, sendo os dois primeiros referentes ao código da Unidade da Federação.  # noqa: E501

        :param ibge_town_code: The ibge_town_code of this BusinessPostalAddress.  # noqa: E501
        :type: str
        """

        self._ibge_town_code = ibge_town_code

    @property
    def country_sub_division(self):
        """Gets the country_sub_division of this BusinessPostalAddress.  # noqa: E501


        :return: The country_sub_division of this BusinessPostalAddress.  # noqa: E501
        :rtype: EnumCountrySubDivision
        """
        return self._country_sub_division

    @country_sub_division.setter
    def country_sub_division(self, country_sub_division):
        """Sets the country_sub_division of this BusinessPostalAddress.


        :param country_sub_division: The country_sub_division of this BusinessPostalAddress.  # noqa: E501
        :type: EnumCountrySubDivision
        """
        if country_sub_division is None:
            raise ValueError("Invalid value for `country_sub_division`, must not be `None`")  # noqa: E501

        self._country_sub_division = country_sub_division

    @property
    def post_code(self):
        """Gets the post_code of this BusinessPostalAddress.  # noqa: E501

        Código de Endereçamento Postal: Composto por um conjunto numérico de oito dígitos, o objetivo principal do CEP é orientar e acelerar o encaminhamento, o tratamento e a entrega de objetos postados nos Correios, por meio da sua atribuição a localidades, logradouros, unidades dos Correios, serviços, órgãos públicos, empresas e edifícios. p.ex. '01311000'   # noqa: E501

        :return: The post_code of this BusinessPostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this BusinessPostalAddress.

        Código de Endereçamento Postal: Composto por um conjunto numérico de oito dígitos, o objetivo principal do CEP é orientar e acelerar o encaminhamento, o tratamento e a entrega de objetos postados nos Correios, por meio da sua atribuição a localidades, logradouros, unidades dos Correios, serviços, órgãos públicos, empresas e edifícios. p.ex. '01311000'   # noqa: E501

        :param post_code: The post_code of this BusinessPostalAddress.  # noqa: E501
        :type: str
        """
        if post_code is None:
            raise ValueError("Invalid value for `post_code`, must not be `None`")  # noqa: E501

        self._post_code = post_code

    @property
    def country(self):
        """Gets the country of this BusinessPostalAddress.  # noqa: E501

        Nome do país  # noqa: E501

        :return: The country of this BusinessPostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this BusinessPostalAddress.

        Nome do país  # noqa: E501

        :param country: The country of this BusinessPostalAddress.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def country_code(self):
        """Gets the country_code of this BusinessPostalAddress.  # noqa: E501

        Código do pais de acordo com o código “alpha3” do ISO-3166  # noqa: E501

        :return: The country_code of this BusinessPostalAddress.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this BusinessPostalAddress.

        Código do pais de acordo com o código “alpha3” do ISO-3166  # noqa: E501

        :param country_code: The country_code of this BusinessPostalAddress.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def geographic_coordinates(self):
        """Gets the geographic_coordinates of this BusinessPostalAddress.  # noqa: E501


        :return: The geographic_coordinates of this BusinessPostalAddress.  # noqa: E501
        :rtype: GeographicCoordinates
        """
        return self._geographic_coordinates

    @geographic_coordinates.setter
    def geographic_coordinates(self, geographic_coordinates):
        """Sets the geographic_coordinates of this BusinessPostalAddress.


        :param geographic_coordinates: The geographic_coordinates of this BusinessPostalAddress.  # noqa: E501
        :type: GeographicCoordinates
        """

        self._geographic_coordinates = geographic_coordinates

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BusinessPostalAddress, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BusinessPostalAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
