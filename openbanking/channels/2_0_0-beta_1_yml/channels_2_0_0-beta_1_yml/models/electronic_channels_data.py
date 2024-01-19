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

class ElectronicChannelsData(object):
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
        'participant': 'ElectronicChannelsParticipant',
        'identification': 'ElectronicChannelIdentification',
        'services': 'list[ElectronicChannelService]'
    }

    attribute_map = {
        'participant': 'participant',
        'identification': 'identification',
        'services': 'services'
    }

    def __init__(self, participant=None, identification=None, services=None):  # noqa: E501
        """ElectronicChannelsData - a model defined in Swagger"""  # noqa: E501
        self._participant = None
        self._identification = None
        self._services = None
        self.discriminator = None
        if participant is not None:
            self.participant = participant
        self.identification = identification
        self.services = services

    @property
    def participant(self):
        """Gets the participant of this ElectronicChannelsData.  # noqa: E501


        :return: The participant of this ElectronicChannelsData.  # noqa: E501
        :rtype: ElectronicChannelsParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this ElectronicChannelsData.


        :param participant: The participant of this ElectronicChannelsData.  # noqa: E501
        :type: ElectronicChannelsParticipant
        """

        self._participant = participant

    @property
    def identification(self):
        """Gets the identification of this ElectronicChannelsData.  # noqa: E501


        :return: The identification of this ElectronicChannelsData.  # noqa: E501
        :rtype: ElectronicChannelIdentification
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this ElectronicChannelsData.


        :param identification: The identification of this ElectronicChannelsData.  # noqa: E501
        :type: ElectronicChannelIdentification
        """
        if identification is None:
            raise ValueError("Invalid value for `identification`, must not be `None`")  # noqa: E501

        self._identification = identification

    @property
    def services(self):
        """Gets the services of this ElectronicChannelsData.  # noqa: E501

        Traz a relação de serviços disponbilizados pelo Canal de Atendimento  # noqa: E501

        :return: The services of this ElectronicChannelsData.  # noqa: E501
        :rtype: list[ElectronicChannelService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this ElectronicChannelsData.

        Traz a relação de serviços disponbilizados pelo Canal de Atendimento  # noqa: E501

        :param services: The services of this ElectronicChannelsData.  # noqa: E501
        :type: list[ElectronicChannelService]
        """
        if services is None:
            raise ValueError("Invalid value for `services`, must not be `None`")  # noqa: E501

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
        if issubclass(ElectronicChannelsData, dict):
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
        if not isinstance(other, ElectronicChannelsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other