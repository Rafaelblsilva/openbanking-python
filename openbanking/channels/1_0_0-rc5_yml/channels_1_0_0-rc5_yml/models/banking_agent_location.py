# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BankingAgentLocation(object):
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
        'postal_address': 'BankingAgentPostalAddress',
        'availability': 'BankingAgentAvailability',
        'phones': 'list[Phone]'
    }

    attribute_map = {
        'postal_address': 'postalAddress',
        'availability': 'availability',
        'phones': 'phones'
    }

    def __init__(self, postal_address=None, availability=None, phones=None):  # noqa: E501
        """BankingAgentLocation - a model defined in Swagger"""  # noqa: E501
        self._postal_address = None
        self._availability = None
        self._phones = None
        self.discriminator = None
        self.postal_address = postal_address
        if availability is not None:
            self.availability = availability
        if phones is not None:
            self.phones = phones

    @property
    def postal_address(self):
        """Gets the postal_address of this BankingAgentLocation.  # noqa: E501


        :return: The postal_address of this BankingAgentLocation.  # noqa: E501
        :rtype: BankingAgentPostalAddress
        """
        return self._postal_address

    @postal_address.setter
    def postal_address(self, postal_address):
        """Sets the postal_address of this BankingAgentLocation.


        :param postal_address: The postal_address of this BankingAgentLocation.  # noqa: E501
        :type: BankingAgentPostalAddress
        """
        if postal_address is None:
            raise ValueError("Invalid value for `postal_address`, must not be `None`")  # noqa: E501

        self._postal_address = postal_address

    @property
    def availability(self):
        """Gets the availability of this BankingAgentLocation.  # noqa: E501


        :return: The availability of this BankingAgentLocation.  # noqa: E501
        :rtype: BankingAgentAvailability
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this BankingAgentLocation.


        :param availability: The availability of this BankingAgentLocation.  # noqa: E501
        :type: BankingAgentAvailability
        """

        self._availability = availability

    @property
    def phones(self):
        """Gets the phones of this BankingAgentLocation.  # noqa: E501


        :return: The phones of this BankingAgentLocation.  # noqa: E501
        :rtype: list[Phone]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this BankingAgentLocation.


        :param phones: The phones of this BankingAgentLocation.  # noqa: E501
        :type: list[Phone]
        """

        self._phones = phones

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
        if issubclass(BankingAgentLocation, dict):
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
        if not isinstance(other, BankingAgentLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
