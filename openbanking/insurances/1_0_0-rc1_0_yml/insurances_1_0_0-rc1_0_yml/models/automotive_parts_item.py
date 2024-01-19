# coding: utf-8

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AutomotivePartsItem(object):
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
        'condition': 'str',
        'type': 'EnumAutomotivePartType'
    }

    attribute_map = {
        'condition': 'condition',
        'type': 'type'
    }

    def __init__(self, condition=None, type=None):  # noqa: E501
        """AutomotivePartsItem - a model defined in Swagger"""  # noqa: E501
        self._condition = None
        self._type = None
        self.discriminator = None
        if condition is not None:
            self.condition = condition
        if type is not None:
            self.type = type

    @property
    def condition(self):
        """Gets the condition of this AutomotivePartsItem.  # noqa: E501

        Novas ou usada. A considerar os domínios abaixo:   1. Novas   2. Usadas   3. Ambas   # noqa: E501

        :return: The condition of this AutomotivePartsItem.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this AutomotivePartsItem.

        Novas ou usada. A considerar os domínios abaixo:   1. Novas   2. Usadas   3. Ambas   # noqa: E501

        :param condition: The condition of this AutomotivePartsItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["NOVAS", "USADAS", "AMBAS"]  # noqa: E501
        if condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def type(self):
        """Gets the type of this AutomotivePartsItem.  # noqa: E501


        :return: The type of this AutomotivePartsItem.  # noqa: E501
        :rtype: EnumAutomotivePartType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AutomotivePartsItem.


        :param type: The type of this AutomotivePartsItem.  # noqa: E501
        :type: EnumAutomotivePartType
        """

        self._type = type

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
        if issubclass(AutomotivePartsItem, dict):
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
        if not isinstance(other, AutomotivePartsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
