# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BusinessOtherDocument(object):
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
        'type': 'str',
        'number': 'str',
        'country': 'str',
        'expiration_date': 'date'
    }

    attribute_map = {
        'type': 'type',
        'number': 'number',
        'country': 'country',
        'expiration_date': 'expirationDate'
    }

    def __init__(self, type=None, number=None, country=None, expiration_date=None):  # noqa: E501
        """BusinessOtherDocument - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._number = None
        self._country = None
        self._expiration_date = None
        self.discriminator = None
        self.type = type
        self.number = number
        self.country = country
        if expiration_date is not None:
            self.expiration_date = expiration_date

    @property
    def type(self):
        """Gets the type of this BusinessOtherDocument.  # noqa: E501

        Número do Tipo de documento informado. De preenchimento obrigatório, para a Pessoa jurídica com domicílio ou sede no exterior, desobrigada de inscrição no CNPJ  # noqa: E501

        :return: The type of this BusinessOtherDocument.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BusinessOtherDocument.

        Número do Tipo de documento informado. De preenchimento obrigatório, para a Pessoa jurídica com domicílio ou sede no exterior, desobrigada de inscrição no CNPJ  # noqa: E501

        :param type: The type of this BusinessOtherDocument.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def number(self):
        """Gets the number of this BusinessOtherDocument.  # noqa: E501

        Número do outro documento. De preenchimento obrigatório, para a Pessoa jurídica com domicílio ou sede no exterior, desobrigada de inscrição no CNPJ  # noqa: E501

        :return: The number of this BusinessOtherDocument.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this BusinessOtherDocument.

        Número do outro documento. De preenchimento obrigatório, para a Pessoa jurídica com domicílio ou sede no exterior, desobrigada de inscrição no CNPJ  # noqa: E501

        :param number: The number of this BusinessOtherDocument.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def country(self):
        """Gets the country of this BusinessOtherDocument.  # noqa: E501

        Pais de emissão do tipo de documento informado. Código do pais de acordo com o código alpha3 do ISO-3166  # noqa: E501

        :return: The country of this BusinessOtherDocument.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this BusinessOtherDocument.

        Pais de emissão do tipo de documento informado. Código do pais de acordo com o código alpha3 do ISO-3166  # noqa: E501

        :param country: The country of this BusinessOtherDocument.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def expiration_date(self):
        """Gets the expiration_date of this BusinessOtherDocument.  # noqa: E501

        Data vigência do tipo de  documento informado, conforme especificação RFC-3339.  # noqa: E501

        :return: The expiration_date of this BusinessOtherDocument.  # noqa: E501
        :rtype: date
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this BusinessOtherDocument.

        Data vigência do tipo de  documento informado, conforme especificação RFC-3339.  # noqa: E501

        :param expiration_date: The expiration_date of this BusinessOtherDocument.  # noqa: E501
        :type: date
        """

        self._expiration_date = expiration_date

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
        if issubclass(BusinessOtherDocument, dict):
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
        if not isinstance(other, BusinessOtherDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
