# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 1.0.3
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalIdentificationDataFiliation(object):
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
        'type': 'EnumFiliationType',
        'civil_name': 'str',
        'social_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'civil_name': 'civilName',
        'social_name': 'socialName'
    }

    def __init__(self, type=None, civil_name=None, social_name=None):  # noqa: E501
        """PersonalIdentificationDataFiliation - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._civil_name = None
        self._social_name = None
        self.discriminator = None
        self.type = type
        self.civil_name = civil_name
        if social_name is not None:
            self.social_name = social_name

    @property
    def type(self):
        """Gets the type of this PersonalIdentificationDataFiliation.  # noqa: E501


        :return: The type of this PersonalIdentificationDataFiliation.  # noqa: E501
        :rtype: EnumFiliationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PersonalIdentificationDataFiliation.


        :param type: The type of this PersonalIdentificationDataFiliation.  # noqa: E501
        :type: EnumFiliationType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def civil_name(self):
        """Gets the civil_name of this PersonalIdentificationDataFiliation.  # noqa: E501

        Nome civil completo da pessoa relativa à filiação. (Direito fundamental da pessoa, o nome civil é aquele atribuído à pessoa natural desde o registro de seu nascimento,  com o qual será identificada por toda a sua vida, bem como após a sua morte)   # noqa: E501

        :return: The civil_name of this PersonalIdentificationDataFiliation.  # noqa: E501
        :rtype: str
        """
        return self._civil_name

    @civil_name.setter
    def civil_name(self, civil_name):
        """Sets the civil_name of this PersonalIdentificationDataFiliation.

        Nome civil completo da pessoa relativa à filiação. (Direito fundamental da pessoa, o nome civil é aquele atribuído à pessoa natural desde o registro de seu nascimento,  com o qual será identificada por toda a sua vida, bem como após a sua morte)   # noqa: E501

        :param civil_name: The civil_name of this PersonalIdentificationDataFiliation.  # noqa: E501
        :type: str
        """
        if civil_name is None:
            raise ValueError("Invalid value for `civil_name`, must not be `None`")  # noqa: E501

        self._civil_name = civil_name

    @property
    def social_name(self):
        """Gets the social_name of this PersonalIdentificationDataFiliation.  # noqa: E501

        Nome social da pessoa natural, se houver.  (aquele pelo qual travestis e transexuais se reconhecem,  bem como são identificados por sua comunidade e em seu meio social, conforme Decreto Local)   # noqa: E501

        :return: The social_name of this PersonalIdentificationDataFiliation.  # noqa: E501
        :rtype: str
        """
        return self._social_name

    @social_name.setter
    def social_name(self, social_name):
        """Sets the social_name of this PersonalIdentificationDataFiliation.

        Nome social da pessoa natural, se houver.  (aquele pelo qual travestis e transexuais se reconhecem,  bem como são identificados por sua comunidade e em seu meio social, conforme Decreto Local)   # noqa: E501

        :param social_name: The social_name of this PersonalIdentificationDataFiliation.  # noqa: E501
        :type: str
        """

        self._social_name = social_name

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
        if issubclass(PersonalIdentificationDataFiliation, dict):
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
        if not isinstance(other, PersonalIdentificationDataFiliation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
