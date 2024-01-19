# coding: utf-8

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InsurancePensionEnumPmbacRemuneration(object):
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
        'interest_rate': 'str',
        'update_indexes': 'list[EnumPersonalUpdateIndex]'
    }

    attribute_map = {
        'interest_rate': 'interestRate',
        'update_indexes': 'updateIndexes'
    }

    def __init__(self, interest_rate=None, update_indexes=None):  # noqa: E501
        """InsurancePensionEnumPmbacRemuneration - a model defined in Swagger"""  # noqa: E501
        self._interest_rate = None
        self._update_indexes = None
        self.discriminator = None
        if interest_rate is not None:
            self.interest_rate = interest_rate
        if update_indexes is not None:
            self.update_indexes = update_indexes

    @property
    def interest_rate(self):
        """Gets the interest_rate of this InsurancePensionEnumPmbacRemuneration.  # noqa: E501

        Taxa de juros para capitalização da PMBaC  # noqa: E501

        :return: The interest_rate of this InsurancePensionEnumPmbacRemuneration.  # noqa: E501
        :rtype: str
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this InsurancePensionEnumPmbacRemuneration.

        Taxa de juros para capitalização da PMBaC  # noqa: E501

        :param interest_rate: The interest_rate of this InsurancePensionEnumPmbacRemuneration.  # noqa: E501
        :type: str
        """

        self._interest_rate = interest_rate

    @property
    def update_indexes(self):
        """Gets the update_indexes of this InsurancePensionEnumPmbacRemuneration.  # noqa: E501


        :return: The update_indexes of this InsurancePensionEnumPmbacRemuneration.  # noqa: E501
        :rtype: list[EnumPersonalUpdateIndex]
        """
        return self._update_indexes

    @update_indexes.setter
    def update_indexes(self, update_indexes):
        """Sets the update_indexes of this InsurancePensionEnumPmbacRemuneration.


        :param update_indexes: The update_indexes of this InsurancePensionEnumPmbacRemuneration.  # noqa: E501
        :type: list[EnumPersonalUpdateIndex]
        """

        self._update_indexes = update_indexes

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
        if issubclass(InsurancePensionEnumPmbacRemuneration, dict):
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
        if not isinstance(other, InsurancePensionEnumPmbacRemuneration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
