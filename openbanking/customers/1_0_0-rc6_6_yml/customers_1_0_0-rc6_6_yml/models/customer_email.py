# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.6
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CustomerEmail(object):
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
        'email': 'str'
    }

    attribute_map = {
        'is_main': 'isMain',
        'email': 'email'
    }

    def __init__(self, is_main=None, email=None):  # noqa: E501
        """CustomerEmail - a model defined in Swagger"""  # noqa: E501
        self._is_main = None
        self._email = None
        self.discriminator = None
        self.is_main = is_main
        self.email = email

    @property
    def is_main(self):
        """Gets the is_main of this CustomerEmail.  # noqa: E501

        Indica se o email informado é o principal  # noqa: E501

        :return: The is_main of this CustomerEmail.  # noqa: E501
        :rtype: bool
        """
        return self._is_main

    @is_main.setter
    def is_main(self, is_main):
        """Sets the is_main of this CustomerEmail.

        Indica se o email informado é o principal  # noqa: E501

        :param is_main: The is_main of this CustomerEmail.  # noqa: E501
        :type: bool
        """
        if is_main is None:
            raise ValueError("Invalid value for `is_main`, must not be `None`")  # noqa: E501

        self._is_main = is_main

    @property
    def email(self):
        """Gets the email of this CustomerEmail.  # noqa: E501

        Endereço de email  # noqa: E501

        :return: The email of this CustomerEmail.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CustomerEmail.

        Endereço de email  # noqa: E501

        :param email: The email of this CustomerEmail.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

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
        if issubclass(CustomerEmail, dict):
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
        if not isinstance(other, CustomerEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
