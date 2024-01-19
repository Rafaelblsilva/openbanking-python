# coding: utf-8

"""
    API Treasure Titles - Open Finance Brasil

    API de informações de operações de Títulos do Tesouro Direto Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Títulos do Tesouro Direto mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. Devem ser considerados como escopo de exposição todos os títulos ofertados pelo Tesouro Direto. A exposição se dará por cada operação de títulos do Tesouro Direto contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LockedWithAdditionalPropertiesErrors(object):
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
        'code': 'str',
        'title': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'code': 'code',
        'title': 'title',
        'detail': 'detail'
    }

    def __init__(self, code=None, title=None, detail=None):  # noqa: E501
        """LockedWithAdditionalPropertiesErrors - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._title = None
        self._detail = None
        self.discriminator = None
        self.code = code
        self.title = title
        self.detail = detail

    @property
    def code(self):
        """Gets the code of this LockedWithAdditionalPropertiesErrors.  # noqa: E501

        Código de erro específico do endpoint  # noqa: E501

        :return: The code of this LockedWithAdditionalPropertiesErrors.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LockedWithAdditionalPropertiesErrors.

        Código de erro específico do endpoint  # noqa: E501

        :param code: The code of this LockedWithAdditionalPropertiesErrors.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def title(self):
        """Gets the title of this LockedWithAdditionalPropertiesErrors.  # noqa: E501

        Título legível por humanos deste erro específico  # noqa: E501

        :return: The title of this LockedWithAdditionalPropertiesErrors.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LockedWithAdditionalPropertiesErrors.

        Título legível por humanos deste erro específico  # noqa: E501

        :param title: The title of this LockedWithAdditionalPropertiesErrors.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def detail(self):
        """Gets the detail of this LockedWithAdditionalPropertiesErrors.  # noqa: E501

        Descrição legível por humanos deste erro específico  # noqa: E501

        :return: The detail of this LockedWithAdditionalPropertiesErrors.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this LockedWithAdditionalPropertiesErrors.

        Descrição legível por humanos deste erro específico  # noqa: E501

        :param detail: The detail of this LockedWithAdditionalPropertiesErrors.  # noqa: E501
        :type: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

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
        if issubclass(LockedWithAdditionalPropertiesErrors, dict):
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
        if not isinstance(other, LockedWithAdditionalPropertiesErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
