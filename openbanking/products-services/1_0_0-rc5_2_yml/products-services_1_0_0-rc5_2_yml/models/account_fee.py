# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.2
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountFee(object):
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
        'priority_services': 'list[AccountPriorityService]',
        'other_services': 'list[AccountOtherService]'
    }

    attribute_map = {
        'priority_services': 'priorityServices',
        'other_services': 'otherServices'
    }

    def __init__(self, priority_services=None, other_services=None):  # noqa: E501
        """AccountFee - a model defined in Swagger"""  # noqa: E501
        self._priority_services = None
        self._other_services = None
        self.discriminator = None
        self.priority_services = priority_services
        if other_services is not None:
            self.other_services = other_services

    @property
    def priority_services(self):
        """Gets the priority_services of this AccountFee.  # noqa: E501

        Lista das Tarifas cobradas sobre Serviços Prioritários  # noqa: E501

        :return: The priority_services of this AccountFee.  # noqa: E501
        :rtype: list[AccountPriorityService]
        """
        return self._priority_services

    @priority_services.setter
    def priority_services(self, priority_services):
        """Sets the priority_services of this AccountFee.

        Lista das Tarifas cobradas sobre Serviços Prioritários  # noqa: E501

        :param priority_services: The priority_services of this AccountFee.  # noqa: E501
        :type: list[AccountPriorityService]
        """
        if priority_services is None:
            raise ValueError("Invalid value for `priority_services`, must not be `None`")  # noqa: E501

        self._priority_services = priority_services

    @property
    def other_services(self):
        """Gets the other_services of this AccountFee.  # noqa: E501

        Lista das Tarifas cobradas sobre outros Serviços, que não prioritários  # noqa: E501

        :return: The other_services of this AccountFee.  # noqa: E501
        :rtype: list[AccountOtherService]
        """
        return self._other_services

    @other_services.setter
    def other_services(self, other_services):
        """Sets the other_services of this AccountFee.

        Lista das Tarifas cobradas sobre outros Serviços, que não prioritários  # noqa: E501

        :param other_services: The other_services of this AccountFee.  # noqa: E501
        :type: list[AccountOtherService]
        """

        self._other_services = other_services

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
        if issubclass(AccountFee, dict):
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
        if not isinstance(other, AccountFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
