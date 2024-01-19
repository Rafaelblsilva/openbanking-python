# coding: utf-8

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.5
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GracePeriod(object):
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
        'amount': 'int',
        'unit': 'EnumGracePeriodUnit'
    }

    attribute_map = {
        'amount': 'amount',
        'unit': 'unit'
    }

    def __init__(self, amount=None, unit=None):  # noqa: E501
        """GracePeriod - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._unit = None
        self.discriminator = None
        self.amount = amount
        self.unit = unit

    @property
    def amount(self):
        """Gets the amount of this GracePeriod.  # noqa: E501

        Informar o prazo de carência  # noqa: E501

        :return: The amount of this GracePeriod.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GracePeriod.

        Informar o prazo de carência  # noqa: E501

        :param amount: The amount of this GracePeriod.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def unit(self):
        """Gets the unit of this GracePeriod.  # noqa: E501


        :return: The unit of this GracePeriod.  # noqa: E501
        :rtype: EnumGracePeriodUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this GracePeriod.


        :param unit: The unit of this GracePeriod.  # noqa: E501
        :type: EnumGracePeriodUnit
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

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
        if issubclass(GracePeriod, dict):
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
        if not isinstance(other, GracePeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
