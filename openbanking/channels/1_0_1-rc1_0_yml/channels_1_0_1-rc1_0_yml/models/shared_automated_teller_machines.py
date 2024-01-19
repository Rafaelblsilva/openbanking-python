# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.1-rc1.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SharedAutomatedTellerMachines(object):
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
        'identification': 'SharedAutomatedTellerMachinesIdentification',
        'postal_address': 'SharedAutomatedTellerMachinesPostalAddress',
        'availability': 'SharedAutomatedTellerMachinesAvailability',
        'services': 'list[SharedAutomatedTellerMachinesServices]'
    }

    attribute_map = {
        'identification': 'identification',
        'postal_address': 'postalAddress',
        'availability': 'availability',
        'services': 'services'
    }

    def __init__(self, identification=None, postal_address=None, availability=None, services=None):  # noqa: E501
        """SharedAutomatedTellerMachines - a model defined in Swagger"""  # noqa: E501
        self._identification = None
        self._postal_address = None
        self._availability = None
        self._services = None
        self.discriminator = None
        if identification is not None:
            self.identification = identification
        if postal_address is not None:
            self.postal_address = postal_address
        if availability is not None:
            self.availability = availability
        if services is not None:
            self.services = services

    @property
    def identification(self):
        """Gets the identification of this SharedAutomatedTellerMachines.  # noqa: E501


        :return: The identification of this SharedAutomatedTellerMachines.  # noqa: E501
        :rtype: SharedAutomatedTellerMachinesIdentification
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this SharedAutomatedTellerMachines.


        :param identification: The identification of this SharedAutomatedTellerMachines.  # noqa: E501
        :type: SharedAutomatedTellerMachinesIdentification
        """

        self._identification = identification

    @property
    def postal_address(self):
        """Gets the postal_address of this SharedAutomatedTellerMachines.  # noqa: E501


        :return: The postal_address of this SharedAutomatedTellerMachines.  # noqa: E501
        :rtype: SharedAutomatedTellerMachinesPostalAddress
        """
        return self._postal_address

    @postal_address.setter
    def postal_address(self, postal_address):
        """Sets the postal_address of this SharedAutomatedTellerMachines.


        :param postal_address: The postal_address of this SharedAutomatedTellerMachines.  # noqa: E501
        :type: SharedAutomatedTellerMachinesPostalAddress
        """

        self._postal_address = postal_address

    @property
    def availability(self):
        """Gets the availability of this SharedAutomatedTellerMachines.  # noqa: E501


        :return: The availability of this SharedAutomatedTellerMachines.  # noqa: E501
        :rtype: SharedAutomatedTellerMachinesAvailability
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this SharedAutomatedTellerMachines.


        :param availability: The availability of this SharedAutomatedTellerMachines.  # noqa: E501
        :type: SharedAutomatedTellerMachinesAvailability
        """

        self._availability = availability

    @property
    def services(self):
        """Gets the services of this SharedAutomatedTellerMachines.  # noqa: E501


        :return: The services of this SharedAutomatedTellerMachines.  # noqa: E501
        :rtype: list[SharedAutomatedTellerMachinesServices]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this SharedAutomatedTellerMachines.


        :param services: The services of this SharedAutomatedTellerMachines.  # noqa: E501
        :type: list[SharedAutomatedTellerMachinesServices]
        """

        self._services = services

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
        if issubclass(SharedAutomatedTellerMachines, dict):
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
        if not isinstance(other, SharedAutomatedTellerMachines):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
