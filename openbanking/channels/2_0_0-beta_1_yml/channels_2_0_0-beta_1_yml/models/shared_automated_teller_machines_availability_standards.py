# coding: utf-8

"""
    API OpenData Channels do Open Finance Brasil

    A API descrita neste documento é referente as API Channels da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 2.0.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SharedAutomatedTellerMachinesAvailabilityStandards(object):
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
        'weekday': 'str',
        'opening_time': 'str',
        'closing_time': 'str'
    }

    attribute_map = {
        'weekday': 'weekday',
        'opening_time': 'openingTime',
        'closing_time': 'closingTime'
    }

    def __init__(self, weekday=None, opening_time=None, closing_time=None):  # noqa: E501
        """SharedAutomatedTellerMachinesAvailabilityStandards - a model defined in Swagger"""  # noqa: E501
        self._weekday = None
        self._opening_time = None
        self._closing_time = None
        self.discriminator = None
        if weekday is not None:
            self.weekday = weekday
        if opening_time is not None:
            self.opening_time = opening_time
        if closing_time is not None:
            self.closing_time = closing_time

    @property
    def weekday(self):
        """Gets the weekday of this SharedAutomatedTellerMachinesAvailabilityStandards.  # noqa: E501

        Dia da semana de abertura  # noqa: E501

        :return: The weekday of this SharedAutomatedTellerMachinesAvailabilityStandards.  # noqa: E501
        :rtype: str
        """
        return self._weekday

    @weekday.setter
    def weekday(self, weekday):
        """Sets the weekday of this SharedAutomatedTellerMachinesAvailabilityStandards.

        Dia da semana de abertura  # noqa: E501

        :param weekday: The weekday of this SharedAutomatedTellerMachinesAvailabilityStandards.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOMINGO", "SEGUNDA_FEIRA", "TERCA_FEIRA", "QUARTA_FEIRA", "QUINTA_FEIRA", "SEXTA_FEIRA", "SABADO"]  # noqa: E501
        if weekday not in allowed_values:
            raise ValueError(
                "Invalid value for `weekday` ({0}), must be one of {1}"  # noqa: E501
                .format(weekday, allowed_values)
            )

        self._weekday = weekday

    @property
    def opening_time(self):
        """Gets the opening_time of this SharedAutomatedTellerMachinesAvailabilityStandards.  # noqa: E501

        Horário de abertura (UTC)  # noqa: E501

        :return: The opening_time of this SharedAutomatedTellerMachinesAvailabilityStandards.  # noqa: E501
        :rtype: str
        """
        return self._opening_time

    @opening_time.setter
    def opening_time(self, opening_time):
        """Sets the opening_time of this SharedAutomatedTellerMachinesAvailabilityStandards.

        Horário de abertura (UTC)  # noqa: E501

        :param opening_time: The opening_time of this SharedAutomatedTellerMachinesAvailabilityStandards.  # noqa: E501
        :type: str
        """

        self._opening_time = opening_time

    @property
    def closing_time(self):
        """Gets the closing_time of this SharedAutomatedTellerMachinesAvailabilityStandards.  # noqa: E501

        Horário de fechamento (UTC)  # noqa: E501

        :return: The closing_time of this SharedAutomatedTellerMachinesAvailabilityStandards.  # noqa: E501
        :rtype: str
        """
        return self._closing_time

    @closing_time.setter
    def closing_time(self, closing_time):
        """Sets the closing_time of this SharedAutomatedTellerMachinesAvailabilityStandards.

        Horário de fechamento (UTC)  # noqa: E501

        :param closing_time: The closing_time of this SharedAutomatedTellerMachinesAvailabilityStandards.  # noqa: E501
        :type: str
        """

        self._closing_time = closing_time

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
        if issubclass(SharedAutomatedTellerMachinesAvailabilityStandards, dict):
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
        if not isinstance(other, SharedAutomatedTellerMachinesAvailabilityStandards):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
