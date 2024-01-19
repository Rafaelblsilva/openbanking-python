# coding: utf-8

"""
    API Pension - Open Finance Brasil

    API de Previdência do Open Finance Brasil – Fase 4. API que retorna informações de Previdência.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Coverage(object):
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
        'type': 'EnumRiskPensionCoverageType',
        'type_additional_infos': 'list[str]',
        'attributes': 'CoverageAttributes'
    }

    attribute_map = {
        'type': 'type',
        'type_additional_infos': 'typeAdditionalInfos',
        'attributes': 'attributes'
    }

    def __init__(self, type=None, type_additional_infos=None, attributes=None):  # noqa: E501
        """Coverage - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._type_additional_infos = None
        self._attributes = None
        self.discriminator = None
        self.type = type
        if type_additional_infos is not None:
            self.type_additional_infos = type_additional_infos
        if attributes is not None:
            self.attributes = attributes

    @property
    def type(self):
        """Gets the type of this Coverage.  # noqa: E501


        :return: The type of this Coverage.  # noqa: E501
        :rtype: EnumRiskPensionCoverageType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Coverage.


        :param type: The type of this Coverage.  # noqa: E501
        :type: EnumRiskPensionCoverageType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def type_additional_infos(self):
        """Gets the type_additional_infos of this Coverage.  # noqa: E501

        Lista de textos para complementar informação relativa ao campo type, quando for selecionada a opção 'OUTROS'. Restrição: Campo de preenchimento obrigatório se 'type' estiver preenchida a opção 'OUTROS'   # noqa: E501

        :return: The type_additional_infos of this Coverage.  # noqa: E501
        :rtype: list[str]
        """
        return self._type_additional_infos

    @type_additional_infos.setter
    def type_additional_infos(self, type_additional_infos):
        """Sets the type_additional_infos of this Coverage.

        Lista de textos para complementar informação relativa ao campo type, quando for selecionada a opção 'OUTROS'. Restrição: Campo de preenchimento obrigatório se 'type' estiver preenchida a opção 'OUTROS'   # noqa: E501

        :param type_additional_infos: The type_additional_infos of this Coverage.  # noqa: E501
        :type: list[str]
        """

        self._type_additional_infos = type_additional_infos

    @property
    def attributes(self):
        """Gets the attributes of this Coverage.  # noqa: E501


        :return: The attributes of this Coverage.  # noqa: E501
        :rtype: CoverageAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Coverage.


        :param attributes: The attributes of this Coverage.  # noqa: E501
        :type: CoverageAttributes
        """

        self._attributes = attributes

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
        if issubclass(Coverage, dict):
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
        if not isinstance(other, Coverage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
