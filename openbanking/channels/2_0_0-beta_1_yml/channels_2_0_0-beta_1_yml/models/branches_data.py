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

class BranchesData(object):
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
        'participant': 'BranchesParticipant',
        'identification': 'BranchIdentification',
        'postal_address': 'BranchPostalAddress',
        'availability': 'BranchAvailability',
        'phones': 'list[BranchPhone]',
        'services': 'list[BranchService]'
    }

    attribute_map = {
        'participant': 'participant',
        'identification': 'identification',
        'postal_address': 'postalAddress',
        'availability': 'availability',
        'phones': 'phones',
        'services': 'services'
    }

    def __init__(self, participant=None, identification=None, postal_address=None, availability=None, phones=None, services=None):  # noqa: E501
        """BranchesData - a model defined in Swagger"""  # noqa: E501
        self._participant = None
        self._identification = None
        self._postal_address = None
        self._availability = None
        self._phones = None
        self._services = None
        self.discriminator = None
        if participant is not None:
            self.participant = participant
        self.identification = identification
        self.postal_address = postal_address
        self.availability = availability
        if phones is not None:
            self.phones = phones
        self.services = services

    @property
    def participant(self):
        """Gets the participant of this BranchesData.  # noqa: E501


        :return: The participant of this BranchesData.  # noqa: E501
        :rtype: BranchesParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this BranchesData.


        :param participant: The participant of this BranchesData.  # noqa: E501
        :type: BranchesParticipant
        """

        self._participant = participant

    @property
    def identification(self):
        """Gets the identification of this BranchesData.  # noqa: E501


        :return: The identification of this BranchesData.  # noqa: E501
        :rtype: BranchIdentification
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this BranchesData.


        :param identification: The identification of this BranchesData.  # noqa: E501
        :type: BranchIdentification
        """
        if identification is None:
            raise ValueError("Invalid value for `identification`, must not be `None`")  # noqa: E501

        self._identification = identification

    @property
    def postal_address(self):
        """Gets the postal_address of this BranchesData.  # noqa: E501


        :return: The postal_address of this BranchesData.  # noqa: E501
        :rtype: BranchPostalAddress
        """
        return self._postal_address

    @postal_address.setter
    def postal_address(self, postal_address):
        """Sets the postal_address of this BranchesData.


        :param postal_address: The postal_address of this BranchesData.  # noqa: E501
        :type: BranchPostalAddress
        """
        if postal_address is None:
            raise ValueError("Invalid value for `postal_address`, must not be `None`")  # noqa: E501

        self._postal_address = postal_address

    @property
    def availability(self):
        """Gets the availability of this BranchesData.  # noqa: E501


        :return: The availability of this BranchesData.  # noqa: E501
        :rtype: BranchAvailability
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this BranchesData.


        :param availability: The availability of this BranchesData.  # noqa: E501
        :type: BranchAvailability
        """
        if availability is None:
            raise ValueError("Invalid value for `availability`, must not be `None`")  # noqa: E501

        self._availability = availability

    @property
    def phones(self):
        """Gets the phones of this BranchesData.  # noqa: E501

        Lista de telefones da Dependência  # noqa: E501

        :return: The phones of this BranchesData.  # noqa: E501
        :rtype: list[BranchPhone]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this BranchesData.

        Lista de telefones da Dependência  # noqa: E501

        :param phones: The phones of this BranchesData.  # noqa: E501
        :type: list[BranchPhone]
        """

        self._phones = phones

    @property
    def services(self):
        """Gets the services of this BranchesData.  # noqa: E501

        Traz a relação de serviços disponbilizados pelo Canal de Atendimento  # noqa: E501

        :return: The services of this BranchesData.  # noqa: E501
        :rtype: list[BranchService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this BranchesData.

        Traz a relação de serviços disponbilizados pelo Canal de Atendimento  # noqa: E501

        :param services: The services of this BranchesData.  # noqa: E501
        :type: list[BranchService]
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
        if issubclass(BranchesData, dict):
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
        if not isinstance(other, BranchesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
