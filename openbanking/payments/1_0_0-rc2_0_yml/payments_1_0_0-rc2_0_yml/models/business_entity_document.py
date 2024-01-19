# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, reponsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openId` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BusinessEntityDocument(object):
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
        'identification': 'str',
        'rel': 'str'
    }

    attribute_map = {
        'identification': 'identification',
        'rel': 'rel'
    }

    def __init__(self, identification=None, rel=None):  # noqa: E501
        """BusinessEntityDocument - a model defined in Swagger"""  # noqa: E501
        self._identification = None
        self._rel = None
        self.discriminator = None
        self.identification = identification
        self.rel = rel

    @property
    def identification(self):
        """Gets the identification of this BusinessEntityDocument.  # noqa: E501

        Número do documento de identificação oficial do titular pessoa jurídica.  # noqa: E501

        :return: The identification of this BusinessEntityDocument.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this BusinessEntityDocument.

        Número do documento de identificação oficial do titular pessoa jurídica.  # noqa: E501

        :param identification: The identification of this BusinessEntityDocument.  # noqa: E501
        :type: str
        """
        if identification is None:
            raise ValueError("Invalid value for `identification`, must not be `None`")  # noqa: E501

        self._identification = identification

    @property
    def rel(self):
        """Gets the rel of this BusinessEntityDocument.  # noqa: E501

        Tipo do documento de identificação oficial do titular pessoa jurídica.  # noqa: E501

        :return: The rel of this BusinessEntityDocument.  # noqa: E501
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this BusinessEntityDocument.

        Tipo do documento de identificação oficial do titular pessoa jurídica.  # noqa: E501

        :param rel: The rel of this BusinessEntityDocument.  # noqa: E501
        :type: str
        """
        if rel is None:
            raise ValueError("Invalid value for `rel`, must not be `None`")  # noqa: E501

        self._rel = rel

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
        if issubclass(BusinessEntityDocument, dict):
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
        if not isinstance(other, BusinessEntityDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
